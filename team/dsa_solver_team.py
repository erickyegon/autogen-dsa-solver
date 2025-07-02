from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
import sys
import os

# Add utils to path for enhanced features
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

def get_enhanced_team(problem_solver_expert, code_executor_agent, max_turns: int = 20,
                     enable_advanced_termination: bool = True):
    """
    Returns an enhanced RoundRobinGroupChat team with advanced termination conditions and error handling.

    Args:
        problem_solver_expert (AssistantAgent): The expert agent that solves problems.
        code_executor_agent (CodeExecutorAgent): The agent that executes code.
        max_turns (int): Maximum number of conversation turns
        enable_advanced_termination (bool): Whether to use advanced termination conditions

    Returns:
        RoundRobinGroupChat: Enhanced team for collaborative problem solving.
    """

    # Enhanced termination conditions
    termination_conditions = []

    # Primary termination: STOP keyword
    termination_conditions.append(TextMentionTermination('STOP'))

    if enable_advanced_termination:
        # Additional termination conditions for robustness
        termination_conditions.append(TextMentionTermination('Task Completed!'))
        termination_conditions.append(TextMentionTermination('Solution Complete'))
        termination_conditions.append(TextMentionTermination('All tests passed'))

        # Fallback: Maximum message limit
        termination_conditions.append(MaxMessageTermination(max_turns))

    # Use the first termination condition (STOP) as primary
    primary_termination = termination_conditions[0]

    # Create enhanced team
    team = RoundRobinGroupChat(
        participants=[problem_solver_expert, code_executor_agent],
        termination_condition=primary_termination,
        max_turns=max_turns
    )

    return team

def get_team(problem_solver_expert, code_executor_agent):
    """
    Backward compatibility wrapper for the original get_team function.

    Args:
        problem_solver_expert (AssistantAgent): The expert agent that solves problems.
        code_executor_agent (CodeExecutorAgent): The agent that executes code.

    Returns:
        RoundRobinGroupChat: Configured team for collaborative problem solving.
    """
    return get_enhanced_team(problem_solver_expert, code_executor_agent, max_turns=15)

def get_complex_problem_team(problem_solver_expert, code_executor_agent):
    """
    Get a team specifically configured for complex problem solving with extended capabilities.

    Args:
        problem_solver_expert (AssistantAgent): The expert agent that solves problems.
        code_executor_agent (CodeExecutorAgent): The agent that executes code.

    Returns:
        RoundRobinGroupChat: Team optimized for complex problem solving.
    """
    return get_enhanced_team(
        problem_solver_expert,
        code_executor_agent,
        max_turns=30,  # More turns for complex problems
        enable_advanced_termination=True
    )

class TeamManager:
    """
    Advanced team manager for handling different types of DSA problems
    """

    def __init__(self):
        self.team_configs = {
            'simple': {'max_turns': 10, 'advanced_termination': False},
            'medium': {'max_turns': 15, 'advanced_termination': True},
            'complex': {'max_turns': 25, 'advanced_termination': True},
            'expert': {'max_turns': 35, 'advanced_termination': True}
        }

    def get_team_for_complexity(self, problem_solver_expert, code_executor_agent,
                               complexity: str = 'medium'):
        """
        Get a team configured for specific problem complexity

        Args:
            problem_solver_expert: Problem solver agent
            code_executor_agent: Code executor agent
            complexity: Problem complexity level ('simple', 'medium', 'complex', 'expert')

        Returns:
            RoundRobinGroupChat: Team configured for the specified complexity
        """
        complexity = complexity.lower()

        if complexity not in self.team_configs:
            print(f"⚠️ Unknown complexity '{complexity}', using 'medium'")
            complexity = 'medium'

        config = self.team_configs[complexity]

        print(f"🤖 Creating team for {complexity} complexity:")
        print(f"   Max turns: {config['max_turns']}")
        print(f"   Advanced termination: {config['advanced_termination']}")

        return get_enhanced_team(
            problem_solver_expert,
            code_executor_agent,
            max_turns=config['max_turns'],
            enable_advanced_termination=config['advanced_termination']
        )

    def get_team_for_problem_type(self, problem_solver_expert, code_executor_agent,
                                 problem_type: str = 'general'):
        """
        Get a team configured for specific problem types

        Args:
            problem_solver_expert: Problem solver agent
            code_executor_agent: Code executor agent
            problem_type: Type of problem ('graph', 'dp', 'scheduling', 'general')

        Returns:
            RoundRobinGroupChat: Team configured for the problem type
        """
        type_configs = {
            'graph': 'medium',
            'dynamic_programming': 'complex',
            'scheduling': 'expert',
            'string': 'medium',
            'tree': 'medium',
            'mathematical': 'complex',
            'general': 'medium'
        }

        complexity = type_configs.get(problem_type.lower(), 'medium')

        print(f"🎯 Problem type: {problem_type} → Complexity: {complexity}")

        return self.get_team_for_complexity(
            problem_solver_expert,
            code_executor_agent,
            complexity
        )