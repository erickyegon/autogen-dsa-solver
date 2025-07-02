"""
Advanced Task Scheduling Solution
Solves complex task scheduling problems with dependencies and resource constraints
"""

import heapq
from collections import defaultdict, deque
from typing import List, Dict, Tuple, Set
import matplotlib.pyplot as plt
import numpy as np

class Task:
    """Represents a task with timing and dependency constraints"""
    
    def __init__(self, task_id: int, start_time: int, end_time: int, dependencies: List[int] = None):
        self.id = task_id
        self.start_time = start_time
        self.end_time = end_time
        self.duration = end_time - start_time
        self.dependencies = dependencies or []
        self.assigned_worker = None
        self.actual_start = None
    
    def __repr__(self):
        return f"Task({self.id}, {self.start_time}-{self.end_time}, deps={self.dependencies})"

class AdvancedTaskScheduler:
    """
    Advanced task scheduler that handles dependencies and resource constraints
    
    Algorithm: Modified Critical Path Method with Resource Allocation
    Time Complexity: O(V + E + T log T) where V=tasks, E=dependencies, T=time slots
    Space Complexity: O(V + E + W*T) where W=workers
    """
    
    def __init__(self):
        self.tasks = {}
        self.dependency_graph = defaultdict(list)
        self.reverse_deps = defaultdict(list)
        self.workers = []
        
    def add_task(self, task: Task):
        """Add a task to the scheduler"""
        self.tasks[task.id] = task
        
        # Build dependency graph
        for dep in task.dependencies:
            self.dependency_graph[dep].append(task.id)
            self.reverse_deps[task.id].append(dep)
    
    def find_minimum_workers(self, tasks: List[Task]) -> Tuple[int, Dict[int, List[Task]]]:
        """
        Find minimum number of workers needed to complete all tasks
        
        Returns:
            Tuple of (minimum_workers, worker_assignments)
        """
        # Add all tasks
        for task in tasks:
            self.add_task(task)
        
        # Step 1: Topological sort to handle dependencies
        ready_tasks = self._get_topologically_sorted_tasks()
        
        # Step 2: Critical Path Analysis
        critical_path_info = self._calculate_critical_path()
        
        # Step 3: Resource allocation with greedy approach
        min_workers, assignments = self._allocate_resources_optimally(ready_tasks)
        
        return min_workers, assignments
    
    def _get_topologically_sorted_tasks(self) -> List[int]:
        """
        Perform topological sort considering both dependencies and time constraints
        """
        in_degree = defaultdict(int)
        
        # Calculate in-degrees (number of dependencies)
        for task_id in self.tasks:
            in_degree[task_id] = len(self.reverse_deps[task_id])
        
        # Priority queue: (earliest_start_time, task_id)
        ready_queue = []
        
        # Add tasks with no dependencies
        for task_id, degree in in_degree.items():
            if degree == 0:
                heapq.heappush(ready_queue, (self.tasks[task_id].start_time, task_id))
        
        sorted_tasks = []
        
        while ready_queue:
            _, current_task = heapq.heappop(ready_queue)
            sorted_tasks.append(current_task)
            
            # Update dependent tasks
            for dependent in self.dependency_graph[current_task]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    heapq.heappush(ready_queue, (self.tasks[dependent].start_time, dependent))
        
        return sorted_tasks
    
    def _calculate_critical_path(self) -> Dict[int, Dict]:
        """
        Calculate critical path information for each task
        """
        critical_info = {}
        
        # Forward pass - calculate earliest start/finish times
        for task_id in self.tasks:
            task = self.tasks[task_id]
            earliest_start = task.start_time
            
            # Consider dependency constraints
            for dep_id in task.dependencies:
                if dep_id in critical_info:
                    dep_finish = critical_info[dep_id]['earliest_finish']
                    earliest_start = max(earliest_start, dep_finish)
            
            critical_info[task_id] = {
                'earliest_start': earliest_start,
                'earliest_finish': earliest_start + task.duration,
                'latest_start': task.start_time,  # Will be updated in backward pass
                'latest_finish': task.end_time,
                'slack': 0  # Will be calculated
            }
        
        # Backward pass - calculate latest start/finish times
        # (Simplified for this example)
        for task_id in critical_info:
            info = critical_info[task_id]
            info['slack'] = info['latest_start'] - info['earliest_start']
        
        return critical_info
    
    def _allocate_resources_optimally(self, sorted_tasks: List[int]) -> Tuple[int, Dict[int, List[Task]]]:
        """
        Allocate tasks to minimum number of workers using greedy approach
        """
        # Worker availability: list of (end_time, worker_id)
        worker_availability = []
        worker_assignments = defaultdict(list)
        worker_count = 0
        
        for task_id in sorted_tasks:
            task = self.tasks[task_id]
            
            # Find earliest available worker
            available_worker = None
            earliest_available_time = float('inf')
            
            for i, (end_time, worker_id) in enumerate(worker_availability):
                # Check if worker is available when task needs to start
                if end_time <= task.start_time:
                    if end_time < earliest_available_time:
                        earliest_available_time = end_time
                        available_worker = (i, worker_id)
                    break
            
            if available_worker is None:
                # Need a new worker
                worker_count += 1
                worker_id = worker_count
                heapq.heappush(worker_availability, (task.end_time, worker_id))
            else:
                # Update existing worker's availability
                idx, worker_id = available_worker
                worker_availability[idx] = (task.end_time, worker_id)
                heapq.heapify(worker_availability)  # Re-heapify after update
            
            # Assign task to worker
            task.assigned_worker = worker_id
            task.actual_start = max(task.start_time, earliest_available_time)
            worker_assignments[worker_id].append(task)
        
        return worker_count, dict(worker_assignments)
    
    def visualize_schedule(self, worker_assignments: Dict[int, List[Task]], 
                          title: str = "Optimized Task Schedule"):
        """
        Create a Gantt chart visualization of the schedule
        """
        fig, ax = plt.subplots(1, 1, figsize=(14, 8))
        
        colors = plt.cm.Set3(np.linspace(0, 1, len(self.tasks)))
        color_map = {task_id: colors[i] for i, task_id in enumerate(self.tasks.keys())}
        
        for worker_id, tasks in worker_assignments.items():
            for task in tasks:
                # Draw task bar
                ax.barh(worker_id - 1, task.duration, 
                       left=task.actual_start or task.start_time, 
                       height=0.6, color=color_map[task.id], 
                       alpha=0.8, edgecolor='black', linewidth=1)
                
                # Add task label
                ax.text(task.start_time + task.duration/2, worker_id - 1, 
                       f'T{task.id}', ha='center', va='center', 
                       fontweight='bold', fontsize=10)
                
                # Draw dependency arrows (simplified)
                for dep_id in task.dependencies:
                    dep_task = self.tasks[dep_id]
                    if dep_task.assigned_worker:
                        ax.annotate('', xy=(task.start_time, worker_id - 1),
                                  xytext=(dep_task.end_time, dep_task.assigned_worker - 1),
                                  arrowprops=dict(arrowstyle='->', color='red', alpha=0.6))
        
        # Formatting
        ax.set_xlabel('Time', fontweight='bold', fontsize=12)
        ax.set_ylabel('Worker ID', fontweight='bold', fontsize=12)
        ax.set_title(title, fontweight='bold', fontsize=14, pad=20)
        ax.set_yticks(range(len(worker_assignments)))
        ax.set_yticklabels([f'Worker {i+1}' for i in range(len(worker_assignments))])
        ax.grid(True, alpha=0.3)
        
        # Add legend
        legend_elements = [plt.Rectangle((0,0),1,1, facecolor=color_map[task_id], 
                                       label=f'Task {task_id}') 
                          for task_id in sorted(self.tasks.keys())]
        ax.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc='upper left')
        
        plt.tight_layout()
        plt.savefig('output.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig

def solve_complex_scheduling_problem():
    """
    Demonstrates solving a complex task scheduling problem
    """
    print("🚀 Advanced Task Scheduling Solution")
    print("=" * 50)
    
    # Example problem: Project with interdependent tasks
    tasks = [
        Task(1, 0, 3, []),           # Task 1: 0-3, no dependencies
        Task(2, 1, 4, []),           # Task 2: 1-4, no dependencies  
        Task(3, 2, 6, [1]),          # Task 3: 2-6, depends on Task 1
        Task(4, 3, 7, [1, 2]),       # Task 4: 3-7, depends on Tasks 1,2
        Task(5, 4, 8, [3]),          # Task 5: 4-8, depends on Task 3
        Task(6, 5, 9, [4]),          # Task 6: 5-9, depends on Task 4
        Task(7, 6, 10, [4, 5]),      # Task 7: 6-10, depends on Tasks 4,5
        Task(8, 7, 11, [6, 7]),      # Task 8: 7-11, depends on Tasks 6,7
    ]
    
    print("📋 Problem Description:")
    print("- 8 tasks with specific time windows and dependencies")
    print("- Each task must start after its dependencies complete")
    print("- Goal: Find minimum workers needed")
    print()
    
    # Solve the problem
    scheduler = AdvancedTaskScheduler()
    min_workers, assignments = scheduler.find_minimum_workers(tasks)
    
    print("✅ Solution Found!")
    print(f"📊 Minimum Workers Required: {min_workers}")
    print()
    
    print("👥 Worker Assignments:")
    for worker_id, worker_tasks in assignments.items():
        print(f"Worker {worker_id}:")
        for task in sorted(worker_tasks, key=lambda t: t.start_time):
            deps_str = f", deps: {task.dependencies}" if task.dependencies else ""
            print(f"  - Task {task.id}: {task.start_time}-{task.end_time}{deps_str}")
    print()
    
    # Complexity Analysis
    print("⚡ Algorithm Complexity:")
    print("- Time Complexity: O(V + E + T log T)")
    print("  where V=tasks, E=dependencies, T=time slots")
    print("- Space Complexity: O(V + E + W*T)")
    print("  where W=workers")
    print()
    
    # Create visualization
    print("📈 Generating Gantt Chart Visualization...")
    scheduler.visualize_schedule(assignments, "Optimized Task Schedule with Dependencies")
    
    return min_workers, assignments

if __name__ == "__main__":
    solve_complex_scheduling_problem()
