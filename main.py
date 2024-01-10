from typing import Optional
from fastapi import FastAPI, Form, File, UploadFile
import os
app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    content = await file.read()
    with open(os.path.join("./", file.filename), "wb") as fp:
        fp.write(content)    
    return {"filename": file.filename}