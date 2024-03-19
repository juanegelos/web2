import streamlit as st
import Functions1

todos = Functions1.leer_archivo()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Functions1.escribir_archivo(todos)

st.title(":red[Mi lista de tareas] :sunglasses:")
st.subheader("Esta es mi lista de tareas pendientes", divider=True)
st.write(":red[Las voy a hacer cuando me de la gana]")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        Functions1.escribir_archivo(todos)
        del st.session_state[todo]
        st.experimental_rerun()
 
st.text_input(label="", placeholder="Agregue una tarea...", on_change=add_todo, 
              key="new_todo")

