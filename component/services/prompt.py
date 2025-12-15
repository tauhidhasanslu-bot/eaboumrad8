

from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


def prompt_generate(user_prompt, user_role):
    systemMessage = SystemMessage(
            content="You are a helpful assistant specialized in / as a" #setting role to a dymanic setting
        )
    humanMessage = SystemMessage(
        content=f"{user_prompt}"
        )
    temp = PromptTemplate(
        template="{system_message}  {user_role}. Provide accurate and concise information related to the user Query: {human_message} based on the role.",
        input_variables=['system_message', 'human_message', 'user_role'] 
        )
    prompt = temp.invoke(input={'system_message': systemMessage.content, 
                                'human_message': humanMessage.content,
                                'user_role': user_role})
    
    return prompt
