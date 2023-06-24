FROM python:3.9

RUN apt-get update \
    && apt-get install -y postgresql-client


WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
