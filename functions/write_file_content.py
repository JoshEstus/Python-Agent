import os
from google.genai import types

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


schema_write_file_content = types.FunctionDeclaration(
        name="write_file_content",
        description="Write to files or make new ones if necessary, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file path for the file contents.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The content that is to be written to the file."
                )
            },
        ),
    )