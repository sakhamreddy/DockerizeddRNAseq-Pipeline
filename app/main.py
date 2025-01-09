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
	
	fastq_files = []
	for file in files:
		if not file.filename.endswith(".fastq"):
		  return {"Error": f"{file.filename} is not a fastq file."}
	
	#save the uploaded files and store metadata in MongoDB
	  
	   	contents = await file.read()
		fastq_files.append({
			"filename": file.filename,
			"content": file.content_type
			"size": len(content),
		)}

	   with open(f"upload/{file.filename}", "wb") as f:

		f.write(contents)
	   
	return {"message": "File uploaded successfully"}

@app.post("/analyze")
async def run_rnaseq_analysis():





