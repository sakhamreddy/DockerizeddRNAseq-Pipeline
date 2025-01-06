#!/usr/bin/env python

from fastapi import FastAPI, uploadFile, File
from pydantic import BaseModel
from pymongo import  MongoClient
import subprocess


app = FastAPI()

#connect to MongoDB
client  = MongoClient("mongodb://localhost:27017/")

database = client["rnaseq_analysis"]

@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
	#save the uploaded files and store metadata in MongoDB
	for file in files:
	   contents = await file.read()
	   with openff"data/{file.filename}", "wb") as f:
		f.write(contents)
	   db.files.insert_one({filename": file.filename})
	return {"message": "File uploaded successfully"}

@app.post("/analyze")
async def run_rnaseq_analysis():





