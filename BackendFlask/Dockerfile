FROM python:3

WORKDIR /serverapp

ENV FLASK_APP=server.py

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "server.py"]