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
from pathlib import Path
from glob import glob

public = Path("public")
scroll_manifests = glob(str(public / "scrolls/*/manifest.json"))


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

        thumb_path = scroll_folder / "thumb.png"
        try:
            homepage = scroll_data["homepage"]
        except KeyError as e:
            homepage = f"https://github.com/hannesfrank/remnote-library/tree/master/public/{scroll_folder.relative_to(public)}"

        data[scroll_id] = scroll_data
        data[scroll_id]["homepage"] = homepage
        data[scroll_id]["thumb"] = thumb_path.relative_to(public).as_posix()
        data[scroll_id]["rating"] = 5
        data[scroll_id]["rating_count"] = 42
        data[scroll_id]["install_count"] = 1337

        install_methods = scroll_data["install"]

        for install_method in install_methods:
            method = install_method["method"]

            if method not in handle_install_method:
                raise NotImplementedError(
                    f"Install method '{method}' of {scroll_id} not supported"
                )

            handle_install_method[method](install_method, scroll_data, scroll_folder)

    return data


def handle_copy_install_method(install_data, scroll_data, scroll_folder: Path):
    """Install by copy something to the clipboard and have the user paste it at the appropriate
    place, e.g. Custom CSS.
    
    Keys:
      - file: A file's content given the file path as string
      - content: Direct string content.
    """
    if "content" in install_data:
        # scroll_data["copy"] = install_data["content"]
        pass
    elif "file" in install_data:
        p = scroll_folder / install_data["file"]
        install_data["content"] = p.read_text()
        # scroll_data["copy"] = p.read_text()


handle_install_method = {"copy": handle_copy_install_method}


if __name__ == "__main__":
    data = build_scroll_data(scroll_manifests)

    with open("src/data.json", "w") as f:
        json.dump(data, f, sort_keys=True, indent=2)
