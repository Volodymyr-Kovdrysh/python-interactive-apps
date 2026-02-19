FILEPATH="data/todos.txt"

def get_todos(filepath=FILEPATH):
    """ Зчитує файл і повертає список тудушок

    :param filepath:
    :return: список
    """
    with open(filepath, "r") as f:
        todos_local = f.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """
    Записує дані у файл
    :param todos_arg:
    :param filepath:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)



if __name__ == "__main__":
    print('hello')
    print(get_todos())