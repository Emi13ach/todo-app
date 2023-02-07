FILEPATH = "todos.txt"

def get_todos(file_path=FILEPATH):
    """Read a text file and return the list of to-do items."""
    with open(file_path, "r") as file:
        todos_data = file.readlines()
        return todos_data

def write_todos(todo_arg, file_path=FILEPATH):
    """Write a list to-do items to the text file. """
    with open(file_path, "w") as f:
        f.writelines(todo_arg)


if __name__ == "__main__":
    print("hello")