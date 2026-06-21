import os

class FileReader:
    def __init__(self):
        pass

    def read_file(self, file_path: str) -> str:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist or is not a valid file.")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def read_directory(self, dir_path: str) -> dict[str, str]:
        if not os.path.isdir(dir_path):
            raise NotADirectoryError(f"The path {dir_path} does not exist or is not a valid directory.")
    
        text_contents = {}
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.txt'):  # Only process .txt files
                    file_path = os.path.join(root, file)
                    try:
                        content = self.read_file(file_path)
                        relative_file_path = os.path.relpath(file_path, dir_path)
                        key_name = os.path.splitext(relative_file_path)[0]
                        text_contents[key_name] = content
                    except Exception as e:
                        print(f"Could not read file {file_path}: {e}")
    
        return text_contents
