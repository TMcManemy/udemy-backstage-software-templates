FROM python:3.9-alpine

COPY ./requirements.txt /tmp

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r /tmp/requirements.txt

COPY src /src

CMD python /src/app.py
