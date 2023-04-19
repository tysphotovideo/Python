from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
class Artist:
    DB = "recipes"
    def __init__(self, data):
        self.id = data["id"]
        self.users_id = data["users_id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.under = data["under"]
        self.user = None
        

    @classmethod
    def create_artist(cls, data):
        query = "INSERT INTO recipe (name,description,instructions,date_made,under,users_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under)s,%(users_id)s)"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def update_artist(cls, data):
        query = "UPDATE recipe SET name=%(name)s,description=%(description)s,instructions= %(instructions)s,date_made=%(date_made)s,under=%(under)s, users_id=%(users_id)s"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete_artist(cls, artist_id):
        data = {
            "id": artist_id
        }
        query = "DELETE FROM recipe WHERE id=%(id)s"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_one(cls, artist_id):
        data = {
            "id": artist_id
        }
        query = "SELECT * FROM recipe WHERE id=%(id)s"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipe"
        results = connectToMySQL(cls.DB).query_db(query)
        artists = []
        for row in results:
            artists.append(cls(row))

        return artists
    
    @classmethod
    def get_one_with_user(cls, data):
        sql = """
            SELECT * FROM recipe
            JOIN users ON users.id = recipe.users_id
        """
        results = connectToMySQL(cls.DB).query_db(sql,data)
        recipes = []
        for row_in_db in results:
            recipe = cls(row_in_db)
            user_data = {
                "id": row_in_db["users.id"],
                "first_name": row_in_db["first_name"],
                "last_name": row_in_db["last_name"],
                "email": row_in_db["email"],
                "password": row_in_db["password"],
                
            }
            recipe.user=user.User(user_data)
            recipes.append(recipe)
        return recipes
    

    
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True # we assume this is true
        
        if len(recipe["name"]) <= 0 or len(recipe["description"]) <= 0 or len(recipe["instructions"]) <= 0 or len(recipe["date_made"])<= 0:
            is_valid = False
            flash("All fields required","recipe")
            return is_valid
        if len(recipe['name']) < 3:
            flash("Name must be at least 3 characters","recipe")
            is_valid= False
        if len(recipe['description']) < 3:
            flash("Description must be at least 3 characters","recipe")
            is_valid= False
        if len(recipe['instructions']) < 3:
            flash("Description must be at least 3 characters","recipe")
            is_valid= False
        return is_valid