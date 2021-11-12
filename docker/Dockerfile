FROM python:3.8-slim

RUN apt-get update && apt-get install -y ffmpeg
COPY ./docker/requirements.txt .
RUN pip install -r requirements.txt

COPY ./src /src
WORKDIR /src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port", "8000"]