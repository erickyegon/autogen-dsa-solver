import asyncio
from team.dsa_solver_team import get_team
from agents.problem_solver_agent import get_problem_solver_expert
from agents.code_executor_agent import get_code_executor_agent
from config.docker_utils import get_docker_executor, start_docker_executor, stop_docker_executor
from config.model_client import get_model_client
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult



model_client = get_model_client("openai/gpt-4o")

async def get_team_and_docker():

    docker = get_docker_executor()
    model_client = get_model_client()
    problem_solver_agent = get_problem_solver_expert(model_client)
    code_executor_agent = get_code_executor_agent(docker)

    team = get_team(problem_solver_agent, code_executor_agent)
    return team, docker

async def run_team(team,task,docker):

    try:
        await start_docker_executor(docker)


        async for message in team.run_stream(task = task):
            print('='*50)
            if isinstance(message, TextMessage):
                print(msg:= f" {message.source}: {message.content}")
                # yield msg
            elif isinstance(message, TaskResult):
                print(msg:=f'Task Result: {message.stop_reason}')
                # yield msg
            print('='*50)


    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        await stop_docker_executor(docker)

async def main():
    team,docker = await get_team_and_docker()
    task = 'Write a Python function to calculate the factorial of a number'

    await run_team(team, task, docker)
    


if __name__ == "__main__":
    # Run the main function using asyncio
    asyncio.run(main())