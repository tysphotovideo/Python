from flask_app.config.mysqlconnection import connectToMySQL
from .ninjas import Ninjas
class Dojos:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES(%(name)s);"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result
    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name= %(name)s,updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        # data = {"id":'id'}
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    
    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninjas(n) )
        return dojo

            
