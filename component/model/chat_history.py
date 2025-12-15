
from component.model.crud_repo import get_all

def GetAllChat(chat_id):
    user_text = get_all(cl_name='user_collection', chat_id=chat_id)
    ai_text = get_all( cl_name='ai_collection', chat_id=chat_id)
    history = {
        'user_message': user_text, 
        'ai_message': ai_text
    }
    return history