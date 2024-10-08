import pathlib
import zipfile as zf

def make_archive(file_paths, dest_dir):
    dest_path=pathlib.Path(dest_dir, "compressed.zip")
    with zf.ZipFile(dest_path, 'w') as arch:
        for path in file_paths:
            arch.write(path, arcname=pathlib.Path(path).name)

if __name__ == "__main__":
    make_archive(["bonus1.py", "bonus3.py", "bonus4.py"], "files")