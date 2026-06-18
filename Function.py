FILE_PATH = 'todos.txt'

def get_todo(filepath=FILE_PATH):
    """ Reads the content in the text file and
    returns it as a list"""
    with open(FILE_PATH, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_args,filepath=FILE_PATH):
    """ Writes the todos list in the text file """
    with open(FILE_PATH, "w") as file:
        file.writelines(todos_args)


if __name__ == '__main__':
    print('Hello')
    print(get_todo())