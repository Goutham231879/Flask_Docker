#base image

From python:3.9
#working directory

WORKDIR /app

#copying 

COPY . /app



#install the requirements

Run pip install -r requirements.txt
#expose the port

EXPOSE 5000
#command to run the app
CMD [ "python" , "./app.py" ]