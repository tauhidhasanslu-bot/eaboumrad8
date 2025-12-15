from dotenv import load_dotenv
from component.services.prompt import prompt_generate
from component.core.hug_model import model
from component.core.gemini_model import model

load_dotenv()
x=True
while x :
    user_role = input('Enter the system role: ')
    user_prompt = input('Ask your question: ')
    if user_role == 'x':
        x=False
    else: 
        print('else is working')
        prompt = prompt_generate(user_prompt=user_prompt, user_role=user_role)
        #print(prompt)
        #hug_model = model()
        gen_model = model()
            #response = hug_model.invoke(prompt)
        #print(gen_model)

        response = gen_model.invoke(prompt)
        print(response)

