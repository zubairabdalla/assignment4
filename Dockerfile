FROM python:3.9
WORKDIR /app
COPY app.py .
COPY sample.bmp .
CMD ["python", "app.py", "sample.bmp"]