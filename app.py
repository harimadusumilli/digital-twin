import os
from openai import OpenAI
import requests
import random
import re
import uuid
import chromadb
import json
import gradio as gr
from pprint import pprint


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

document_education_skills = """
Sir M.V.I.T
Bachelor of Engineering - BE, Electrical, Electronics and Communications Engineering
College: Sir.M.V.I.T
AWS Certified Cloud Practitioner
IBM Enterprise Design Thinking Practitioner

Technical Skills:
AI & Automation: Agentic AI, Generative AI, GitHub Copilot, TravAI, Playwright, pytest, Selenium, Gauge, Taiko, WATIR, Tool calling (AI - Python)D,CI/CD, Agile, Scrum, AWS, Databricks, Guidewire, ServiceNow, Informatica, 
Java, Python, .Net, React, Angular, SQL, SQL Server, MongoDB, Dynatrace, JMeter, Mountebank-Service Virtualization
"""

document_addl_hobbies_info = """
Additional Info:
-I love cooking specially for friends and family. I enjoy experimenting with different cuisines and flavors. My favorite dishes to cook are Butter Chicken,
Indian Chinese, Fish Fry and Pasta. I like cooking and sharing my culinary creations with others. I also enjoy trying out new recipes and exploring different cooking techniques. 
I learn about recipes from Youtube or from my friends and family.
- I played Tennis till I was in college. 
- I also love a little reading in my free time, reading any interesting books or articles that catch my attention.


-I enjoy playing the guitar and listening to a wide range of music genres. My favorite genres include rock, blues, and classical music. I often play guitar for relaxation 
and entertainment. I also enjoy attending live music concerts and discovering new artists. Music is a big part of my hobby and I find it to be a great way to express myself 
creatively. I also like to learn new songs and techniques on the guitar, and I like to record a tune or create my own arraangements of popular songs
"""
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



#--------------------------------------------------------------------------------
# Chunking function
#--------------------------------------------------------------------------------------------------
# ".", "!" or "?" (optionally followed by closing quotes/brackets) that is followed by whitespace;
# the lookahead (?=\s) avoids matching things like "3.14"
SENTENCE_END = re.compile(r"[.!?][\"')\]]*(?=\s)")


def _last_sentence_end(window: str) -> int:
    """Return the index just after the last sentence end in window, or -1 if none."""
    matches = list(SENTENCE_END.finditer(window))
    return matches[-1].end() if matches else -1


def _find_cut(window: str, half: int) -> int:
    """Return the best cut index inside window, or -1 to keep the hard cut.

    Boundaries are tried in priority order: paragraph break, newline, sentence end, space.
    A boundary is accepted only if it lies past `half`.
    """
    for sep in ("\n\n", "\n"):
        i = window.rfind(sep)  # rfind returns the LAST occurrence, or -1
        if i != -1 and i + len(sep) > half:
            return i + len(sep)  # cut just after the separator

    pos = _last_sentence_end(window)
    if pos > half:
        return pos

    i = window.rfind(" ")
    if i != -1 and i + 1 > half:
        return i + 1
    return -1


def chunk_document(text: str, chunk_size: int = 300, overlap: int = 30) -> list[str]:
    """Split text into overlapping chunks of up to chunk_size characters.

    Each chunk overlaps the previous one by `overlap` characters. If a chunk would
    end mid-sentence, the cut moves back to the nearest natural boundary, tried in
    this order: paragraph break, newline, sentence end, space. A boundary is used
    only if it lies past the halfway point of the chunk.

    Args:
        text: the full document to split.
        chunk_size: maximum number of characters per chunk.
        overlap: number of characters shared between consecutive chunks.

    Returns:
        A list of chunk strings.
    """
    # Overlap must be smaller than chunk_size, otherwise the window never moves forward
    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("chunk_size must be positive and overlap must be between 0 and chunk_size - 1")

    chunks = []                # accumulates the finished chunks
    start = 0                  # index in `text` where the current chunk begins
    half = chunk_size // 2     # a boundary must be located after this position to be used
    while start < len(text):   # keep going until the whole text is covered
        # Default cut: chunk_size characters ahead, or the end of the text if it comes sooner
        end = min(start + chunk_size, len(text))

        if end < len(text):  # only adjust when the chunk is cut mid-text (not the last chunk)
            window = text[start:end]  # the candidate chunk we may shorten
            cut = _find_cut(window, half)  # -1 means no suitable boundary; keep the hard cut
            if cut != -1:
                end = start + cut  # convert window-relative index to a text-wide index

        chunks.append(text[start:end])  # save the chunk (end is exclusive)

        if end >= len(text):  # reached the end of the document, so stop;
            break             # otherwise we'd emit a chunk made only of overlap

        # Next chunk starts `overlap` characters before this one ended, creating the overlap.
        # max(..., start + 1) only matters when a chunk is shorter than the overlap; it guarantees
        # forward progress so the loop can never get stuck.
        start = max(end - overlap, start + 1)
    return chunks  # list of all chunks, in document order


#---------------------------------------------------------------------------------------------------------------------
# RAG: Chunk, Embed & Store in ChromaDB
#----------------------------------------------------------------------------------------------
documents = [
    {"text": document_professional_summary, "source": "Professional Summary"},
    {"text": document_education_skills, "source": "Education and Skills"},
    {"text": document_addl_hobbies_info, "source": "Additional Hobbies Information"}
]

chunks = []
ids = []
metadatas = []

for doc in documents:
    # Prepare the lists
    chunks_ = chunk_document(doc["text"])
    ids_ = [str(uuid.uuid4()) for _ in range(len(chunks_))]
    metadatas_ = [{"source": doc["source"], "chunk_index": i} for i in range(len(chunks_))]
    #.... Add to main lists
    chunks.extend(chunks_)
    ids.extend(ids_)
    metadatas.extend(metadatas_)

# Quick test: show the first 50 characters of the first two chunks
for i, chunk in enumerate(chunks):
    #print(f"----chunk {i + 1} (text): {len(chunk)} chars----")
    print(f"Chunk {i + 1} (ID: {ids[i]}, Source: {metadatas[i]['source']}, Chunk Index: {metadatas[i]['chunk_index']},Length: {len(chunk)}):")
    print(chunk)
    print()  # add a blank line for readability between chunks

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=chunks
)
embeddings = [item.embedding for item in response.data]
from pprint import pprint
#pprint(response.data)

# Now `embeddings` contains the vector representation for each chunk of text
print(f"Created {len(embeddings)} embeddings")
#print(f"Embedding dimensions: {len(embeddings[1]) if embeddings else 0}")

# initialize ChromaDb Client for persistent storage
chroma_client = chromadb.PersistentClient(path="./chroma_db_twin_hari")

# initialize chroma db for in-memory storage
#chroma_client = chroma_db.Client()

collection = chroma_client.get_or_create_collection(name="Hari_Profile_digital_twin")

if collection.get()["ids"]:
    collection.delete(collection.get()["ids"])

#pprint(collection.get())

#Adding data to chroma Db
collection.add(
    ids=ids,
    embeddings=embeddings,
    metadatas=metadatas,
    documents=chunks
)

#pprint(collection.get())

# Get Embeddings for the chunks
#pprint(collection.get(include=["documents","metadatas","embeddings"]))

#---------------------------------------------------------------------------------------------------------------------
# Main Response function
#------------------------------------------------------------------------------------------------------------------------------------
def respond_ai(message, history):
    #Logs for debugging
    print("\n====================\n")
    print(f"User message:\n{message}\n")
    
# RAG
    #Generate embedding for a test query

    #Embed the query using the same model we used for the chunks to ensure compatibility
    #Tip: you will need to convery the query into a list
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=[message]
    )
    query_embedding = response.data[0].embedding

    #Search ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
        
    )

    #Stitch the retrieved chunks to create the context for the response
    context = "\n---\n".join(results['documents'][0])
    print(f"User message:\n{message}\n")
    print(f"Context retrieved this turn:\n{context}\n")
    
    #update the system message with the retrieved context
    system_message_enhanced = system_message + "\nContext:\n" + context


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
        tools=tools  # the tools the model is allowed to request
    )

    # The model's reply (named assistant_message so we don't overwrite the user's `message`)
    assistant_message = response.choices[0].message
    print("Reply from the model:", assistant_message)  # Debugging line
    print("Tool calls:", assistant_message.tool_calls)  # None if the model asked for no tools
    
        # No tools requested: the model's text is the final answer, so return it to Gradio
        # if not assistant_message.tool_calls:
        #     return assistant_message.content
    while assistant_message.tool_calls:  # Keep handling tool calls until there are none left
        from pprint import pprint
        pprint(assistant_message.tool_calls)
    # Tools requested: first record the model's request in the conversation
    # (the API requires this to come BEFORE the tool results)
        messages.append(assistant_message)

    # Run every requested tool; handle_tool_call returns a LIST of results, so we use extend
    # (extend adds each item of the list; append would add the whole list as one item)
        messages.extend(handle_tool_call(assistant_message.tool_calls))

        # Call the model again with the updated conversation
        response = client.chat.completions.create(
            model="gpt-6-luna",
            messages=messages,
            #max_tokens=2000,
            temperature=1,
            reasoning_effort="none",
            tools=tools
        )
        assistant_message = response.choices[0].message
        print("Reply from the model:", assistant_message)  # Debugging line
        print("Tool calls:", assistant_message.tool_calls)  # None if the model asked for no tools
             
    return assistant_message.content


#-----------------------------------------------------------------------------------------------
# Tool Call
#-------------------------------------------------------------------------------------------------------------------------
if os.getenv("PUSHOVER_TOKEN") is None:
    raise Exception("PUSHOVER_TOKEN environment variable is not set.")
else:
    PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN")

if os.getenv("PUSHOVER_USER") is None:
    raise Exception("PUSHOVER_USER environment variable is not set.")
else:
    PUSHOVER_USER = os.getenv("PUSHOVER_USER")

pushover_url = "https://api.pushover.net/1/messages.json"

tools = [] #Getting ready by making tio blank so that we can append later the tool definitions

# Function to send a message via Pushover
def send_pushover_message(message: str):
    payload = {
        "token": PUSHOVER_TOKEN,
        "user": PUSHOVER_USER,
        "message": message
    }
    response = requests.post(pushover_url, data=payload)
    if response.status_code != 200:
        raise Exception(f"Failed to send Pushover message: {response.text}")
    return response.json()

# Definition of the Pushover message sending function for tool-calling
send_pushover_message_function = {
    "name": "send_pushover_message",
    "description": "Sends a message via Pushover to Hari's Phone, use this to alert me about important events, completed tasks or time sensitive information",
    "parameters": {
        "type": "object",
        "properties": {
            "message": {"type": "string", "description": "The message to send via Pushover to the user's device"
            }
        },
        "required": ["message"]
    }
}

tools.append({"type":"function", "function":send_pushover_message_function})
#Simulate rolling a single six-sided die This is the second tool
def roll_dice():
    return random.randint(1, 6)

#Describe the function of rolling a die for the LLM, including its name, description, and parameters
roll_dice_function = {
    "name": "roll_dice",
    "description": "Simulate rolling a single six-sided die, use this when the user wants to roll a die",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

#Now add this tool to the list of available tools for the LLMt
tools.append({"type":"function", "function":roll_dice_function})

#--------------------------------------------------------------------------------------------------------
# Tool Handler
#--------------------------------------------------------------------------------------------------------------
# Runs every tool the model asked for and returns a list of result messages
def handle_tool_call(tool_calls):
    #import json  # needed to convert the JSON text arguments into a Python dict
    tool_results = []  # collects one result per tool call
    for tool_call in tool_calls:  # the model may request several tools at once
        function_name = tool_call.function.name
        # arguments arrive as JSON text, e.g. '{"message": "Hi"}' -> {"message": "Hi"}
        args = json.loads(tool_call.function.arguments)

        if function_name == "send_pushover_message":
        # Now send the notification using the parsed arguments
            send_pushover_message(args["message"])  # This is the actual function call
            content = f"Notification sent with message: {args['message']}"
            print("Notification sent with message:", args["message"])
        elif function_name == "roll_dice":
            content = f"Rolled a die and got: {roll_dice()}"
        else:
            content = f"Unknown tool: {function_name}"
    # The reply for the model; tool_call_id tells it which request this answers
        tool_call_result = {
            "role": "tool",
            #"content": f"Notification sent with message: {args['message']}",
            "content": content,
            "tool_call_id": tool_call.id
        }
        tool_results.append(tool_call_result)  # append adds ONE item to the list

    return tool_results


#-------------------------------------------------------------------------------------------------------------------------------------------
# Launch Gradio interface
#----------------------------------------------------------------------------------------------------------------------------

#gr.ChatInterface(fn=respond_ai, title="Hari Adusumilli Twin").launch()
custom_css = """
body, .gradio-container {
    background: #000 !important;
    color: #9acbff;
}

.gradio-container .prose, .gradio-container h1 {
    color: #9acbff;
}

.gradio-container .user {
    background-color: #e8c547 !important;
    color: #4b1673;
}

.gradio-container .user .prose,
.gradio-container .user .prose * {
    color: #4b1673 !important;
}

.gradio-container textarea {
    background: #000 !important;
    color: #9acbff !important;
    border: 2px solid #e8c547 !important;
}

.gradio-container textarea::placeholder {
    color: #82a8ca;
}
"""

theme_colors = {
    "body_background_fill": "#000000",
    "background_fill_primary": "#000000",
    "background_fill_secondary": "#111111",
    "block_background_fill": "#111111",
    "panel_background_fill": "#000000",
    "input_background_fill": "#000000",
    "body_text_color": "#9acbff",
    "block_label_text_color": "#9acbff",
    "button_primary_background_fill": "#e8c547",
    "button_primary_background_fill_hover": "#f4d875",
    "button_primary_text_color": "#102a56",
    "button_secondary_background_fill": "#e8c547",
    "button_secondary_background_fill_hover": "#f4d875",
    "button_secondary_text_color": "#102a56",
    "button_cancel_background_fill": "#e8c547",
    "button_cancel_background_fill_hover": "#f4d875",
    "button_cancel_text_color": "#102a56",
}
dark_theme = gr.themes.Monochrome().set(
    **theme_colors,
    **{f"{name}_dark": color for name, color in theme_colors.items()},
)

with gr.Blocks(title="Hari Adusumilli Twin") as demo:
    gr.ChatInterface(fn=respond_ai, chatbot=gr.Chatbot(label="Hari Adusumilli Digital Twin", show_label=True), api_visibility="private")


##demo.launch(inbrowser=True, theme=dark_theme, share=True, css=custom_css, footer_links=["gradio", "settings", "runs"])

demo = gr.ChatInterface(
    fn=respond_ai,
     chatbot=gr.Chatbot(label="Digital Twin - Chatbot", show_label=True), api_visibility="private",
    title="Hari Adusumilli - Digital Twin"
)

port = int(os.environ.get("PORT", 7860))

demo.launch(
    server_name="0.0.0.0",
    server_port=port
)

    