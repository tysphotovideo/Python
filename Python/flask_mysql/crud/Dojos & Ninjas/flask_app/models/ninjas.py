from flask_app.config.mysqlconnection import connectToMySQL
class Ninjas:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name,age,dojo_id) VALUES(%(first_name)s, %(last_name)s, %(age)s,%(dojo_id)s);"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result
    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name= %(first_name)s,last_name= %(last_name)s,email=%(age)s,updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        # data = {"id":'id'}
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    @classmethod
    def getOne(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])

            
