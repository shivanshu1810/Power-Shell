"""File organizer: sort a messy folder (like Downloads) into folders by file type.

It does a PREVIEW by default and moves nothing until you add --apply.

Usage:
    python file_organizer.py ~/Downloads            (preview)
    python file_organizer.py ~/Downloads --apply    (actually move files)
"""
import shutil
import sys
from pathlib import Path

TYPES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv", ".pptx"},
    "Installers": {".exe", ".msi", ".dmg", ".pkg"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Media": {".mp3", ".mp4", ".mov", ".wav", ".mkv"},
}


def folder_for(path):
    ext = path.suffix.lower()
    for folder, extensions in TYPES.items():
        if ext in extensions:
            return folder
    return "Other"


def main():
    if len(sys.argv) < 2:
        print("Usage: python file_organizer.py FOLDER [--apply]")
        return
    root = Path(sys.argv[1]).expanduser()
    apply = "--apply" in sys.argv
    if not root.is_dir():
        print(f"{root} is not a folder.")
        return

    for item in sorted(root.iterdir()):
        if not item.is_file():  # skip folders, only move files
            continue
        target_dir = root / folder_for(item)
        target = target_dir / item.name
        # Don't overwrite: add a number if the name is already taken
        n = 1
        while target.exists():
            target = target_dir / f"{item.stem}_{n}{item.suffix}"
            n += 1
        print(f"{item.name}  ->  {target_dir.name}/")
        if apply:
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(target))

    if not apply:
        print("\nPreview only. Run again with --apply to move the files.")


if __name__ == "__main__":
    main()
