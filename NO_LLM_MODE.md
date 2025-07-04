# No-LLM Mode for Web-Eval-Agent

This mode eliminates the need for a nested LLM by providing direct browser control to the calling agent.

## Why No-LLM Mode?

The original architecture uses a nested LLM:
```
Your Agent (Claude/GPT) → MCP Tool → Browser-Use Agent (needs another LLM) → Browser
```

With No-LLM mode:
```
Your Agent (Claude/GPT) → MCP Tool → Direct Browser Control → Browser
```

## Benefits

1. **No nested API costs** - Only your main agent uses API calls
2. **Full control** - Your agent sees everything and makes all decisions
3. **Simpler architecture** - No dependency on operative.sh or additional LLM APIs
4. **Transparent operation** - You see exactly what the browser sees

## How to Enable

Set the environment variable before running:
```bash
export WEB_EVAL_USE_BROWSER_USE_SUBAGENT=false
```

## How It Works

Instead of using browser-use's Agent (which needs its own LLM), the tool:
1. Takes screenshots at each step
2. Extracts page information (title, URL, text, interactive elements)
3. Returns this info to YOUR agent
4. YOUR agent decides what to do next

## Example Usage

When you call the web_eval_agent tool in no-LLM mode:

1. **Initial Response**: You'll get a screenshot and page analysis
2. **Interactive Elements**: List of buttons, links, inputs you can interact with
3. **Next Steps**: You decide what to click, type, or navigate to

## Limitations

- Requires more back-and-forth between your agent and the tool
- Your agent needs to understand web page structure
- May be slower for complex multi-step tasks

## When to Use

- When you want to avoid nested LLM costs
- When you need full visibility into browser actions
- When you don't have access to Anthropic/OpenAI APIs
- When you want your agent to learn from direct browser interaction