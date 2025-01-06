from python3.9

## Install R and update the necessary packages

RUN apt-get update && apt-get install -y r-base

##Install python dependencies

COPY requirements.txt
RUN pip install -r requirements.txt

#COPY application files
COPY  ..

#Run the FASTAPI application

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

