import os
import shutil

def find_and_move_folders():
    target_folder = "java.lang.ArrayIndexOutOfBoundsException"
    target_string = "java.lang.ArrayIndexOutOfBoundsException"
    os.makedirs(target_folder, exist_ok=True)
    
    moved_folders = set()
    
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".log"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        if target_string in f.read():
                            folder_to_move = os.path.abspath(root)
                            if folder_to_move != os.path.abspath(target_folder) and folder_to_move not in moved_folders:
                                shutil.move(folder_to_move, os.path.join(target_folder, os.path.basename(folder_to_move)))
                                moved_folders.add(folder_to_move)
                                print(f"Moved: {folder_to_move} -> {target_folder}")
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

if __name__ == "__main__":
    find_and_move_folders()