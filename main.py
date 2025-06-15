from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001")

server_params = StdioServerParameters(
    command="npx",
    # Make sure to update to the full absolute path to your math_server.py file
    args=["@browsermcp/mcp@latest"],
)


async def chat_with_agent():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            print(*[tool.name for tool in tools])
            agent = create_react_agent(model, tools)

            # Start conversation history
            messages = [
                {
                    "role": "system",
                    "content": "You are a good researcher and LinkedIn content creator who can create LinkedIn content that is relevant and engaging. You can given tools to control browser use these tools to accomplish user given task. Think step by step, plan and then execute.",
                }
            ]

            print("Type 'exit' or 'quit' to end the chat.")
            while True:
                user_input = input("\nYou: ")
                if user_input.strip().lower() in {"exit", "quit"}:
                    print("Bye bye!")
                    break

                # Add user message to history
                messages.append({"role": "user", "content": user_input})

                # Call the agent with the full message history
                agent_response = await agent.ainvoke({"messages": messages})

                # Extract agent's reply and add to history
                ai_message = agent_response["messages"][-1].content
                print(f"Agent: {ai_message}")


if __name__ == "__main__":
    asyncio.run(chat_with_agent())