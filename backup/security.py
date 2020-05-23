from user import User
users = [User(1,'obo','asdd')]

username_mapping = {u.username:u for u in users}

userid_mabing = {u.id:u for u in users}

def authenticate(username,password):
    user = username_mapping.get(username,None)
    if user and user.password == password:
        return user

def idenitiy(payload):
    print(payload)
    user_id = payload['identity']
    return userid_mabing.get(user_id,None)