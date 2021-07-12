from db import database


def authenticate(email, password):
    '''This function authenticate user, it returns user object if user exist and false otherwise'''
    for user in database:
        if user['email'] == email and user['password'] == password:
            return user
    return False
