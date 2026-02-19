# from functions import get_todos, write_todos
import time
import functions
import os

os.makedirs("data", exist_ok=True)
todos_path = os.path.join("data", "todos.txt")

if not os.path.exists(todos_path):
    with open(todos_path, "w") as f:
        pass

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if user_action.lower().startswith('add'):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.lower().startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            row = f"{index+1} -- {item.strip('\n')}"
            print(row)
    elif user_action.lower().startswith('edit'):
        try:
            number = int(user_action[5:])

            number = number - 1
            if number < 0:
                raise IndexError
            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Ваша команда не зовсім зрозуміла")
            continue
        except IndexError:
            print("Не вірний номер тудушки")
            continue


    elif user_action.lower().startswith('complete'):
        try:
            number = int(user_action[9:])
            number = number - 1
            if number < 0:
                raise IndexError
            todos = functions.get_todos()

            completed_todo = todos.pop(number)

            functions.write_todos(todos)

            message = f"\tТудушка \"{completed_todo.strip('\n')}\" була успішно виконана!"
            print(message)
        except IndexError:
            print("Не вірний номер тудушки")
            continue

    elif user_action.lower().startswith('exit'):
        break
    else:
        print('invalid input')

    print( ' Успішне виконня команди')







print("Babay!")