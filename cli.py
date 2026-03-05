# from functions import get_todos, write_todos
import time
import functions
import os

os.makedirs("data", exist_ok=True)
todos_path = os.path.join("data", "todos.txt")

if not os.path.exists(todos_path):
    with open(todos_path, "w", encoding='utf-8') as f:
        pass

def success():
    print("Успішне виконання команди")

def do_add(user_action):
    todo = user_action[4:] + "\n"
    todos = functions.get_todos()
    todos.append(todo)
    functions.write_todos(todos)
    return True

def do_show(user_action):
    todos = functions.get_todos()
    for index, item in enumerate(todos):
        row = f"{index + 1} -- {item.strip('\n')}"
        print(row)
    return True

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
    return True

def do_complete(user_action):
    number = int(user_action[9:]) - 1
    if number < 0:
        raise IndexError

    todos = functions.get_todos()
    completed_todo = todos.pop(number)
    functions.write_todos(todos)

    message = f"\tТудушка \"{completed_todo.strip('\n')}\" була успішно виконана!"
    print(message)
    return True

def do_exit(user_action):
    return False

# Таблиця команд (Command Dispatcher Table)
COMMANDS = {
    "add": do_add,
    "show": do_show,
    "edit": do_edit,
    "complete": do_complete,
    "exit": do_exit,
}

def dispatch(user_action):
    """
        Dictionary Dispatcher:
        - беремо перше слово як "команду"
        - знаходимо обробник у COMMANDS
        - викликаємо його
    """

    user_action = user_action.strip()
    if not user_action:
        print("invalid input")
        return True

    cmd = user_action.split(maxsplit=1)[0].lower()
    handler = COMMANDS.get(cmd)

    if handler is None:
        print("invalid input")
        return True

    try:
        should_continue = handler(user_action)
        if should_continue:
            success()
        return should_continue

    except ValueError:
        print("Ваша команда не зовсім зрозуміла")
        return True
    except IndexError:
        print("Не вірний номер тудушки")
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