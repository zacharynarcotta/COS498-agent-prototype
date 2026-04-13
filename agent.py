"""Module that allows the LessonAgent to be run in Python"""

import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    """Running the agent"""
    async for message in query(
        prompt="What files are in this directory?",
        options=ClaudeAgentOptions(allowed_tools=["Bash", "Glob"]),
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
