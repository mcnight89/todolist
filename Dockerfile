FROM python:3.10.7-slim

WORKDIR /opt

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["bash", "entrypoint.sh"]

CMD ["gunicorn", "ToDo.wsgi", "-w", "4", "-b", "0.0.0.0:8000"]

