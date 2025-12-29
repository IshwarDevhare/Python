import os

FILEPATH = FILEPATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "todos.txt"
)

def get_todos(filepath = FILEPATH):
    """
    READ a text file and returns the list of to-do items
    
    :param filepath: Description
    """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath = FILEPATH):
    """
    Write to-tos to the file
    
    :param todos_arg: Description
    :param filepath: Description
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)



if __name__ == "__main__":
    print("test hello")
