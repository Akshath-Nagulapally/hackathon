import asyncio

from agents import Agent, Runner, function_tool

from dotenv import load_dotenv

from no_cookies import run_browse

load_dotenv()


from langchain_openai import ChatOpenAI
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()




course_names = ["CS128", "CS173", "CS341"]

current_date = "13th march 2025"

login_credentials = f"My login credentials are as follows: {os.environ.get('email')} and {os.environ.get('password')}"

student_question = "What is the hardest part of this semester going to be?"

for x in course_names:

    information = []
    website_name = x
    
    prompt = f"""
    The current date is {current_date}
    The login credentials are as follows: {login_credentials}
    Your job is to visit {website_name} at UIUC and tell me what the most important thing is to accomplish for my grade.
    The student's question is as follows: {student_question}
    """
    
    info_bit = run_browse(prompt)
    print(info_bit)
    information.append(str(info_bit))


empty_string = ""

for thing in information:
    empty_string += thing


print("This is the empty_string_array" + empty_string)


