FILEPATH="todos.txt"
def get_todo(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local
def write_todo(todo_arg,filepath=FILEPATH):
    with open(filepath,"w") as file_local:
        file_local.writelines(todo_arg)

print(__name__)
if __name__ == "__main__":
    print("im functions inner statement ")
