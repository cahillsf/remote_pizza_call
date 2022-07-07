FROM python:3.9-alpine
RUN mkdir /app
WORKDIR /app
ADD ./ /app
RUN pip3 install -r requirements.txt
CMD ["python3", "server.py"]