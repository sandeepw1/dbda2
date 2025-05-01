FROM python3.12-alpine3.21
RUN pip3 install flask
RUN mkdir /app
COPY index.py /app/
CMD ["python3", "/app/index.py"]
