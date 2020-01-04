FROM python

WORKDIR /app
COPY build /app/build
COPY *.py /app

ENTRYPOINT ["python", "dedbeetz.py"]
