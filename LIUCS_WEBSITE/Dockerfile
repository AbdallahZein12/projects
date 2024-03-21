FROM caddy:latest

WORKDIR /app

COPY Caddyfile /etc/caddy/Caddyfile

EXPOSE 80

RUN apk --no-cache add python3 py3-pip && \
    pip3 install --upgrade pip setuptools && \
    apk add --no-cache bash curl

COPY liucsflask/requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY liucsflask /app

RUN pip3 install --no-cache-dir Flask gunicorn

EXPOSE 8000

CMD ["bash", "-c", "gunicorn -b 0.0.0.0:8000 main:app & caddy run --config /etc/caddy/Caddyfile"]

