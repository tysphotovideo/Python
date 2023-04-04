from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Cookies:
    def __init__( self , data ):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.num_boxes = data['num_boxes']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookies;"
        results = connectToMySQL('Cookies').query_db(query)
        cookies = []
        for cookie in results:
            cookies.append( cls(cookie) )
        return cookies
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO cookies (customer_name,cookie_type,num_boxes) VALUES(%(customer_name)s, %(cookie_type)s, %(num_boxes)s);"
        result = connectToMySQL('Cookies').query_db(query,data)
        return result
    
    @classmethod
    def update(cls,data):
        query = "UPDATE cookies SET customer_name= %(customer_name)s,cookie_type= %(cookie_type)s,num_boxes=%(num_boxes)s WHERE id=%(id)s;"
        return connectToMySQL('Cookies').query_db(query,data)
        
    @classmethod
    def getOne(cls,data):
        query = "SELECT * FROM cookies WHERE id = %(id)s;"
        result = connectToMySQL('Cookies').query_db(query,data)
        
        return cls(result[0])

    @staticmethod
    def validate_cookie(cookies):
        is_valid = True # we assume this is true
        if len(cookies["customer_name"]) <= 0 or len(cookies["cookie_type"]) <= 0 or len(cookies["num_boxes"]) <= 0:
            is_valid = False
            flash("All fields required")
            return is_valid
        if len(cookies['customer_name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(cookies['cookie_type']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if int(cookies['num_boxes']) <= 0:
            flash("Number of boxes must be 1 or greater.")
            is_valid = False
        
        return is_valid        
