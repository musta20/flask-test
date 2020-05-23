from werkzeug.security import safe_str_cmp
from models import UserModel



def authenticate(username,password):
    user = UserModel.find_user_by_username(username)
    if user and user.password == password:
        return user

def idenitiy(payload):
    user_id = payload['identity']
    return UserModel.find_user_by_id(user_id)