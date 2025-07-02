# Core Model Configuration
MODEL = 'gpt-4o'
FALLBACK_MODEL = 'gpt-3.5-turbo'

# Termination Configuration
TEXT_MENTION_TERMINATION = 'STOP'
ADDITIONAL_TERMINATION_PHRASES = [
    'Task Completed!',
    'Solution Complete',
    'All tests passed',
    'STOP'
]

# Docker Configuration
DOCKER_WORK_DIR = 'tmp'
DOCKER_TIMEOUT = 180  # Increased for complex problems
DOCKER_IMAGE = 'python:3.9-slim'

# Team Configuration
MAX_TURNS = 15
MAX_TURNS_COMPLEX = 30
MAX_TURNS_EXPERT = 40

# Problem Complexity Mapping
COMPLEXITY_CONFIG = {
    'Easy': {
        'max_turns': 10,
        'timeout': 60,
        'enable_advanced_features': False
    },
    'Medium': {
        'max_turns': 15,
        'timeout': 120,
        'enable_advanced_features': True
    },
    'Hard': {
        'max_turns': 25,
        'timeout': 180,
        'enable_advanced_features': True
    },
    'Expert': {
        'max_turns': 35,
        'timeout': 300,
        'enable_advanced_features': True
    }
}

# Enhanced Features Configuration
ENABLE_PROBLEM_ANALYZER = True
ENABLE_ERROR_HANDLER = True
ENABLE_VISUALIZATIONS = True
ENABLE_PERFORMANCE_METRICS = True

# Visualization Settings
VISUALIZATION_DPI = 300
VISUALIZATION_FORMAT = 'png'
VISUALIZATION_OUTPUT_DIR = 'output'

# Error Handling Configuration
MAX_ERROR_RETRIES = 3
ENABLE_DETAILED_ERROR_ANALYSIS = True
ENABLE_CODE_SUGGESTIONS = True

# Performance Monitoring
ENABLE_EXECUTION_TIMING = True
ENABLE_MEMORY_MONITORING = False  # Requires additional setup
PERFORMANCE_LOG_FILE = 'performance.log'

# Code Quality Standards
ENFORCE_TYPE_HINTS = True
ENFORCE_DOCSTRINGS = True
ENFORCE_ERROR_HANDLING = True
MINIMUM_TEST_COVERAGE = 3  # Minimum number of test cases

# Problem Categories
SUPPORTED_PROBLEM_TYPES = [
    'Graph Algorithms',
    'Dynamic Programming',
    'Tree & Binary Search',
    'String Algorithms',
    'Mathematical Problems',
    'Scheduling & Optimization',
    'Data Structure Design',
    'Greedy Algorithms',
    'Divide & Conquer'
]

# Language Support
SUPPORTED_LANGUAGES = ['Python', 'Java', 'C++', 'JavaScript', 'R']
DEFAULT_LANGUAGE = 'Python'

# Language-specific configurations
LANGUAGE_CONFIG = {
    'Python': {
        'file_extension': '.py',
        'execution_command': 'python',
        'strengths': ['General purpose', 'Data science', 'Rapid prototyping'],
        'best_for': ['Dynamic programming', 'Graph algorithms', 'General DSA']
    },
    'Java': {
        'file_extension': '.java',
        'execution_command': 'javac && java',
        'strengths': ['Object-oriented', 'Performance', 'Enterprise'],
        'best_for': ['Large-scale algorithms', 'Data structures', 'System design']
    },
    'C++': {
        'file_extension': '.cpp',
        'execution_command': 'g++ -o program && ./program',
        'strengths': ['High performance', 'Memory control', 'Competitive programming'],
        'best_for': ['Performance-critical algorithms', 'Mathematical computations']
    },
    'JavaScript': {
        'file_extension': '.js',
        'execution_command': 'node',
        'strengths': ['Web development', 'Asynchronous programming', 'JSON handling'],
        'best_for': ['Web-based algorithms', 'Tree traversals', 'String processing']
    },
    'R': {
        'file_extension': '.R',
        'execution_command': 'Rscript',
        'strengths': ['Statistical computing', 'Data analysis', 'Mathematical modeling'],
        'best_for': ['Statistical algorithms', 'Mathematical optimization', 'Data analysis problems']
    }
}

# Advanced Algorithm Categories
ALGORITHM_COMPLEXITY_TARGETS = {
    'sorting': 'O(n log n)',
    'searching': 'O(log n)',
    'graph_traversal': 'O(V + E)',
    'shortest_path': 'O((V + E) log V)',
    'dynamic_programming': 'O(n²)',
    'string_matching': 'O(n + m)',
    'scheduling': 'O(n log n)'
}
