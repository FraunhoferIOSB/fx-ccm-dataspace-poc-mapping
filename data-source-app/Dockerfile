FROM python:3

WORKDIR /assetapp

ENV FLASK_APP=app.py

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8500

CMD ["python", "app.py"]