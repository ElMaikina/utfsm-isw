
FROM python:3.10 as django
USER root
ENV PYHONBUFFERED = 1
WORKDIR /gitgud-san-benito/back
COPY ./requirements.txt ./
COPY ./manage.py ./
COPY . ./
RUN pip install -r requirements.txt


EXPOSE 8000 3000 4000 8080 5432



