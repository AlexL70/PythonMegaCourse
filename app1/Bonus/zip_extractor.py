import zipfile

def extract_archive(arch_path, dest_dir):
    with zipfile.ZipFile(arch_path, 'r') as arch:
        arch.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive("files/compressed.zip", "files/Extracted")