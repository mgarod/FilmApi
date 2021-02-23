FROM python:3.9.2

RUN apt-get update && apt-get install -y sqlite3

COPY . app/
WORKDIR app
RUN pip install -r requirements.txt

ENV ENV_FILE_LOCATION=.env
RUN python init_db.py
ENTRYPOINT /bin/bash -c "python app.py"
