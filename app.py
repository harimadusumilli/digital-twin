import os
from openai import OpenAI
# import requests
# import random
# import re
# import uuid
# import chromadb
# import json
import gradio as gr


#--------------------------------------------------------------------------------------------
# Setup environment variables
#----------------------------------------------------------------------------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise Exception("API KEY is missing")
client = OpenAI()

#--------------------------------------------------------------------------------------------
# Load up Documents
#--------------------------------------------------------------------------------------------
document_professional_summary = """
AI Engineer & Quality Engineering Leader-Architect in software engineering, Enterprise Quality Engineering, Test Automation, and Technology Delivery. 
Transforming teams through Agile, AI, DevOps, Software and Quality-first engineering (TDD/ATDD), and enhancing productivity with AI is my passion. 
As a Software Engineering Professional, I focus on mentoring teams, use AI for improving productivity, technical coaching (Test Automation) now Agentic - AI,refining processes, and driving continuous improvement and engage with teams on a continuous basis, hands on as required. I thrive on building high-performing teams that deliver software with
I thrive on building high-performing teams that deliver software with speed, efficiency, and excellence. Let's connect and discuss how engineering can be a gamechanger!

Areas of strength: 
Test Architecture, Software Development, Agile Methodologies, Release Management, AI Enabled Quality Engineering, AWS Certified, Technical Support, Devops(CI/CD) and Leading Teams.

professional experience:

Title:Sr Software Engineer
Selective - May 2026 - Present
location: Hartford, Connecticut (CT)
Currently establishing standards for software quality Handling System teams for flag ship product in the commerical lines domain.
Using Agentic AI to create automated tests
Migrated Java based selenium testing to .Net - Playwright using Agentic AI automation - reduced migration effort by approximately more than 70%
Leading the Commercial Lines of Business Quality Engineering Team to support bi-weekly releases. 

Travelers
Title:Sr Software Engineer
December 2018 - March 2026 (7 years 5 months)
location: Hartford, Connecticut
Established standards for software quality and testing for flagship Strategic platform in BSI(Bond & Speciality Insurance) - Guidewire domain using Gauge and Taiko. Resulted in 0 license cost and scaled across 
the line of business for more than 70+ engineers.
Established Software Test Automation to run in CI/CD pipelines using containers (Docker). Resulted in quicker delivery from quarterly to monthly. Also, eliminated the need for using VMs.
Established Service Virtaulization using Mountebank.
Sunset tools ALM for defect tracking and established in-house defect Test execution report management system, saving licensing cost by more than 20K year on year.
Coached and taught engineers on Test Automation,Software Quality Engineering practices BDD/ATDD, and Agile practices
Introduced Software Test Automation strategy (Testing Pyramid) in the Data Engineering Space to improve quality.

Corporate System Associates
Title:QE - COE Lead - Consultant - Travelers
June 2018 - December 2018 (7 months)
Successfully demonstrated and created proof of concepts for Test Automation and Quality Engineering practices within the organization for establishing best practices and driving adoption across teams
Hartford, Connecticut

Company:IBM
Title:Build and Release Management Lead
June 2017 - June 2018 (1 year 1 month)
location: Remote United States
Worked as a Build and Release Management Lead for a flagship IBM product IDRM,ensuring smooth and efficient software release processes.
Collaborated with development and QA teams to streamline build and release management process. 

Company:Gilbarco Veeder Root / Gilbarco
Title: Software Quality Engineering Specialist / Sr. Test Lead
June 2014 - June 2017 (3 years 1 month)
location:Simsbury, Connecticut 
Worked as a Software Test Lead/Sr Software Quality engineer 
using Software Engineering techniques, principles and established Test Automation across
the organization for a flag ship web application of Veeder Root - FuelQuest
Organization. Ensured good Test practices are adhered by various teams to create high quality and robust products. Brought time regression testing time from 1 week to 2 hours

Yale University Careers
Title: Sr. Test lead / Sr. Software Engineer - Contract
March 2013 - June 2014 (1 year 4 months)
New Haven, Connecticut
Worked as a Test lead and developed a Web application Testing Framework
using Software engineering principles , design and techniques to automate
testing for ServiceNow application implementation. Have trained and mentored
manual testers to perform effective testing and trained testers in Automation.  
Eliminated manual testing and reduced regression testing time from 1 week to 1 day and introduced exploratory testing to improve quality of the product.


GENCO, A FedEx Company
Title: Sr Test Lead - Consultant
October 2009 - June 2011 (1 year 9 months)
Greater Milwaukee Area
Worked as  Consultant - Test Lead and developed a Windows based Test
Automation framework using .Net Technologies - C# for their Supply Chain 
logistics application. The Test Automation Framework was able to cut down
Testing time by about 50% . Mentored software testers on approaching Automation and teaching them various Testing techniques. 

SumTotal Systems
Title: Sr. Tech Support Engineer
March 2007 - August 2009 (2 years 6 months)
Bellevue, Washington
Worked as Sr Tech Support Engineer providing technical assistance and support for SumTotal Systems products which are widely used in the training and learning space across various organizations.
Responsibilities included troubleshooting technical issues, providing solutions, and ensuring customer satisfaction. 
Collaborated with development and sustained engineering teams to resolve product defects and improve overall product quality.

    
SumTotal Systems
Title: Build & Release Manager
January 2006 - January 2007 (1 year 1 month)
Hyderabad, India
Worked as Build & Release Manager responsible for managing the build and release processes for SumTotal Systems products. Coordinated with development, QA, and operations teams to ensure smooth and timely releases. 
Implemented and maintained build automation tools and processes to improve efficiency and reduce errors. 

Title: Sr. Tech Support Lead
May 2004 - January 2006 (1 year 9 months)
Hyderabad, India
Worked as Sr. Tech Support Lead providing technical assistance and support for SumTotal Systems products. 
Led a team of technical support engineers, providing guidance and mentorship to ensure high-quality support delivery. 
Responsibilities included managing support escalations, coordinating with development teams for issue resolution, and ensuring timely communication with customers

Cordys
Lead Development
August 2001 - March 2004 (2 years 8 months)
Worked as Lead Development responsible for leading the development team in designing, implementing, and maintaining software solutions. Coordinated with cross-functional teams to ensure successful project delivery
Responsibilities included overseeing the development lifecycle, ensuring code quality, and mentoring junior developers.

Additional Experience:
Dell – Contract Project Manager (March 2012- March 2013), Bridgewater Associates – Sr. Test Lead - Contract (July 2011 – Feb 2012),), Dev & Test Lead – Cordys’ R&D India, Volvo commercial finance, Inspire Tech & Satyam Computer Services Ltd."""


#------------------------------------------------------------------------------------
# System Message
#-----------------------------------------------------------------------------------------------------------------------
system_message = """

# ROLE

You are Hari M Adusumilli's Digital Twin.

Your purpose is to answer questions as if you are representing Hari's professional knowledge, experience, opinions, and communication style.

You are not pretending to be Hari in real life. Instead, you are a digital representation of Hari based on the information provided to you. 

# ABOUT HARI

Hari is a Quality Engineering Leader, Technical Coach, AI Evangelist, Strategist, and Engineering Transformation Leader.

Areas of expertise:

- Quality Engineering
- Test Automation
- Acceptance Test Driven Development (ATDD)
- Agile Delivery
- AI Adoption
- Engineering Leadership
- Technical Coaching
- GitHub Copilot
- Local AI Solutions
- RAG Systems
- AI Strategy

# PERSONALITY

- Helpful and approachable
- Practical and hands-on
- Focused on business outcomes
- Enjoys teaching and mentoring
- Prefers actionable advice over theory
- Explains concepts step-by-step
- Encourages experimentation and continuous learning

# COMMUNICATION STYLE

- Be concise but informative.
- Use clear, simple language.
- Prefer examples over abstract explanations.
- Break complex topics into steps.
- Avoid excessive jargon.


# WORKFLOW

When answering questions:

1. Determine whether the question is about Hari's background, skills, experience, projects, interests, or opinions.
2. Use available profile information as the primary source of truth.
3. If information is unavailable, clearly state that the information is not currently available. Request them to provide their contact details name, email or phone number.Let them know that you will send this information to Hari for contact purposes.
4. Never invent achievements, certifications, employers, projects, or personal details.
5. Provide responses consistent with Hari's known experience and expertise.

# CRITICAL RULES

1. Never fabricate information.
2. Never claim Hari worked somewhere unless provided in the source material.
3. Never invent certifications, degrees, or accomplishments.
4. If uncertain, state:
   I don't have enough information to answer that.
5. Distinguish between known facts and inferred opinions.
6. Remain professional and respectful at all times.

# EXAMPLE BEHAVIOR

Question:
What are Hari's strengths?

Answer:
Hari's strengths include quality engineering leadership, technical coaching, AI adoption strategy, test automation, and helping teams improve engineering practices.

Question:
What company does Hari currently work for?

Answer:
I don't have that information in my current knowledge base.

# OUTPUT STYLE

Answer naturally in first person when representing Hari's perspective.

Example:

"I've spent much of my career helping teams improve quality engineering practices, test automation, and software delivery."

Do not repeatedly announce that you are an AI or digital twin unless asked."""


#---------------------------------------------------------------------------------------------------------------------
# Main Response function
#------------------------------------------------------------------------------------------------------------------------------------
def respond_ai(message, history):
    #Logs for debugging
    print("\n====================\n")
    print(f"User message:\n{message}\n")
    
    #update the system message with the retrieved context
    system_message_enhanced = system_message + "\nContext:\n" + document_professional_summary
    print("\nContext this turn:\n",system_message_enhanced)

    # Build the full conversation: system message + past chat + the new user message
    messages = [{"role": "system", "content": system_message_enhanced}] + history + [{"role": "user", "content": message}]
    print("Messages sent to the model:", messages)  # Debugging line

    
    # Keep calling the model until it answers with plain text instead of asking for tools
    #while True:
    response = client.chat.completions.create(
        model="gpt-6-luna",
        messages=messages,
        #max_tokens=2000,
        temperature=1,
        reasoning_effort="none"
        #tools=tools  # the tools the model is allowed to request
    )

    # The model's reply (named assistant_message so we don't overwrite the user's `message`)
    assistant_message = response.choices[0].message
    print("Reply from the model:", assistant_message)  # Debugging line
             
    return assistant_message.content
#-------------------------------------------------------------------------------------------------------------------------------------------
# Launch Gradio interface
#----------------------------------------------------------------------------------------------------------------------------

#gr.ChatInterface(fn=respond_ai, title="Hari Adusumilli Twin").launch()
demo = gr.ChatInterface(
    fn=respond_ai,
    title="Hari Adusumilli Twin"
)

port = int(os.environ.get("PORT", 7860))

demo.launch(
    server_name="0.0.0.0",
    server_port=port
)

    