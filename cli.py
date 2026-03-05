# from functions import get_todos, write_todos
import time
import functions
import os

os.makedirs("data", exist_ok=True)
todos_path = os.path.join("data", "todos.txt")

if not os.path.exists(todos_path):
    with open(todos_path, "w", encoding='utf-8') as f:
        pass

def do_add(user_action):
    todo = user_action[4:] + "\n"
    todos = functions.get_todos()
    todos.append(todo)
    functions.write_todos(todos)

def do_show():
    todos = functions.get_todos()
    for index, item in enumerate(todos):
        row = f"{index + 1} -- {item.strip('\n')}"
        print(row)

def do_edit(user_action):
    """
    edit <number>
    """
    number = int(user_action[5:]) - 1
    if number < 0:
        raise IndexError

    todos = functions.get_todos()
    new_todo = input("Enter new todo: ")
    todos[number] = new_todo + "\n"
    functions.write_todos(todos)

def do_complete(user_action):
    number = int(user_action[9:]) - 1
    if number < 0:
        raise IndexError

    todos = functions.get_todos()
    completed_todo = todos.pop(number)
    functions.write_todos(todos)

    message = f"\tТудушка \"{completed_todo.strip('\n')}\" була успішно виконана!"
    print(message)

def dispatch(user_action):
    """
    Виконує одну команду.

    Повертає:
        True  — продовжувати REPL
        False — вийти (exit)
    """
    user_action = user_action.strip()

    if user_action.lower().startswith('add'):
        do_add(user_action)
        print(' Успішне виконня команди')
        return True

    if user_action.lower().startswith('show'):
        do_show()
        print(' Успішне виконня команди')
        return True

    if user_action.lower().startswith('edit'):
        try:
            do_edit(user_action)
            print(' Успішне виконня команди')
        except ValueError:
            print("Ваша команда не зовсім зрозуміла")
        except IndexError:
            print("Не вірний номер тудушки")
        return True

    if user_action.lower().startswith('complete'):
        try:
            do_complete(user_action)
            print(' Успішне виконня команди')
        except IndexError:
            print("Не вірний номер тудушки")
        return True

    if user_action.lower().startswith('exit'):
        return False

    print('invalid input')
    return True

def repl():
    now = time.strftime("%b %d, %Y %H:%M:%S")
    print(now)
    while True:
        user_action = input("Type add, show, edit, complete or exit: ")
        if not dispatch(user_action):
            break

    print("Babay!")

def main():
    repl()



if __name__ == '__main__':
    main()