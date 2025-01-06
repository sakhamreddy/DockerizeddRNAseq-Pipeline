#!/usr/bin/env python

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import  MongoClient
from typing import list

app = FastAPI()

@app.get("/")
async def related():
	return {"message": "hello world"}


