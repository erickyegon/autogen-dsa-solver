import streamlit as st
import asyncio
from typing import AsyncGenerator

# Assuming these imports are correct based on your project structure
# You might need to adjust the paths if your project structure changes
from main import get_team_and_docker
from config.docker_utils import start_docker_executor, stop_docker_executor
# from config.model_client import get_model_client # Not directly used in the provided snippet
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="DSA Solver AI",
    page_icon="🧠", # Brain icon for problem solving
    layout="centered", # Can be "wide" for more content horizontally
    initial_sidebar_state="expanded" # Or "collapsed"
)

# --- Custom CSS for a professional look ---
st.markdown("""
    <style>
    /* General body styling */
    body {
        font-family: 'Segoe UI', sans-serif;
        color: #333;
        background-color: #f0f2f6; /* Light gray background */
    }
    
    /* Header styling */
    h1 {
        color: #2c3e50; /* Darker blue-gray for titles */
        text-align: center;
        margin-bottom: 20px;
        font-size: 2.5em;
        font-weight: 700;
    }
    
    /* Subheader/description styling */
    .stMarkdown p {
        color: #555;
        text-align: center;
        margin-bottom: 40px;
        font-size: 1.1em;
    }
    
    /* Input field styling */
    .stTextInput label {
        font-weight: 600;
        color: #2c3e50;
    }
    .stTextInput input[type="text"] {
        border-radius: 8px;
        border: 1px solid #ced4da;
        padding: 10px 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05); /* Subtle shadow */
        transition: all 0.3s ease;
    }
    .stTextInput input[type="text"]:focus {
        border-color: #007bff; /* Blue border on focus */
        box-shadow: 0 0 0 0.2rem rgba(0,123,255,.25);
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #007bff; /* Primary blue */
        color: white;
        border-radius: 8px;
        padding: 12px 25px;
        font-size: 1.1em;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 10px rgba(0,123,255,0.2);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #0056b3; /* Darker blue on hover */
        box-shadow: 0 6px 15px rgba(0,123,255,0.3);
    }
    .stButton > button:active {
        background-color: #004085;
        box-shadow: none;
    }
    
    /* Streamlit chat message containers */
    .stChatMessage {
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .stChatMessage [data-element-type="markdown-container"] {
        padding: 0 !important; /* Remove internal padding if any */
        margin: 0 !important;
    }

    /* Specific chat message styling for differentiation */
    .stChatMessage[data-testid="stChatMessage"] {
        background-color: #e9ecef; /* Light gray for agent messages */
        border-left: 5px solid #6c757d; /* Gray border */
    }

    .stChatMessage[data-testid="stChatMessage"][data-avatar="👤"] {
        background-color: #d1e7dd; /* Light green for user messages */
        border-left: 5px solid #28a745; /* Green border */
    }
    
    /* Message content styling */
    .stChatMessage p {
        margin: 0;
        font-size: 1.0em;
        line-height: 1.6;
    }

    /* Container for the main interaction area */
    .main .block-container {
        max-width: 800px; /* Limit width for better readability */
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    /* Status messages (e.g., 'Solving your question...') */
    .stStatus {
        color: #007bff;
        font-style: italic;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Application Title and Description ---
st.title("🧠 DSA Code AI Helper")
st.markdown("Unlock efficient solutions for your Data Structures and Algorithms problems with the power of AI.")

# --- Input Section ---
st.subheader("Your DSA Challenge:")
task_input = st.text_area(
    "Describe your DSA problem in detail:",
    value='Can you give me a solution to add 2 numbers using Python?',
    height=150,
    help="Be as specific as possible for better results. Include constraints, desired language, etc."
)

# --- Global state for conversation (optional but good for context) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display previous messages ---
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user", avatar="👤"):
            st.markdown(msg["content"])
    elif msg["role"] == "ProblemSolverExpert":
        with st.chat_message("ProblemSolverExpert", avatar="🧑‍💻"):
            st.markdown(msg["content"])
    elif msg["role"] == "CodeExecutorAgent":
        with st.chat_message("CodeExecutorAgent", avatar="🤖"):
            st.markdown(msg["content"])
    else: # Default for other types or initial messages
        st.info(msg["content"]) # Use st.info for "Task Result" etc.

# --- Core Logic for Running Autogen Team ---
async def run_autogen_team(team, task: str, docker) -> AsyncGenerator[dict, None]:
    """
    Runs the Autogen team and yields messages in a structured format.
    """
    try:
        # Using st.status for a better user experience during long operations
        with st.status("Initializing AI team and Docker environment...", expanded=True) as status:
            status.update(label="Starting Docker Executor...", state="running", expanded=True)
            await start_docker_executor(docker)
            status.update(label="Docker Executor Ready. Dispatching task...", state="running", expanded=True)

            async for message in team.run_stream(task=task):
                if isinstance(message, TextMessage):
                    role = message.source
                    content = f"{message.source}: {message.content}"
                    status.update(label=f"AI Team working: {message.source}", state="running")
                    yield {"role": role, "content": content}
                elif isinstance(message, TaskResult):
                    stop_reason = message.stop_reason if message.stop_reason else "Task completed."
                    content = f"Task Result: {stop_reason}"
                    status.update(label="Task Completed!", state="complete", expanded=False)
                    yield {"role": "system", "content": content}
                    break # Stop looping after TaskResult
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        st.exception(e) # Show full traceback in debug mode
        yield {"role": "error", "content": f"Error: {e}"}
    finally:
        if docker:
            with st.status("Stopping Docker Executor...", expanded=True) as status:
                await stop_docker_executor(docker)
                status.update(label="Docker Executor Stopped.", state="complete", expanded=False)

# --- Button to Trigger Solving ---
if st.button("Solve DSA Problem"):
    if not task_input.strip():
        st.warning("Please enter a DSA question before clicking 'Solve'.")
    else:
        st.session_state.messages.append({"role": "user", "content": f"user: {task_input}"})
        # Use a placeholder for dynamic updates
        chat_placeholder = st.empty()

        async def stream_messages():
            team, docker = await get_team_and_docker() # Get team and docker only once
            full_response = ""
            for message_data in st.session_state.messages:
                if message_data["role"] == "user":
                    with chat_placeholder.chat_message("user", avatar="👤"):
                        st.markdown(message_data["content"])
                elif message_data["role"] == "ProblemSolverExpert":
                    with chat_placeholder.chat_message("ProblemSolverExpert", avatar="🧑‍💻"):
                        st.markdown(message_data["content"])
                elif message_data["role"] == "CodeExecutorAgent":
                    with chat_placeholder.chat_message("CodeExecutorAgent", avatar="🤖"):
                        st.markdown(message_data["content"])
                else:
                    with chat_placeholder:
                        st.info(message_data["content"])


            async for msg_data in run_autogen_team(team, task_input, docker):
                st.session_state.messages.append(msg_data)
                # Display new message immediately
                with chat_placeholder: # This will create a new chat message section
                    if msg_data["role"] == "user": # This shouldn't happen unless you append user message again
                        st.chat_message("user", avatar="👤").markdown(msg_data["content"])
                    elif msg_data["role"] == "ProblemSolverExpert":
                        st.chat_message("ProblemSolverExpert", avatar="🧑‍💻").markdown(msg_data["content"])
                    elif msg_data["role"] == "CodeExecutorAgent":
                        st.chat_message("CodeExecutorAgent", avatar="🤖").markdown(msg_data["content"])
                    else: # For TaskResult or system messages
                        st.info(msg_data["content"]) # Use info for system messages

        # Run the async function
        asyncio.run(stream_messages())

# --- Footer or additional info ---
st.markdown("---")
st.markdown("Developed with Autogen and Streamlit. For educational purposes only.")
st.markdown("[GitHub Repo](https://github.com/erickyegon/autogen-dsa-solver.git)")