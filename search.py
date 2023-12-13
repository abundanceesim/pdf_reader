import os
import glob

def search_files_by_extension(extension):
    # Get the current directory
    current_directory = os.getcwd()

    # Create a file path pattern with the specified extension
    pattern = f"*.{extension}"

    # Use glob to find files matching the pattern
    matching_files = glob.glob(os.path.join(current_directory, pattern))

    file_names = []
    for file_path in matching_files:
        file_names.append(file_path)

    return file_names

