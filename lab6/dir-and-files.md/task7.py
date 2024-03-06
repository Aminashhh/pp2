def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'rb') as source_file:
            file_contents = source_file.read()

            with open(destination_path, 'wb') as destination_file:
                destination_file.write(file_contents)

        print(f"'{source_path}' successfully copied to '{destination_path}'.")

    except FileNotFoundError:
        print(f"'{source_path}' or '{destination_path}' not found.")

if __name__ == "__main__":
    source_file_path = input(" ")
    destination_file_path = input(" ")

    copy_file(source_file_path, destination_file_path)