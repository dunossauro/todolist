FROM python:3.6.5-stretch
MAINTAINER Eduardo Mendes <mendesxeduardo@gmail.com>

WORKDIR /code/

COPY ./requirements.txt /code/
COPY . /code/
RUN pip install -r ./requirements.txt

EXPOSE 8080

CMD ["python3", "-i", "project/api.py"]
