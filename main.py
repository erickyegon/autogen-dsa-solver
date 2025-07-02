import asyncio
import sys
import os
from typing import AsyncGenerator, Dict, Any, Optional
import traceback

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

# Core AutoGen imports
from team.dsa_solver_team import get_team
from agents.problem_solver_agent import get_problem_solver_expert
from agents.code_executor_agent import get_code_executor_agent
from config.docker_utils import get_docker_executor, start_docker_executor, stop_docker_executor
from config.model_client import get_model_client, create_dsa_client, get_dsa_optimized_model
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

# Enhanced utilities
try:
    from utils.problem_analyzer import AdvancedProblemAnalyzer
    from utils.error_handler import ProfessionalErrorHandler
    from utils.visualization import DSAVisualizer
    ENHANCED_FEATURES = True
except ImportError as e:
    print(f"⚠️ Enhanced features not available: {e}")
    ENHANCED_FEATURES = False

# Initialize enhanced components
if ENHANCED_FEATURES:
    problem_analyzer = AdvancedProblemAnalyzer()
    error_handler = ProfessionalErrorHandler()
    visualizer = DSAVisualizer()
else:
    problem_analyzer = None
    error_handler = None
    visualizer = None

model_client = get_model_client("openai/gpt-4o")

async def get_enhanced_team_and_docker(problem_type: str = "general",
                                      complexity: str = "medium"):
    """
    Get enhanced team with advanced problem-solving capabilities and optimized model selection

    Args:
        problem_type: Type of DSA problem for model optimization
        complexity: Problem complexity level

    Returns:
        Tuple of (team, docker_executor) with enhanced agents
    """
    try:
        print("🚀 Initializing Enhanced DSA Solver Team...")
        print(f"🎯 Problem Type: {problem_type}, Complexity: {complexity}")

        # Initialize Docker executor
        docker = get_docker_executor()
        print("✅ Docker executor initialized")

        # Initialize optimized model client for DSA problems
        model_client_instance = create_dsa_client(problem_type, complexity)
        print("✅ Optimized model client initialized")

        # Create enhanced agents
        problem_solver_agent = get_problem_solver_expert(model_client_instance)
        code_executor_agent = get_code_executor_agent(docker)
        print("✅ Enhanced agents created")

        # Create team with enhanced capabilities using team manager
        from team.dsa_solver_team import TeamManager
        team_manager = TeamManager()
        team = team_manager.get_team_for_complexity(
            problem_solver_agent,
            code_executor_agent,
            complexity
        )
        print("✅ Enhanced team assembled with complexity-based configuration")

        return team, docker

    except Exception as e:
        print(f"❌ Error initializing team: {e}")
        if error_handler:
            analysis = error_handler.analyze_error(str(e))
            print(error_handler.format_error_report(analysis))
        raise

# Backward compatibility
async def get_team_and_docker():
    """Backward compatibility wrapper"""
    return await get_enhanced_team_and_docker()

async def run_enhanced_team(team, task: str, docker, complexity: str = "Medium",
                           language: str = "Python", optimization: bool = True):
    """
    Run enhanced team with advanced problem analysis and error handling

    Args:
        team: AutoGen team instance
        task: Problem description
        docker: Docker executor
        complexity: Problem complexity level
        language: Preferred programming language
        optimization: Whether to focus on optimization
    """
    try:
        print("🚀 Starting Enhanced DSA Problem Solving Session")
        print("=" * 60)

        # Pre-process task with problem analyzer
        if problem_analyzer and ENHANCED_FEATURES:
            print("🔍 Analyzing problem...")
            analysis = problem_analyzer.analyze_problem(task, complexity)

            print(f"📊 Problem Category: {analysis.category}")
            print(f"⚡ Suggested Algorithms: {', '.join(analysis.suggested_algorithms[:2])}")
            print(f"🎯 Complexity Target: {analysis.time_complexity_target}")
            print("=" * 60)

            # Enhance task with analysis
            enhanced_task = f"""
**PROBLEM ANALYSIS:**
- Category: {analysis.category}
- Difficulty: {complexity}
- Language: {language}
- Optimization Focus: {optimization}

**ALGORITHMIC GUIDANCE:**
- Key Concepts: {', '.join(analysis.key_concepts[:3])}
- Suggested Approaches: {', '.join(analysis.suggested_algorithms[:2])}
- Complexity Target: {analysis.time_complexity_target}

**ORIGINAL PROBLEM:**
{task}

**REQUIREMENTS:**
- Provide comprehensive error handling
- Include detailed test cases with edge cases
- Explain algorithm choice and complexity analysis
- Use professional code structure with proper documentation
"""
        else:
            enhanced_task = task

        # Start Docker executor
        await start_docker_executor(docker)
        print("✅ Docker environment ready")

        # Run team with enhanced task
        message_count = 0
        async for message in team.run_stream(task=enhanced_task):
            message_count += 1
            print(f"\n📨 Message {message_count}")
            print("=" * 50)

            if isinstance(message, TextMessage):
                print(f"🤖 {message.source}:")
                print(f"💬 {message.content}")

                # Check for errors in code execution
                if "error" in message.content.lower() and error_handler and ENHANCED_FEATURES:
                    print("\n🔍 Error detected - analyzing...")
                    analysis = error_handler.analyze_error(message.content)
                    print(f"💡 Suggestion: {analysis.suggested_fix}")

            elif isinstance(message, TaskResult):
                print(f"🎯 Task Result: {message.stop_reason}")
                print("✅ Problem solving session completed!")
                break

            print("=" * 50)

        print(f"\n📊 Session Summary: {message_count} messages exchanged")

    except Exception as e:
        print(f"❌ An error occurred during execution: {e}")

        if error_handler and ENHANCED_FEATURES:
            print("\n🔍 Analyzing error...")
            analysis = error_handler.analyze_error(str(e))
            print(error_handler.format_error_report(analysis))
        else:
            print("💡 Enable enhanced features for detailed error analysis")
            traceback.print_exc()

    finally:
        try:
            await stop_docker_executor(docker)
            print("🛑 Docker environment stopped")
        except Exception as e:
            print(f"⚠️ Warning: Error stopping Docker: {e}")

# Backward compatibility
async def run_team(team, task, docker):
    """Backward compatibility wrapper"""
    return await run_enhanced_team(team, task, docker)

async def solve_complex_problem(problem_description: str, complexity: str = "Hard",
                              language: str = "Python", optimization: bool = True):
    """
    Solve a complex DSA problem using the enhanced team with intelligent model selection

    Args:
        problem_description: Detailed problem description
        complexity: Problem complexity (Easy, Medium, Hard, Expert)
        language: Preferred programming language
        optimization: Whether to focus on optimization
    """
    try:
        print("🚀 ENHANCED DSA SOLVER - COMPLEX PROBLEM MODE")
        print("=" * 60)

        # Analyze problem type for optimal model selection
        problem_type = "general"
        if problem_analyzer and ENHANCED_FEATURES:
            analysis = problem_analyzer.analyze_problem(problem_description, complexity)
            problem_type = analysis.category.lower().replace(" ", "_")
            print(f"🔍 Detected problem type: {analysis.category}")

        # Get enhanced team with optimized model selection
        team, docker = await get_enhanced_team_and_docker(problem_type, complexity.lower())

        # Run enhanced problem solving
        await run_enhanced_team(team, problem_description, docker, complexity, language, optimization)

        print("\n🎉 Complex problem solving completed!")

    except Exception as e:
        print(f"❌ Error in complex problem solving: {e}")
        if error_handler and ENHANCED_FEATURES:
            analysis = error_handler.analyze_error(str(e))
            print(error_handler.format_error_report(analysis))
        raise

async def demo_enhanced_features():
    """
    Demonstrate the enhanced features with various problem types
    """
    print("🎯 ENHANCED FEATURES DEMONSTRATION")
    print("=" * 60)

    demo_problems = [
        {
            'description': '''I have a bunch of tasks that need to be done, like projects at work. Each task has a specific time it's
planned to start and a time it's planned to finish. The tricky part is that some tasks can only begin
after other specific tasks are completely finished. I have several 'workers' or 'platforms' that can each
handle one task at a time. My goal is to figure out the absolute minimum number of workers/platforms I need
to complete all these tasks on time, considering all their start, end, and dependency requirements.''',
            'complexity': 'Expert',
            'language': 'Python'
        },
        {
            'description': 'Find the shortest path in a weighted graph with negative edge weights, detecting negative cycles',
            'complexity': 'Hard',
            'language': 'Python'
        },
        {
            'description': 'Implement a data structure that supports insert, delete, and getRandom in O(1) time',
            'complexity': 'Medium',
            'language': 'Python'
        }
    ]

    for i, problem in enumerate(demo_problems, 1):
        print(f"\n🎯 Demo Problem {i}: {problem['complexity']} Level")
        print("-" * 40)
        print(f"Description: {problem['description'][:100]}...")

        try:
            await solve_complex_problem(
                problem['description'],
                problem['complexity'],
                problem['language']
            )
        except Exception as e:
            print(f"❌ Demo problem {i} failed: {e}")

        print("\n" + "=" * 60)

async def main():
    """
    Enhanced main function with multiple operation modes
    """
    import sys

    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()

        if mode == "demo":
            await demo_enhanced_features()
        elif mode == "complex":
            problem = input("🎯 Enter your complex DSA problem: ")
            complexity = input("📊 Complexity level (Easy/Medium/Hard/Expert) [Hard]: ") or "Hard"
            language = input("💻 Programming language [Python]: ") or "Python"

            await solve_complex_problem(problem, complexity, language)
        else:
            print("❌ Unknown mode. Use 'demo' or 'complex'")
    else:
        # Default: Run with a sample complex problem
        print("🚀 ENHANCED DSA SOLVER - DEFAULT MODE")
        print("=" * 50)

        team, docker = await get_enhanced_team_and_docker()

        # Sample complex scheduling problem
        task = '''I have a bunch of tasks that need to be done, like projects at work. Each task has a specific time it's
planned to start and a time it's planned to finish. The tricky part is that some tasks can only begin
after other specific tasks are completely finished. I have several 'workers' or 'platforms' that can each
handle one task at a time. My goal is to figure out the absolute minimum number of workers/platforms I need
to complete all these tasks on time, considering all their start, end, and dependency requirements.'''

        await run_enhanced_team(team, task, docker, "Expert", "Python", True)

if __name__ == "__main__":
    print("🧠 ENHANCED DSA AI SOLVER")
    print("=" * 40)
    print("Usage:")
    print("  python main.py          - Run with sample complex problem")
    print("  python main.py demo     - Run demonstration of enhanced features")
    print("  python main.py complex  - Interactive complex problem solving")
    print("=" * 40)

    # Run the main function using asyncio
    asyncio.run(main())