"""
Demonstration of Enhanced DSA Solver Features
Shows the advanced capabilities of the upgraded system
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from utils.problem_analyzer import AdvancedProblemAnalyzer
from utils.visualization import DSAVisualizer
import matplotlib.pyplot as plt

def demo_problem_analysis():
    """Demonstrate the advanced problem analysis capabilities"""
    print("🔍 ADVANCED PROBLEM ANALYSIS DEMO")
    print("=" * 50)
    
    analyzer = AdvancedProblemAnalyzer()
    
    # Complex scheduling problem
    scheduling_problem = """
    I have a bunch of tasks that need to be done, like projects at work. Each task has a specific time it's 
    planned to start and a time it's planned to finish. The tricky part is that some tasks can only begin 
    after other specific tasks are completely finished. I have several 'workers' or 'platforms' that can each 
    handle one task at a time. My goal is to figure out the absolute minimum number of workers/platforms I need 
    to complete all these tasks on time, considering all their start, end, and dependency requirements.
    """
    
    print("📋 Problem:")
    print(scheduling_problem[:200] + "...")
    print()
    
    # Analyze the problem
    analysis = analyzer.analyze_problem(scheduling_problem, "Hard")
    
    print("🎯 Analysis Results:")
    print(f"Category: {analysis.category}")
    print(f"Subcategory: {analysis.subcategory}")
    print(f"Difficulty: {analysis.difficulty}")
    print()
    
    print("🧠 Key Concepts:")
    for concept in analysis.key_concepts:
        print(f"  • {concept}")
    print()
    
    print("⚡ Suggested Algorithms:")
    for algo in analysis.suggested_algorithms:
        print(f"  • {algo}")
    print()
    
    print("📊 Complexity Targets:")
    print(f"  Time: {analysis.time_complexity_target}")
    print(f"  Space: {analysis.space_complexity_target}")
    print()
    
    print("⚠️ Common Pitfalls:")
    for pitfall in analysis.common_pitfalls:
        print(f"  • {pitfall}")
    print()
    
    print("💡 Optimization Hints:")
    for hint in analysis.optimization_hints:
        print(f"  • {hint}")
    print()

def demo_strategic_hints():
    """Demonstrate the strategic hint system"""
    print("💡 STRATEGIC HINT SYSTEM DEMO")
    print("=" * 50)
    
    analyzer = AdvancedProblemAnalyzer()
    
    problems = [
        "Find the shortest path in a weighted graph with negative edges",
        "Implement a data structure that supports insert, delete, and get random element in O(1)",
        "Given an array of integers, find the maximum sum of non-adjacent elements"
    ]
    
    for i, problem in enumerate(problems, 1):
        print(f"🎯 Problem {i}: {problem}")
        hint = analyzer.get_strategic_hint(problem)
        print(hint)
        print("-" * 40)

def demo_visualizations():
    """Demonstrate the advanced visualization capabilities"""
    print("📊 ADVANCED VISUALIZATION DEMO")
    print("=" * 50)
    
    visualizer = DSAVisualizer()
    
    # 1. Graph Visualization
    print("🌐 Creating Graph Visualization...")
    edges = [(1, 2, 4), (1, 3, 2), (2, 3, 1), (2, 4, 5), (3, 4, 8), (3, 5, 10), (4, 5, 2)]
    visualizer.visualize_graph(edges, directed=True, title="Weighted Directed Graph")
    print("✅ Graph visualization saved as output.png")
    print()
    
    # 2. Algorithm Steps Visualization
    print("📈 Creating Algorithm Steps Visualization...")
    steps = [
        {
            'array': [64, 34, 25, 12, 22, 11, 90],
            'highlight': [0, 1],
            'description': 'Initial array - comparing first two elements'
        },
        {
            'array': [34, 64, 25, 12, 22, 11, 90],
            'highlight': [1, 2],
            'description': 'Swapped 64 and 34 - comparing next pair'
        },
        {
            'array': [34, 25, 64, 12, 22, 11, 90],
            'highlight': [2, 3],
            'description': 'Swapped 64 and 25 - continuing bubble sort'
        },
        {
            'array': [25, 34, 12, 22, 11, 64, 90],
            'highlight': [5, 6],
            'description': 'Final pass - array nearly sorted'
        }
    ]
    visualizer.visualize_algorithm_steps(steps, "Bubble Sort Algorithm Steps")
    print("✅ Algorithm steps visualization saved as output.png")
    print()
    
    # 3. Complexity Analysis
    print("⚡ Creating Complexity Analysis...")
    complexities = {
        'time': {
            'Bubble Sort': 'O(n²)',
            'Quick Sort': 'O(n log n)',
            'Merge Sort': 'O(n log n)',
            'Binary Search': 'O(log n)',
            'Linear Search': 'O(n)'
        },
        'space': {
            'Bubble Sort': 'O(1)',
            'Quick Sort': 'O(log n)',
            'Merge Sort': 'O(n)',
            'Binary Search': 'O(1)',
            'Linear Search': 'O(1)'
        }
    }
    visualizer.visualize_complexity_analysis(complexities, "Algorithm Complexity Comparison")
    print("✅ Complexity analysis saved as output.png")
    print()
    
    # 4. Scheduling Gantt Chart
    print("📅 Creating Scheduling Gantt Chart...")
    tasks = [
        {'id': 1, 'start': 0, 'end': 3, 'worker': 0},
        {'id': 2, 'start': 1, 'end': 4, 'worker': 1},
        {'id': 3, 'start': 3, 'end': 6, 'worker': 0},
        {'id': 4, 'start': 4, 'end': 7, 'worker': 1},
        {'id': 5, 'start': 6, 'end': 9, 'worker': 0},
        {'id': 6, 'start': 7, 'end': 10, 'worker': 1}
    ]
    visualizer.create_scheduling_gantt(tasks, "Optimized Task Scheduling")
    print("✅ Gantt chart saved as output.png")
    print()

def demo_complex_problem_categories():
    """Demonstrate problem categorization for various complex problems"""
    print("🎯 COMPLEX PROBLEM CATEGORIZATION DEMO")
    print("=" * 50)
    
    analyzer = AdvancedProblemAnalyzer()
    
    complex_problems = [
        {
            'title': 'Advanced Graph Problem',
            'description': 'Find all strongly connected components in a directed graph and determine if the graph is a DAG'
        },
        {
            'title': 'Dynamic Programming Challenge', 
            'description': 'Given a matrix of costs, find the minimum cost path from top-left to bottom-right with specific movement constraints'
        },
        {
            'title': 'String Algorithm Problem',
            'description': 'Implement a suffix tree and use it to find all occurrences of multiple patterns simultaneously'
        },
        {
            'title': 'Mathematical Algorithm',
            'description': 'Find the number of ways to arrange n distinct objects in a circle such that no two adjacent objects satisfy a given condition'
        }
    ]
    
    for problem in complex_problems:
        print(f"🔍 {problem['title']}:")
        print(f"   {problem['description']}")
        
        analysis = analyzer.analyze_problem(problem['description'], "Expert")
        print(f"   📊 Category: {analysis.category}")
        print(f"   ⚡ Key Algorithm: {analysis.suggested_algorithms[0] if analysis.suggested_algorithms else 'Custom approach needed'}")
        print(f"   🎯 Complexity: {analysis.time_complexity_target}")
        print()

def main():
    """Run all demonstrations"""
    print("🚀 ENHANCED DSA SOLVER CAPABILITIES DEMONSTRATION")
    print("=" * 60)
    print()
    
    try:
        # Demo 1: Problem Analysis
        demo_problem_analysis()
        print()
        
        # Demo 2: Strategic Hints
        demo_strategic_hints()
        print()
        
        # Demo 3: Visualizations
        demo_visualizations()
        print()
        
        # Demo 4: Complex Problem Categories
        demo_complex_problem_categories()
        print()
        
        print("🎉 DEMONSTRATION COMPLETE!")
        print("=" * 60)
        print("✨ The Enhanced DSA Solver now includes:")
        print("   • Advanced problem analysis and categorization")
        print("   • Strategic hint generation without spoiling solutions")
        print("   • Sophisticated visualizations for algorithms and data structures")
        print("   • Complex problem handling with expert-level insights")
        print("   • Real-time complexity analysis and optimization suggestions")
        print()
        print("🚀 Ready to solve the most challenging algorithmic problems!")
        
    except Exception as e:
        print(f"❌ Error during demonstration: {e}")
        print("💡 Make sure all dependencies are installed:")
        print("   pip install matplotlib networkx seaborn numpy")

if __name__ == "__main__":
    main()
