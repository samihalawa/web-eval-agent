# Web-Eval-Agent Without OPERATIVE_API_KEY

This fork has been modified to bypass the OPERATIVE_API_KEY requirement. The original code used operative.sh as a proxy for Claude API calls, but this version allows you to use your own LLM providers directly.

## Changes Made

1. **API Validation Bypass**: The `validate_api_key()` function now always returns `True`
2. **Removed API Key Checks**: Startup validation and per-tool validation have been removed
3. **Alternative LLM Support**: Added support for direct API keys from multiple providers

## How to Use

### Default: Use Gemini (Recommended)
The `.env` file includes a Gemini API key that works with browser-use:
```bash
# Already configured in .env:
GOOGLE_API_KEY=AIzaSyC8zNr008DeS7ipixHGKxMKfBnXz-L7OD8
WEB_EVAL_USE_BROWSER_USE_SUBAGENT=true
```

### Option 1: Use Your Own Anthropic API Key
```bash
export ANTHROPIC_API_KEY="your-anthropic-api-key"
# Run the MCP server normally
```

### Option 2: Use OpenAI API
```bash
export OPENAI_API_KEY="your-openai-api-key"
# Run the MCP server normally
```

### Option 3: Disable Browser-Use Subagent
To use direct browser control without any nested LLM:
```bash
export WEB_EVAL_USE_BROWSER_USE_SUBAGENT=false
```

### Option 4: Use Original Operative.sh (Fallback)
If no other API keys are configured, it falls back to the operative.sh proxy.

## Files Modified

- `webEvalAgent/src/api_utils.py`: Bypassed API validation
- `webEvalAgent/mcp_server.py`: Removed API key validation checks
- `webEvalAgent/src/browser_utils.py`: Added alternative LLM configuration
- `webEvalAgent/src/llm_config.py`: New file for LLM provider selection

## Note

The core browser automation functionality remains unchanged. Only the API key validation and LLM provider selection have been modified.

## Performance Considerations

- Using direct API keys may be slower than operative.sh's optimized proxy
- The original claims 2x speed improvement through their service
- For best results, use Claude 3.5 Sonnet via Anthropic API key