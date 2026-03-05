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

def repl():
    now = time.strftime("%b %d, %Y %H:%M:%S")
    print(now)
    while True:
        user_action = input("Type add, show, edit, complete or exit: ")
        user_action = user_action.strip()

        if user_action.lower().startswith('add'):
            do_add(user_action)
        elif user_action.lower().startswith('show'):
            do_show()
        elif user_action.lower().startswith('edit'):
            try:
                do_edit(user_action)
            except ValueError:
                print("Ваша команда не зовсім зрозуміла")
                continue
            except IndexError:
                print("Не вірний номер тудушки")
                continue
        elif user_action.lower().startswith('complete'):
            try:
                do_complete(user_action)
            except IndexError:
                print("Не вірний номер тудушки")
                continue
        elif user_action.lower().startswith('exit'):
            break
        else:
            print('invalid input')

        print( ' Успішне виконня команди')

    print("Babay!")

def main():
    repl()



if __name__ == '__main__':
    main()