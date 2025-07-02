"""
Advanced Problem Analyzer for DSA Problems
Categorizes and provides strategic hints for complex algorithmic problems
"""

import re
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class ProblemAnalysis:
    category: str
    subcategory: str
    difficulty: str
    key_concepts: List[str]
    suggested_algorithms: List[str]
    time_complexity_target: str
    space_complexity_target: str
    common_pitfalls: List[str]
    optimization_hints: List[str]

class AdvancedProblemAnalyzer:
    """
    Analyzes DSA problems and provides strategic guidance
    """
    
    def __init__(self):
        self.patterns = {
            'graph': [
                r'\b(graph|node|edge|vertex|vertices|path|cycle|connected|component)\b',
                r'\b(shortest path|dijkstra|bfs|dfs|topological|mst|spanning tree)\b',
                r'\b(adjacency|neighbor|directed|undirected|weighted)\b'
            ],
            'dynamic_programming': [
                r'\b(optimal|maximum|minimum|subsequence|substring)\b',
                r'\b(knapsack|fibonacci|coin|change|edit distance|lcs)\b',
                r'\b(overlapping|subproblem|memoization|tabulation)\b'
            ],
            'tree': [
                r'\b(tree|binary|bst|avl|heap|trie|segment)\b',
                r'\b(root|leaf|parent|child|ancestor|descendant)\b',
                r'\b(traversal|inorder|preorder|postorder|level)\b'
            ],
            'string': [
                r'\b(string|pattern|match|substring|subsequence|palindrome)\b',
                r'\b(kmp|rabin|karp|suffix|prefix|anagram)\b',
                r'\b(character|alphabet|lexicographic)\b'
            ],
            'array': [
                r'\b(array|subarray|sliding window|two pointer)\b',
                r'\b(sort|merge|partition|binary search)\b',
                r'\b(rotation|duplicate|missing)\b'
            ],
            'scheduling': [
                r'\b(task|job|schedule|deadline|priority|resource)\b',
                r'\b(worker|platform|machine|processor|cpu)\b',
                r'\b(dependency|constraint|allocation|optimization)\b'
            ],
            'mathematical': [
                r'\b(prime|factor|gcd|lcm|modular|arithmetic)\b',
                r'\b(combinatorial|permutation|probability)\b',
                r'\b(number theory|geometry|matrix)\b'
            ]
        }
        
        self.algorithm_suggestions = {
            'graph': {
                'shortest_path': ['Dijkstra', 'Bellman-Ford', 'Floyd-Warshall', 'A*'],
                'traversal': ['DFS', 'BFS', 'Topological Sort'],
                'connectivity': ['Union-Find', 'Tarjan\'s Algorithm', 'Kosaraju\'s Algorithm'],
                'spanning_tree': ['Kruskal\'s Algorithm', 'Prim\'s Algorithm']
            },
            'dynamic_programming': {
                'optimization': ['Bottom-up DP', 'Top-down DP with Memoization'],
                'sequence': ['LIS', 'LCS', 'Edit Distance'],
                'partition': ['Knapsack variants', 'Coin Change', 'Subset Sum']
            },
            'tree': {
                'traversal': ['DFS variants', 'BFS/Level-order', 'Morris Traversal'],
                'search': ['Binary Search Tree operations', 'Balanced tree operations'],
                'construction': ['Tree building from traversals', 'Serialization/Deserialization']
            },
            'scheduling': {
                'optimization': ['Greedy scheduling', 'Critical Path Method', 'Resource allocation'],
                'constraints': ['Topological sorting', 'Interval scheduling', 'Load balancing']
            }
        }

    def analyze_problem(self, problem_text: str, complexity: str = "Medium") -> ProblemAnalysis:
        """
        Analyzes a problem description and returns strategic guidance
        """
        problem_lower = problem_text.lower()
        
        # Detect primary category
        category_scores = {}
        for category, patterns in self.patterns.items():
            score = 0
            for pattern in patterns:
                matches = len(re.findall(pattern, problem_lower, re.IGNORECASE))
                score += matches
            category_scores[category] = score
        
        primary_category = max(category_scores, key=category_scores.get)
        
        # Generate analysis based on detected category
        analysis = self._generate_analysis(primary_category, problem_text, complexity)
        
        return analysis
    
    def _generate_analysis(self, category: str, problem_text: str, complexity: str) -> ProblemAnalysis:
        """
        Generates detailed analysis for the detected problem category
        """
        
        if category == 'scheduling':
            return ProblemAnalysis(
                category="Scheduling & Optimization",
                subcategory="Resource Allocation with Constraints",
                difficulty=complexity,
                key_concepts=[
                    "Task Dependencies", "Resource Constraints", "Critical Path",
                    "Topological Sorting", "Greedy Optimization", "Graph Theory"
                ],
                suggested_algorithms=[
                    "Topological Sort for dependency resolution",
                    "Greedy algorithm for resource allocation",
                    "Critical Path Method (CPM)",
                    "Interval scheduling maximization",
                    "Load balancing algorithms"
                ],
                time_complexity_target="O(V + E) for dependency graph, O(n log n) for scheduling",
                space_complexity_target="O(V + E) for graph representation",
                common_pitfalls=[
                    "Not handling circular dependencies",
                    "Ignoring resource constraints",
                    "Suboptimal greedy choices",
                    "Not considering task preemption"
                ],
                optimization_hints=[
                    "Use topological sort to handle dependencies",
                    "Apply greedy algorithm for resource allocation",
                    "Consider priority queues for task scheduling",
                    "Implement efficient data structures for tracking"
                ]
            )
        
        elif category == 'graph':
            return ProblemAnalysis(
                category="Graph Algorithms",
                subcategory="Graph Traversal & Pathfinding",
                difficulty=complexity,
                key_concepts=[
                    "Graph Representation", "DFS/BFS", "Shortest Path",
                    "Cycle Detection", "Connected Components"
                ],
                suggested_algorithms=[
                    "Depth-First Search (DFS)",
                    "Breadth-First Search (BFS)",
                    "Dijkstra's Algorithm",
                    "Union-Find for connectivity"
                ],
                time_complexity_target="O(V + E) for traversal, O((V + E) log V) for shortest path",
                space_complexity_target="O(V + E) for adjacency representation",
                common_pitfalls=[
                    "Not handling disconnected graphs",
                    "Infinite loops in cyclic graphs",
                    "Incorrect edge weight handling"
                ],
                optimization_hints=[
                    "Use adjacency list for sparse graphs",
                    "Implement early termination conditions",
                    "Consider bidirectional search for pathfinding"
                ]
            )
        
        elif category == 'dynamic_programming':
            return ProblemAnalysis(
                category="Dynamic Programming",
                subcategory="Optimization Problems",
                difficulty=complexity,
                key_concepts=[
                    "Optimal Substructure", "Overlapping Subproblems",
                    "Memoization", "Tabulation", "State Transition"
                ],
                suggested_algorithms=[
                    "Bottom-up Dynamic Programming",
                    "Top-down DP with Memoization",
                    "Space-optimized DP"
                ],
                time_complexity_target="O(n²) to O(n³) depending on state space",
                space_complexity_target="O(n) to O(n²) with optimization",
                common_pitfalls=[
                    "Incorrect state definition",
                    "Missing base cases",
                    "Inefficient space usage"
                ],
                optimization_hints=[
                    "Identify optimal substructure",
                    "Use space optimization techniques",
                    "Consider iterative vs recursive approaches"
                ]
            )
        
        # Default analysis for other categories
        return ProblemAnalysis(
            category=category.replace('_', ' ').title(),
            subcategory="General Problem",
            difficulty=complexity,
            key_concepts=["Algorithm Design", "Data Structures", "Complexity Analysis"],
            suggested_algorithms=["Brute Force", "Optimized Approach"],
            time_complexity_target="Depends on problem constraints",
            space_complexity_target="O(1) to O(n) preferred",
            common_pitfalls=["Edge case handling", "Integer overflow", "Time limit exceeded"],
            optimization_hints=["Analyze constraints carefully", "Consider multiple approaches"]
        )

    def get_strategic_hint(self, problem_text: str) -> str:
        """
        Provides a strategic hint without giving away the solution
        """
        analysis = self.analyze_problem(problem_text)
        
        hint = f"""
🎯 **Strategic Approach Hint:**

**Problem Type:** {analysis.category}
**Key Insight:** Focus on {analysis.key_concepts[0]} and {analysis.key_concepts[1]}

**Think About:**
- {analysis.optimization_hints[0]}
- What data structure would efficiently handle the main operations?
- Can you break this into smaller subproblems?

**Complexity Target:** {analysis.time_complexity_target}
"""
        return hint
