#!/usr/bin/env python3
"""
Alternative LLM configuration for bypassing operative.sh proxy
"""

import os
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

def get_llm_client(tool_call_id: str = None):
    """
    Get an LLM client based on available API keys.
    
    Priority:
    1. Direct Anthropic API key
    2. OpenAI API key (using GPT-4)
    3. Local LLM via Ollama
    """
    
    # Option 1: Direct Anthropic API
    if os.environ.get("ANTHROPIC_API_KEY") and os.environ.get("ANTHROPIC_API_KEY") != 'not_a_real_key':
        return ChatAnthropic(
            model="claude-3-5-sonnet-20241022",
            api_key=os.environ.get("ANTHROPIC_API_KEY")
        )
    
    # Option 2: OpenAI API
    elif os.environ.get("OPENAI_API_KEY"):
        return ChatOpenAI(
            model="gpt-4-turbo-preview",
            api_key=os.environ.get("OPENAI_API_KEY")
        )
    
    # Option 3: Local Ollama
    else:
        try:
            from langchain_community.llms import Ollama
            return Ollama(model="llama2")
        except:
            # Fallback to a mock LLM for testing
            raise Exception(
                "No LLM API key found. Please set one of:\n"
                "- ANTHROPIC_API_KEY for Claude\n"
                "- OPENAI_API_KEY for GPT-4\n"
                "- Or install Ollama for local LLM"
            )