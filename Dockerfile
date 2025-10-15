FROM python:3.11.0  

RUN mkdir /task-manager


WORKDIR /task-manager

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1 

RUN pip install --upgrade pip 

COPY requirements.txt  /task-manager/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /task-manager/

EXPOSE 8000

CMD ["gunicorn", "server.wsgi:application", "--bind", "0.0.0.0:8000"]