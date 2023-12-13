from search import search_files_by_extension
from reader import read_pdf

extension = "pdf"
found_files = search_files_by_extension(extension)

if found_files:
    print(f"Found {len(found_files)} .pdf files")
    for file_path in found_files:
        print(file_path)
        read_pdf(file_path)
else:
    print(f"No '.{extension}' files found in the current directory.")