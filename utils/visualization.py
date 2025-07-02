"""
Advanced Visualization Utilities for DSA Problems
Creates visual representations of algorithms and data structures
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from typing import List, Dict, Tuple, Optional
import seaborn as sns

class DSAVisualizer:
    """
    Advanced visualizer for Data Structures and Algorithms
    """
    
    def __init__(self):
        plt.style.use('seaborn-v0_8')
        self.colors = {
            'primary': '#2E86AB',
            'secondary': '#A23B72', 
            'accent': '#F18F01',
            'success': '#C73E1D',
            'background': '#F5F5F5'
        }
    
    def visualize_graph(self, edges: List[Tuple], weights: Optional[Dict] = None, 
                       directed: bool = False, title: str = "Graph Visualization"):
        """
        Visualizes a graph with optional weights
        """
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))
        
        # Create graph
        G = nx.DiGraph() if directed else nx.Graph()
        
        # Add edges
        for edge in edges:
            if len(edge) == 2:
                G.add_edge(edge[0], edge[1])
            elif len(edge) == 3:
                G.add_edge(edge[0], edge[1], weight=edge[2])
        
        # Layout
        pos = nx.spring_layout(G, k=2, iterations=50)
        
        # Draw nodes
        nx.draw_networkx_nodes(G, pos, node_color=self.colors['primary'], 
                              node_size=1000, alpha=0.9, ax=ax)
        
        # Draw edges
        if directed:
            nx.draw_networkx_edges(G, pos, edge_color=self.colors['secondary'],
                                 arrows=True, arrowsize=20, alpha=0.7, ax=ax)
        else:
            nx.draw_networkx_edges(G, pos, edge_color=self.colors['secondary'],
                                 alpha=0.7, ax=ax)
        
        # Draw labels
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', ax=ax)
        
        # Draw edge weights if provided
        if weights or any(len(edge) == 3 for edge in edges):
            edge_labels = {}
            for edge in edges:
                if len(edge) == 3:
                    edge_labels[(edge[0], edge[1])] = edge[2]
                elif weights and (edge[0], edge[1]) in weights:
                    edge_labels[edge] = weights[edge]
            
            if edge_labels:
                nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10, ax=ax)
        
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.axis('off')
        plt.tight_layout()
        plt.savefig('output.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig
    
    def visualize_tree(self, tree_data: Dict, title: str = "Tree Visualization"):
        """
        Visualizes a tree structure
        """
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))
        
        G = nx.DiGraph()
        
        def add_tree_edges(node, parent=None):
            if parent is not None:
                G.add_edge(parent, node)
            
            if isinstance(tree_data.get(node), dict):
                for child in tree_data[node]:
                    add_tree_edges(child, node)
            elif isinstance(tree_data.get(node), list):
                for child in tree_data[node]:
                    add_tree_edges(child, node)
        
        # Build tree from root
        root = list(tree_data.keys())[0]
        add_tree_edges(root)
        
        # Use hierarchical layout
        pos = nx.nx_agraph.graphviz_layout(G, prog='dot') if hasattr(nx, 'nx_agraph') else nx.spring_layout(G)
        
        # Draw tree
        nx.draw_networkx_nodes(G, pos, node_color=self.colors['accent'], 
                              node_size=800, alpha=0.9, ax=ax)
        nx.draw_networkx_edges(G, pos, edge_color=self.colors['primary'],
                              arrows=True, arrowsize=15, alpha=0.7, ax=ax)
        nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', ax=ax)
        
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.axis('off')
        plt.tight_layout()
        plt.savefig('output.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig
    
    def visualize_algorithm_steps(self, steps: List[Dict], title: str = "Algorithm Steps"):
        """
        Visualizes algorithm execution steps
        """
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        axes = axes.flatten()
        
        for i, step in enumerate(steps[:4]):  # Show up to 4 steps
            ax = axes[i]
            
            if 'array' in step:
                # Visualize array operations
                array = step['array']
                colors = ['red' if j in step.get('highlight', []) else self.colors['primary'] 
                         for j in range(len(array))]
                
                bars = ax.bar(range(len(array)), array, color=colors, alpha=0.8)
                ax.set_title(f"Step {i+1}: {step.get('description', '')}", fontweight='bold')
                ax.set_xlabel('Index')
                ax.set_ylabel('Value')
                
                # Add value labels on bars
                for j, bar in enumerate(bars):
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                           f'{array[j]}', ha='center', va='bottom')
            
            elif 'graph' in step:
                # Visualize graph operations
                G = nx.Graph()
                edges = step['graph']
                G.add_edges_from(edges)
                
                pos = nx.spring_layout(G)
                node_colors = [self.colors['success'] if node in step.get('highlight', []) 
                              else self.colors['primary'] for node in G.nodes()]
                
                nx.draw(G, pos, node_color=node_colors, with_labels=True, 
                       ax=ax, node_size=500, font_weight='bold')
                ax.set_title(f"Step {i+1}: {step.get('description', '')}", fontweight='bold')
        
        # Hide unused subplots
        for i in range(len(steps), 4):
            axes[i].axis('off')
        
        plt.suptitle(title, fontsize=18, fontweight='bold')
        plt.tight_layout()
        plt.savefig('output.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig
    
    def visualize_complexity_analysis(self, complexities: Dict[str, List], 
                                    title: str = "Complexity Analysis"):
        """
        Visualizes time/space complexity comparison
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Time complexity visualization
        if 'time' in complexities:
            algorithms = list(complexities['time'].keys())
            n_values = np.logspace(1, 4, 50)  # From 10 to 10000
            
            for algo in algorithms:
                complexity = complexities['time'][algo]
                if complexity == 'O(1)':
                    y_values = np.ones_like(n_values)
                elif complexity == 'O(log n)':
                    y_values = np.log2(n_values)
                elif complexity == 'O(n)':
                    y_values = n_values
                elif complexity == 'O(n log n)':
                    y_values = n_values * np.log2(n_values)
                elif complexity == 'O(n²)':
                    y_values = n_values ** 2
                elif complexity == 'O(2^n)':
                    y_values = 2 ** (n_values / 1000)  # Scale down for visualization
                else:
                    y_values = n_values  # Default to linear
                
                ax1.plot(n_values, y_values, label=f'{algo}: {complexity}', linewidth=2)
            
            ax1.set_xlabel('Input Size (n)', fontweight='bold')
            ax1.set_ylabel('Time Units', fontweight='bold')
            ax1.set_title('Time Complexity Comparison', fontweight='bold')
            ax1.set_xscale('log')
            ax1.set_yscale('log')
            ax1.legend()
            ax1.grid(True, alpha=0.3)
        
        # Space complexity visualization
        if 'space' in complexities:
            algorithms = list(complexities['space'].keys())
            space_values = [complexities['space'][algo] for algo in algorithms]
            
            # Convert complexity strings to numeric values for visualization
            numeric_values = []
            for complexity in space_values:
                if 'O(1)' in complexity:
                    numeric_values.append(1)
                elif 'O(log n)' in complexity:
                    numeric_values.append(2)
                elif 'O(n)' in complexity:
                    numeric_values.append(3)
                elif 'O(n²)' in complexity:
                    numeric_values.append(4)
                else:
                    numeric_values.append(2.5)
            
            bars = ax2.bar(algorithms, numeric_values, color=self.colors['accent'], alpha=0.8)
            ax2.set_ylabel('Space Complexity Level', fontweight='bold')
            ax2.set_title('Space Complexity Comparison', fontweight='bold')
            ax2.set_ylim(0, 5)
            
            # Add complexity labels on bars
            for i, (bar, complexity) in enumerate(zip(bars, space_values)):
                height = bar.get_height()
                ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        complexity, ha='center', va='bottom', fontweight='bold')
        
        plt.suptitle(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig('output.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig
    
    def create_scheduling_gantt(self, tasks: List[Dict], title: str = "Task Scheduling"):
        """
        Creates a Gantt chart for task scheduling problems
        """
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))
        
        # Sort tasks by start time
        sorted_tasks = sorted(tasks, key=lambda x: x.get('start', 0))
        
        colors = plt.cm.Set3(np.linspace(0, 1, len(sorted_tasks)))
        
        for i, task in enumerate(sorted_tasks):
            start = task.get('start', 0)
            duration = task.get('duration', task.get('end', start + 1) - start)
            worker = task.get('worker', i % 3)  # Assign to workers cyclically
            
            ax.barh(worker, duration, left=start, height=0.6, 
                   color=colors[i], alpha=0.8, 
                   label=f"Task {task.get('id', i+1)}")
            
            # Add task label
            ax.text(start + duration/2, worker, f"T{task.get('id', i+1)}", 
                   ha='center', va='center', fontweight='bold')
        
        ax.set_xlabel('Time', fontweight='bold')
        ax.set_ylabel('Worker/Resource', fontweight='bold')
        ax.set_title(title, fontweight='bold', pad=20)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('output.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig
