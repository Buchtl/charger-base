FROM python:3.11-slim

ENV LOG_DIR=/var/log/charger_base
RUN mkdir -p $LOG_DIR &&\
  chmod 777 $LOG_DIR &&\
  mkdir -p /app &&\
  chmod 777 /app

COPY ./src/ /app/src/
COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

# Set non-root user
USER nobody

ENV PYTHONUNBUFFERED=1 \
    DB_URL="pi4b:5432" \
    DB_USER="charger" \
    DB_PASSWORD="charger" \
    DB_NAME="charger" \
    POLLING_PERIOD="1"

CMD ["sh", "-c", "python3 -m src.charger_base --dburl \"$DB_URL\" --dbuser \"$DB_USER\" --dbpass \"$DB_PASSWORD\" --dbname \"$DB_NAME\" --ptime \"$POLLING_PERIOD\""]
