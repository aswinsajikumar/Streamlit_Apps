import streamlit as st

st.title("📝 To-Do List")

# Create memory for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

task = st.text_input("Enter a new task")

if st.button("Add Task"):
    if task:
        st.session_state.tasks.append(
            {"task": task, "done": False}
        )
        st.success("Task added")

st.subheader("Your Tasks")

for i, t in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4, 1])

    with col1:
        done = st.checkbox(t["task"], value=t["done"], key=f"done_{i}")
        st.session_state.tasks[i]["done"] = done

    with col2:
        if st.button("❌", key=f"delete_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()
