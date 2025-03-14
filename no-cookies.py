from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()


async def browse(instruction: str):
    agent = Agent(
        task=instruction,
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

def run_browse(instruction):
    asyncio.run(browse(instruction))

course_list = ["CS173", "CS128"]
platforms = ["https://courses.grainger.illinois.edu/cs173/sp2025/ALL-lectures/", "https://cs128.org/"]


current_date = "13th march 2025"

login_credentials = f"My login credentials are as follows: {os.environ.get('email')} and {os.environ.get('password')}"

website_name = "CS128"

prompt = f"""
The current date is {current_date}
The login credentials are as follows: {login_credentials}
Your job is to visit {website_name} at UIUC and tell me what the most important thing is to accomplish for my grade.
"""

run_browse(prompt)