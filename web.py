import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My Todo App.")
st.subheader("This is my Todo App")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    print(index, todo)
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print(checkbox, index)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...", key="new_todo", on_change=add_todo)
