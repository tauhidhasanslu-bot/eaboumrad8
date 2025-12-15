from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import JSONResponse
from component.model.crud_repo import insert
from component.core.hug_model import model
from component.core.gemini_model import model, ImageModel
from component.services.prompt import prompt_generate
from component.services.generate_image import GenerateImage
from component.model.chat_history import GetAllChat

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/query")
async def query(user_prompt:str = Form(...),
                user_role:str = Form(...),
                chat_id:int = Form(...)):
    try:
        prompt = prompt_generate(user_prompt=user_prompt, user_role=user_role)
        print(prompt)

        ur_data = {
            'text': user_prompt,
            'chat_id' : chat_id
        }
        ur_id = insert(ur_data, cl_name='user_collection')
        #hug_model = model()
        #response = hug_model.invoke(prompt)
        gen_model = model()
        response = gen_model.invoke(prompt)
        res_text = response.content
        ai_data = {
            'text': res_text,
            'chat_id' : chat_id,
            'ur_id': ur_id
        }
        ai_id = insert(ai_data, cl_name='ai_collection')
        data = {
            'text': res_text,
            'ur_id': ur_id,
            'ai_id': ai_id
        }
        message = JSONResponse(
             status_code=200,
             content={
             'status': True,
             'statuscode': 200,
             'data': data
             }
        )
        print(message)
        return message
    except Exception as ex:
        message = JSONResponse(
             status_code=200,
             content={
             'status': True,
             'statuscode': 200,
             'text': str(ex)
             }
        )
        print(message)
        return message


@app.post("/api/chat/")
async def get_chat_history(chat_id: int = Form(...)):
        
        try:
            chats = GetAllChat(chat_id=chat_id)
            response = JSONResponse(
                 status_code=200,
                 content={
                 'status': True,
                 'statuscode': 200,
                 'text': chats
                }
            )
            return response
        
        except Exception as e:

            response = JSONResponse(
                 status_code=500,
                 content={
                'status': False,
                'statuscode': 500,
                'text': str(e)
                }
            )

            return response



"""

@app.post("/api/image-generator/")
async def generate_image(prompt: str = Form(...)):
    try:
        client = ImageModel()
        image = GenerateImage(prompt, client)  # PIL Image

        buffer = BytesIO()
        image.save(buffer, format="PNG")
        image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        return JSONResponse(
            status_code=200,
            content={
                "status": True,
                "statuscode": 200,
                "image": image_base64
            }
        )

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

"""


@app.post('/api/image-generator/')
async def generat_image(prompt = Form()):
     try:
          client = ImageModel()
          image = GenerateImage(prompt, client)
          response = {
               'status': False,
               'statuscode': 500,
               'image': image
          }
          return response
     except Exception as ex:
          response = {
               'status': False,
               'statuscode': 500,
               'image': str(ex)
          }
          return response