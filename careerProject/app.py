import os
from dotenv import load_dotenv
from google import genai

load_dotenv() #load .env
api_key = os.getenv("GEMINI_API_KEY")# get api key

client = genai.Client(api_key=api_key) # create gemini client

generation_config = {
    'max_output_tokens': 500,
    'thinking_level': 'medium',
}

student_name=input("Student name : ")
education = input ("Education : ")
skills = input ("Skills : ")
projects = input("Projects : ")
experience = input("Experience : ")

user_input= input("Enter your Query : ") # input user se lenge aur niche response me define karenge

#system prompt = default prompt which ai alway remain when generate any output

#context enginerring = app ye iske hisab se sochega 
student_context= f"""
name:{student_name}
education:{education}
skills:{skills}
projects:{projects}
experience:{experience}
"""

#prompt engineer
career_prompt = f"""
ROLE: You are CareerTwin, You are an AI career advisor for post-grad students

CONTEXT:
CareerTwin helps students understand software engineering career paths, required technical skills, learning priorities, projects and interview preparation.

OBJECTIVE:
analyze the student current profile against their target job role .

ANALYSIS_REQUIREMENTS:
1. Profile Summary
- Summarize the student's current technical profile

2. Strengths
- Identify skills, projects, education or experience that are relevant to the target role.

3. Skill gaps
- Identify important skills required for target role that are missing or insufficiently represented.

4. Priority Skills
- Select the most important missing skills that student should learn first.

5. Interview Topics
- Identify technical topics the student should explore for the target role

6. Recommendations
- Provide practical next steps for becoming job ready

CONTEXT:
CareerTwin helps students understand software engineering career paths, required technical skills, learning priorities, projects and interview preparation.

TASK:
Answer the student's career related question clearly and practically. Give recommendations that are relevant to the student's career goal

CONSTRAINTS:
- Do not provide unrelated information
- Do not assume skills that the student has not mentioned
- Prefer practical and actionable recommendations
- Keep the response concise and easy to understand

{student_context}

OUTPUT_FORMAT:
Profile Summary:
<summary>

Strengths:
- <strength>
- <strength>

Skill Gaps:
- <skill>
- <skill>

Priority Skills:
1. <skill>
2. <skill>
3. <skill>

Interview Topics:
- <topic>
- <topic>

Recommendations:
1. <recommendation>
2. <recommendation>
3. <recommendation>


STUDENT QUESTION:
{user_input}

"""

# Send request
response = client.interactions.create(
    model = "gemini-flash-latest",
    input = user_input, #input take from user
    generation_config=generation_config,
)

# response 
print("==== GEMINI ====")
print(response.output_text)