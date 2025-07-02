# euri_client.py
"""
Custom Euri AI client for AutoGen Studio
Enhanced with multiple model support and better formatting
"""

import logging
import json
import re
import asyncio
import os
from typing import Sequence, Union, Optional, Mapping, Any, AsyncGenerator
from dotenv import load_dotenv

# Third-party imports
from euriai import EuriaiClient
from pydantic import BaseModel

# AutoGen imports
from autogen_core.models import ChatCompletionClient, ModelInfo, CreateResult, RequestUsage, LLMMessage
from autogen_core import CancellationToken
from autogen_core.tools import Tool, ToolSchema
from autogen_core._component_config import Component

# Configure logging to reduce verbosity
logging.basicConfig(level=logging.WARNING)

# Available models mapping
AVAILABLE_MODELS = {
    "gpt-4.1-nano": {
        "name": "GPT 4.1 Nano",
        "family": "gpt-4.1-nano",
        "description": "Lightweight, fast, and cost-effective for simple tasks",
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "context_length": 32000,
        "tags": ["Fast", "Efficient", "Short context"]
    },
    "gpt-4.1-mini": {
        "name": "GPT 4.1 Mini", 
        "family": "gpt-4.1-mini",
        "description": "Enhanced logic and reasoning, more capable than Nano, but still efficient",
        "vision": True,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "context_length": 64000,
        "tags": ["Reasoning", "General-purpose", "Efficient"]
    },
    "openai/gpt-4o": {
        "name": "GPT-4o",
        "family": "openai/gpt-4o",
        "description": "OpenAI's flagship multimodal model with advanced reasoning and vision capabilities",
        "vision": True,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "context_length": 128000,
        "tags": ["Multimodal", "Advanced reasoning", "OpenAI"]
    },
    "anthropic/claude-sonnet-4": {
        "name": "Claude Sonnet 4",
        "family": "anthropic/claude-sonnet-4",
        "description": "Anthropic's smart, efficient model for everyday use with strong reasoning capabilities",
        "vision": True,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "context_length": 200000,
        "tags": ["Reasoning", "General-purpose", "Anthropic"]
    },
    "gemini-2.0-flash": {
        "name": "Gemini 2.0 Flash",
        "family": "gemini-2.0-flash", 
        "description": "Fast, cost-efficient version of Gemini, optimized for value",
        "vision": True,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "context_length": 128000,
        "tags": ["Fast", "Cost-efficient", "Google"]
    },
    "google/gemini-2.5-flash": {
        "name": "Gemini 2.5 Flash",
        "family": "google/gemini-2.5-flash",
        "description": "Google's production-ready Gemini 2.5 Flash with enhanced performance and reliability",
        "vision": True,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "context_length": 128000,
        "tags": ["Production", "Enhanced", "Google"]
    },
    "gemini-2.5-pro-preview": {
        "name": "Gemini 2.5 Pro Preview",
        "family": "gemini-2.5-pro-preview",
        "description": "Google's latest multimodal model, understands both text and images",
        "vision": True,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "context_length": 256000,
        "tags": ["Multimodal", "Advanced reasoning", "Google"]
    },
    "gemini-2.5-flash-preview": {
        "name": "Gemini 2.5 Flash Preview",
        "family": "gemini-2.5-flash-preview",
        "description": "Preview version of Gemini 2.5 Flash with enhanced capabilities",
        "vision": True,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "context_length": 128000,
        "tags": ["Preview", "Enhanced", "Google"]
    },
    "llama-4-scout": {
        "name": "Llama 4 Scout",
        "family": "llama-4-scout-175b-instruct",
        "description": "Meta's Llama 4, focused on factual accuracy and reduced hallucinations",
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "context_length": 128000,
        "tags": ["Factual", "Accurate", "Meta"]
    },
    "llama-4-maverick": {
        "name": "Llama 4 Maverick",
        "family": "llama-4-maverick-175b-instruct",
        "description": "Latest with extended context window (128K tokens)",
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "context_length": 128000,
        "tags": ["Long context", "Document analysis", "Meta"]
    },
    "llama-3.3-70b": {
        "name": "Llama 3.3 70B",
        "family": "llama-3.3-70b-versatile",
        "description": "Large, high-performance model for a wide range of tasks",
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "context_length": 128000,
        "tags": ["High performance", "Versatile", "Meta"]
    },
    "deepseek-r1-distill-llama-70b": {
        "name": "Deepseek R1 Distilled 70B",
        "family": "deepseek-r1-distill-llama-70b",
        "description": "Specialized in math and science, distilled for efficiency",
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "context_length": 128000,
        "tags": ["Math/code", "Technical", "DeepSeek"]
    },
    "qwen-qwq-32b": {
        "name": "Qwen QwQ 32B",
        "family": "qwen-qwq-32b",
        "description": "Alibaba's Qwen model, strong at complex reasoning and multilingual tasks",
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "context_length": 128000,
        "tags": ["Reasoning", "Multilingual", "Alibaba"]
    },
    "mistral-saijo-24b": {
        "name": "Mistral Saijo 24B",
        "family": "mistral-saijo-24b",
        "description": "Mistral's model with strong multilingual capabilities",
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "context_length": 128000,
        "tags": ["Multilingual", "General-purpose", "Mistral"]
    }
}
# Configuration schema for AutoGen Studio
class QuietEuriConfig(BaseModel):
    """Configuration schema for QuietEuriChatCompletionClient"""
    api_key: Optional[str] = None
    model: str = "deepseek-r1-distill-llama-70b"  # Default model
    temperature: float = 0.1
    max_tokens: int = 2000

class QuietEuriChatCompletionClient(ChatCompletionClient):
    """Enhanced Euri AI chat completion client with AutoGen Studio compatibility"""
    
    component_config_schema = QuietEuriConfig

    def __init__(self, api_key: str = None, model: str = "deepseek-r1-distill-llama-70b"):
        # If no API key provided, try to get from environment
        if api_key is None:
            api_key = os.getenv("EURI_API_KEY")
        
        if not api_key:
            raise ValueError("EURI_API_KEY must be set in environment variables or passed as parameter")
        
        # Validate model
        if model not in AVAILABLE_MODELS:
            available = ", ".join(AVAILABLE_MODELS.keys())
            raise ValueError(f"Model '{model}' not supported. Available models: {available}")
            
        self._client = EuriaiClient(
            api_key=api_key,
            model=model
        )
        self._model = model
        self._model_config = AVAILABLE_MODELS[model]
        self._model_info = self._create_model_info()
        self._total_usage = RequestUsage(prompt_tokens=0, completion_tokens=0)
    
    def _create_model_info(self) -> ModelInfo:
        """Create ModelInfo based on selected model configuration"""
        config = self._model_config
        return ModelInfo(
            family=config["family"],
            vision=config["vision"],
            function_calling=config["function_calling"],
            json_output=config["json_output"],
            structured_output=config["structured_output"]
        )
    
    @property
    def model_info(self) -> ModelInfo:
        return self._model_info
    
    @property 
    def capabilities(self) -> ModelInfo:
        return self._model_info
    
    @property
    def model_name(self) -> str:
        """Get the display name of the current model"""
        return self._model_config["name"]
    
    @property
    def model_description(self) -> str:
        """Get the description of the current model"""
        return self._model_config["description"]
    
    @classmethod
    def list_available_models(cls) -> dict:
        """Get list of all available models with their information"""
        return AVAILABLE_MODELS
    
    @classmethod
    def print_available_models(cls):
        """Print a formatted list of available models"""
        print("\n🤖 Available Euri AI Models:")
        print("=" * 50)
        
        for model_id, config in AVAILABLE_MODELS.items():
            tags_str = " | ".join(config["tags"])
            print(f"\n📋 {config['name']}")
            print(f"   ID: {model_id}")
            print(f"   Description: {config['description']}")
            print(f"   Vision: {'✅' if config['vision'] else '❌'}")
            print(f"   Context: {config['context_length']:,} tokens")
            print(f"   Tags: {tags_str}")
    
    async def create(
        self,
        messages: Sequence[LLMMessage],
        *,
        tools: Sequence[Union[Tool, ToolSchema]] = [],
        json_output: Optional[Union[bool, type[BaseModel]]] = None,
        extra_create_args: Mapping[str, Any] = {},
        cancellation_token: Optional[CancellationToken] = None,
    ) -> CreateResult:
        try:
            prompt = self._messages_to_prompt(messages)
            
            if json_output and isinstance(json_output, type) and issubclass(json_output, BaseModel):
                schema = json_output.model_json_schema()
                prompt = f"{prompt}\n\nRespond with JSON matching this schema:\n{json.dumps(schema, indent=2)}"
            elif json_output is True:
                prompt = f"{prompt}\n\nRespond with valid JSON only."
            
            raw_response = self._client.generate_completion(
                prompt=prompt,
                temperature=extra_create_args.get('temperature', 0.1),
                max_tokens=extra_create_args.get('max_tokens', 2000)
            )
            
            clean_content = self._format_response(raw_response)
            
            usage = RequestUsage(
                prompt_tokens=int(len(prompt.split()) * 1.3),
                completion_tokens=int(len(str(clean_content).split()) * 1.3)
            )
            
            self._total_usage = RequestUsage(
                prompt_tokens=self._total_usage.prompt_tokens + usage.prompt_tokens,
                completion_tokens=self._total_usage.completion_tokens + usage.completion_tokens
            )
            
            return CreateResult(
                content=clean_content,
                finish_reason="stop",
                usage=usage,
                cached=False,
                logprobs=None
            )
            
        except Exception as e:
            return CreateResult(
                content=f"Error: {str(e)}",
                finish_reason="error",
                usage=RequestUsage(prompt_tokens=0, completion_tokens=0),
                cached=False,
                logprobs=None
            )
    
    async def create_stream(
        self,
        messages: Sequence[LLMMessage],
        *,
        tools: Sequence[Union[Tool, ToolSchema]] = [],
        json_output: Optional[Union[bool, type[BaseModel]]] = None,
        extra_create_args: Mapping[str, Any] = {},
        cancellation_token: Optional[CancellationToken] = None,
    ) -> AsyncGenerator[Union[str, CreateResult], None]:
        result = await self.create(
            messages=messages,
            tools=tools,
            json_output=json_output,
            extra_create_args=extra_create_args,
            cancellation_token=cancellation_token
        )
        
        # Simulate streaming by yielding chunks with proper formatting
        if isinstance(result.content, str):
            # Split by sentences to maintain readability during streaming
            sentences = self._split_into_sentences(result.content)
            for sentence in sentences:
                yield sentence
                await asyncio.sleep(0.02)  # Slightly slower for better readability
        
        yield result
    
    def count_tokens(
        self, 
        messages: Sequence[LLMMessage], 
        *, 
        tools: Sequence[Union[Tool, ToolSchema]] = []
    ) -> int:
        prompt = self._messages_to_prompt(messages)
        return int(len(prompt.split()) * 1.3)
    
    def remaining_tokens(
        self, 
        messages: Sequence[LLMMessage], 
        *, 
        tools: Sequence[Union[Tool, ToolSchema]] = []
    ) -> int:
        used_tokens = self.count_tokens(messages, tools=tools)
        context_length = self._model_config["context_length"]
        return max(0, context_length - used_tokens)
    
    def total_usage(self) -> RequestUsage:
        return self._total_usage
    
    def actual_usage(self) -> RequestUsage:
        return self._total_usage
    
    async def close(self) -> None:
        pass
    
    def _format_response(self, response) -> str:
        """Enhanced response formatting with better text processing"""
        raw_content = self._extract_content(response)
        
        if not raw_content:
            return ""
        
        # Clean and format the content
        formatted_content = self._clean_text(raw_content)
        formatted_content = self._format_markdown(formatted_content)
        formatted_content = self._fix_spacing(formatted_content)
        
        return formatted_content
    
    def _extract_content(self, response) -> str:
        """Extract content from various response formats"""
        if isinstance(response, str):
            return response
        if isinstance(response, dict):
            if 'choices' in response and response['choices']:
                return response['choices'][0]['message']['content']
            if 'content' in response:
                return response['content']
            if 'text' in response:
                return response['text']
            if 'message' in response:
                return response['message']
        return str(response)
    
    def _clean_text(self, text: str) -> str:
        """Clean up text formatting issues"""
        if not text:
            return ""
        
        # Remove excessive whitespace while preserving intentional formatting
        text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)  # Max 2 consecutive newlines
        text = re.sub(r'[ \t]+', ' ', text)  # Multiple spaces/tabs to single space
        text = re.sub(r' *\n *', '\n', text)  # Remove spaces around newlines
        
        # Fix common formatting issues
        text = re.sub(r'([.!?])\s*([A-Z])', r'\1 \2', text)  # Ensure space after sentence endings
        text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)  # Add space between camelCase words if needed
        
        return text.strip()
    
    def _format_markdown(self, text: str) -> str:
        """Improve markdown formatting"""
        if not text:
            return ""
        
        # Ensure proper spacing around headers
        text = re.sub(r'^(#{1,6})\s*(.+)$', r'\1 \2', text, flags=re.MULTILINE)
        
        # Ensure proper spacing around code blocks
        text = re.sub(r'```(\w*)\n', r'```\1\n', text)
        text = re.sub(r'\n```', r'\n```', text)
        
        # Fix list formatting
        text = re.sub(r'^(\s*)[-*+]\s+', r'\1- ', text, flags=re.MULTILINE)
        text = re.sub(r'^(\s*)\d+\.\s+', r'\1\g<1>. ', text, flags=re.MULTILINE)
        
        # Ensure proper spacing around bold/italic
        text = re.sub(r'\*\*([^*]+)\*\*', r'**\1**', text)
        text = re.sub(r'\*([^*]+)\*', r'*\1*', text)
        
        return text
    
    def _fix_spacing(self, text: str) -> str:
        """Fix spacing and line breaks for better readability"""
        if not text:
            return ""
        
        lines = text.split('\n')
        formatted_lines = []
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                formatted_lines.append('')
                continue
            
            # Add proper spacing after certain elements
            if line.startswith(('#', '-', '*', '+')):
                if i > 0 and formatted_lines and formatted_lines[-1]:
                    formatted_lines.append('')
            
            formatted_lines.append(line)
        
        # Join lines and clean up excessive blank lines
        result = '\n'.join(formatted_lines)
        result = re.sub(r'\n{3,}', '\n\n', result)
        
        return result.strip()
    
    def _split_into_sentences(self, text: str) -> list[str]:
        """Split text into sentences for streaming while preserving formatting"""
        if not text:
            return []
        
        # Split by sentences but keep code blocks and lists intact
        sentences = []
        current_sentence = ""
        in_code_block = False
        
        lines = text.split('\n')
        for line in lines:
            if '```' in line:
                in_code_block = not in_code_block
                current_sentence += line + '\n'
                if not in_code_block:
                    sentences.append(current_sentence)
                    current_sentence = ""
                continue
            
            if in_code_block:
                current_sentence += line + '\n'
                continue
            
            # For regular text, split by sentence endings
            line_sentences = re.split(r'([.!?]+\s+)', line)
            for part in line_sentences:
                current_sentence += part
                if re.match(r'[.!?]+\s+$', part):
                    sentences.append(current_sentence)
                    current_sentence = ""
        
        if current_sentence.strip():
            sentences.append(current_sentence)
        
        return [s for s in sentences if s.strip()]
    
    def _messages_to_prompt(self, messages: Sequence[LLMMessage]) -> str:
        """Convert messages to a well-formatted prompt"""
        prompt_parts = []
        for msg in messages:
            if hasattr(msg, 'content'):
                content = msg.content
                source = getattr(msg, 'source', 'user')
            elif isinstance(msg, dict):
                source = msg.get('source', 'user')
                content = msg.get('content', '')
            else:
                content = str(msg)
                source = 'user'
            
            if content:
                # Clean the content before adding to prompt
                cleaned_content = self._clean_text(str(content))
                prompt_parts.append(f"{source.title()}: {cleaned_content}")
        
        return "\n\n".join(prompt_parts)
    
    @classmethod
    def _from_config(cls, config: Union[dict, QuietEuriConfig]) -> "QuietEuriChatCompletionClient":
        """Create client from configuration - required for AutoGen Studio"""
        if isinstance(config, dict):
            config = QuietEuriConfig(**config)
        return cls(
            api_key=config.api_key,
            model=config.model
        )

# Convenience functions
def create_quiet_euri_client(model: str = "deepseek-r1-distill-llama-70b", **kwargs):
    """Create a quiet Euri client with minimal logging and enhanced formatting"""
    return QuietEuriChatCompletionClient(model=model, **kwargs)

def get_euri_client(model: str = "deepseek-r1-distill-llama-70b"):
    """Get Euri client instance with specified model"""
    return QuietEuriChatCompletionClient(model=model)

# For AutoGen Studio compatibility - create default instance
def get_default_euri_client():
    """Get default Euri client instance"""
    return QuietEuriChatCompletionClient()

# Enhanced DSA-specific model selection
DSA_OPTIMIZED_MODELS = {
    "mathematical": "deepseek-r1-distill-llama-70b",  # Best for math/algorithms
    "reasoning": "openai/gpt-4o",  # Best for complex reasoning
    "coding": "deepseek-r1-distill-llama-70b",  # Best for code generation
    "general": "anthropic/claude-sonnet-4",  # Best for general DSA problems
    "complex": "gemini-2.5-pro-preview",  # Best for complex multi-step problems
    "optimization": "qwen-qwq-32b",  # Good for optimization problems
    "default": "openai/gpt-4o"  # Safe default choice
}

def get_dsa_optimized_model(problem_type: str = "general", complexity: str = "medium") -> str:
    """
    Get the optimal model for specific DSA problem types

    Args:
        problem_type: Type of DSA problem (mathematical, reasoning, coding, etc.)
        complexity: Problem complexity (easy, medium, hard, expert)

    Returns:
        Model name optimized for the problem type
    """
    # Map complexity to model preference
    if complexity.lower() == "expert":
        return DSA_OPTIMIZED_MODELS.get("complex", DSA_OPTIMIZED_MODELS["default"])
    elif problem_type.lower() in ["math", "mathematical", "number_theory"]:
        return DSA_OPTIMIZED_MODELS["mathematical"]
    elif problem_type.lower() in ["graph", "dynamic_programming", "complex_algorithms"]:
        return DSA_OPTIMIZED_MODELS["reasoning"]
    elif problem_type.lower() in ["implementation", "coding", "data_structures"]:
        return DSA_OPTIMIZED_MODELS["coding"]
    elif problem_type.lower() in ["optimization", "scheduling", "greedy"]:
        return DSA_OPTIMIZED_MODELS["optimization"]
    else:
        return DSA_OPTIMIZED_MODELS["general"]

def create_dsa_client(problem_type: str = "general", complexity: str = "medium",
                     custom_model: str = None) -> QuietEuriChatCompletionClient:
    """
    Create a model client optimized for DSA problems

    Args:
        problem_type: Type of DSA problem
        complexity: Problem complexity level
        custom_model: Override with custom model if specified

    Returns:
        Optimized QuietEuriChatCompletionClient instance
    """
    if custom_model:
        model = custom_model
    else:
        model = get_dsa_optimized_model(problem_type, complexity)

    print(f"🤖 Selected model: {AVAILABLE_MODELS[model]['name']} for {problem_type} ({complexity})")
    return QuietEuriChatCompletionClient(model=model)

# Compatibility functions for existing code
def model_client(model: str = "openai/gpt-4o"):
    """Create a model client with specified model - compatibility function"""
    return QuietEuriChatCompletionClient(model=model)

def get_model_client(model: str = "openai/gpt-4o"):
    """Get model client instance with specified model - compatibility function"""
    return QuietEuriChatCompletionClient(model=model)

# Disable verbose AutoGen logging
logger = logging.getLogger(__name__)
for name in logging.root.manager.loggerDict:
    if name.startswith('autogen'):
        logging.getLogger(name).setLevel(logging.WARNING)

load_dotenv()

# Example usage and model listing
if __name__ == "__main__":
    # Print available models
    QuietEuriChatCompletionClient.print_available_models()
    
    # Example of creating clients with different models
    print("\n🚀 Example Usage:")
    print("=" * 30)
    
    print("\n# Create a client with GPT 4.1 Mini for reasoning tasks:")
    print("client = create_quiet_euri_client('gpt-4.1-mini')")
    
    print("\n# Create a client with Gemini 2.5 Pro for multimodal tasks:")
    print("client = create_quiet_euri_client('gemini-2.5-pro-preview')")
    
    print("\n# Create a client with Llama 4 Scout for factual accuracy:")
    print("client = create_quiet_euri_client('llama-4-scout')")
    
    print("\n# Create a client with DeepSeek for math/code tasks:")
    print("client = create_quiet_euri_client('deepseek-r1-distill-llama-70b')")