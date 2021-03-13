FROM python:3.9

ENV MODE=PRODUCTION

COPY ./requirements.txt .
COPY ./uwsgi.ini .
COPY ./tools ./tools
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
WORKDIR /tools/AFL
RUN ls && make && make install
WORKDIR /tools/screen-4.8.0
RUN ls
RUN ./configure && make
WORKDIR /
ENTRYPOINT [ "uwsgi", "--ini", "uwsgi.ini"]
