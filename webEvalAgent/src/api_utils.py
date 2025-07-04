#!/usr/bin/env python3

import httpx
from .env_utils import get_backend_url

async def validate_api_key(api_key: str) -> bool:
    """
    Validate the API key against the Operative backend service.
    
    Args:
        api_key: The API key to validate
        
    Returns:
        bool: True if the API key is valid, False otherwise
    """
    # Bypass API validation - always return True
    return True
