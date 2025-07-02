"""
Comprehensive Verification Script for R Language Integration
Checks all components to ensure R support is properly implemented
"""

import sys
import os
import importlib.util

def check_file_exists(filepath, description):
    """Check if a file exists and report status"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} - NOT FOUND")
        return False

def check_content_in_file(filepath, search_text, description):
    """Check if specific content exists in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if search_text in content:
                print(f"✅ {description}: Found in {filepath}")
                return True
            else:
                print(f"❌ {description}: NOT found in {filepath}")
                return False
    except Exception as e:
        print(f"❌ {description}: Error reading {filepath} - {e}")
        return False

def check_import_works(module_path, description):
    """Check if a module can be imported successfully"""
    try:
        spec = importlib.util.spec_from_file_location("test_module", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        print(f"✅ {description}: Import successful")
        return True
    except Exception as e:
        print(f"❌ {description}: Import failed - {e}")
        return False

def main():
    """Run comprehensive verification of R language integration"""
    print("🔍 COMPREHENSIVE R LANGUAGE INTEGRATION VERIFICATION")
    print("=" * 60)
    
    checks_passed = 0
    total_checks = 0
    
    # 1. Check core configuration files
    print("\n📋 1. CONFIGURATION FILES")
    print("-" * 30)
    
    # Constants.py - R language support
    total_checks += 1
    if check_content_in_file("config/constants.py", "'R'", "R in SUPPORTED_LANGUAGES"):
        checks_passed += 1
    
    total_checks += 1
    if check_content_in_file("config/constants.py", "LANGUAGE_CONFIG", "LANGUAGE_CONFIG exists"):
        checks_passed += 1
    
    total_checks += 1
    if check_content_in_file("config/constants.py", "'.R'", "R file extension configured"):
        checks_passed += 1
    
    total_checks += 1
    if check_content_in_file("config/constants.py", "'Rscript'", "R execution command configured"):
        checks_passed += 1
    
    # 2. Check Streamlit app
    print("\n🌐 2. STREAMLIT APPLICATION")
    print("-" * 30)
    
    total_checks += 1
    if check_content_in_file("app.py", '"R"', "R in language selectbox"):
        checks_passed += 1
    
    total_checks += 1
    if check_content_in_file("app.py", "Statistical & R Algorithms", "R-specific examples"):
        checks_passed += 1
    
    # 3. Check agent configuration
    print("\n🤖 3. AGENT CONFIGURATION")
    print("-" * 30)
    
    total_checks += 1
    if check_content_in_file("agents/problem_solver_agent.py", "MULTI-LANGUAGE EXPERTISE", "Multi-language expertise section"):
        checks_passed += 1
    
    total_checks += 1
    if check_content_in_file("agents/problem_solver_agent.py", "**R**: Statistical algorithms", "R expertise description"):
        checks_passed += 1
    
    # 4. Check templates
    print("\n📋 4. CODE TEMPLATES")
    print("-" * 30)
    
    total_checks += 1
    if check_file_exists("templates/r_code_template.R", "R code template"):
        checks_passed += 1
    
    total_checks += 1
    if check_content_in_file("templates/r_code_template.R", "solve_dsa_problem", "R template function"):
        checks_passed += 1
    
    total_checks += 1
    if check_content_in_file("templates/r_code_template.R", "tryCatch", "R error handling"):
        checks_passed += 1
    
    # 5. Check enhanced utilities
    print("\n🛠️ 5. ENHANCED UTILITIES")
    print("-" * 30)
    
    total_checks += 1
    if check_file_exists("utils/problem_analyzer.py", "Problem analyzer"):
        checks_passed += 1
    
    total_checks += 1
    if check_file_exists("utils/error_handler.py", "Error handler"):
        checks_passed += 1
    
    total_checks += 1
    if check_file_exists("utils/visualization.py", "Visualizer"):
        checks_passed += 1
    
    total_checks += 1
    if check_file_exists("tools/enhanced_dsa_tools.py", "Enhanced tools"):
        checks_passed += 1
    
    # 6. Check README documentation
    print("\n📖 6. DOCUMENTATION")
    print("-" * 30)
    
    total_checks += 1
    if check_content_in_file("README.md", "**R**", "R language in README"):
        checks_passed += 1
    
    total_checks += 1
    if check_content_in_file("README.md", "Statistical algorithms", "R capabilities described"):
        checks_passed += 1
    
    total_checks += 1
    if check_content_in_file("README.md", "Languages-5", "Language count badge updated"):
        checks_passed += 1
    
    # 7. Check requirements
    print("\n📦 7. DEPENDENCIES")
    print("-" * 30)
    
    total_checks += 1
    if check_content_in_file("requirements.txt", "matplotlib", "Visualization dependencies"):
        checks_passed += 1
    
    total_checks += 1
    if check_content_in_file("requirements.txt", "networkx", "Graph visualization dependencies"):
        checks_passed += 1
    
    # 8. Test imports
    print("\n🔧 8. IMPORT VERIFICATION")
    print("-" * 30)
    
    # Test if enhanced modules can be imported
    try:
        sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
        from config.constants import SUPPORTED_LANGUAGES, LANGUAGE_CONFIG
        
        total_checks += 1
        if 'R' in SUPPORTED_LANGUAGES:
            print("✅ R in SUPPORTED_LANGUAGES (runtime check)")
            checks_passed += 1
        else:
            print("❌ R NOT in SUPPORTED_LANGUAGES (runtime check)")
        
        total_checks += 1
        if 'R' in LANGUAGE_CONFIG:
            print("✅ R in LANGUAGE_CONFIG (runtime check)")
            checks_passed += 1
            
            # Check R configuration details
            r_config = LANGUAGE_CONFIG['R']
            print(f"   📄 File extension: {r_config.get('file_extension', 'NOT SET')}")
            print(f"   ⚙️ Execution command: {r_config.get('execution_command', 'NOT SET')}")
            print(f"   💪 Strengths: {len(r_config.get('strengths', []))} items")
            print(f"   🎯 Best for: {len(r_config.get('best_for', []))} items")
        else:
            print("❌ R NOT in LANGUAGE_CONFIG (runtime check)")
            
    except ImportError as e:
        print(f"❌ Import test failed: {e}")
        total_checks += 2  # Account for the two checks we couldn't perform
    
    # 9. Test enhanced features
    print("\n🚀 9. ENHANCED FEATURES TEST")
    print("-" * 30)
    
    try:
        from utils.problem_analyzer import AdvancedProblemAnalyzer
        analyzer = AdvancedProblemAnalyzer()
        
        # Test R-specific problem analysis
        r_problem = "Implement linear regression with gradient descent in R"
        analysis = analyzer.analyze_problem(r_problem, "medium")
        
        total_checks += 1
        if analysis and hasattr(analysis, 'category'):
            print("✅ Problem analyzer works with R problems")
            checks_passed += 1
            print(f"   📊 Detected category: {analysis.category}")
        else:
            print("❌ Problem analyzer failed for R problems")
            
    except Exception as e:
        print(f"❌ Enhanced features test failed: {e}")
        total_checks += 1
    
    # Final summary
    print("\n" + "=" * 60)
    print("📊 VERIFICATION SUMMARY")
    print("=" * 60)
    
    success_rate = (checks_passed / total_checks) * 100 if total_checks > 0 else 0
    
    print(f"✅ Checks passed: {checks_passed}/{total_checks}")
    print(f"📈 Success rate: {success_rate:.1f}%")
    
    if success_rate >= 95:
        print("\n🎉 EXCELLENT! R language integration is COMPLETE!")
        print("✅ All components properly updated and configured")
        print("🚀 Enhanced DSA Solver ready for R algorithm problems")
    elif success_rate >= 85:
        print("\n🎯 GOOD! R language integration is mostly complete")
        print("⚠️ Minor issues detected - review failed checks")
    elif success_rate >= 70:
        print("\n⚠️ PARTIAL! R language integration needs attention")
        print("🔧 Several components need updates")
    else:
        print("\n❌ INCOMPLETE! R language integration has major issues")
        print("🛠️ Significant work needed to complete integration")
    
    # Specific R readiness check
    r_ready_checks = [
        'R' in globals().get('SUPPORTED_LANGUAGES', []) if 'SUPPORTED_LANGUAGES' in globals() else False,
        os.path.exists("templates/r_code_template.R"),
        os.path.exists("utils/problem_analyzer.py"),
        success_rate >= 85
    ]
    
    if all(r_ready_checks):
        print("\n🔍 R LANGUAGE READINESS: ✅ READY")
        print("   📝 Configuration: Complete")
        print("   📋 Templates: Available") 
        print("   🛠️ Tools: Functional")
        print("   🎯 Integration: Successful")
    else:
        print("\n🔍 R LANGUAGE READINESS: ❌ NOT READY")
        print("   🔧 Additional work required")
    
    return success_rate >= 85

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
