FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install flask
CMD ["python","app/app.py"]
