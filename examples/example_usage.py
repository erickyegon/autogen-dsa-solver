#!/usr/bin/env python3
"""
DSA Solver AI - Example Usage

This file demonstrates how to use the DSA Solver AI system programmatically.
"""

import asyncio
import os
from pathlib import Path
import sys

# Add the parent directory to the path so we can import our modules
sys.path.append(str(Path(__file__).parent.parent))

from main import get_team_and_docker, run_team


async def solve_problem(problem_description: str):
    """
    Solve a DSA problem using the AI team.
    
    Args:
        problem_description (str): Description of the problem to solve
    """
    print(f"🧠 Solving problem: {problem_description}")
    print("=" * 80)
    
    # Get the team and docker executor
    team, docker = await get_team_and_docker()
    
    # Run the team to solve the problem
    await run_team(team, problem_description, docker)
    
    print("=" * 80)
    print("✅ Problem solving completed!")


async def main():
    """
    Main function demonstrating various DSA problems.
    """
    print("🚀 DSA Solver AI - Example Usage")
    print("=" * 80)
    
    # Example problems to solve
    problems = [
        "Write a Python function to implement binary search",
        "Create a solution for the two-sum problem with O(n) time complexity",
        "Implement a function to reverse a linked list",
        "Write a function to find the longest common subsequence of two strings",
        "Create a function to detect if a binary tree is balanced"
    ]
    
    # Solve each problem (you can comment out some to test specific ones)
    for i, problem in enumerate(problems[:1], 1):  # Only solve first problem for demo
        print(f"\n📋 Problem {i}/{len(problems)}")
        await solve_problem(problem)
        
        # Add a delay between problems to avoid overwhelming the system
        if i < len(problems):
            print("\n⏳ Waiting 5 seconds before next problem...")
            await asyncio.sleep(5)
    
    print("\n🎉 All problems solved successfully!")


if __name__ == "__main__":
    # Make sure environment variables are set
    if not os.getenv("EURI_API_KEY"):
        print("❌ Error: EURI_API_KEY environment variable not set!")
        print("Please set your API key in the .env file or environment variables.")
        sys.exit(1)
    
    # Run the example
    asyncio.run(main())
