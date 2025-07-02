"""
Simple test to verify the enhanced DSA Solver app functionality
"""

import streamlit as st
import asyncio
import sys
import os

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

# Test basic imports
def test_imports():
    """Test if all required imports work"""
    try:
        from main import get_team_and_docker, get_enhanced_team_and_docker
        from config.constants import SUPPORTED_LANGUAGES, LANGUAGE_CONFIG
        from utils.problem_analyzer import AdvancedProblemAnalyzer
        return True, "All imports successful"
    except Exception as e:
        return False, f"Import error: {e}"

def test_r_support():
    """Test R language support"""
    try:
        from config.constants import SUPPORTED_LANGUAGES, LANGUAGE_CONFIG
        
        if 'R' not in SUPPORTED_LANGUAGES:
            return False, "R not in SUPPORTED_LANGUAGES"
        
        if 'R' not in LANGUAGE_CONFIG:
            return False, "R not in LANGUAGE_CONFIG"
        
        r_config = LANGUAGE_CONFIG['R']
        required_keys = ['file_extension', 'execution_command', 'strengths', 'best_for']
        
        for key in required_keys:
            if key not in r_config:
                return False, f"R config missing {key}"
        
        return True, f"R support complete: {r_config['file_extension']}, {r_config['execution_command']}"
    except Exception as e:
        return False, f"R support test error: {e}"

def test_enhanced_features():
    """Test enhanced features"""
    try:
        from utils.problem_analyzer import AdvancedProblemAnalyzer
        from utils.error_handler import ProfessionalErrorHandler
        from tools.enhanced_dsa_tools import EnhancedDSATools
        
        # Test problem analyzer
        analyzer = AdvancedProblemAnalyzer()
        analysis = analyzer.analyze_problem("Find shortest path in graph", "medium")
        
        if not analysis or not hasattr(analysis, 'category'):
            return False, "Problem analyzer not working"
        
        # Test error handler
        handler = ProfessionalErrorHandler()
        error_analysis = handler.analyze_error("ValueError: invalid input")
        
        if not error_analysis or not hasattr(error_analysis, 'error_type'):
            return False, "Error handler not working"
        
        # Test enhanced tools
        tools = EnhancedDSATools()
        test_cases = tools.generate_test_cases('array', 'medium')
        
        if not test_cases or len(test_cases) == 0:
            return False, "Enhanced tools not working"
        
        return True, f"Enhanced features working: {analysis.category}, {error_analysis.error_type}, {len(test_cases)} test cases"
    except Exception as e:
        return False, f"Enhanced features error: {e}"

async def test_team_creation():
    """Test team creation"""
    try:
        from main import get_enhanced_team_and_docker
        
        # Test basic team creation
        team, docker = await get_enhanced_team_and_docker("general", "medium")
        
        if team is None or docker is None:
            return False, "Team or docker is None"
        
        return True, "Enhanced team created successfully"
    except Exception as e:
        return False, f"Team creation error: {e}"

def main():
    """Run comprehensive app functionality test"""
    st.set_page_config(
        page_title="DSA Solver Test",
        page_icon="🧪",
        layout="centered"
    )
    
    st.title("🧪 DSA Solver App Functionality Test")
    st.markdown("---")
    
    # Test 1: Imports
    st.subheader("1. 📦 Import Test")
    import_success, import_msg = test_imports()
    if import_success:
        st.success(f"✅ {import_msg}")
    else:
        st.error(f"❌ {import_msg}")
    
    # Test 2: R Support
    st.subheader("2. 📊 R Language Support Test")
    r_success, r_msg = test_r_support()
    if r_success:
        st.success(f"✅ {r_msg}")
    else:
        st.error(f"❌ {r_msg}")
    
    # Test 3: Enhanced Features
    st.subheader("3. 🚀 Enhanced Features Test")
    enhanced_success, enhanced_msg = test_enhanced_features()
    if enhanced_success:
        st.success(f"✅ {enhanced_msg}")
    else:
        st.error(f"❌ {enhanced_msg}")
    
    # Test 4: Team Creation
    st.subheader("4. 👥 Team Creation Test")
    if st.button("Test Team Creation"):
        with st.spinner("Creating enhanced team..."):
            try:
                team_success, team_msg = asyncio.run(test_team_creation())
                if team_success:
                    st.success(f"✅ {team_msg}")
                else:
                    st.error(f"❌ {team_msg}")
            except Exception as e:
                st.error(f"❌ Team creation test failed: {e}")
    
    # Test 5: Language Configuration Display
    st.subheader("5. 🌐 Language Configuration")
    try:
        from config.constants import SUPPORTED_LANGUAGES, LANGUAGE_CONFIG
        
        st.write(f"**Supported Languages:** {len(SUPPORTED_LANGUAGES)}")
        for lang in SUPPORTED_LANGUAGES:
            if lang in LANGUAGE_CONFIG:
                config = LANGUAGE_CONFIG[lang]
                st.write(f"- **{lang}**: {config['file_extension']} ({config['execution_command']})")
            else:
                st.write(f"- **{lang}**: ❌ Configuration missing")
    except Exception as e:
        st.error(f"❌ Language configuration error: {e}")
    
    # Test 6: Simple Problem Analysis
    st.subheader("6. 🔍 Problem Analysis Test")
    test_problem = st.text_input("Enter a test problem:", "Find shortest path in a graph")
    
    if st.button("Analyze Problem"):
        try:
            from utils.problem_analyzer import AdvancedProblemAnalyzer
            analyzer = AdvancedProblemAnalyzer()
            analysis = analyzer.analyze_problem(test_problem, "medium")
            
            if analysis:
                st.success("✅ Problem analysis successful!")
                st.write(f"**Category:** {analysis.category}")
                st.write(f"**Suggested Algorithms:** {', '.join(analysis.suggested_algorithms[:3])}")
                st.write(f"**Key Concepts:** {', '.join(analysis.key_concepts[:3])}")
            else:
                st.error("❌ Problem analysis failed")
        except Exception as e:
            st.error(f"❌ Problem analysis error: {e}")
    
    # Summary
    st.markdown("---")
    st.subheader("📊 Test Summary")
    
    total_tests = 3  # Import, R support, Enhanced features
    passed_tests = sum([import_success, r_success, enhanced_success])
    
    if passed_tests == total_tests:
        st.success(f"🎉 All {total_tests} core tests passed! App should work correctly.")
    elif passed_tests >= 2:
        st.warning(f"⚠️ {passed_tests}/{total_tests} tests passed. App may have limited functionality.")
    else:
        st.error(f"❌ Only {passed_tests}/{total_tests} tests passed. App needs fixes.")
    
    # Instructions
    st.markdown("---")
    st.subheader("🚀 Next Steps")
    if passed_tests == total_tests:
        st.info("""
        ✅ **All tests passed!** The main app should work correctly.
        
        **To run the main app:**
        ```bash
        streamlit run app.py
        ```
        
        **Features available:**
        - 5 programming languages (Python, Java, C++, JavaScript, R)
        - Enhanced problem analysis
        - Professional error handling
        - Optimized model selection
        """)
    else:
        st.warning("""
        ⚠️ **Some tests failed.** Please check the error messages above.
        
        **Common fixes:**
        1. Ensure all dependencies are installed: `pip install -r requirements.txt`
        2. Check that Docker is running
        3. Verify environment variables are set
        """)

if __name__ == "__main__":
    main()
