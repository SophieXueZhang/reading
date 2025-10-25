#!/usr/bin/env python3
"""
Reading Comprehension Tool - Web Interface
Streamlit-based visual interface
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import streamlit as st
from difficulty_levels import DifficultyLevel
from reading_passages import PassageDatabase
from questions import QuestionBank
from evaluator import Evaluator
from progress_tracker import ProgressTracker
from api_config import APIConfig

# Page configuration
st.set_page_config(
    page_title="Reading Comprehension Tool",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .passage-card {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .question-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #1E88E5;
        margin: 1rem 0;
    }
    .correct-answer {
        background-color: #C8E6C9;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #4CAF50;
    }
    .wrong-answer {
        background-color: #FFCDD2;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #F44336;
    }
    .stats-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'tracker' not in st.session_state:
    st.session_state.tracker = ProgressTracker()
if 'evaluator' not in st.session_state:
    st.session_state.evaluator = Evaluator()
if 'current_passage' not in st.session_state:
    st.session_state.current_passage = None
if 'current_questions' not in st.session_state:
    st.session_state.current_questions = []
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'selected_grade' not in st.session_state:
    st.session_state.selected_grade = None

def main():
    """Main application"""

    # Header
    st.markdown('<h1 class="main-header">📚 Reading Comprehension Tool</h1>', unsafe_allow_html=True)
    st.markdown("### Improve your reading skills with interactive passages and questions!")

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Choose a page:",
        ["🏠 Home", "📖 Start Reading", "📊 Progress Report", "❓ Help"]
    )

    if page == "🏠 Home":
        show_home()
    elif page == "📖 Start Reading":
        show_reading_practice()
    elif page == "📊 Progress Report":
        show_progress()
    elif page == "❓ Help":
        show_help()

def show_home():
    """Show home page"""

    # API Key Configuration Section
    with st.expander("⚙️ API Configuration", expanded=not APIConfig.is_configured()):
        st.markdown("### OpenAI API Key Setup")
        st.info("💡 Enter your OpenAI API key to enable AI-powered features (optional for current reading tool)")

        # Show current status
        current_key = APIConfig.get_api_key()
        if current_key:
            st.success(f"✓ API Key configured: {APIConfig.mask_api_key(current_key)}")
        else:
            st.warning("⚠️ No API key configured")

        # API Key input
        col1, col2 = st.columns([3, 1])

        with col1:
            new_api_key = st.text_input(
                "Enter your OpenAI API Key:",
                type="password",
                placeholder="sk-proj-...",
                help="Your API key will be saved securely in the .env file"
            )

        with col2:
            st.markdown("<br>", unsafe_allow_html=True)  # Spacing
            if st.button("Save Key", use_container_width=True, type="primary"):
                if new_api_key:
                    is_valid, message = APIConfig.validate_api_key(new_api_key)
                    if is_valid:
                        APIConfig.save_api_key(new_api_key)
                        st.success("✓ API key saved successfully!")
                        st.rerun()
                    else:
                        st.error(f"❌ {message}")
                else:
                    st.warning("Please enter an API key")

        st.caption("🔒 Your API key is stored locally and never shared")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="stats-box">
            <h2>📚</h2>
            <h3>12 Passages</h3>
            <p>Grade K-5</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="stats-box">
            <h2>🎯</h2>
            <h3>8 Question Types</h3>
            <p>Comprehensive Skills</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="stats-box">
            <h2>📈</h2>
            <h3>Progress Tracking</h3>
            <p>Monitor Growth</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Quick stats
    stats = st.session_state.tracker.get_overall_stats()

    if stats['total_passages_read'] > 0:
        st.subheader("Your Quick Stats")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Passages Read", stats['total_passages_read'])
        with col2:
            st.metric("Questions Answered", stats['total_questions_answered'])
        with col3:
            st.metric("Correct Answers", stats['total_correct'])
        with col4:
            st.metric("Accuracy", f"{stats['overall_accuracy']:.1f}%")

    st.markdown("---")

    # Feature overview
    st.subheader("What You'll Learn")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **📖 Reading Skills:**
        - Understanding main ideas
        - Identifying supporting details
        - Making inferences
        - Analyzing characters
        """)

    with col2:
        st.markdown("""
        **🎓 Question Types:**
        - Main Idea & Theme
        - Vocabulary in Context
        - Cause and Effect
        - Sequence of Events
        """)

    st.markdown("---")
    st.info("👈 Use the sidebar to start reading practice or view your progress!")

def show_reading_practice():
    """Show reading practice interface"""
    st.subheader("📖 Reading Practice")

    # Step 1: Select grade level
    if not st.session_state.selected_grade:
        select_grade()

    # Step 2: Select passage
    elif not st.session_state.current_passage:
        select_passage()

    # Step 3: Show passage and questions
    elif not st.session_state.show_results:
        show_passage_and_questions()

    # Step 4: Show results
    else:
        show_session_results()

def select_grade():
    """Grade selection interface"""
    st.markdown("### Step 1: Select Your Grade Level")

    levels = DifficultyLevel.get_all_levels()

    cols = st.columns(3)
    grade_options = ['K', '1', '2', '3', '4', '5']

    for idx, grade in enumerate(grade_options):
        with cols[idx % 3]:
            info = levels[grade]
            button_text = "Kindergarten" if grade == "K" else f"Grade {grade}"
            if st.button(
                button_text,
                key=f"grade_{grade}",
                use_container_width=True
            ):
                st.session_state.selected_grade = grade
                st.rerun()
            st.caption(info['description'])

def select_passage():
    """Passage selection interface"""
    st.markdown(f"### Step 2: Select a Passage (Grade {st.session_state.selected_grade})")

    passages = PassageDatabase.get_passages_by_grade(st.session_state.selected_grade)

    if not passages:
        st.error("No passages available for this grade level.")
        if st.button("← Back to Grade Selection"):
            st.session_state.selected_grade = None
            st.rerun()
        return

    col1, col2 = st.columns(2)

    for idx, passage_data in enumerate(passages):
        with col1 if idx % 2 == 0 else col2:
            with st.container():
                st.markdown(f"**{passage_data['title']}**")
                st.caption(f"Type: {passage_data['type'].title()}")

                if st.button("Read This", key=f"passage_{passage_data['id']}", use_container_width=True):
                    passage = PassageDatabase.get_passage_by_id(passage_data['id'])
                    questions = QuestionBank.get_questions_for_passage(passage_data['id'])

                    st.session_state.current_passage = passage
                    st.session_state.current_questions = questions
                    st.session_state.answers = {}
                    st.session_state.show_results = False
                    st.rerun()

    st.markdown("---")
    if st.button("← Back to Grade Selection"):
        st.session_state.selected_grade = None
        st.rerun()

def show_passage_and_questions():
    """Show passage and questions"""
    passage = st.session_state.current_passage
    questions = st.session_state.current_questions

    # Show passage
    st.markdown(f"### 📖 {passage.title}")
    st.caption(f"Grade {passage.grade} | {passage.type.title()}")

    st.markdown('<div class="passage-card">', unsafe_allow_html=True)
    st.markdown(passage.content)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Show questions
    st.markdown("### 🎯 Comprehension Questions")
    st.info("Read each question carefully and select your answer.")

    for idx, question in enumerate(questions):
        st.markdown(f'<div class="question-card">', unsafe_allow_html=True)
        st.markdown(f"**Question {idx + 1} of {len(questions)}**")
        st.caption(f"Type: {question.type}")
        st.markdown(f"**{question.text}**")

        # Radio buttons for options
        answer = st.radio(
            "Select your answer:",
            options=['A', 'B', 'C', 'D'],
            format_func=lambda x: f"{x}. {question.options[x]}",
            key=f"q_{idx}",
            index=None
        )

        if answer:
            st.session_state.answers[idx] = answer

        st.markdown('</div>', unsafe_allow_html=True)

    # Submit button
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        if len(st.session_state.answers) == len(questions):
            if st.button("Submit Answers", use_container_width=True, type="primary"):
                st.session_state.show_results = True
                st.rerun()
        else:
            st.warning(f"Please answer all {len(questions)} questions before submitting.")

    with col3:
        if st.button("Start Over", use_container_width=True):
            reset_session()
            st.rerun()

def show_session_results():
    """Show results after answering questions"""
    passage = st.session_state.current_passage
    questions = st.session_state.current_questions
    evaluator = st.session_state.evaluator

    st.markdown("### 🎉 Session Results")

    # Evaluate all answers
    results = []
    for idx, question in enumerate(questions):
        user_answer = st.session_state.answers[idx]
        result = evaluator.evaluate_answer(question, user_answer)
        results.append(result)

    # Show summary
    summary = evaluator.generate_performance_summary(results)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Questions", summary['total_questions'])
    with col2:
        st.metric("Correct Answers", summary['correct_answers'])
    with col3:
        st.metric("Accuracy", f"{summary['accuracy']:.1f}%")

    # Performance level
    performance = evaluator.get_performance_level(summary['accuracy'])
    if summary['accuracy'] >= 80:
        st.success(f"🌟 {performance}")
    elif summary['accuracy'] >= 60:
        st.info(f"👍 {performance}")
    else:
        st.warning(f"💪 {performance}")

    st.markdown("---")

    # Show individual results
    st.markdown("### 📝 Question Review")

    for idx, (question, result) in enumerate(zip(questions, results)):
        user_answer = st.session_state.answers[idx]

        if result['correct']:
            st.markdown(f'<div class="correct-answer">', unsafe_allow_html=True)
            st.markdown(f"**✓ Question {idx + 1}: Correct!**")
        else:
            st.markdown(f'<div class="wrong-answer">', unsafe_allow_html=True)
            st.markdown(f"**✗ Question {idx + 1}: Incorrect**")

        st.markdown(f"**{question.text}**")
        st.markdown(f"Your answer: **{user_answer}. {question.options[user_answer]}**")

        if not result['correct']:
            st.markdown(f"Correct answer: **{question.correct_answer}. {question.options[question.correct_answer]}**")

        st.markdown(f"💡 {result['explanation']}")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("")

    # Save progress
    st.session_state.tracker.record_session(
        passage.grade,
        passage.id,
        passage.title,
        results
    )

    st.markdown("---")

    # Action buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Read Another Passage", use_container_width=True, type="primary"):
            reset_session()
            st.rerun()
    with col2:
        if st.button("View Progress Report", use_container_width=True):
            reset_session()
            st.rerun()

def show_progress():
    """Show progress report"""
    st.subheader("📊 Your Progress Report")

    stats = st.session_state.tracker.get_overall_stats()

    if stats['total_passages_read'] == 0:
        st.info("You haven't completed any reading sessions yet. Start practicing to see your progress!")
        return

    # Overall stats
    st.markdown("### Overall Statistics")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Passages Read", stats['total_passages_read'])
    with col2:
        st.metric("Questions Answered", stats['total_questions_answered'])
    with col3:
        st.metric("Correct Answers", stats['total_correct'])
    with col4:
        st.metric("Overall Accuracy", f"{stats['overall_accuracy']:.1f}%")

    # Progress by grade
    st.markdown("### Progress by Grade Level")

    if stats['passages_by_grade']:
        for grade, count in stats['passages_by_grade'].items():
            if count > 0:
                st.markdown(f"**Grade {grade}:** {count} passage(s)")

    # Recent sessions
    st.markdown("### Recent Sessions")
    recent = st.session_state.tracker.get_recent_sessions()

    if recent:
        for session in recent:
            with st.expander(f"{session['passage_title']} (Grade {session['grade']})"):
                st.metric("Accuracy", f"{session['accuracy']:.1f}%")
                st.markdown(f"Correct: {session['correct_answers']}/{session['total_questions']}")

    # Improvement trend
    trend = st.session_state.tracker.get_improvement_trend()
    st.markdown("### Trend")
    st.info(trend)

def show_help():
    """Show help page"""
    st.subheader("❓ Help & Instructions")

    st.markdown("""
    ### How to Use This Tool

    **1. Start Reading Practice:**
    - Choose your grade level (K-5)
    - Select a passage to read
    - Read carefully and take your time
    - Answer comprehension questions
    - Get immediate feedback and explanations

    **2. Question Types:**
    - **Main Idea:** What is the passage mostly about?
    - **Supporting Details:** Specific facts from the text
    - **Inference:** What can you figure out from clues?
    - **Vocabulary:** What do words mean in context?
    - **Sequence:** What happened in order?
    - **Cause and Effect:** Why did things happen?

    **3. Tips for Success:**
    - Read the passage slowly and carefully
    - Think about what you read
    - Reread parts you don't understand
    - Use context clues for unknown words
    - Practice regularly to improve!

    **4. Progress Tracking:**
    - View your overall statistics
    - Track improvement over time
    - Review recent reading sessions
    - Identify areas for improvement
    """)

def reset_session():
    """Reset session state"""
    st.session_state.current_passage = None
    st.session_state.current_questions = []
    st.session_state.answers = {}
    st.session_state.show_results = False
    st.session_state.selected_grade = None

if __name__ == '__main__':
    main()
