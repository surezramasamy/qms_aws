FROM python:3.9.15-buster
WORKDIR /app
COPY ./my_app ./
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r /app/requirements.txt --no-cache-dir

# CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
CMD ["gunicorn","drg.wsgi:application","--bind","0.0.0.0:8000"]

