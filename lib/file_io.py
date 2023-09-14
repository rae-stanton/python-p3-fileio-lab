def write_file(file_name, file_content):
    if not isinstance(file_name, str):
        file_name = str(file_name)

    file_name += ".txt"

    with open(file_name, "w") as file:
        file.write(file_content)


write_file("example", "This is the actual content of the file.")

# end of write file


def append_file(file_name, append_content):
    file_name = str(file_name)

    with open(f'{file_name}.txt', 'a', encoding='utf-8') as file:
        file.write(append_content)


append_file("log_file", "Log 2")


def read_file(file_name):
    if not isinstance(file_name, str):
        file_name = str(file_name)

    with open(f'{file_name}.txt', encoding='utf-8') as text_file:
        return text_file.read()
