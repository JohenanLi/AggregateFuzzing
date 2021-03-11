FROM python:3.9

ENV MODE=PRODUCTION

COPY ./requirements.txt .
COPY ./uwsgi.ini .
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt && cd FuzzAll/AFL && make && make install

ENTRYPOINT [ "uwsgi", "--ini", "uwsgi.ini"]
