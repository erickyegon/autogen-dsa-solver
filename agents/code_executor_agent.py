from autogen_agentchat.agents import CodeExecutorAgent
from config.model_client import model_client

Euri_client = model_client("openai/gpt-4o")

def get_code_executor_agent(docker_executor):
    """
    Returns an enhanced CodeExecutorAgent with professional error handling and feedback.

    Args:
        docker_executor (DockerCommandLineCodeExecutor): The docker command line executor to use.

    Returns:
        CodeExecutorAgent: Enhanced code executor agent with better error handling.
    """

    # Enhanced description for better code execution and error handling
    enhanced_description = """A professional code executor agent that provides comprehensive error handling, debugging support, and educational feedback for code execution in Docker containers.

🔧 CODE EXECUTION EXCELLENCE:
- Safe execution of Python code in Docker containers
- Comprehensive error analysis and debugging
- Professional feedback and suggestions
- Code validation and syntax checking

🛡️ ERROR HANDLING EXPERTISE:
- Detailed error analysis with root cause identification
- Clear explanations of syntax, runtime, and logic errors
- Actionable suggestions for code fixes
- Best practices recommendations

The agent executes code safely in isolated Docker containers and provides detailed feedback on results, errors, and potential improvements."""

    code_executor_agent = CodeExecutorAgent(
        name='CodeExecutorAgent',
        description=enhanced_description,
        code_executor=docker_executor
    )

    return code_executor_agent