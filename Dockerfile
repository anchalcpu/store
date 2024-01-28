FROM python:3.8

# set the working directory in the container
WORKDIR /store

# copy the dependencies file to the working directory
COPY requirements.txt .
#COPY a.txt .
# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY store/ .

VOLUME ["/storage"]

#ENTRYPOINT ["python", "./cli.py"]

# command to run on container start
ENTRYPOINT [ "python", "__main__.py" ]