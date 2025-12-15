from langchain_google_genai import ChatGoogleGenerativeAI
from google import genai


def model(model_name='models/gemini-2.5-flash'):
    model = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=0.5, 
        top_p=0.8)  #model parameters adjusted 
    return model

def ImageModel():
    client = genai.Client()
    return client

    
