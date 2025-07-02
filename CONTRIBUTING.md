# Contributing to DSA Solver AI

Thank you for your interest in contributing to DSA Solver AI! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

1. **Search existing issues** first to avoid duplicates
2. **Use issue templates** when available
3. **Provide detailed information**:
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, Docker version)
   - Error messages and logs

### Suggesting Features

1. **Check the roadmap** in README.md first
2. **Open a feature request** with:
   - Clear description of the feature
   - Use cases and benefits
   - Possible implementation approach
   - Any relevant examples or mockups

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes** following our coding standards
4. **Add tests** for new functionality
5. **Update documentation** as needed
6. **Commit with clear messages**
7. **Push to your fork**
8. **Create a pull request**

## 📋 Development Guidelines

### Code Style

- **Python**: Follow PEP 8 guidelines
- **Docstrings**: Use Google-style docstrings
- **Type Hints**: Include type hints for function parameters and returns
- **Comments**: Write clear, concise comments for complex logic

### Testing

- **Unit Tests**: Add tests for new functions and classes
- **Integration Tests**: Test agent interactions and workflows
- **Docker Tests**: Verify Docker container functionality
- **UI Tests**: Test Streamlit interface components

### Documentation

- **README Updates**: Update README.md for new features
- **Code Documentation**: Document all public functions and classes
- **Examples**: Provide usage examples for new features
- **Architecture**: Update architecture diagrams if needed

## 🏗️ Development Setup

### Prerequisites

- Python 3.8+
- Docker Desktop
- Git
- Code editor (VS Code recommended)

### Local Development

```bash
# Clone your fork
git clone https://github.com/yourusername/dsa-solver-ai.git
cd dsa-solver-ai

# Create virtual environment
python -m venv dev_env
source dev_env/bin/activate  # Windows: dev_env\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If available

# Set up pre-commit hooks
pre-commit install

# Run tests
python -m pytest tests/

# Start development server
streamlit run app.py
```

### Project Structure

```
DSA Solver/
├── agents/          # AI agent implementations
├── config/          # Configuration and utilities
├── team/            # Team orchestration
├── tools/           # Additional tools (extensible)
├── utils/           # Utility functions
├── tests/           # Test files
├── docs/            # Documentation
└── examples/        # Usage examples
```

## 🧪 Testing Guidelines

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_agents.py

# Run with coverage
python -m pytest --cov=agents tests/
```

### Writing Tests

```python
import pytest
from agents.problem_solver_agent import get_problem_solver_expert

def test_problem_solver_creation():
    """Test that problem solver agent is created correctly."""
    agent = get_problem_solver_expert()
    assert agent.name == 'ProblemSolverExpert'
    assert agent.model_client is not None

@pytest.mark.asyncio
async def test_code_execution():
    """Test code execution functionality."""
    # Test implementation here
    pass
```

## 📝 Pull Request Guidelines

### Before Submitting

- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No merge conflicts

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Other (please describe)

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added for new functionality
```

## 🏷️ Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist

1. Update version numbers
2. Update CHANGELOG.md
3. Run full test suite
4. Create release branch
5. Tag release
6. Update documentation
7. Deploy to production

## 🤔 Questions?

- **General Questions**: Open a discussion on GitHub
- **Bug Reports**: Create an issue
- **Feature Requests**: Open a feature request
- **Security Issues**: Email security@example.com

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for helping make DSA Solver AI better! 🚀
