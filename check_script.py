from collections import defaultdict
import os
import re
from xml.etree import ElementTree

lang = re.compile(r"[\./\w]+/Languages/")


def file_iter():
    return (
        (root_unix, files)
        for root, _, files in os.walk(".")
        if (root_unix := root.replace("\\", "/"))
        and not root_unix.startswith(("./git", "./legacy"))
        and lang.match(root_unix)
        and files
    )


def build_file_tree():
    file_tree: defaultdict[str, list[str]] = defaultdict(list)

    for root, files in file_iter():
        defs = lang.sub("", root)
        for file in files:
            file_tree[f"{defs}/{file}"].append(f"{root}/{file}")

    return file_tree


def build_def_tree():
    def_tree: defaultdict[str, list[tuple[str, str]]] = defaultdict(list)

    for root, files in file_iter():
        defs = lang.sub("", root)
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


check_duplicate_file()
check_duplicate_defs()
