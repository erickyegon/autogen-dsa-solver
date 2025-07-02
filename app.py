"""
Enhanced DSA Solver Streamlit App
Production-ready version with comprehensive features and robust error handling
"""

import streamlit as st
import asyncio
import sys
import os

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

# Import enhanced functionality with fallbacks
try:
    from main import get_enhanced_team_and_docker, run_enhanced_team
    from config.constants import SUPPORTED_LANGUAGES, LANGUAGE_CONFIG
    from utils.problem_analyzer import AdvancedProblemAnalyzer
    ENHANCED_AVAILABLE = True
except ImportError as e:
    st.error(f"Enhanced features not available: {e}")
    ENHANCED_AVAILABLE = False

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Enhanced DSA Solver AI",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Header ---
st.title("🚀 Enhanced DSA Solver AI")
st.markdown("**Elite-level algorithmic problem solving with multi-language support**")

if ENHANCED_AVAILABLE:
    st.success("✅ Enhanced features loaded successfully!")
else:
    st.warning("⚠️ Running in basic mode - some features may be limited")

# --- Sidebar ---
with st.sidebar:
    st.header("🎯 Problem Categories")
    
    problem_categories = [
        "📊 Graph Algorithms",
        "🔄 Dynamic Programming", 
        "🌳 Tree & Binary Search",
        "📝 String Algorithms",
        "🔢 Mathematical Problems",
        "📅 Scheduling & Optimization",
        "🏗️ Data Structure Design",
        "⚡ Greedy Algorithms",
        "🔀 Divide & Conquer"
    ]
    
    problem_category = st.selectbox("Select Problem Type:", problem_categories)
    
    st.header("💡 Example Problems")
    
    example_problems = {
        "📊 Graph Algorithms": [
            "Find shortest path between two nodes using Dijkstra's algorithm",
            "Detect cycles in a directed graph using DFS",
            "Find minimum spanning tree of a connected graph"
        ],
        "🔄 Dynamic Programming": [
            "Solve 0/1 knapsack problem with optimization",
            "Find longest common subsequence between two strings",
            "Calculate minimum edit distance between strings"
        ],
        "📅 Scheduling & Optimization": [
            "Schedule tasks with dependencies to minimize completion time",
            "Allocate minimum workers for overlapping tasks",
            "Optimize resource allocation with constraints"
        ],
        "📊 Statistical & R Algorithms": [
            "Implement linear regression with gradient descent in R",
            "Perform statistical analysis to detect outliers",
            "Create time series forecasting using ARIMA model"
        ]
    }
    
    if problem_category in example_problems:
        for example in example_problems[problem_category]:
            if st.button(f"📋 {example[:50]}...", key=example):
                st.session_state.selected_example = example

# --- Main Content ---
st.markdown("---")

# Problem input
st.subheader("📝 Describe Your DSA Problem")
task_input = st.text_area(
    "Enter your problem description:",
    value=st.session_state.get('selected_example', ''),
    height=150,
    placeholder="Example: I have a bunch of tasks that need to be done, like projects at work. Each task has a specific time it's planned to start and a time it's planned to finish..."
)

# Configuration
col1, col2, col3 = st.columns(3)
with col1:
    complexity = st.selectbox("🎚️ Expected Complexity:", ["Easy", "Medium", "Hard", "Expert"])
with col2:
    if ENHANCED_AVAILABLE:
        language = st.selectbox("💻 Preferred Language:", SUPPORTED_LANGUAGES)
    else:
        language = st.selectbox("💻 Preferred Language:", ["Python", "Java", "C++", "JavaScript", "R"])
with col3:
    optimization = st.checkbox("⚡ Focus on Optimization", value=True)

# Language info
if ENHANCED_AVAILABLE and language in LANGUAGE_CONFIG:
    config = LANGUAGE_CONFIG[language]
    st.info(f"🔧 **{language}**: {', '.join(config['strengths'])} | Best for: {', '.join(config['best_for'])}")

# Solve button
solve_button = st.button("🚀 Solve DSA Problem", type="primary")

if solve_button:
    if not task_input.strip():
        st.warning("⚠️ Please enter a DSA problem before clicking 'Solve'.")
    else:
        # Show progress
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Enhanced prompt
        enhanced_prompt = f"""
**Problem Complexity:** {complexity}
**Preferred Language:** {language}
**Optimization Focus:** {'Yes' if optimization else 'No'}
**Problem Category:** {problem_category}

**Problem Description:**
{task_input}

**Requirements:**
- Provide detailed algorithm analysis
- Include time and space complexity
- Show step-by-step solution approach
- Include comprehensive test cases
- Explain optimization opportunities
- Handle edge cases properly
"""
        
        async def solve_problem():
            try:
                # Step 1: Problem Analysis
                status_text.text("🔍 Analyzing problem...")
                progress_bar.progress(20)
                
                if ENHANCED_AVAILABLE:
                    analyzer = AdvancedProblemAnalyzer()
                    analysis = analyzer.analyze_problem(task_input, complexity.lower())
                    
                    st.subheader("🔍 Problem Analysis")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Category:** {analysis.category}")
                        st.write(f"**Difficulty:** {analysis.difficulty}")
                    with col2:
                        st.write(f"**Key Concepts:** {', '.join(analysis.key_concepts[:3])}")
                        st.write(f"**Target Complexity:** {analysis.time_complexity_target}")
                    
                    # Determine problem type for model optimization
                    problem_type = analysis.category.lower().replace(" ", "_")
                else:
                    problem_type = "general"
                
                # Step 2: Team Initialization
                status_text.text("🤖 Initializing AI team...")
                progress_bar.progress(40)
                
                if ENHANCED_AVAILABLE:
                    try:
                        team, docker = await get_enhanced_team_and_docker(problem_type, complexity.lower())
                        st.success(f"✅ Enhanced team ready for {problem_type} problems")
                    except Exception as e:
                        st.warning(f"⚠️ Enhanced team unavailable, using standard team")
                        from main import get_team_and_docker
                        team, docker = await get_team_and_docker()
                else:
                    st.info("🔄 Using basic team configuration")
                    team, docker = None, None
                
                # Step 3: Problem Solving
                status_text.text("🧠 Solving problem...")
                progress_bar.progress(60)
                
                # Create result container
                result_container = st.container()
                
                with result_container:
                    st.subheader("🧠 AI Problem Solving")
                    
                    if ENHANCED_AVAILABLE and team and docker:
                        # Use enhanced team
                        with st.spinner("🤖 AI agents collaborating..."):
                            try:
                                await run_enhanced_team(team, task_input, docker, complexity, language, optimization)
                                st.success("✅ Problem solved successfully!")
                            except Exception as e:
                                st.error(f"❌ Error during solving: {e}")
                                # Provide fallback solution
                                st.info("💡 Providing basic solution approach...")
                                provide_basic_solution(task_input, language, complexity)
                    else:
                        # Provide basic solution
                        st.info("🔧 Generating basic solution...")
                        provide_basic_solution(task_input, language, complexity)
                
                # Step 4: Complete
                status_text.text("✅ Solution complete!")
                progress_bar.progress(100)
                
            except Exception as e:
                st.error(f"❌ Unexpected error: {e}")
                st.info("💡 Try simplifying your problem description or check the system status.")
        
        # Run the async function
        asyncio.run(solve_problem())

def provide_basic_solution(problem, language, complexity):
    """Provide a basic solution when enhanced features aren't available"""
    
    st.markdown("### 🔧 Basic Solution Approach")
    
    # Simple problem categorization
    if any(word in problem.lower() for word in ['graph', 'node', 'edge', 'path']):
        category = "Graph Algorithm"
        suggestions = ["Consider BFS/DFS for traversal", "Use Dijkstra for shortest path", "Apply topological sort for dependencies"]
    elif any(word in problem.lower() for word in ['dynamic', 'optimal', 'maximum', 'minimum']):
        category = "Dynamic Programming"
        suggestions = ["Identify overlapping subproblems", "Define state transitions", "Consider memoization or tabulation"]
    elif any(word in problem.lower() for word in ['sort', 'search', 'array']):
        category = "Array/Sorting Algorithm"
        suggestions = ["Consider merge sort or quicksort", "Use binary search for sorted arrays", "Think about two-pointer techniques"]
    else:
        category = "General Algorithm"
        suggestions = ["Break down the problem into smaller parts", "Consider time/space trade-offs", "Think about edge cases"]
    
    st.write(f"**Detected Category:** {category}")
    
    st.markdown("### 💡 Suggested Approach:")
    for i, suggestion in enumerate(suggestions, 1):
        st.write(f"{i}. {suggestion}")
    
    st.markdown(f"### 💻 {language} Implementation Tips:")
    
    if language == "Python":
        st.code("""
# Python template
def solve_problem(input_data):
    # Input validation
    if not input_data:
        return None
    
    # Main algorithm logic
    result = process_data(input_data)
    
    # Return result
    return result

def process_data(data):
    # Implement your algorithm here
    pass
        """, language="python")
    
    elif language == "R":
        st.code("""
# R template
solve_problem <- function(input_data) {
  # Input validation
  if (is.null(input_data) || length(input_data) == 0) {
    return(NULL)
  }
  
  # Main algorithm logic
  result <- process_data(input_data)
  
  # Return result
  return(result)
}

process_data <- function(data) {
  # Implement your algorithm here
}
        """, language="r")
    
    else:
        st.write(f"💡 Implement your solution in {language} following best practices for the language.")
    
    st.markdown("### 📊 Complexity Analysis:")
    st.write("- **Time Complexity:** Analyze the number of operations")
    st.write("- **Space Complexity:** Consider memory usage")
    st.write("- **Optimization:** Look for redundant operations")

# --- Footer ---
st.markdown("---")
st.markdown("**Developed with AutoGen and Streamlit. Enhanced with multi-language support and advanced AI collaboration.**")

if ENHANCED_AVAILABLE:
    st.success("🚀 **Enhanced Mode Active** - Full AI collaboration with optimized model selection")
else:
    st.info("🔧 **Basic Mode** - Limited functionality, consider installing enhanced dependencies")

# Display system status
with st.expander("🔍 System Status"):
    st.write("**Enhanced Features:**", "✅ Available" if ENHANCED_AVAILABLE else "❌ Not Available")
    if ENHANCED_AVAILABLE:
        st.write("**Supported Languages:**", len(SUPPORTED_LANGUAGES))
        st.write("**Problem Categories:**", len(problem_categories))
        st.write("**AI Models:**", "Optimized selection available")
    else:
        st.write("**Mode:**", "Basic functionality only")
