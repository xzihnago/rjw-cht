from collections import defaultdict
import json
import os
import pathlib
import re
from xml.etree import ElementTree

script_dir = pathlib.Path(__file__).parent.resolve()
lang_folder = re.compile(r".+/Languages/")


def file_iter():
    return (
        (root_unix, files)
        for root, _, files in os.walk(".")
        if (root_unix := root.replace("\\", "/"))
        and not root_unix.startswith(("./git"))
        and all(ignore not in root_unix for ignore in ignore_list)
        and lang_folder.match(root_unix)
        and files
    )


def build_file_tree():
    file_tree: defaultdict[str, list[str]] = defaultdict(list)

    for root, files in file_iter():
        defs = lang_folder.sub("", root)
        for file in files:
            file_tree[f"{defs}/{file}"].append(f"{root}/{file}")

    return file_tree


def build_def_tree():
    def_tree: defaultdict[str, list[tuple[str, str]]] = defaultdict(list)

    for root, files in file_iter():
        defs = lang_folder.sub("", root)
        for file in filter(lambda f: f.endswith(".xml"), files):
            path = f"{root}/{file}"
            tree = ElementTree.parse(path)

            for node in tree.iter("LanguageData"):
                for child in node:
                    def_tree[defs].append((child.tag, path))

    return def_tree


def check_duplicate_file():
    file_tree = build_file_tree()

    for key, value in file_tree.items():
        if len(value) > 1:
            print(f"\x1b[31mDuplicate Files: {key}\x1b[0m")
            for file in value:
                print(f"  {file}")
            print()


def check_duplicate_defs():
    def_tree = build_def_tree()

    for key, value in def_tree.items():
        path_defs = tuple(zip(*value))
        if len(path_defs[0]) != len(set(path_defs[0])):
            dupl_tree: defaultdict[str, list[tuple[str, str]]] = defaultdict(list)
            for defs, path in value:
                dupl_tree[defs].append((defs, path))

            print(f"\x1b[33mDuplicate Defs: {key}")
            for defs, value in dupl_tree.items():
                if len(value) > 1:
                    print(f"\x1b[33m  {defs}\x1b[0m")
                    for defs, path in value:
                        print(f"    {path}")
            print()


with open(f"{script_dir}/duplicate_checker_ignore.json", "r", encoding="utf-8") as f:
    ignore_list = json.load(f)

check_duplicate_file()
check_duplicate_defs()
