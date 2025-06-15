# Auto Browse

This repository demonstrates the powerful combination of **LangGraph reactive agents** and **BrowserMCP** to automate browser interactions for LinkedIn research and content creation tasks.

## 🚀 Overview

The project showcases an intelligent agent that can:
- Research topics and trends on LinkedIn
- Analyze competitor content and engagement
- Generate relevant and engaging LinkedIn posts
- Automate browser-based tasks for content research

## 🛠️ Technology Stack

- **[LangGraph](https://github.com/langchain-ai/langgraph)**: Reactive agent framework for building stateful, multi-actor applications
- **[BrowserMCP](https://github.com/modelcontextprotocol/servers/tree/main/src/browser)**: Model Context Protocol server for browser automation
- **[Google Gemini](https://ai.google.dev/)**: Advanced language model for content generation
- **[MCP (Model Context Protocol)](https://modelcontextprotocol.io/)**: Standardized protocol for connecting AI models with external tools

## 📋 Prerequisites

- Python 3.11 or higher
- Node.js (for BrowserMCP)
- Google AI API key

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd linked-job-apply
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   # or if using uv:
   uv sync
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_google_ai_api_key_here
   ```

4. **Install BrowserMCP (automatically handled by the script):**
   The application automatically installs and runs `@browsermcp/mcp@latest` via npx.

## 🚀 Usage

Run the interactive agent:

```bash
python main.py
```

The agent will start and display available browser tools. You can then interact with it using natural language commands such as:

- "Research the latest trends in AI on LinkedIn"
- "Find popular posts about Python programming and analyze their engagement"
- "Create a LinkedIn post about machine learning best practices"
- "Browse LinkedIn profiles of top AI researchers"

Type `exit` or `quit` to end the session.

## 🤖 Agent Capabilities

The agent is configured as a LinkedIn researcher and content creator with the following capabilities:

### Browser Automation
- Navigate to LinkedIn and other websites
- Extract content from web pages
- Interact with web elements (click, scroll, type)
- Take screenshots for analysis

### Content Research
- Analyze trending topics and hashtags
- Study competitor content strategies
- Gather engagement metrics and insights
- Monitor industry discussions

### Content Creation
- Generate LinkedIn posts based on research
- Optimize content for engagement
- Suggest relevant hashtags and mentions
- Create content calendars and strategies

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Input    │───▶│  LangGraph Agent │───▶│  Google Gemini  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │   BrowserMCP     │
                       │   (via MCP)      │
                       └──────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │   Web Browser    │
                       │   Automation     │
                       └──────────────────┘
```

## 📁 Project Structure

```
linked-job-apply/
├── main.py              # Main application entry point
├── pyproject.toml       # Project configuration and dependencies
├── .env                 # Environment variables (create this)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🔧 Configuration

The agent can be customized by modifying the system prompt in `main.py`:

```python
messages = [
    {
        "role": "system",
        "content": "You are a good researcher and LinkedIn content creator..."
    }
]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph) for the reactive agent framework
- [Model Context Protocol](https://modelcontextprotocol.io/) for standardized tool integration
- [BrowserMCP](https://github.com/modelcontextprotocol/servers) for browser automation capabilities
- [Google AI](https://ai.google.dev/) for the Gemini language model

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub or reach out to the maintainers.

---

**Happy LinkedIn content creation! 🎉**