import os

class FileReader:
    """
    ファイルから、あるいはディレクトリ内のすべてのテキストファイルから再帰的にテキストを読み込むクラス。
    """
    def __init__(self):
        pass

    def read_file(self, file_path: str) -> str:
        """
        テキストの内容を読み込み、文字列として返す。
        
        :param file_path: テキストファイルへのパス。
        :return: ファイルの内容を文字列として返す。
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist or is not a valid file.")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def read_directory(self, dir_path: str) -> dict[str, str]:
        """
        ディレクトリ内のすべてのテキスト・ファイルを再帰的に読み込み、
        ファイル名とその内容を辞書として返す。

        :param dir_path: ディレクトリへのパス。
        :return: 辞書。キーはファイル名、値はテキストファイルの内容。
        """
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
