# app/database.py
import firebase_admin
from firebase_admin import credentials, firestore

# Path to your downloaded Firebase service account key
cred = credentials.Certificate('D:\\Pdf Project\\app\\serviceAccountKey.json')


# Initialize Firebase Admin SDK with the credentials
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# Function to get Firestore client
def get_db():
    return db
