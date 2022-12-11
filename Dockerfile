#Pull the python:3.8 container from the hub
FROM python:3.10

#Make below changes to the above continer

#Copy the below files to current directry of the pulled container
ADD web3helpers.py .
ADD webserver.py .
ADD .env .

#Install python external packages 
RUN pip install web3
RUN pip install python-decouple

#Expose the port
EXPOSE 8080

#Execute below commands while running the container
CMD ["python3", "webserver.py"]