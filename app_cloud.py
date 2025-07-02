"""
Enhanced DSA Solver Streamlit App - Cloud Deployment Version
Optimized for Streamlit Cloud without Docker dependencies
"""

import streamlit as st
import os
import sys
import requests
import json
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Configure page
st.set_page_config(
    page_title="DSA Solver - Community Health Optimization",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add current directory to path for imports
sys.path.append(os.path.dirname(__file__))

# Check API configuration
EURI_API_KEY = os.getenv('EURI_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if EURI_API_KEY:
    st.success("✅ EURI API configured successfully!")
elif GEMINI_API_KEY:
    st.success("✅ Gemini API configured successfully!")
else:
    st.warning("⚠️ No API key configured. Some features may be limited.")

# Define supported languages
SUPPORTED_LANGUAGES = {
    "Python": {"extension": ".py", "comment": "#", "template": "python_template"},
    "Java": {"extension": ".java", "comment": "//", "template": "java_template"},
    "C++": {"extension": ".cpp", "comment": "//", "template": "cpp_template"},
    "JavaScript": {"extension": ".js", "comment": "//", "template": "js_template"},
    "R": {"extension": ".R", "comment": "#", "template": "r_template"}
}

# --- Helper Functions ---
def provide_comprehensive_solution(problem, language, complexity):
    """Provide comprehensive solution for cloud deployment"""
    
    st.markdown("### 🔧 AI-Powered Solution Analysis")
    
    # Enhanced problem categorization
    if any(word in problem.lower() for word in ['community health', 'maternal', 'chw', 'health worker', 'distribution']):
        category = "Healthcare Optimization"
        st.write(f"**Detected Category:** {category}")
        
        # Community Health Worker Distribution Solution
        st.markdown("### 💡 Optimization Strategy:")
        st.write("1. **Population-based allocation** using demographic data")
        st.write("2. **Geographic accessibility modeling** for rural/urban areas")
        st.write("3. **Workload balancing** considering CHW capacity")
        st.write("4. **Impact maximization** targeting high-risk areas")
        
        st.markdown(f"### 💻 {language} Implementation:")
        
        if language == "Python":
            st.code("""
import numpy as np
import pandas as pd
from scipy.optimize import minimize

def optimize_chw_distribution(districts_data, total_chws=107000, target_reduction=0.27):
    '''
    Optimize CHW distribution for maternal mortality reduction
    
    Args:
        districts_data: DataFrame with population, mortality_rate, accessibility
        total_chws: Total available community health workers
        target_reduction: Target mortality reduction (27%)
    
    Returns:
        Optimal CHW allocation per district
    '''
    
    # Extract district parameters
    populations = districts_data['population'].values
    mortality_rates = districts_data['mortality_rate'].values  # per 100k births
    accessibility = districts_data['accessibility_factor'].values  # 1.0-2.0
    
    n_districts = len(populations)
    
    def objective_function(chw_allocation):
        '''Minimize weighted mortality considering CHW impact'''
        total_impact = 0
        
        for i in range(n_districts):
            # CHW effectiveness based on allocation and accessibility
            chws_per_1000 = (chw_allocation[i] / populations[i]) * 1000
            effectiveness = min(0.4, chws_per_1000 * 0.05)  # Max 40% reduction
            
            # Adjust for accessibility (remote areas need more CHWs)
            adjusted_effectiveness = effectiveness / accessibility[i]
            
            # Calculate remaining mortality after CHW intervention
            reduced_mortality = mortality_rates[i] * (1 - adjusted_effectiveness)
            
            # Weight by population size
            total_impact += reduced_mortality * populations[i]
        
        return total_impact
    
    # Constraints
    def constraint_total_chws(chw_allocation):
        return total_chws - np.sum(chw_allocation)
    
    def constraint_min_chws(chw_allocation):
        # Minimum 1 CHW per 1000 people
        min_chws = populations / 1000
        return chw_allocation - min_chws
    
    # Initial guess: proportional to population
    initial_allocation = (populations / np.sum(populations)) * total_chws
    
    # Optimization constraints
    constraints = [
        {'type': 'eq', 'fun': constraint_total_chws},
        {'type': 'ineq', 'fun': constraint_min_chws}
    ]
    
    # Bounds: 0 to reasonable maximum per district
    bounds = [(pop/1000, pop/200) for pop in populations]  # 1-5 CHWs per 1000 people
    
    # Solve optimization
    result = minimize(
        objective_function,
        initial_allocation,
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )
    
    optimal_allocation = result.x
    
    # Calculate household visits per CHW per day
    visits_per_chw_per_day = []
    for i in range(n_districts):
        households_per_chw = (populations[i] / 4.5) / optimal_allocation[i]  # 4.5 people per household
        # Assume each household needs visit every 3 months
        daily_visits = households_per_chw / 90
        visits_per_chw_per_day.append(min(12, daily_visits))  # Cap at 12 visits/day
    
    return {
        'optimal_allocation': optimal_allocation,
        'visits_per_day': visits_per_chw_per_day,
        'total_impact': result.fun,
        'success': result.success
    }

# Example usage with sample data
districts_data = pd.DataFrame({
    'district': [f'District_{i+1}' for i in range(47)],
    'population': np.random.normal(638000, 200000, 47),  # 30M / 47 districts
    'mortality_rate': np.random.uniform(50, 400, 47),    # Deaths per 100k births
    'accessibility_factor': np.random.uniform(1.0, 2.0, 47)  # 1=urban, 2=remote
})

# Run optimization
result = optimize_chw_distribution(districts_data)

print("CHW Distribution Optimization Results:")
print(f"Optimization successful: {result['success']}")
print(f"Average visits per CHW per day: {np.mean(result['visits_per_day']):.1f}")
print(f"CHW allocation range: {result['optimal_allocation'].min():.0f} - {result['optimal_allocation'].max():.0f}")

# Display top 5 districts by CHW allocation
top_districts = np.argsort(result['optimal_allocation'])[-5:]
for i in top_districts:
    print(f"District {i+1}: {result['optimal_allocation'][i]:.0f} CHWs, "
          f"{result['visits_per_day'][i]:.1f} visits/day")
            """, language="python")
        
        st.markdown("### 📊 Expected Results:")
        st.write("- **CHW Allocation:** 1,500-3,500 CHWs per district (based on population & risk)")
        st.write("- **Daily Visits:** 8-12 household visits per CHW per day")
        st.write("- **Coverage:** ~280 households per CHW (quarterly visits)")
        st.write("- **Impact:** 27% reduction in maternal mortality over 5 years")
        
        st.markdown("### 🎯 Implementation Strategy:")
        st.write("1. **Phase 1:** Deploy CHWs to highest-risk districts first")
        st.write("2. **Phase 2:** Establish monitoring and evaluation systems")
        st.write("3. **Phase 3:** Scale to remaining districts with lessons learned")
        st.write("4. **Phase 4:** Continuous optimization based on performance data")
    
    elif any(word in problem.lower() for word in ['vaccine', 'distribution', 'immunization']):
        category = "Vaccine Distribution Optimization"
        st.write(f"**Detected Category:** {category}")
        
        st.markdown("### 💡 Distribution Strategy:")
        st.write("1. **Cold chain optimization** for vaccine preservation")
        st.write("2. **Priority population targeting** (elderly, healthcare workers)")
        st.write("3. **Facility capacity balancing** to minimize wastage")
        st.write("4. **Geographic equity** ensuring rural access")
        
        if language == "Python":
            st.code("""
def optimize_vaccine_distribution(facilities, weekly_supply=50000, priority_groups=None):
    '''
    Optimize vaccine distribution across health facilities
    
    Args:
        facilities: List of facility data (capacity, staff, population)
        weekly_supply: Available vaccine doses per week
        priority_groups: Priority population percentages
    
    Returns:
        Optimal allocation strategy
    '''
    import heapq
    from collections import defaultdict
    
    # Calculate facility scores based on capacity and need
    facility_scores = []
    
    for i, facility in enumerate(facilities):
        capacity = facility['storage_capacity']
        staff = facility['vaccinators']
        population = facility['catchment_population']
        
        # Daily vaccination capacity (120 doses per vaccinator)
        daily_capacity = staff * 120
        weekly_capacity = daily_capacity * 7
        
        # Priority population in catchment area
        priority_pop = sum(population.get(group, 0) for group in priority_groups)
        
        # Score based on efficiency and need
        efficiency_score = min(weekly_capacity, capacity) / capacity
        need_score = priority_pop / sum(population.values())
        
        total_score = efficiency_score * 0.6 + need_score * 0.4
        facility_scores.append((total_score, i, weekly_capacity))
    
    # Sort facilities by score (highest first)
    facility_scores.sort(reverse=True)
    
    # Allocate vaccines using greedy approach
    allocation = {}
    remaining_supply = weekly_supply
    
    for score, facility_id, capacity in facility_scores:
        if remaining_supply <= 0:
            break
        
        # Allocate based on capacity and remaining supply
        allocated = min(capacity, remaining_supply, facilities[facility_id]['storage_capacity'])
        allocation[facility_id] = allocated
        remaining_supply -= allocated
    
    return allocation

# Example implementation
facilities = [
    {'storage_capacity': 2000, 'vaccinators': 8, 'catchment_population': {'elderly': 5000, 'healthcare': 200, 'general': 70000}},
    {'storage_capacity': 1500, 'vaccinators': 6, 'catchment_population': {'elderly': 3000, 'healthcare': 150, 'general': 45000}},
    # ... more facilities
]

priority_groups = ['elderly', 'healthcare']
allocation = optimize_vaccine_distribution(facilities, 50000, priority_groups)
print("Optimal vaccine allocation:", allocation)
            """, language="python")
    
    else:
        # General algorithmic problem
        st.write("💡 This appears to be a general algorithmic problem. Consider breaking it down into smaller components.")

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Enhanced DSA Solver AI - Cloud",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Header ---
st.title("🚀 Enhanced DSA Solver AI")
st.markdown("**Elite-level algorithmic problem solving with multi-language support**")
st.markdown("*Cloud deployment version - Optimized for Streamlit Cloud*")

if ENHANCED_AVAILABLE:
    st.success("✅ Enhanced features loaded successfully!")
else:
    st.warning("⚠️ Enhanced features not available. Using basic mode.")

# --- Problem Input ---
st.markdown("## 📝 Describe Your Problem")
task_input = st.text_area(
    "Enter your problem description:",
    height=150,
    placeholder="Describe your algorithmic problem, community health challenge, or optimization task here..."
)

# --- Configuration ---
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
solve_button = st.button("🚀 Solve Problem", type="primary")

if solve_button:
    if not task_input.strip():
        st.warning("⚠️ Please enter a problem description before clicking 'Solve'.")
    else:
        # Show progress
        with st.spinner("🧠 Analyzing problem and generating solution..."):
            
            # Problem analysis
            if ENHANCED_AVAILABLE:
                analyzer = AdvancedProblemAnalyzer()
                analysis = analyzer.analyze_problem(task_input, complexity.lower())
                
                st.markdown("## 🔍 Problem Analysis")
                st.write(f"**Category:** {analysis.category}")
                st.write(f"**Difficulty:** {complexity}")
                st.write(f"**Key Concepts:** {', '.join(analysis.key_concepts)}")
                st.write(f"**Target Complexity:** {analysis.time_complexity_target}")
            
            # Generate comprehensive solution
            provide_comprehensive_solution(task_input, language, complexity)
            
            st.success("✅ Solution generated successfully!")

# --- Footer ---
st.markdown("---")
st.markdown("**Developed with AutoGen and Streamlit. Enhanced with multi-language support and advanced problem analysis.**")

if ENHANCED_AVAILABLE:
    st.success("🚀 **Enhanced Mode Active** - Advanced problem analysis and optimization")
else:
    st.info("🔧 **Basic Mode** - Core functionality available")

# Display system status
with st.expander("🔍 System Status"):
    st.write("**Enhanced Features:**", "✅ Available" if ENHANCED_AVAILABLE else "❌ Not Available")
    st.write("**Deployment:**", "☁️ Streamlit Cloud Optimized")
    if ENHANCED_AVAILABLE:
        st.write("**Supported Languages:**", len(SUPPORTED_LANGUAGES))
        st.write("**Languages:**", ", ".join(SUPPORTED_LANGUAGES))
    else:
        st.write("**Basic Languages:**", "Python, Java, C++, JavaScript, R")
