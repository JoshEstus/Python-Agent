import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if file_path:
        target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        print(os.path.exists(target_dir))
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
    except Exception as e:
        return f"Error: creating dirs {target_dir}: {e}"

    try:
        with open(target_dir, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error: writing to file {target_dir}: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
