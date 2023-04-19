from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
class Sighting:
    DB = "sighting"
    def __init__(self, data):
        self.id = data["id"]
        self.location = data["location"]
        self.what = data["what"]
        self.date = data["date"]
        self.num_sas = data["num_sas"]
        self.user_id = data["user_id"]
        self.user = None
        

    @classmethod
    def create_sighting(cls, data):
        query = "INSERT INTO sighting (location,what,date,num_sas,user_id) VALUES (%(location)s, %(what)s, %(date)s, %(num_sas)s ,%(user_id)s)"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def update_sighting(cls, data):
        query = "UPDATE sighting SET location=%(location)s,what=%(what)s,date= %(date)s,num_sas=%(num_sas)s"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete_sighting(cls, sas_id):
        data = {
            "id": sas_id
        }
        query = "DELETE FROM sighting WHERE id=%(id)s"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_one(cls, sas_id):
        data = {
            "id": sas_id
        }
        query = "SELECT * FROM sighting WHERE id=%(id)s"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sighting"
        results = connectToMySQL(cls.DB).query_db(query)
        sighting = []
        for row in results:
            sighting.append(cls(row))

        return sighting
    
    @classmethod
    def get_one_with_user(cls, data):
        sql = """
            SELECT * FROM sighting
            JOIN user ON user.id = sighting.user_id
        """
        results = connectToMySQL(cls.DB).query_db(sql,data)
        sightings = []
        for row_in_db in results:
            sighting = cls(row_in_db)
            user_data = {
                "id": row_in_db["user.id"],
                "first_name": row_in_db["first_name"],
                "last_name": row_in_db["last_name"],
                "email": row_in_db["email"],
                "password": row_in_db["password"],
                
            }
            sighting.user=user.User(user_data)
            sightings.append(sighting)
        return sightings
    

    
    
    @staticmethod
    def validate_sighting(sighting):
        is_valid = True # we assume this is true
        
        if len(sighting["location"]) <= 0 or len(sighting["what"]) <= 0 or len(sighting["date"]) <= 0 or len(sighting["num_sas"])<= 0:
            is_valid = False
            flash("All fields required","sighting")
            return is_valid
        if int(sighting['num_sas']) < 0:
            flash("Number of Sasquatches must be at least 1 character","sighting")
            is_valid= False
        return is_valid