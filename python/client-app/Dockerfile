FROM python:3.7.2

ENV HTTP_PROXY="http://127.0.0.1:3128"
ENV HTTPS_PROXY="http://127.0.0.1:3128"

ADD client.py /
ADD requirements.txt /

WORKDIR /

RUN pip install -r requirements.txt

EXPOSE 8001

#CMD [ "python", "./client.py" ]
ENTRYPOINT ["python",  "./client.py"]
