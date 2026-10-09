import os
import subprocess

mods_path = "D:/Steam/steamapps/common/RimWorld/Mods"

os.chdir(mods_path)
for folder in os.listdir():
    if os.path.isdir(folder) and ".git" in os.listdir(folder):
        os.chdir(folder)
        subprocess.run(["git", "gc", "--aggressive", "--prune"], shell=True)
        os.chdir("..")
