import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.environ.get('emsi_client_id')
client_secret = os.environ.get('emsi_client_secret')
client_scope = os.environ.get('emsi_client_scope')

url = "https://auth.emsicloud.com/connect/token"

payload = f"client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials&scope={client_scope}"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)

access_token = response.json()['access_token']

url = "https://emsiservices.com/skills/versions/latest/extract"

querystring = {"language":"en"}

jd = """
Full job description
Are you passionate about pushing the boundaries of AI to deliver innovative solutions? At PLACE, we are at the forefront of transforming the real estate lifecycle using AI-driven technologies.


Location: Edmonton, Alberta. We welcome remote candidates from Alberta/BC with the ability to occasionally visit our office.


About PLACE: PLACE is a pioneering end-to-end technology and business services platform aimed at revolutionizing the real estate lifecycle. If you're eager to harness the power of AI to redefine the real estate landscape, we might just be your next destination. Our partners, top-tier real estate teams, trust us with a spectrum of services from bookkeeping and talent acquisition to design and legal. Consumers prefer PLACE-backed teams for the unmatched real estate experience we help deliver.


What You'll Do:

Architect and Innovate: Develop high-end natural language understanding applications using Python and JavaScript, ensuring flawless integration with our legacy systems.
Be at the AI Forefront: Lead the development of applications for AI giants like GPT-3/GPT-4. Transition these from proof-of-concept stages to production, ensuring robustness and reliability.
ML Mastery: Design, develop, and optimize machine learning models for applications ranging from text classification to recommendation systems.
Collaborative Leadership: Offer technical guidance in Agile Sprints, working closely with cross-functional teams. Your insights will be pivotal in driving innovation and ensuring timely project completion.
Code Excellence: Champion high-quality coding practices, conducting in-depth code reviews to spot bugs, improve performance, and nurture best practices.

What We're Looking For:

Tech Pro: Proven expertise in Python and JavaScript, having worked on intricate AI projects.
AI Guru: Deep experience in natural language applications, especially around Information Retrieval and Generative AI Systems.
Framework Fanatic: Hands-on skills with frameworks like TensorFlow, PyTorch, and XGBoost,Langchain
Cloud Champion: Proficient in AWS services, especially Lambda, EFS, Vector Databases, and DynamoDB.
AI Enthusiast: Acquaintance with advanced ML models such as GPT-3/4, T5, and BERT.
Integration Expert: A proven track record of integrating third-party APIs into AI systems.
Team Player: Stellar communication skills, adept at collaborating with various teams and breaking down tech jargon.
Agile Ace: Proven leadership in Agile environments, steering teams towards success.

Why Join PLACE?

Innovative Environment: Shape the future of AI-powered solutions in a market ripe for disruption.
Continuous Learning: Stay ahead with opportunities for skill enhancement and professional growth.
Our Team & Culture: Become a part of a visionary team of engineers, data scientists, and product champions. Enjoy a culture that celebrates innovation, collaboration, and diversity.

Benefits:

Medical, Dental, and Vision Coverage
Company Stock Purchase Program
Professional Development Opportunities
Flexible Working Hours
Work-Life Balance Initiatives
Regular Team Events and Bonding Sessions"""

payload = "{ \"text\": \"... Senior project manager responsible for operational excellence of fleet ...\", \"confidenceThreshold\": 0.6 }"

headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

r = response.json()

data = r['data']
      
for elem in data:
    print(elem['skill']['name'])