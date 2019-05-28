FROM python:3.7-alpine
ADD ./requirements.txt /
RUN pip install --upgrade pip; \
    pip install -r /requirements.txt; mkdir /code; 
WORKDIR /code
ENTRYPOINT ["python"]