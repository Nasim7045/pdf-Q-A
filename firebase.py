import firebase_admin
from firebase_admin import credentials, firestore

# Path to your Firebase service account key file
cred = credentials.Certificate("D:/Pdf Project/uploads/serviceAccountKey.json")  # Ensure path is correct
firebase_admin.initialize_app(cred)

db = firestore.client()

# Function to add user data to Firestore
def add_user_to_firestore(user_data):
    try:
        # Add the user data to Firestore
        users_ref = db.collection('users')
        doc_ref = users_ref.add(user_data)  # Automatically generates a unique document ID
        return doc_ref.id  # Return the document ID (user_id)
    except Exception as e:
        return str(e)  # Return the error message if there's an issue

# Function to get all users from Firestore
def get_all_users():
    try:
        # Get all users from the 'users' collection
        users_ref = db.collection('users')
        docs = users_ref.stream()
        users = [{"id": doc.id, **doc.to_dict()} for doc in docs]
        return users
    except Exception as e:
        return {"error": str(e)}  # Return an error message if there's an issue
