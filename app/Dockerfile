FROM ubuntu

WORKDIR /usr/src/

COPY requirements.txt ./
RUN apt-get update -y
RUN apt-get install python3-pip -y 
RUN apt-get install mysql-server mysql-client -y 
RUN apt-get install gcc libmysqlclient-dev -y 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN  apt-get remove python-watchdog 

# COPY . .

ENTRYPOINT [ "python3", "-m", "flask", "run", "--debug", "--host=0.0.0.0", "--reload"]
# ENTRYPOINT [ "python3", "__init__.py"]