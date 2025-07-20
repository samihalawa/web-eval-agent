# 🌊 WebFlow Navigator

> *Intelligent web automation and testing made simple*

![WebFlow Navigator Light Mode](https://github.com/user-attachments/assets/dc7a52cf-1ec2-45e2-b3ff-c36c9267f940)

WebFlow Navigator is a modern, intelligent web automation and testing platform that combines the power of AI-driven browser automation with a beautiful, intuitive control center. Built for developers, testers, and automation engineers who demand both functionality and elegance.

## ✨ What Makes WebFlow Navigator Special

**🎯 Intelligent Automation**: Powered by advanced AI models that understand your web applications like a human user would.

**🎨 Beautiful Interface**: Modern, responsive control center with both light and dark themes.

**🔄 Real-time Monitoring**: Watch your tests run live with comprehensive logging and network monitoring.

**🛠️ Developer-Friendly**: Built as an MCP (Model Context Protocol) server that integrates seamlessly with modern AI development tools.

## 🚀 Key Features

### 🌐 Advanced Browser Automation
- **Smart Navigation**: AI-powered element detection and interaction
- **Visual Feedback**: Real-time screenshots and browser state monitoring
- **Interactive Control**: Pause, resume, or stop automation at any time
- **Cross-platform**: Works on Windows, macOS, and Linux

### 📊 Comprehensive Monitoring
- **Console Logs**: Real-time JavaScript console monitoring
- **Network Activity**: Track XHR/Fetch requests and responses
- **Agent Status**: Visual indicators for automation state
- **Error Detection**: Automatic capture and reporting of issues

### 🎨 Modern Control Center
- **Dual Themes**: Beautiful light and dark mode interfaces
- **Responsive Design**: Works perfectly on desktop and mobile
- **Split/Joined Views**: Flexible layout options for different workflows
- **Copy-to-Clipboard**: Easy log sharing and debugging

### 🔧 Developer Integration
- **MCP Protocol**: Native integration with Cursor, Cline, and other AI tools
- **RESTful API**: Programmatic access to all features
- **Real-time Events**: WebSocket-based live updates
- **Extensible**: Easy to customize and extend

## 🏁 Quick Start

### Prerequisites
- Python 3.11 or higher
- Node.js and npm (for Playwright installation)
- Modern web browser

### Installation

1. **Install WebFlow Navigator**
   ```bash
   pip install webflow-navigator
   ```

2. **Install Playwright browsers**
   ```bash
   npx playwright install
   ```

3. **Start WebFlow Navigator**
   ```bash
   webflow-navigator
   ```

4. **Open your browser** and navigate to `http://localhost:5000`

## 🎮 Usage

### Basic Web Testing

```python
from webflow_navigator import WebFlowNavigator

# Initialize navigator
navigator = WebFlowNavigator()

# Start a test session
result = navigator.evaluate_web_app(
    url="http://localhost:3000",
    task="Test the user registration flow and report any UX issues"
)

print(result.summary)
```

### Using with AI Development Tools

WebFlow Navigator integrates seamlessly with AI development environments:

**In Cursor/Cline:**
```
Test my React app at http://localhost:3000 - use webflow-navigator to check the signup flow and identify any usability issues.
```

**MCP Configuration:**
```json
{
  "webflow-navigator": {
    "command": "webflow-navigator",
    "args": ["--server"],
    "env": {
      "WEBFLOW_API_KEY": "your-key-here"
    }
  }
}
```

## 🎨 Interface Modes

### Light Mode
![WebFlow Navigator Light Mode](https://github.com/user-attachments/assets/dc7a52cf-1ec2-45e2-b3ff-c36c9267f940)

Clean, professional interface perfect for daytime development sessions.

### Dark Mode  
![WebFlow Navigator Dark Mode](https://github.com/user-attachments/assets/08ee9947-9e58-46cc-9ad1-c83674082afe)

Eye-friendly dark theme ideal for extended coding sessions and low-light environments.

## 📊 MCP Tools Reference

WebFlow Navigator provides powerful MCP tools for AI development environments:

| Tool | Description | Parameters |
|------|-------------|------------|
| `webflow_evaluate` | Run comprehensive web app evaluation | `url`, `task`, `headless_browser` |
| `webflow_navigate` | Navigate to specific page and capture state | `url`, `wait_for` |
| `webflow_interact` | Perform specific interactions on page | `action`, `target`, `value` |
| `webflow_screenshot` | Capture page screenshot | `full_page`, `element_selector` |
| `webflow_setup_session` | Configure browser session with auth | `url`, `login_flow` |

### Example Tool Usage

```bash
# In your AI development environment
"Use webflow_evaluate to test my e-commerce site at http://localhost:3000. Focus on the checkout process and identify any friction points."

"Take a webflow_screenshot of the homepage and then use webflow_navigate to test the search functionality."
```

## 🔍 Monitoring and Debugging

### Console Monitoring
WebFlow Navigator automatically captures:
- JavaScript errors and warnings
- Console.log outputs  
- Performance metrics
- Resource loading issues

### Network Monitoring
Track all network activity:
- XHR and Fetch requests
- Response status codes
- Request/response headers
- Timing information

### Visual Debugging
- Real-time browser screenshots
- Element highlighting
- Click and interaction visualization
- Step-by-step action replay

## 🛠️ Advanced Configuration

### Environment Variables

```bash
# Core settings
WEBFLOW_API_KEY=your-api-key-here
WEBFLOW_PORT=5000
WEBFLOW_HOST=localhost

# Browser settings
WEBFLOW_HEADLESS=false
WEBFLOW_BROWSER=chromium
WEBFLOW_VIEWPORT_WIDTH=1920
WEBFLOW_VIEWPORT_HEIGHT=1080

# Performance settings
WEBFLOW_TIMEOUT=30000
WEBFLOW_WAIT_FOR_SELECTOR_TIMEOUT=10000
WEBFLOW_MAX_RETRIES=3
```

## 🏗️ Architecture

WebFlow Navigator is built with modern technologies:

- **Backend**: Python with Flask and SocketIO
- **Frontend**: Modern HTML5, CSS3, and JavaScript
- **Automation**: Playwright for browser control
- **AI Integration**: Support for OpenAI, Anthropic, and Google models
- **Protocol**: MCP (Model Context Protocol) for AI tool integration

## 📋 Example Output Report

```text
📊 WebFlow Navigator Evaluation Report for http://localhost:3000 complete!
📝 Task: Test the user registration flow and report any UX issues.

🔍 Agent Steps
  📍 1. Navigate → http://localhost:3000
  📍 2. Click     "Sign Up"      (button)
  📍 3. Fill      "Email"        (input)
  📍 4. Fill      "Password"     (input)
  📍 5. Click     "Register"     (button)
  📍 6. Verify    "Welcome!"     (success message)
🏁 Flow completed successfully – Registration UX is intuitive and smooth.

🖥️ Console Logs (5)
  1. [info] React App started successfully
  2. [debug] API call: POST /api/register
  3. [info] User registered successfully
     …

🌐 Network Requests (8)
  1. POST /api/register                     201
  2. GET  /api/user/profile                 200
     …

⏱️ Timeline
  01:16:23.293 🖥️ Console [info] React App started
  01:16:25.412 🤖 Navigate → Sign Up page
  01:16:27.891 🤖 Fill registration form
  01:16:30.205 🤖 ✅ Registration successful
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/your-org/webflow-navigator.git
cd webflow-navigator

# Install development dependencies
pip install -e ".[dev]"

# Start development server
python -m webflow_navigator --dev
```

## 📝 License

WebFlow Navigator is released under the MIT License. See [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

WebFlow Navigator builds upon the excellent work of:
- [Playwright](https://playwright.dev) for browser automation
- [MCP](https://modelcontextprotocol.io) for AI tool integration
- [Flask](https://flask.palletsprojects.com) for the web framework
- [Tailwind CSS](https://tailwindcss.com) for beautiful styling

---

**Built with ❤️ for the developer community**

*WebFlow Navigator - Making web automation intelligent, beautiful, and accessible to everyone.*
