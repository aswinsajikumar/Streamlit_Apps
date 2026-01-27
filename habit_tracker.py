import streamlit as st

st.title("📅 Daily Habit Tracker")

if "habits" not in st.session_state:
    st.session_state.habits = []

habit = st.text_input("Enter a new habit")

if st.button("Add Habit"):
    if habit:
        st.session_state.habits.append(
            {"habit": habit, "done": False}
        )
        st.success("Habit added")

st.subheader("Today's Habits")

for i, h in enumerate(st.session_state.habits):
    checked = st.checkbox(h["habit"], value=h["done"], key=i)
    st.session_state.habits[i]["done"] = checked