import streamlit as st
from datetime import date

st.set_page_config(
    page_title="AI-Powered Student Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI-Powered Student Assistant")
st.write("Your simple digital assistant for study, planning and notes.")

menu = st.sidebar.selectbox(
    "Choose an option",
    ["🏠 Home", "🤖 Student Chatbot", "📚 Study Planner", "📝 Notes"]
)

if menu == "🏠 Home":
    st.header("Welcome! 👋")
    st.write("This app helps students organize their studies.")
    
    st.info("Use the menu on the left to start.")

elif menu == "🤖 Student Chatbot":
    st.header("🤖 Student Chatbot")

    question = st.text_input("Ask your study question:")

    if st.button("Get Answer"):
        if question.strip():
            st.success(
                "Keep learning! For your question: "
                + question
                + "\n\nTry understanding the topic step-by-step and practice with examples."
            )
        else:
            st.warning("Please enter a question.")

elif menu == "📚 Study Planner":
    st.header("📚 Study Planner")

    subject = st.text_input("Subject")
    study_date = st.date_input("Study Date", date.today())
    topic = st.text_input("Topic")
    hours = st.number_input("Study Hours", min_value=1, max_value=12, value=2)

    if st.button("Create Study Plan"):
        if subject and topic:
            st.success("Study plan created!")
            st.write("📖 Subject:", subject)
            st.write("📅 Date:", study_date)
            st.write("📌 Topic:", topic)
            st.write("⏰ Study Hours:", hours)
        else:
            st.warning("Please enter subject and topic.")

elif menu == "📝 Notes":
    st.header("📝 My Notes")

    note_title = st.text_input("Note Title")
    note = st.text_area("Write your notes here:")

    if st.button("Save Note"):
        if note_title and note:
            st.success("Note saved successfully!")
            st.write("###", note_title)
            st.write(note)
        else:
            st.warning("Please enter a title and note.")
