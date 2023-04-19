from flask_app.config.mysqlconnection import connectToMySQL
import re

from flask_app.models import artist
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash
class User:
    DB = "recipes"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data["password"]
        self.recipes = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, password) VALUES ( %(first_name)s, %(last_name)s,%(email)s, %(password)s)"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s"
        result = connectToMySQL(cls.DB).query_db(query, data)
        print("************** Start of printing ****************")
        print("Printing data:", data)
        print("Printing result:", result)
        print("************** End of printing ****************")
        return cls(result[0])
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email=%(email)s"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET email=%(email)s WHERE id=%(id)s"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    
    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.DB).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        # if len(user["first_name"]) <= 0 or len(user["last_name"]) <= 0 or len(user["email"]) or len(user["password"]) <= 0:
        #     is_valid = False
        #     flash("All fields required")
        #     return is_valid
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters","register")
            is_valid= False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters","register")
            is_valid= False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid= False
        if user['password'] != user['confirm']:
            flash("Passwords don't match","register")
            
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid
    