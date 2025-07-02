from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

def get_team(problem_solver_expert, code_executor_agent):
    """
    Returns a RoundRobinGroupChat team configured with the provided agents and a termination condition.
    
    Args:
        problem_solver_expert (AssistantAgent): The expert agent that solves problems.
        code_executor_agent (CodeExecutorAgent): The agent that executes code.
    
    Returns:
        RoundRobinGroupChat: Configured team for collaborative problem solving.
    """
    termination_condition = TextMentionTermination('STOP')
    
    team = RoundRobinGroupChat(
        participants=[problem_solver_expert, code_executor_agent],
        termination_condition=termination_condition,
        max_turns=15
    )
    
    return team