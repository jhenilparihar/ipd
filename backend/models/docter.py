from mongo_engine import db
from pymongo.errors import DuplicateKeyError
from mongoengine import NotUniqueError

class Docter(db.Document):
    # username = db.StringField(required=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    age = db.IntField(required=True)
    gender = db.StringField(required=True)
    registration_number = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)

    meta = {'collection': 'docters'}

    @classmethod
    def add_docter(cls, args):
        try:
            user = cls(**args)
            user.save()
            return {"error": False, "data": user}
        
        except (DuplicateKeyError, NotUniqueError):
            return {"error": True, "message": "User with same mobile already exists"}
        
        except:
            return {"error": True, "message": "Error adding user"}

    @classmethod
    def get_docter_by_registration_number(cls, registration_number):
        try:
            docter = cls.objects.get(registration_number=registration_number)
            return {"error": False, "data": docter}
        
        except cls.DoesNotExist:
            return {"error": True, "message": "User does not exist"}
        
        except:
            return {"error": True, "message": "Error getting user"}