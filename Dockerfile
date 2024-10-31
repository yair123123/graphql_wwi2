FROM python:3.10-slim
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./app app
ENV PYTHONPATH=/
CMD ["python", "app/main.py"]