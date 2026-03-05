# from functions import get_todos, write_todos
import argparse
import time
import functions
import os
import sys
import click

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


def build_parser():
    parser = argparse.ArgumentParser(
        prog="todo",
        description="Todo: REPL (без аргументів) або CLI-команда (через argparse).",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Додати тудушку")
    p_add.add_argument("text", nargs="+", help="Текст тудушки (можна без лапок)")

    sub.add_parser("show", help="Показати список")

    p_edit = sub.add_parser("edit", help="Редагувати тудушку (номер)")
    p_edit.add_argument("number", type=int, help="Номер тудушки (1..n)")

    p_complete = sub.add_parser("complete", help="Позначити виконаною (номер)")
    p_complete.add_argument("number", type=int, help="Номер тудушки (1..n)")

    sub.add_parser("repl", help="Запустити REPL явно")

    return parser

def run_from_args(args):
    if args.command == "add":
        text = " ".join(args.text)
        dispatch(f"add {text}")

    elif args.command == "show":
        dispatch("show")

    elif args.command == "edit":
        dispatch(f"edit {args.number}")

    elif args.command == "complete":
        dispatch(f"complete {args.number}")

    elif args.command == "repl":
        repl()



@click.group(help="Todo CLI через click (альтернатива argparse).")
def click_cli():
    pass

@click_cli.command("add")
@click.argument("text", nargs=-1)  # дозволяє писати без лапок: add Buy milk
def click_add(text):
    dispatch("add " + " ".join(text))

@click_cli.command("show")
def click_show():
    dispatch("show")

@click_cli.command("edit")
@click.argument("number", type=int)
def click_edit(number):
    dispatch(f"edit {number}")

@click_cli.command("complete")
@click.argument("number", type=int)
def click_complete(number):
    dispatch(f"complete {number}")

@click_cli.command("repl")
def click_repl():
    repl()

def main():
    if len(sys.argv) == 1:
        repl()
        return

    if sys.argv[1] == "click":
        # click очікує sys.argv як для програми, тож "з’їдаємо" слово click
        sys.argv = [sys.argv[0]] + sys.argv[2:]
        click_cli()
        return

    parser = build_parser()
    args = parser.parse_args()
    run_from_args(args)


if __name__ == '__main__':
    main()