FROM node:lts-alpine

WORKDIR /app

COPY . .

EXPOSE 3000    

COPY ./entrypoint.sh .
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["sh", "/app/entrypoint.sh"]
