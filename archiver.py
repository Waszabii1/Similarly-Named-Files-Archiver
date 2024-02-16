import pathlib
import shutil

print("To specify file paths please use the form \X\Y\Z")
source_dir = pathlib.Path(input("Folder you want archiving? "))
print(source_dir)

fold_keys = set()

target_dir_input = input("Folder that you want the archive to go? (Press Y to put in same folder under the name X/Archive) ").upper()

if target_dir_input == "Y":
    Archive = "Archive"
    target_dir_root = pathlib.Path(source_dir / Archive)
else:
    target_dir_root = pathlib.Path(target_dir_input)
print(target_dir_root)
target_dir_root.mkdir(exist_ok=True)
fold_num_input = int(input("How many numbers do you want to archive by? \nE.g. If you want 1000123 to go into folder 1000 the number would be 4 "))
x_num_input = int(input("How many x's do you want after the folder name \nE.g. If you want 1000123 to go into folder 1000xxx the number would be 3 "))

for file in source_dir.glob("*.*"):
    fold_keys.add(file.stem[:fold_num_input])
 
for k in fold_keys:

    newfolder = k + ("x" * x_num_input)

    if k:

        target_dir = target_dir_root / newfolder

        target_dir.mkdir(exist_ok = True)

        for p in source_dir.glob(k + "*.*"):

            print(f"{p.name} moved to {target_dir}/{p.name}")

            shutil.move(p, target_dir / p.name)