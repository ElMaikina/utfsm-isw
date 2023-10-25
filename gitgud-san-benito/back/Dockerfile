
FROM python:3.10 as postgres

ENV PYHONBUFFERED = 1
WORKDIR /gitgud-san-benito/back
COPY ./requirements.txt ./
COPY ./manage.py ./
COPY . ./
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver




