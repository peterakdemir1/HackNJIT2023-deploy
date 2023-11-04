from pymongo.mongo_client import MongoClient
import certifi
from hacknjit2023_models.image import Image
from hacknjit2023_models.user import User
import hacknjit2023_db_constants as db_const
import streamlit as st

class DbConnection:

    CA = certifi.where()
    uri = f"mongodb+srv://host:{db_const.PASSWORD}@cluster0.hx0xfxy.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
    client = MongoClient(uri, tlsCAFile=CA)

    def __init__(self):
        # Send a ping to confirm a successful connection
        try:    
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def get_db(self):
        return self.client['hacknjit2023']
    

class UsersDao:
    
    def __init__(self, db_conn: DbConnection):
        self.DB_CONN = db_conn
        self.DB = self.DB_CONN.get_db()
        self.COLLECTION = self.DB['users']

    def insert_one(self, user: User):
        try:
            res = self.COLLECTION.insert_one(user.__dict__)
            if not res.inserted_id:
                raise Exception
            return user
        except Exception as e:
            print(e)
            return None

    def find_any(self, user: User=None):
        return [user for user in self.COLLECTION.find(user.__dict__ if user else {})]

class ImagesDao:

    def __init__(self, db_conn: DbConnection):
        self.DB_CONN = db_conn
        self.DB = self.DB_CONN.get_db()
        self.COLLECTION = self.DB['images']
    
    def insert_one(self, image: Image):
        try:
            res = self.COLLECTION.insert_one(image.__dict__)
            if not res.inserted_id:
                raise Exception
            return image
        except Exception as e:
            print(e)
            return None
    
    def find_any(self, image: Image=None):
        return [image for image in self.COLLECTION.find(image.__dict__ if image else {})]

@st.cache_resource
def cache_db_conn():
    return DbConnection()

DB_CONN = cache_db_conn()

@st.cache_resource
def cache_daos(_db_conn):
    return UsersDao(_db_conn), ImagesDao(_db_conn)

users_dao, images_dao = cache_daos(DB_CONN)