import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def answer_prompt_bard(query):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(query)
    return response.text

def create_prompt_from_description(input_text):
    prompt = "If the following text has less than 90 words than elaborate it till 90 words approximately, and if it has more than 90 words than compress it to approximately 90 words - '" + input_text + "'. No need of Hashtags. No need of URL link. Start with response(compressed or elaborated text) directly, no formalities. "
    return prompt