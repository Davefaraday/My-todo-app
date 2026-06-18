import streamlit as st
import Function

todos = Function.get_todo()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    Function.write_todos(todos)


st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')

for index, t in enumerate(todos):
    checkbox = st.checkbox(t, key=t)
    if checkbox:
        todos.pop(index)
        Function.write_todos(todos)
        del st.session_state[t]
        st.rerun()


st.text_input(label='', placeholder='Add new todo',
              on_change=add_todo, key='new_todo')

