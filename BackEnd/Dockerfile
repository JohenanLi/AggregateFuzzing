FROM python:3.9

ENV MODE=PRODUCTION

COPY ./requirements.txt .
COPY ./uwsgi.ini .
COPY ./FuzzAll ./FuzzAll
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
WORKDIR /FuzzAll/AFL
RUN yum install afl
RUN ls && make && make install
WORKDIR .
ENTRYPOINT [ "uwsgi", "--ini", "uwsgi.ini"]
