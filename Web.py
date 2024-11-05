import streamlit as st
import functions

st.title("My Todo App")
st.subheader("This is a todo app")
st.text("to increase productivity")
todos = functions.get_todo()

def add_todo():
    todo_to_add=st.session_state["new_todo"]+"\n"
    todos.append(todo_to_add)
    functions.write_todo(todos)

for todo in todos:
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="newtodo",placeholder="Add a new todo",
              on_change=add_todo,key="new_todo")
