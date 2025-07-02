"""
Comprehensive Error Handling Utilities for DSA Solver
Provides professional error analysis, debugging, and recovery mechanisms
"""

import traceback
import sys
import re
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass

@dataclass
class ErrorAnalysis:
    """Structured error analysis result"""
    error_type: str
    error_message: str
    line_number: Optional[int]
    column_number: Optional[int]
    suggested_fix: str
    explanation: str
    prevention_tips: List[str]
    code_example: Optional[str] = None

class ProfessionalErrorHandler:
    """
    Professional error handler for DSA problems and code execution
    """
    
    def __init__(self):
        self.common_errors = {
            'IndentationError': {
                'explanation': 'Python requires consistent indentation (4 spaces recommended)',
                'common_causes': ['Mixed tabs and spaces', 'Inconsistent indentation levels', 'Missing indentation after colons'],
                'fix_template': 'Use exactly 4 spaces for each indentation level'
            },
            'SyntaxError': {
                'explanation': 'Code structure violates Python syntax rules',
                'common_causes': ['Missing colons', 'Unmatched parentheses/brackets', 'Invalid variable names'],
                'fix_template': 'Check syntax rules and fix structural issues'
            },
            'ValueError': {
                'explanation': 'Function received argument of correct type but inappropriate value',
                'common_causes': ['Invalid input values', 'Out-of-range parameters', 'Empty sequences'],
                'fix_template': 'Validate input values before processing'
            },
            'IndexError': {
                'explanation': 'Attempted to access index outside sequence bounds',
                'common_causes': ['Array bounds exceeded', 'Empty list access', 'Off-by-one errors'],
                'fix_template': 'Check array bounds and validate indices'
            },
            'TypeError': {
                'explanation': 'Operation performed on inappropriate data type',
                'common_causes': ['Wrong data type passed', 'None values', 'String/number confusion'],
                'fix_template': 'Verify data types and add type checking'
            },
            'KeyError': {
                'explanation': 'Dictionary key does not exist',
                'common_causes': ['Typos in key names', 'Missing keys', 'Case sensitivity'],
                'fix_template': 'Use .get() method or check key existence'
            },
            'RecursionError': {
                'explanation': 'Maximum recursion depth exceeded',
                'common_causes': ['Infinite recursion', 'Missing base case', 'Deep recursion'],
                'fix_template': 'Add proper base case or use iterative approach'
            }
        }
    
    def analyze_error(self, error_message: str, code: str = "") -> ErrorAnalysis:
        """
        Analyze error and provide comprehensive debugging information
        
        Args:
            error_message: The error message from execution
            code: The code that caused the error (optional)
            
        Returns:
            ErrorAnalysis: Structured analysis of the error
        """
        # Extract error type and details
        error_type = self._extract_error_type(error_message)
        line_number, column_number = self._extract_location(error_message)
        
        # Get error-specific information
        error_info = self.common_errors.get(error_type, {
            'explanation': 'An unexpected error occurred',
            'common_causes': ['Unknown cause'],
            'fix_template': 'Review code logic and implementation'
        })
        
        # Generate specific fix suggestion
        suggested_fix = self._generate_fix_suggestion(error_type, error_message, code)
        
        # Create prevention tips
        prevention_tips = self._generate_prevention_tips(error_type)
        
        # Generate code example if applicable
        code_example = self._generate_code_example(error_type, error_message)
        
        return ErrorAnalysis(
            error_type=error_type,
            error_message=error_message,
            line_number=line_number,
            column_number=column_number,
            suggested_fix=suggested_fix,
            explanation=error_info['explanation'],
            prevention_tips=prevention_tips,
            code_example=code_example
        )
    
    def _extract_error_type(self, error_message: str) -> str:
        """Extract error type from error message"""
        # Look for common error patterns
        for error_type in self.common_errors.keys():
            if error_type in error_message:
                return error_type
        
        # Try to extract from traceback format
        match = re.search(r'(\w+Error):', error_message)
        if match:
            return match.group(1)
        
        return "UnknownError"
    
    def _extract_location(self, error_message: str) -> Tuple[Optional[int], Optional[int]]:
        """Extract line and column numbers from error message"""
        line_match = re.search(r'line (\d+)', error_message)
        line_number = int(line_match.group(1)) if line_match else None
        
        # Look for column information (less common)
        col_match = re.search(r'column (\d+)', error_message)
        column_number = int(col_match.group(1)) if col_match else None
        
        return line_number, column_number
    
    def _generate_fix_suggestion(self, error_type: str, error_message: str, code: str) -> str:
        """Generate specific fix suggestion based on error type and context"""
        
        if error_type == "IndentationError":
            if "expected an indented block" in error_message:
                return "Add proper indentation (4 spaces) after the function definition, if statement, or loop"
            elif "unindent does not match" in error_message:
                return "Ensure consistent indentation levels throughout the code block"
            else:
                return "Fix indentation by using exactly 4 spaces for each level"
        
        elif error_type == "SyntaxError":
            if "invalid syntax" in error_message:
                return "Check for missing colons, unmatched parentheses, or invalid keywords"
            elif "EOF while scanning" in error_message:
                return "Add missing closing parenthesis, bracket, or quote"
            else:
                return "Review Python syntax rules and fix structural issues"
        
        elif error_type == "ValueError":
            return "Add input validation to check for valid values before processing"
        
        elif error_type == "IndexError":
            return "Add bounds checking: if 0 <= index < len(array) before accessing"
        
        elif error_type == "TypeError":
            return "Add type checking and ensure correct data types are used"
        
        elif error_type == "KeyError":
            return "Use dict.get(key, default) or check if key exists before accessing"
        
        elif error_type == "RecursionError":
            return "Add proper base case or convert to iterative solution"
        
        else:
            return f"Review the {error_type} and check algorithm logic"
    
    def _generate_prevention_tips(self, error_type: str) -> List[str]:
        """Generate prevention tips for specific error types"""
        
        tips_map = {
            "IndentationError": [
                "Use a consistent text editor with visible whitespace",
                "Configure editor to use 4 spaces instead of tabs",
                "Use Python linters like pylint or flake8"
            ],
            "SyntaxError": [
                "Use an IDE with syntax highlighting",
                "Write code incrementally and test frequently",
                "Use parentheses to clarify complex expressions"
            ],
            "ValueError": [
                "Always validate input parameters",
                "Use try-except blocks for risky operations",
                "Add assertions for expected value ranges"
            ],
            "IndexError": [
                "Always check array bounds before accessing",
                "Use enumerate() for safe iteration with indices",
                "Consider using .get() for dictionaries"
            ],
            "TypeError": [
                "Use type hints in function definitions",
                "Add isinstance() checks for critical operations",
                "Validate input types at function entry"
            ],
            "KeyError": [
                "Use dict.get() with default values",
                "Check key existence with 'in' operator",
                "Use defaultdict for automatic key creation"
            ],
            "RecursionError": [
                "Always define clear base cases",
                "Consider iterative alternatives for deep recursion",
                "Use sys.setrecursionlimit() carefully if needed"
            ]
        }
        
        return tips_map.get(error_type, ["Review code logic and best practices"])
    
    def _generate_code_example(self, error_type: str, error_message: str) -> Optional[str]:
        """Generate corrected code example for common errors"""
        
        examples = {
            "IndentationError": '''
# ❌ Incorrect:
def solve_problem():
"""Docstring"""
return result

# ✅ Correct:
def solve_problem():
    """Docstring"""
    return result
''',
            "IndexError": '''
# ❌ Incorrect:
arr = [1, 2, 3]
print(arr[3])  # IndexError

# ✅ Correct:
arr = [1, 2, 3]
if len(arr) > 3:
    print(arr[3])
else:
    print("Index out of bounds")
''',
            "ValueError": '''
# ❌ Incorrect:
def process_data(data):
    return int(data)  # ValueError if data is not numeric

# ✅ Correct:
def process_data(data):
    try:
        return int(data)
    except ValueError:
        print(f"Invalid data: {data}")
        return None
''',
            "TypeError": '''
# ❌ Incorrect:
def add_numbers(a, b):
    return a + b  # TypeError if a or b is None

# ✅ Correct:
def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b
'''
        }
        
        return examples.get(error_type)
    
    def format_error_report(self, analysis: ErrorAnalysis) -> str:
        """Format error analysis into a comprehensive report"""
        
        report = f"""
🚨 **ERROR ANALYSIS REPORT**
{'=' * 50}

❌ **Error Type:** {analysis.error_type}
📍 **Location:** Line {analysis.line_number or 'Unknown'}
💬 **Message:** {analysis.error_message}

🔍 **Explanation:**
{analysis.explanation}

🔧 **Suggested Fix:**
{analysis.suggested_fix}

💡 **Prevention Tips:**
"""
        
        for i, tip in enumerate(analysis.prevention_tips, 1):
            report += f"{i}. {tip}\n"
        
        if analysis.code_example:
            report += f"\n📝 **Code Example:**\n{analysis.code_example}"
        
        report += "\n" + "=" * 50
        
        return report

def create_robust_code_wrapper(code: str) -> str:
    """
    Wrap user code with comprehensive error handling
    
    Args:
        code: User's algorithm code
        
    Returns:
        Enhanced code with error handling
    """
    
    wrapper = f'''
import traceback
import sys
from typing import Any, Optional

def execute_with_error_handling():
    """Execute user code with comprehensive error handling"""
    try:
        # User's code starts here
{code}
        
        # If we reach here, code executed successfully
        print("✅ Code executed successfully!")
        
    except IndentationError as e:
        print("❌ INDENTATION ERROR")
        print(f"🔍 Issue: {{e}}")
        print("💡 Fix: Use exactly 4 spaces for indentation")
        print("📝 Example:")
        print("def function():")
        print("    # 4 spaces here")
        print("    return result")
        
    except SyntaxError as e:
        print("❌ SYNTAX ERROR")
        print(f"🔍 Issue: {{e}}")
        print("💡 Fix: Check for missing colons, parentheses, or quotes")
        
    except ValueError as e:
        print("❌ VALUE ERROR")
        print(f"🔍 Issue: {{e}}")
        print("💡 Fix: Validate input values before processing")
        
    except IndexError as e:
        print("❌ INDEX ERROR")
        print(f"🔍 Issue: {{e}}")
        print("💡 Fix: Check array bounds before accessing")
        
    except TypeError as e:
        print("❌ TYPE ERROR")
        print(f"🔍 Issue: {{e}}")
        print("💡 Fix: Verify data types and add type checking")
        
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {{type(e).__name__}}")
        print(f"🔍 Issue: {{e}}")
        print("💡 Fix: Review algorithm logic and implementation")
        print("🔍 Full traceback:")
        traceback.print_exc()

# Execute the wrapped code
execute_with_error_handling()
'''
    
    return wrapper

if __name__ == "__main__":
    # Demo the error handler
    handler = ProfessionalErrorHandler()
    
    # Example error analysis
    sample_error = "IndentationError: expected an indented block after function definition on line 4"
    analysis = handler.analyze_error(sample_error)
    
    print(handler.format_error_report(analysis))
