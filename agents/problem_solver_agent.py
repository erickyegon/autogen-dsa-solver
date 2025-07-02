from autogen_agentchat.agents import AssistantAgent
from config.model_client import model_client

Euri_client = model_client("openai/gpt-4o")



def get_problem_solver_expert(model_client=None):
    """Returns a problem solver expert agent."""
    # Create the problem solver expert agent
    # Use provided model_client or default to Euri_client
    client = model_client if model_client is not None else Euri_client

    problem_solver_expert = AssistantAgent(
        name='ProblemSolverExpert',
        description="An expert agent that solves problems using code execution.",
        model_client=client,
        system_message='''You are a problem solver agent that is an expert in solving DSA problems.

IMPORTANT RULES:
1. You will be working with a code executor agent to execute code
2. First provide a way to solve the task/problem
3. Then provide the code in Python Block format with PROPER INDENTATION (use 4 spaces for each indentation level)
4. You can provide Shell script as well if code fails due to missing libraries, use pip install command
5. You should only give a single code block and pass it to executor agent
6. If there's an error, provide the corrected code in Python Block format with PROPER INDENTATION
7. Once the code has been successfully executed, explain the results in detail
8. Make sure each code has 3 test cases and the output of each test case is printed
9. If you need to save files, use output.png or output.txt or output.gif
10. Once everything is done, explain the results and say "STOP" to stop the conversation

CRITICAL: Always ensure proper Python indentation in code blocks. Use 4 spaces for each indentation level.

Example of proper indentation:
```python
def function_name(param1, param2):
    # This line is indented with 4 spaces
    result = param1 + param2
    return result
```'''
    )

    return problem_solver_expert

