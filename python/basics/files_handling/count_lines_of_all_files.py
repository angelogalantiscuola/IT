import os


# count all characters in a single file
def count_characters_of_a_file(file_path: str) -> int:
    if not os.path.isfile(file_path):
        print("Error: path is not a file")
        return 0
    with open(file_path, "r") as f:
        lines = f.readlines()
        # count all characters in file
        characters = 0
        for line in lines:
            characters += len(line)
    return characters


# count characters of all files in a directory, except for files in hidden directories
def count_characters_of_all_files_except_hidden(path: str) -> int:
    characters = 0

    if not os.path.isdir(path):
        print("Error: path is not a directory")
        return 0
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            if file[0] != ".":
                pass
                characters += count_characters_of_all_files_except_hidden(file_path)
        else:
            print(file_path)
            characters += count_characters_of_a_file(file_path)
    return characters


if __name__ == "__main__":
    path = "."
    result = count_characters_of_all_files_except_hidden(path)
    print(result)
