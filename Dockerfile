FROM ubuntu

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get update -y
RUN apt-get install python3-pip -y 
RUN apt-get install mysql-server mysql-client -y 
RUN apt-get install gcc libmysqlclient-dev -y 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV FLASK_DEBUG="1"
EXPOSE 5000

COPY . .

ENTRYPOINT [ "python3", "-m", "flask", "run", "--debug", "--host=0.0.0.0"]