from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os
from .firebase import add_user_to_firestore, get_all_users

app = FastAPI()

# Serve static files like app.js, index.html, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/", StaticFiles(directory=".", html=True), name="html")

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    file_location = f"./uploads/{file.filename}"
    os.makedirs(os.path.dirname(file_location), exist_ok=True)  # Ensure the upload directory exists

    # Save the uploaded file
    with open(file_location, "wb") as file_obj:
        file_obj.write(file.file.read())

    # Add user to Firebase Firestore (customize as needed)
    user_data = {
        "filename": file.filename,
        "upload_date": "2024-11-08"  # Example timestamp (adjust to your actual needs)
    }
    user_id = add_user_to_firestore(user_data)

    return JSONResponse(content={"message": "File uploaded successfully", "user_id": user_id})

@app.get("/users")
async def get_users():
    try:
        # Get all users from Firestore
        users = get_all_users()
        if users:  # If there are users, return them
            return {"users": users}
        else:
            return {"message": "No users found."}
    except Exception as e:
        return {"error": str(e)}  # Return the error message if there's an issue
