FROM python:3.11.4

WORKDIR /root/NobyRobot

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3","-m","NobyRobot"]
