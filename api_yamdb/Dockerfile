FROM python:3.7-slim

WORKDIR /app

COPY . .

RUN pip3 install -r /app/requirements.txt --no-cache-dir

RUN python3 /app/manage.py collectstatic --noinput

CMD ["python3", "manage.py", "runserver", "0:8000"] 