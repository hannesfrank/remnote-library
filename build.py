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
    "^((?P<name>[^@<]+)(\s+|<))?((?P<email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)>?)?$"
)
repo_regex = re.compile("^(?P<repo>https://github.com/[^/]+/[^/]+).*$")


def resolve_to_public(path):
    return path.relative_to(public).as_posix()


def build_scroll_data(scroll_manifests):
    data = {}

    for manifest in scroll_manifests:
        manifest = Path(manifest)
        # Besides the data in the manifest there is additional data which a database would store or generate
        # - rating (average stars+number ratings)
        # - install/download count
        # - (when user accounts + API) install/update status

        # The author can also be discovered from git: git shortlog -n -s -- myfolder

        with manifest.open("r") as f:
            scroll_data = json.load(f)

        scroll_id = scroll_data["id"]
        scroll_folder = manifest.parent

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

        install_methods = scroll_data["install"]

        for install_method in install_methods:
            method = install_method["method"]

            if method not in handle_install_method:
                raise NotImplementedError(
                    f"Install method '{method}' of {scroll_id} not supported!"
                )

            handle_install_method[method](install_method, scroll_data, scroll_folder)

        data[scroll_id] = scroll_data

    return data


def handle_shelf_custom_css(scroll_data, scroll_folder: Path):
    """
    This snippet has to be copy&pasted before the code block is inserted.
    Since we can not properly paste code blocks yet the copy&paste has to be 2 steps of copy&paste.
    
    TODO: Later when we install using the API this block should be generated as a whole automatically. 
    """
    # TODO: The leading empty rem is required for the H1 to work.
    template = f"""-
- # {scroll_data["name"]}
    - id: {scroll_data["id"]}
    - version: {scroll_data["version"]}
    - [Homepage]({scroll_data["homepage"]})"""
    report_template = """
    - [Report Problem or Suggest Improvement]({})"""
    code_template = """
    - ## Code
        - Make or move a new Custom CSS block here and copy&paste the second part from the library."""
    tags_template = """
    - ## Tags
        - {}"""
    demo_template = """
    - ## Demo
{}"""
    if "repo" in scroll_data:
        report_title = urllib.parse.quote(
            f"Report: {scroll_data['name']} v{scroll_data['version']}"
        )
        report_body = urllib.parse.quote(
            f"""
- **Id:** {scroll_data["id"]}
- **Version:** {scroll_data["version"]}
- **Type:** Problem/Suggestion (choose one)

Describe the problem you are having with the scroll.
Make sure to include a screenshot :)
"""
        )
        report_url = f"{scroll_data['repo']}/issues/new?title=Report:{report_title}&body={report_body}"
        template += report_template.format(report_url)

    template += code_template

    config = scroll_data.get("config", {})
    if "tags" in config:
        template += tags_template.format(config["tags"])

    if "demo" in config:
        demo = scroll_folder / config["demo"]
        demo_rems = demo.read_text()
        indented_demo_rems = textwrap.indent(demo_rems, " " * 8)
        template += demo_template.format(indented_demo_rems)

    scroll_data["customCSSBlock"] = template


def handle_copy_install_method(install_data, scroll_data, scroll_folder: Path):
    """Install by copy something to the clipboard and have the user paste it at the appropriate
    place, e.g. Custom CSS.
    
    Keys:
      - file: A file's content given the file path as string
      - content: Direct string content.
    """
    if "file" in install_data:
        p = scroll_folder / install_data["file"]
        install_data["content"] = p.read_text()


handle_install_method = {"copy": handle_copy_install_method}
handle_shelf = {"Custom CSS": handle_shelf_custom_css}

if __name__ == "__main__":
    data = build_scroll_data(scroll_manifests)

    with open("src/data.json", "w") as f:
        json.dump(data, f, sort_keys=True, indent=2)
