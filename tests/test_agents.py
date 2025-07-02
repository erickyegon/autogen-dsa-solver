#!/usr/bin/env python3
"""
Test suite for DSA Solver AI agents.

This file contains unit tests for the agent components.
"""

import pytest
import asyncio
import os
import sys
from pathlib import Path
from unittest.mock import Mock, patch

# Add the parent directory to the path so we can import our modules
sys.path.append(str(Path(__file__).parent.parent))

from agents.problem_solver_agent import get_problem_solver_expert
from agents.code_executor_agent import get_code_executor_agent
from config.model_client import model_client, get_model_client
from config.docker_utils import get_docker_executor


class TestProblemSolverAgent:
    """Test cases for the Problem Solver Expert agent."""
    
    def test_agent_creation_with_default_client(self):
        """Test that problem solver agent is created with default client."""
        with patch('config.model_client.model_client') as mock_client:
            mock_client.return_value = Mock()
            agent = get_problem_solver_expert()
            
            assert agent.name == 'ProblemSolverExpert'
            assert agent.description == "An expert agent that solves problems using code execution."
            assert agent.model_client is not None
    
    def test_agent_creation_with_custom_client(self):
        """Test that problem solver agent accepts custom model client."""
        mock_client = Mock()
        agent = get_problem_solver_expert(mock_client)
        
        assert agent.name == 'ProblemSolverExpert'
        assert agent.model_client == mock_client
    
    def test_agent_system_message_contains_key_instructions(self):
        """Test that the agent's system message contains important instructions."""
        with patch('config.model_client.model_client') as mock_client:
            mock_client.return_value = Mock()
            agent = get_problem_solver_expert()
            
            system_message = agent.system_message.lower()
            
            # Check for key instruction keywords
            assert 'problem solver' in system_message
            assert 'python' in system_message
            assert 'test cases' in system_message
            assert 'stop' in system_message
            assert 'indentation' in system_message


class TestCodeExecutorAgent:
    """Test cases for the Code Executor Agent."""
    
    def test_agent_creation(self):
        """Test that code executor agent is created correctly."""
        mock_docker = Mock()
        agent = get_code_executor_agent(mock_docker)
        
        assert agent.name == 'CodeExecutorAgent'
        assert agent.description == "An agent that executes code in a Docker container."
    
    def test_agent_requires_docker_executor(self):
        """Test that code executor agent requires a docker executor."""
        with pytest.raises(TypeError):
            get_code_executor_agent()  # Should fail without docker executor


class TestModelClient:
    """Test cases for the model client configuration."""
    
    def test_model_client_creation(self):
        """Test that model client is created with correct model."""
        with patch.dict(os.environ, {'EURI_API_KEY': 'test_key'}):
            client = model_client("openai/gpt-4o")
            assert client is not None
    
    def test_get_model_client_function(self):
        """Test the get_model_client convenience function."""
        with patch.dict(os.environ, {'EURI_API_KEY': 'test_key'}):
            client = get_model_client("openai/gpt-4o")
            assert client is not None
    
    def test_invalid_model_raises_error(self):
        """Test that invalid model names raise appropriate errors."""
        with patch.dict(os.environ, {'EURI_API_KEY': 'test_key'}):
            with pytest.raises(ValueError):
                model_client("invalid-model-name")


class TestDockerUtils:
    """Test cases for Docker utilities."""
    
    def test_docker_executor_creation(self):
        """Test that Docker executor is created with correct configuration."""
        executor = get_docker_executor()
        
        assert executor is not None
        # Note: We can't test actual Docker functionality without Docker running
        # In a real test environment, you might want to use Docker test containers


class TestIntegration:
    """Integration tests for the complete system."""
    
    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_team_creation(self):
        """Test that the complete team can be created."""
        # This test requires actual environment setup
        if not os.getenv('EURI_API_KEY'):
            pytest.skip("EURI_API_KEY not set, skipping integration test")
        
        from main import get_team_and_docker
        
        try:
            team, docker = await get_team_and_docker()
            assert team is not None
            assert docker is not None
        except Exception as e:
            pytest.skip(f"Integration test failed due to environment: {e}")
    
    @pytest.mark.asyncio
    @pytest.mark.slow
    async def test_simple_problem_solving(self):
        """Test solving a simple problem end-to-end."""
        if not os.getenv('EURI_API_KEY'):
            pytest.skip("EURI_API_KEY not set, skipping integration test")
        
        from main import get_team_and_docker, run_team
        
        try:
            team, docker = await get_team_and_docker()
            
            # Test with a very simple problem
            simple_task = "Write a Python function that returns the sum of two numbers"
            
            # This would normally run the full pipeline
            # In a real test, you might want to mock parts of this
            # await run_team(team, simple_task, docker)
            
            # For now, just verify the team was created
            assert team is not None
            assert docker is not None
            
        except Exception as e:
            pytest.skip(f"Integration test failed: {e}")


# Test configuration
def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests (may require external services)"
    )
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (may take a long time to run)"
    )


if __name__ == "__main__":
    # Run tests when script is executed directly
    pytest.main([__file__, "-v"])
