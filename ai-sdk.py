import asyncio

from agents import Agent, Runner, function_tool

import os
from dotenv import load_dotenv

from agents import Agent, Runner, function_tool
from sdk import student_question
import agentops
agentops.init("5110af17-2d42-47e6-85c1-41e9015150a4")

from sdk import empty_string

# Load API key from environment variables
load_dotenv()  # Load variables from .env file if it exists
#context = empty_string


@function_tool
def get_weather(city: str) -> str:
    return "The hardest part of the course is the MP"


agent = Agent(
    name="Hello world",
    instructions="You are a helpful agent who answers questions.",
)


async def main():
    result = await Runner.run(agent, input= "This is the question that the student asked:" + student_question + "This is the data:" + empty_string)
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
