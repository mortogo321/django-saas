FROM python:3.12.3-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/server

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN chmod a+x /app/server/entrypoint.sh

ENTRYPOINT ["/app/server/entrypoint.sh"]
