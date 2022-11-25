def get_file_text(path: str):
    """Получить текст файла в параметре path."""
    with open(path) as file:
        return file.read()
