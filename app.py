import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Avanish Prajapati | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"  # Expands the sidebar so your photo shows immediately
)

# ----------------- SIDEBAR PROFILE PHOTO & CONTACT -----------------
with st.sidebar:
    # Adding your photo safely with the updated container width parameter
    try:
        st.image("IMG_20260405_142654_104.webp", use_container_width=True)
    except Exception:
        st.info("💡 Place 'IMG_20260405_142654_104.webp' in your project folder to display your profile picture.")
    
    st.markdown("### 🌐 Connect With Me")
    st.write("📞 **Phone:** (+91) 7355421678")
    st.write("📧 **Email:** avanishprajapati324@gmail.com")
    
    # Updated direct URLs to your personal professional profiles
    st.markdown("""
    [🔗 LinkedIn](https://www.linkedin.com/in/avanish-prajapati-49b43b249/) | 
    [💻 LeetCode](https://leetcode.com/u/Avanish1/) | 
    [🐙 GitHub](https://github.com/Avanish2909)
    """)

# ----------------- HEADER SECTION -----------------
st.title("Avanish Prajapati")
st.subheader("AI/ML-focused Software Engineer")
st.write(
    "AI/ML-focused Software Engineer with hands-on experience building real-time systems "
    "using ESP32 and LLM APIs. Strong in Python, REST APIs, and full-stack development. "
    "Built edge-AI applications and mentored 200+ students in programming and AI concepts."
)

st.divider()

# ----------------- KEY METRICS -----------------
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
with metric_col1:
    st.metric(label="DSA Problems Solved", value="800+")
with metric_col2:
    st.metric(label="Students Mentored", value="200+")
with metric_col3:
    st.metric(label="Live Coding Sessions", value="100+")
with metric_col4:
    st.metric(label="Real-world Projects", value="50+")

st.divider()

# ----------------- TECHNICAL SKILLS -----------------
st.header("🛠️ Technical Skills")

st.write("**Languages:** Python, Java, JavaScript")
st.write("**AI/ML & GenAI:** Regression, Classification, CNN, LSTM (Basic), LLMs, RAG, Agentic AI, Prompt Engineering")
st.write("**Backend:** FastAPI, Spring Boot, REST APIs, MySQL, FAISS, ChromaDB")
st.write("**Frontend & Tools:** React.js, Git, Postman, Arduino, ESP32, Streamlit")

st.divider()

# ----------------- PROJECTS -----------------
st.header("🚀 Featured Projects")

with st.expander("🤖 AI Question Bank Generator & Test Simulator", expanded=True):
    st.caption("**Stack:** Python, FastAPI, Streamlit, Gemini 2.5 Flash API, PyPDF, JSON, Git")
    st.write("""
    - Built an automated web portal using Streamlit and a decoupled FastAPI backend on Render to asynchronously process binary PDF uploads and extract raw text streams seamlessly.
    - Integrated Gemini 2.5 Flash LLM to algorithmically analyze document token metrics, dynamically compute exam durations, and generate complex MCQ structures with strict schema enforcement.
    - Designed an intelligent Test Simulator engine featuring continuous multi-page session-state tracking, automated background live countdown timers, and immediate scorecard analytical calculations.
    - Implemented resilient data parsing utilities and custom CORS middleware to sanitize raw unstructured LLM payloads into pristine JSON arrays, eliminating runtime rendering drops.
    """)
    st.link_button("🌐 Open Live App", "https://ai-test-app-z9z8owezbm9p4csuch9dtk.streamlit.app/")

st.markdown("") # Spacing

with st.expander("📄 AI Resume Analyzer & Matchmaker (GenAI)", expanded=True):
    st.caption("**Stack:** Python, Streamlit, Gemini 2.5 Flash API, PyMuPDF, Pandas, Git")
    st.write("""
    - Built an automated web portal using Streamlit and Google Gemini LLM to parse PDF/DOCX resumes and evaluate them against Job Descriptions with high semantic accuracy.
    - Designed an intelligent ATS tracking matrix providing structural feedback on match percentages, keyword gaps, and profile optimizations.
    - Created an automated career matchmaking dashboard that dynamically reads candidate stacks and injects custom URL-encoded LinkedIn query links for live Indian tech opportunities.
    - Leveraged state-handling parameters to maintain data persistence across frontend view switches, eliminating runtime rendering drops.
    """)
    st.link_button("🌐 Open Live App", "https://resumeanalyzer-fhrkmzcsiwxihm8vpoib3m.streamlit.app/")

st.divider()

# ----------------- EXPERIENCE -----------------
st.header("💼 Professional Experience")

st.subheader("Coding and Robotics Trainer | Wizklub Learning Pvt. Ltd.")
st.caption("📅 November 2024 - Present")
st.write("""
- Delivered 100+ live coding sessions, improving student project completion rate by ~40%.
- Mentored 200+ students in AI and programming, enabling them to build 50+ real-world projects.
- Designed structured project roadmaps, improving student presentation quality and technical understanding.
- Conducted robotics workshops integrating ESP32 and IoT concepts.
""")

st.write("")

st.subheader("Software Development Engineer Intern | Bluestock Fintech")
st.caption("📅 June 2024 - August 2024")
st.write("""
- Built and optimized full-stack web modules using JavaScript and MySQL, improving page load performance by ~25%.
- Developed REST-based backend integrations and dynamic UI components.
- Collaborated in Agile sprints, contributing to feature releases and bug fixes.
- Participated in code reviews and implemented performance improvements based on user feedback.
""")

st.divider()

# ----------------- EDUCATION -----------------
st.header("🎓 Education")

edu_col1, edu_col2 = st.columns(2)

with edu_col1:
    st.subheader("Sir Chhotu Ram Institute of Engineering and Technology")
    st.write("B. Tech in Computer Science & Engineering")
    st.caption("📅 Nov 2020 - June 2024 | **CGPA: 7.91**")

with edu_col2:
    st.subheader("Victory Inter College")
    st.write("• **12th (PCM)** — 63.8% (2020)")
    st.write("• **10th** — 74.5% (2018)")

st.divider()
st.caption("Built using Streamlit | Avanish Prajapati © 2026")