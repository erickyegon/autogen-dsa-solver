from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor

from config.constants import DOCKER_WORK_DIR, DOCKER_TIMEOUT

def get_docker_executor():
    """
    Returns a DockerCommandLineCodeExecutor instance with the specified work directory and timeout.
     
    Returns:
         DockerCommandLineCodeExecutor: A DockerCommandLineCodeExecutor instance with the specified work directory and timeout.
         
    """
         
    docker_executor = DockerCommandLineCodeExecutor(
        work_dir=DOCKER_WORK_DIR,
        timeout=DOCKER_TIMEOUT,
        )
    
    return docker_executor

async def start_docker_executor(docker_executor):
    """
    Starts the DockerCommandLineCodeExecutor instance.

    Args:
        docker_executor (DockerCommandLineCodeExecutor): A DockerCommandLineCodeExecutor instance to start.

    """

    await docker_executor.start()
    print("Started DockerExecutor")
    
async def stop_docker_executor(docker_executor):
    """
    Stops the DockerCommandLineCodeExecutor instance.

    Args:
        docker_executor (DockerCommandLineCodeExecutor): A DockerCommandLineCodeExecutor instance to stop.

    """
    await docker_executor.stop()
    print("Stopped DockerExecutor")
    
    