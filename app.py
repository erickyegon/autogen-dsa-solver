import streamlit as st
import asyncio
from main import get_team_and_docker,run_team
from config.docker_utils import get_docker_executor, start_docker_executor, stop_docker_executor
from config.model_client import get_model_client
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

st.title("DSA Solver")
st.write("This is a simple DSA solver application.")

task = st.text_input("Enter your DSA Question here",value='Can you give me a solution to add 2 numbers?')

async def run(team, task, docker):
    try:
        await start_docker_executor(docker)
        async for message in team.run_stream(task = task):
            print('='*50)
            if isinstance(message, TextMessage):
                print(msg:= f"{message.source}: {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg:=f'Task Result: {message.stop_reason}')
                yield msg

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await stop_docker_executor(docker)




if st.button("Solve"):
    st.write('Solving your question...')

    
    task = task

    async def collect_messages():
        team,docker = await get_team_and_docker()
        async for msg in run(team, task, docker):
            # if isinstance(msg, str):
            if msg.startswith('user'):
                with st.chat_message('user',avatar='👤'):
                    st.markdown(msg)
            elif msg.startswith('ProblemSolverExpert'):
                with st.chat_message('ProblemSolverExpert',avatar='🧑🏻‍💻') :
                    st.markdown(msg)
            elif msg.startswith('CodeExecutorAgent'):
                with st.chat_message('CodeExecutorAgent',avatar='🤖'):
                    st.markdown(msg)
            else:
                st.markdown(msg)

    asyncio.run(collect_messages())