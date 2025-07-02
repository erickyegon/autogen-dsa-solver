"""
Professional Code Template for DSA Solutions
This template ensures robust, error-handled, and well-documented code
"""

from typing import List, Optional, Union, Any
import sys
import traceback

class DSASolution:
    """
    Professional DSA Solution Template with comprehensive error handling
    """
    
    def __init__(self):
        self.debug_mode = False
    
    def validate_input(self, data: Any, expected_type: type, min_length: int = 0) -> bool:
        """
        Comprehensive input validation
        
        Args:
            data: Input data to validate
            expected_type: Expected data type
            min_length: Minimum length for sequences
            
        Returns:
            bool: True if valid, raises exception if invalid
        """
        try:
            # Check for None
            if data is None:
                raise ValueError("Input cannot be None")
            
            # Check type
            if not isinstance(data, expected_type):
                raise TypeError(f"Expected {expected_type.__name__}, got {type(data).__name__}")
            
            # Check length for sequences
            if hasattr(data, '__len__') and len(data) < min_length:
                raise ValueError(f"Input length {len(data)} is less than minimum required {min_length}")
            
            return True
            
        except Exception as e:
            print(f"❌ Input validation failed: {e}")
            raise
    
    def handle_edge_cases(self, data: Any) -> Optional[Any]:
        """
        Handle common edge cases
        
        Args:
            data: Input data
            
        Returns:
            Result for edge case or None if not an edge case
        """
        # Empty input
        if hasattr(data, '__len__') and len(data) == 0:
            if self.debug_mode:
                print("🔍 Edge case: Empty input detected")
            return []
        
        # Single element
        if hasattr(data, '__len__') and len(data) == 1:
            if self.debug_mode:
                print("🔍 Edge case: Single element detected")
            return data
        
        return None
    
    def solve_with_error_handling(self, input_data: Any, algorithm_func, *args, **kwargs) -> Optional[Any]:
        """
        Execute algorithm with comprehensive error handling
        
        Args:
            input_data: Input to the algorithm
            algorithm_func: The algorithm function to execute
            *args, **kwargs: Additional arguments for the algorithm
            
        Returns:
            Algorithm result or None if error occurred
        """
        try:
            # Input validation
            if hasattr(self, 'validate_input_for_problem'):
                self.validate_input_for_problem(input_data)
            
            # Handle edge cases
            edge_result = self.handle_edge_cases(input_data)
            if edge_result is not None:
                return edge_result
            
            # Execute main algorithm
            if self.debug_mode:
                print(f"🚀 Executing algorithm: {algorithm_func.__name__}")
            
            result = algorithm_func(input_data, *args, **kwargs)
            
            if self.debug_mode:
                print(f"✅ Algorithm completed successfully")
            
            return result
            
        except ValueError as ve:
            print(f"❌ Value Error: {ve}")
            print("💡 Suggestion: Check input values and constraints")
            return None
            
        except TypeError as te:
            print(f"❌ Type Error: {te}")
            print("💡 Suggestion: Verify input data types")
            return None
            
        except IndexError as ie:
            print(f"❌ Index Error: {ie}")
            print("💡 Suggestion: Check array bounds and indices")
            return None
            
        except KeyError as ke:
            print(f"❌ Key Error: {ke}")
            print("💡 Suggestion: Verify dictionary keys exist")
            return None
            
        except RecursionError as re:
            print(f"❌ Recursion Error: {re}")
            print("💡 Suggestion: Check for infinite recursion or increase recursion limit")
            return None
            
        except MemoryError as me:
            print(f"❌ Memory Error: {me}")
            print("💡 Suggestion: Optimize algorithm for memory usage")
            return None
            
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")
            print(f"📍 Error Type: {type(e).__name__}")
            if self.debug_mode:
                print("🔍 Full traceback:")
                traceback.print_exc()
            print("💡 Suggestion: Review algorithm logic and implementation")
            return None
    
    def run_comprehensive_tests(self, algorithm_func, test_cases: List[dict]) -> bool:
        """
        Run comprehensive test suite with error handling
        
        Args:
            algorithm_func: Algorithm function to test
            test_cases: List of test case dictionaries with 'input', 'expected', 'description'
            
        Returns:
            bool: True if all tests pass
        """
        print("🧪 RUNNING COMPREHENSIVE TEST SUITE")
        print("=" * 50)
        
        passed = 0
        total = len(test_cases)
        
        for i, test_case in enumerate(test_cases, 1):
            try:
                print(f"\n📋 Test Case {i}: {test_case.get('description', 'No description')}")
                print(f"📥 Input: {test_case['input']}")
                print(f"🎯 Expected: {test_case['expected']}")
                
                # Run the algorithm
                result = self.solve_with_error_handling(test_case['input'], algorithm_func)
                
                print(f"📤 Got: {result}")
                
                # Compare results
                if result == test_case['expected']:
                    print("✅ PASSED")
                    passed += 1
                else:
                    print("❌ FAILED")
                    print(f"💡 Expected {test_case['expected']}, but got {result}")
                
            except Exception as e:
                print(f"❌ TEST ERROR: {e}")
        
        print(f"\n📊 TEST RESULTS: {passed}/{total} tests passed")
        
        if passed == total:
            print("🎉 ALL TESTS PASSED!")
            return True
        else:
            print(f"⚠️  {total - passed} tests failed")
            return False

def create_professional_solution_template():
    """
    Template for creating professional DSA solutions
    """
    template = '''
def solve_problem(input_data):
    """
    Professional solution with comprehensive error handling
    
    Args:
        input_data: Problem input
        
    Returns:
        Solution result or None if error
        
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    solution = DSASolution()
    solution.debug_mode = True  # Enable for debugging
    
    def algorithm_implementation(data):
        """
        Core algorithm implementation
        """
        # TODO: Implement your algorithm here
        # Example structure:
        
        # Step 1: Preprocessing
        processed_data = preprocess(data)
        
        # Step 2: Main algorithm logic
        result = main_algorithm(processed_data)
        
        # Step 3: Post-processing
        final_result = postprocess(result)
        
        return final_result
    
    def validate_input_for_problem(data):
        """Problem-specific input validation"""
        solution.validate_input(data, list, min_length=1)  # Adjust as needed
        # Add more specific validations here
    
    # Attach validation method
    solution.validate_input_for_problem = validate_input_for_problem
    
    # Execute with error handling
    return solution.solve_with_error_handling(input_data, algorithm_implementation)

def main():
    """
    Main function with comprehensive testing
    """
    print("🚀 PROFESSIONAL DSA SOLUTION")
    print("=" * 40)
    
    # Define test cases
    test_cases = [
        {
            'input': [],  # Edge case: empty input
            'expected': [],
            'description': 'Empty input'
        },
        {
            'input': [1],  # Edge case: single element
            'expected': [1],
            'description': 'Single element'
        },
        {
            'input': [1, 2, 3, 4, 5],  # Normal case
            'expected': [1, 2, 3, 4, 5],  # Adjust expected result
            'description': 'Normal case'
        },
        {
            'input': [5, 4, 3, 2, 1],  # Reverse order
            'expected': [1, 2, 3, 4, 5],  # Adjust expected result
            'description': 'Reverse order'
        }
    ]
    
    # Run tests
    solution = DSASolution()
    success = solution.run_comprehensive_tests(solve_problem, test_cases)
    
    if success:
        print("\\n🎯 COMPLEXITY ANALYSIS:")
        print("Time Complexity: O(?)")  # Update with actual complexity
        print("Space Complexity: O(?)")  # Update with actual complexity
        
        print("\\n💡 OPTIMIZATION OPPORTUNITIES:")
        print("- List potential optimizations here")
        
        print("\\n🔍 ALGORITHM EXPLANATION:")
        print("- Explain the algorithm approach")
        print("- Discuss why this approach is optimal")
        print("- Mention alternative approaches")

if __name__ == "__main__":
    main()
'''
    
    return template

if __name__ == "__main__":
    print("📋 Professional Code Template for DSA Solutions")
    print("=" * 50)
    print("This template provides:")
    print("✅ Comprehensive error handling")
    print("✅ Input validation")
    print("✅ Edge case management")
    print("✅ Professional testing framework")
    print("✅ Clear documentation structure")
    print("✅ Debugging capabilities")
    print("\nUse this template to create robust, production-ready DSA solutions!")
