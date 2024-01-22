FROM python:3.11.5

ADD Referance.py .

RUN pip install beautifulsoup4 requests

CMD ["python", "./Referance.py"]