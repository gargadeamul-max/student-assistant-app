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
    ["🏠 Home", "🤖 Student Chatbot", "📚 Study Planner", "📝 Notes", "❓ Quiz Generator"]
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
            q = question.lower()

            if "python" in q:
                answer = """Python is a high-level, interpreted programming language.
It is easy to learn and is widely used in web development, artificial intelligence,
machine learning, data science and automation.

Example:
print("Hello World")"""

            elif "ai" in q or "artificial intelligence" in q:
                answer = """Artificial Intelligence (AI) is a technology that enables
computers to perform tasks that normally require human intelligence, such as
learning, reasoning and understanding language."""

            elif "machine learning" in q:
                answer = """Machine Learning is a branch of AI in which computers
learn patterns from data and use those patterns to make predictions or decisions."""

            else:
                answer = """I can help with common study topics such as Python,
Artificial Intelligence and Machine Learning. Try asking a specific question."""

            st.success(answer)
        else:
            st.warning("Please enter a question.")

elif menu == "📚 Study Planner":
    st.header("📚 Study Planner")

    subject = st.text_input("Subject")
    study_date = st.date_input("Study Date", date.today())
    topic = st.text_input("Topic")
    hours = st.number_input(
        "Study Hours",
        min_value=1,
        max_value=12,
        value=2
    )

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
elif menu == "❓ Quiz Generator":
    st.header("❓ Quiz Generator")

    topic = st.text_input("Enter quiz topic:")

    if st.button("Generate Quiz"):
        if topic.strip():
            st.subheader(f"📚 Quiz: {topic}")

            st.write("**1. What is the main purpose of studying this topic?**")
            st.radio(
                "Choose your answer:",
                ["Learning concepts", "Playing games", "Watching movies", "None"],
                key="q1"
            )

            st.write("**2. Which option is related to the topic?**")
            st.radio(
                "Choose your answer:",
                [topic, "Cooking", "Sports", "Music"],
                key="q2"
            )

            st.write("**3. Why is this topic important?**")
            st.radio(
                "Choose your answer:",
                ["For learning and knowledge", "For sleeping", "For shopping", "None"],
                key="q3"
            )
            st.success("Quiz generated successfully! 🎉")
        else:
            st.warning("Please enter a quiz topic.")
              
