import pathlib
import re

script_dir = pathlib.Path(__file__).parent.resolve()
cjk = re.compile(r".+[\u4E00-\u9FFF].+\n")

with open(f"{script_dir}/TranslationReport_ignore.txt", "r", encoding="utf8") as f:
    ignore_lines = [
        line
        for line in f.readlines()
        if line != "\n" and not line.startswith("========== ")
    ]

with open(f"{script_dir}/TranslationReport.txt", "r", encoding="utf8") as f:
    filtered_lines = [
        line
        for line in f.readlines()
        if line not in ignore_lines and not cjk.match(line)
    ]

with open(f"{script_dir}/TranslationReport_filtered.txt", "w", encoding="utf8") as f:
    f.writelines(filtered_lines)
