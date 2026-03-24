import os
import shutil

# Path to organize files from
DOWNLOADS_PATH = os.path.expanduser("~/Downloads")

# Mapping extensions to folders 
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Code": [".py", ".js", ".cpp", ".html", ".css"]
}


def organize_files():
    if not os.path.exists(DOWNLOADS_PATH):
        print("Downloads folder not found!")
        return

    for file in os.listdir(DOWNLOADS_PATH):
        file_path = os.path.join(DOWNLOADS_PATH, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)

            moved = False

            for folder, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    folder_path = os.path.join(DOWNLOADS_PATH, folder)

                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    shutil.move(file_path, os.path.join(folder_path, file))
                    print(f"Moved: {file} → {folder}")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(DOWNLOADS_PATH, "Others")

                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)

                shutil.move(file_path, os.path.join(other_folder, file))
                print(f"Moved: {file} → Others")


if __name__ == "__main__":
    organize_files()
    print("\n✅ Files organized successfully!")