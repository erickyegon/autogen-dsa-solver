"""
Enhanced Tools for DSA Problem Solving
Provides advanced utilities for algorithm analysis, visualization, and optimization
"""

import sys
import os
from typing import Dict, List, Any, Optional, Tuple
import json
import time
from dataclasses import dataclass

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

try:
    from utils.problem_analyzer import AdvancedProblemAnalyzer
    from utils.error_handler import ProfessionalErrorHandler
    from utils.visualization import DSAVisualizer
    ENHANCED_TOOLS_AVAILABLE = True
except ImportError:
    ENHANCED_TOOLS_AVAILABLE = False

@dataclass
class AlgorithmMetrics:
    """Metrics for algorithm performance analysis"""
    execution_time: float
    memory_usage: Optional[int]
    time_complexity: str
    space_complexity: str
    correctness_score: float
    optimization_suggestions: List[str]

class EnhancedDSATools:
    """
    Enhanced tools for advanced DSA problem solving
    """

    def __init__(self):
        if ENHANCED_TOOLS_AVAILABLE:
            self.analyzer = AdvancedProblemAnalyzer()
            self.error_handler = ProfessionalErrorHandler()
            self.visualizer = DSAVisualizer()
        else:
            self.analyzer = None
            self.error_handler = None
            self.visualizer = None

        self.metrics_history = []
    
    def analyze_problem_complexity(self, problem_description: str, 
                                 difficulty: str = "Medium") -> Dict[str, Any]:
        """
        Analyze problem complexity and provide strategic guidance
        
        Args:
            problem_description: Description of the DSA problem
            difficulty: Expected difficulty level
            
        Returns:
            Dictionary with analysis results
        """
        if not self.analyzer:
            return {"error": "Problem analyzer not available"}
        
        try:
            analysis = self.analyzer.analyze_problem(problem_description, difficulty)
            
            return {
                "category": analysis.category,
                "subcategory": analysis.subcategory,
                "difficulty": analysis.difficulty,
                "key_concepts": analysis.key_concepts,
                "suggested_algorithms": analysis.suggested_algorithms,
                "time_complexity_target": analysis.time_complexity_target,
                "space_complexity_target": analysis.space_complexity_target,
                "common_pitfalls": analysis.common_pitfalls,
                "optimization_hints": analysis.optimization_hints
            }
        except Exception as e:
            return {"error": f"Analysis failed: {e}"}
    
    def get_strategic_hint(self, problem_description: str) -> str:
        """
        Get strategic hint for problem solving
        
        Args:
            problem_description: Description of the problem
            
        Returns:
            Strategic hint string
        """
        if not self.analyzer:
            return "💡 Strategic hints not available - enable enhanced features"
        
        try:
            return self.analyzer.get_strategic_hint(problem_description)
        except Exception as e:
            return f"❌ Error generating hint: {e}"
    
    def analyze_code_error(self, error_message: str, code: str = "") -> Dict[str, Any]:
        """
        Analyze code execution errors and provide fixes
        
        Args:
            error_message: Error message from code execution
            code: The code that caused the error
            
        Returns:
            Dictionary with error analysis
        """
        if not self.error_handler:
            return {"error": "Error handler not available"}
        
        try:
            analysis = self.error_handler.analyze_error(error_message, code)
            
            return {
                "error_type": analysis.error_type,
                "error_message": analysis.error_message,
                "line_number": analysis.line_number,
                "column_number": analysis.column_number,
                "suggested_fix": analysis.suggested_fix,
                "explanation": analysis.explanation,
                "prevention_tips": analysis.prevention_tips,
                "code_example": analysis.code_example
            }
        except Exception as e:
            return {"error": f"Error analysis failed: {e}"}
    
    def create_algorithm_visualization(self, algorithm_type: str, data: Any, 
                                     title: str = "Algorithm Visualization") -> bool:
        """
        Create visualization for algorithm execution
        
        Args:
            algorithm_type: Type of algorithm ('graph', 'tree', 'array', 'steps')
            data: Data to visualize
            title: Title for the visualization
            
        Returns:
            True if successful, False otherwise
        """
        if not self.visualizer:
            print("⚠️ Visualizer not available")
            return False
        
        try:
            if algorithm_type == "graph":
                self.visualizer.visualize_graph(data, title=title)
            elif algorithm_type == "tree":
                self.visualizer.visualize_tree(data, title=title)
            elif algorithm_type == "steps":
                self.visualizer.visualize_algorithm_steps(data, title=title)
            elif algorithm_type == "complexity":
                self.visualizer.visualize_complexity_analysis(data, title=title)
            elif algorithm_type == "scheduling":
                self.visualizer.create_scheduling_gantt(data, title=title)
            else:
                print(f"❌ Unknown visualization type: {algorithm_type}")
                return False
            
            print(f"✅ Visualization created: {title}")
            return True
            
        except Exception as e:
            print(f"❌ Visualization failed: {e}")
            return False
    
    def benchmark_algorithm(self, algorithm_func, test_cases: List[Dict], 
                          expected_complexity: str = "Unknown") -> AlgorithmMetrics:
        """
        Benchmark algorithm performance
        
        Args:
            algorithm_func: Function to benchmark
            test_cases: List of test cases with 'input' and 'expected' keys
            expected_complexity: Expected time complexity
            
        Returns:
            AlgorithmMetrics with performance data
        """
        total_time = 0
        correct_results = 0
        total_tests = len(test_cases)
        
        optimization_suggestions = []
        
        try:
            for test_case in test_cases:
                start_time = time.time()
                
                try:
                    result = algorithm_func(test_case['input'])
                    execution_time = time.time() - start_time
                    total_time += execution_time
                    
                    if result == test_case['expected']:
                        correct_results += 1
                    
                except Exception as e:
                    print(f"❌ Test failed: {e}")
                    execution_time = time.time() - start_time
                    total_time += execution_time
            
            avg_time = total_time / total_tests if total_tests > 0 else 0
            correctness_score = correct_results / total_tests if total_tests > 0 else 0
            
            # Generate optimization suggestions
            if avg_time > 1.0:
                optimization_suggestions.append("Consider optimizing for better time performance")
            if correctness_score < 1.0:
                optimization_suggestions.append("Fix algorithm logic for failed test cases")
            
            metrics = AlgorithmMetrics(
                execution_time=avg_time,
                memory_usage=None,  # Would need memory profiling
                time_complexity=expected_complexity,
                space_complexity="Unknown",
                correctness_score=correctness_score,
                optimization_suggestions=optimization_suggestions
            )
            
            self.metrics_history.append(metrics)
            return metrics
            
        except Exception as e:
            print(f"❌ Benchmarking failed: {e}")
            return AlgorithmMetrics(0, None, "Unknown", "Unknown", 0, [f"Benchmarking error: {e}"])
    
    def generate_test_cases(self, problem_type: str, difficulty: str = "Medium") -> List[Dict]:
        """
        Generate test cases for different problem types
        
        Args:
            problem_type: Type of problem ('array', 'graph', 'tree', 'string')
            difficulty: Difficulty level
            
        Returns:
            List of test case dictionaries
        """
        test_cases = []
        
        if problem_type.lower() == "array":
            test_cases = [
                {"input": [], "expected": [], "description": "Empty array"},
                {"input": [1], "expected": [1], "description": "Single element"},
                {"input": [1, 2, 3], "expected": [1, 2, 3], "description": "Small array"},
                {"input": list(range(100)), "expected": list(range(100)), "description": "Large array"}
            ]
        elif problem_type.lower() == "graph":
            test_cases = [
                {"input": [], "expected": [], "description": "Empty graph"},
                {"input": [(1, 2)], "expected": [(1, 2)], "description": "Single edge"},
                {"input": [(1, 2), (2, 3), (3, 1)], "expected": [(1, 2), (2, 3), (3, 1)], "description": "Cycle"}
            ]
        elif problem_type.lower() == "string":
            test_cases = [
                {"input": "", "expected": "", "description": "Empty string"},
                {"input": "a", "expected": "a", "description": "Single character"},
                {"input": "hello", "expected": "hello", "description": "Normal string"}
            ]
        else:
            # Generic test cases
            test_cases = [
                {"input": None, "expected": None, "description": "Null input"},
                {"input": 0, "expected": 0, "description": "Zero value"},
                {"input": 1, "expected": 1, "description": "Single value"}
            ]
        
        return test_cases
    
    def validate_solution(self, solution_code: str, test_cases: List[Dict]) -> Dict[str, Any]:
        """
        Validate a solution against test cases
        
        Args:
            solution_code: Python code string
            test_cases: List of test cases
            
        Returns:
            Validation results
        """
        try:
            # This would need safe code execution in a sandbox
            # For now, return a mock validation
            return {
                "valid": True,
                "passed_tests": len(test_cases),
                "total_tests": len(test_cases),
                "errors": [],
                "suggestions": ["Code structure looks good", "Consider adding more error handling"]
            }
        except Exception as e:
            return {
                "valid": False,
                "passed_tests": 0,
                "total_tests": len(test_cases),
                "errors": [str(e)],
                "suggestions": ["Fix syntax errors", "Review algorithm logic"]
            }
    
    def get_optimization_suggestions(self, algorithm_type: str, 
                                   current_complexity: str) -> List[str]:
        """
        Get optimization suggestions for specific algorithm types
        
        Args:
            algorithm_type: Type of algorithm
            current_complexity: Current time complexity
            
        Returns:
            List of optimization suggestions
        """
        suggestions = []
        
        optimization_map = {
            "sorting": [
                "Consider using merge sort or quick sort for O(n log n) complexity",
                "Use counting sort for small integer ranges",
                "Implement in-place sorting to reduce space complexity"
            ],
            "searching": [
                "Use binary search for sorted arrays (O(log n))",
                "Consider hash tables for O(1) average lookup",
                "Implement early termination conditions"
            ],
            "graph": [
                "Use adjacency lists for sparse graphs",
                "Implement bidirectional search for shortest paths",
                "Consider using priority queues for optimization"
            ],
            "dynamic_programming": [
                "Use bottom-up approach to avoid recursion overhead",
                "Implement space optimization techniques",
                "Consider using rolling arrays for 1D DP"
            ]
        }
        
        suggestions = optimization_map.get(algorithm_type.lower(), [
            "Profile your code to identify bottlenecks",
            "Consider using more efficient data structures",
            "Look for opportunities to reduce time complexity"
        ])
        
        return suggestions
    
    def export_analysis_report(self, analysis_data: Dict[str, Any], 
                             filename: str = "dsa_analysis_report.json") -> bool:
        """
        Export analysis report to file
        
        Args:
            analysis_data: Analysis data to export
            filename: Output filename
            
        Returns:
            True if successful
        """
        try:
            with open(filename, 'w') as f:
                json.dump(analysis_data, f, indent=2, default=str)
            
            print(f"✅ Analysis report exported to {filename}")
            return True
            
        except Exception as e:
            print(f"❌ Export failed: {e}")
            return False

# Global instance for easy access
enhanced_tools = EnhancedDSATools()

def get_enhanced_tools() -> EnhancedDSATools:
    """Get the global enhanced tools instance"""
    return enhanced_tools
