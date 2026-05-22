import asyncio
import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from google.antigravity import Agent, LocalAgentConfig

async def init_environment():
    async with Agent(LocalAgentConfig()) as agent:
        response = await agent.chat("Hello, World!")
        print(await response.text())

if __name__ == "__main__":
    asyncio.run(init_environment())
