from autogen_agentchat.agents import CodeExecutorAgent
from config.model_client import model_client

Euri_client = model_client("openai/gpt-4o")



def get_code_executor_agent(docker_executor):
    
    """Returns an instance of the   CodeExecutorAgent.
    
    
    Args:
        docker_executor (DockerCommandLineCodeExecutor): The docker command line Executor  to use.
        
    Returns:
        CodeExecutorAgent: configured code executor agent.
        
    """
    code_executor_agent = CodeExecutorAgent(
        name='CodeExecutorAgent',
        description="An agent that executes code in a Docker container.",
        code_executor=docker_executor,
    )
    
    return code_executor_agent