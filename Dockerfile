FROM python:3.9

WORKDIR /usr/src/dashboard

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY dashboard.py config.py boot.sh app.db ./
RUN chmod +x boot.sh

ENV FLASK_APP dashboard.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]

