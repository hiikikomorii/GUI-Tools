import os
import shutil

current_script = os.path.basename(__file__)
folder_path = os.path.dirname(os.path.abspath(__file__))

for item in os.listdir(folder_path):
    if item == current_script:
        continue

    item_path = os.path.join(folder_path, item)
    if os.path.isfile(item_path) or os.path.islink(item_path):
        os.unlink(item_path)
    elif os.path.isdir(item_path):
        shutil.rmtree(item_path)

print("All files was deleted")
