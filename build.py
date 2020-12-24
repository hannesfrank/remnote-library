"""
This script parses the scrolls directory and outputs a json file which can be imported by the
library component.

This should be done always after you cange a manifest.
TODO: Incorporate this into an automated build process (Github action, npm script, git hook).

Once we have a server this should be done dynamically by the backend.

Medium Term:
- Turn this into a *librarian* script with commands to build, verify manifests, update manifests 
"""

import json
import glob
import re
import textwrap
import urllib

from pathlib import Path

public = Path("public")
scroll_manifests = glob.glob(str(public / "scrolls/*/manifest.json"))

author_regex = re.compile(
    "^((?P<name>[^@<]+)(\s*|<))?((?P<email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)>?)?$"
)
repo_regex = re.compile("^(?P<repo>https://github.com/[^/]+/[^/]+).*$")


def resolve_to_public(path):
    return path.relative_to(public).as_posix()


def build_scroll_data(scroll_manifests):
    data = {}
    raw_data = []
    for manifest in scroll_manifests:
        manifest = Path(manifest)

        # Besides the data in the manifest there is additional data which a database would store or generate
        # - rating (average stars+number ratings)
        # - install/download count
        # - (when user accounts + API) install/update status

        # The author can also be discovered from git: git shortlog -n -s -- myfolder

        with manifest.open("r") as f:
            try:
                scroll_data = json.load(f)
            except Exception as e:
                print(f"There was a problem parsing the manifest of {manifest.parent}")
                raise e
            scroll_folder = manifest.parent
            raw_data.append((scroll_data, scroll_folder))

    for scroll_data, scroll_folder in raw_data:
        scroll_id = scroll_data["id"]

        match = author_regex.match(scroll_data["author"])
        scroll_data["author"] = match.groupdict()
        if "name" in scroll_data["author"]:
            scroll_data["author"]["name"] = scroll_data["author"]["name"].strip()

        # TODO: Check if thumb exists. If not use a default image. One for each shelf (CSS, User Script, Template, ...).
        thumb_name = scroll_data["thumb"] if "thumb" in scroll_data else "thumb.png"
        thumb_path = scroll_folder / thumb_name
        scroll_data["thumb"] = resolve_to_public(thumb_path)

        if "version" not in scroll_data:
            scroll_data["version"] = "0.0.0"

        if "preview" in scroll_data:
            preview_path = scroll_folder / scroll_data["preview"]
            scroll_data["preview"] = resolve_to_public(preview_path)

        # TODO: Read description from markdown
        # TODO: These are handled by the backend later:
        scroll_data["rating"] = 5
        scroll_data["ratingCount"] = 42
        scroll_data["installCount"] = 1337

        if "homepage" not in scroll_data:
            scroll_data[
                "homepage"
            ] = f"https://github.com/hannesfrank/remnote-library/tree/master/public/{resolve_to_public(scroll_folder)}"
        match = repo_regex.match(scroll_data["homepage"])
        if match:
            scroll_data["repo"] = match.groupdict()["repo"]

        shelf = scroll_data["shelf"]
        if shelf not in handle_shelf:
            raise NotImplementedError(f"Shelf '{shelf}' does not exist yet!")

        handle_shelf[shelf](scroll_data, scroll_folder)

        data[scroll_id] = scroll_data

    return data


def handle_shelf_custom_css(scroll_data, scroll_folder: Path):
    """
    This snippet has to be copy&pasted before the code block is inserted. Since we can not properly
    paste code blocks yet the copy&paste has to be 2 steps of copy&paste.

    A Custom CSS block consists of:
      - metadata (description, id, version, homepage, report link)
      - Tags (Optional: List of styling tags. These are preserved on updates. The user must
        migrate/merge them manually.)
      - Demo (Optional: Show an example of what the style does.)
      - Code (This is preplaced by auto updates. Users who want to tinker with this are expected to
        move it somewhere else or just copy the code form the additional install methods.)
      - Customization (Optional: This is preserved by auto updates, only if there is a major update
        this has to be migrated manually)

    """
    # TODO: The leading empty rem is required for the H1 to work.
    custom_css_block = f"""-
- # {scroll_data["name"]}
    - {" ".join(scroll_data["description"].splitlines())}
    - id: {scroll_data["id"]}
    - version: {scroll_data["version"]}
    - [Homepage]({scroll_data["homepage"]})"""
    report_template = """
    - [Report Problem or Suggest Improvement]({})"""
    tags_template = """
    - ## Tags
{}"""
    demo_template = """
    - ## Demo
{}"""
    code_template = """
    - ## Code
{}"""
    customization_template = """
    - ## Customization
{}"""

    if "repo" in scroll_data:
        report_title = urllib.parse.quote(
            f"RemNote Library Report: {scroll_data['name']} v{scroll_data['version']}"
        )
        report_body = urllib.parse.quote(
            f"""
**Please check first if there is an update of this scroll available.**

---

- **Id:** {scroll_data["id"]}
- **Version:** {scroll_data["version"]}
- **Type:** Problem/Suggestion (choose one)

- [ ] Describe the problem you are having with the scroll or how it should be improved.
- [ ] _Add_ a short description to the title (don't replace it completely!) so people know what this is about.
- [ ] Make sure to include a screenshot or image to make your issue easy to understand.

---
"""
        )
        report_url = (
            f"{scroll_data['repo']}/issues/new?title={report_title}&body={report_body}"
        )
        custom_css_block += report_template.format(report_url)

    config = scroll_data.get("config", {})

    # --- Style Tags ---
    if "tags" in config:
        tag_rems = "\n".join(f"- {tag}" for tag in config["tags"])
        indented_tag_rems = textwrap.indent(tag_rems, " " * 8)
        custom_css_block += tags_template.format(indented_tag_rems)

    # --- Demo ---
    if "demo" in config:
        demo = scroll_folder / config["demo"]
        demo_rems = demo.read_text().strip()
        indented_demo_rems = textwrap.indent(demo_rems, " " * 8)
        custom_css_block += demo_template.format(indented_demo_rems)

    # --- Code ---
    # In the end only the customCSSBlock matteres for the Custom CSS shelf
    handle_install_methods(scroll_data, scroll_folder)
    indented_code = textwrap.indent(scroll_data["install"]["content"], " " * 8)
    custom_css_block += code_template.format(indented_code)

    # --- Customization ---
    if "customization" in config:
        customization_css = manifest_content_to_rem(
            config["customization"], scroll_data, scroll_folder
        )
        indented_customization_css = textwrap.indent(customization_css, " " * 8)
        custom_css_block += customization_template.format(indented_customization_css)

    scroll_data["customCSSBlock"] = custom_css_block


def handle_install_methods(scroll_data, scroll_folder):
    scroll_id = scroll_data["id"]
    install_methods = scroll_data["install"]
    if isinstance(install_methods, list):
        # TODO: Legacy install mode. Rework this.
        # I don't quite remember for which use case I wanted multiple install methods.
        # Maybe for text templates which should be available for multiple text expanders?
        # Another use would be page templates consisting of css to copy and text which would benefit
        # from general install methods (pairs of buttonTitle: textToCopy) in the frontend.
        print(f"FIXME: Legacy install method in {scroll_id}")
        for install_method in install_methods:
            method = install_method["method"]
            if method not in handle_install_method:
                raise NotImplementedError(
                    f"Install method '{method}' of {scroll_id} not supported!"
                )
            handle_install_method[method](install_method, scroll_data, scroll_folder)
        # There is only one (Custom CSS) install for now
        scroll_data["install"] = scroll_data["install"][0]

    elif isinstance(install_methods, dict):
        # Custom CSS copy install
        # This is the most recent and currently only used spec
        handle_copy_install_method(install_methods, scroll_data, scroll_folder)
    else:
        raise ValueError(f"{scroll_id} install method cannot be parsed.")


def handle_copy_install_method(install_data, scroll_data, scroll_folder: Path):
    """Install by copy something to the clipboard and have the user paste it at the appropriate
    place, e.g. Custom CSS.
    
    Keys:
      - file: A file's content given the file path as string
      - content: Direct string content.
    """
    if "file" in install_data:
        # TODO: Legacy install method
        p = scroll_folder / install_data["file"]
        install_data["content"] = manifest_content_to_rem(
            p.read_text(), scroll_data, scroll_folder
        )
    elif "content" in install_data:
        install_data["content"] = manifest_content_to_rem(
            install_data["content"], scroll_data, scroll_folder
        )


def make_enabled_marker(info):
    if "enabled" in info:
        if info["enabled"]:
            return "[ ] "
        else:
            return "[x] "
    else:
        return ""


def make_code_block(code, lang="css"):
    return f"""```css
{code}
```"""


def manifest_content_to_rem(info, scroll_data, scroll_folder: Path):
    """Turn the value of "content" from a Custom CSS copy install spec into RemNote flavored markdown."""
    # TODO: This turned pretty spaghetti. I should at least unit test this. Better would be to
    # validate this using a json schema.
    # TODO: Generalize install.content to use install.description with default value `## Code`
    # TODO: Make formatting class/closure since scroll_data and scroll_folder is passed as arguments a lot
    copy_template = """- {enabled_marker}{description}
{indented_content}"""

    if isinstance(info, str):
        return make_code_block(info)

    elif isinstance(info, dict):
        if "content" in info:
            # Subtree with more blocks
            if "description" not in info:
                raise KeyError(
                    f"{scroll_data['id']} install content must have description."
                )
            content = manifest_content_to_rem(
                info["content"], scroll_data, scroll_folder
            )
            return copy_template.format(
                enabled_marker=make_enabled_marker(info),
                description=info["description"],
                indented_content=textwrap.indent(content, " " * 4),
            )
            return
        if "css" in info:
            content = info["css"]
        elif "file" in info:
            content_file = scroll_folder / info["file"]
            content = content_file.read_text()
        else:
            raise KeyError(
                f"{scroll_data['id']} install has neither 'css' nor 'file' key."
            )

        if "description" in info:
            description = info["description"]
            # TODO: Allow enabled/disabled without a description
            code_block = make_code_block(content.strip())
            return copy_template.format(
                enabled_marker=make_enabled_marker(info),
                description=description,
                indented_content=textwrap.indent(code_block, " " * 4),
            )
        else:
            return make_code_block(content.strip())

    elif isinstance(info, list):
        return "\n".join(
            manifest_content_to_rem(item, scroll_data, scroll_folder) for item in info
        )
    else:
        raise ValueError(f"{info} can not be parsed")


handle_install_method = {"copy": handle_copy_install_method}
handle_shelf = {"Custom CSS": handle_shelf_custom_css}

if __name__ == "__main__":
    data = build_scroll_data(scroll_manifests)

    with open("src/data.json", "w") as f:
        json.dump(data, f, sort_keys=True, indent=2)
    print("Building Scrolls. Complete!")
