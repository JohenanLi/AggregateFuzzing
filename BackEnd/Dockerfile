FROM python:3.9

ENV MODE=PRODUCTION

COPY ./requirements.txt .
COPY ./uwsgi.ini .
COPY ./tools ./tools
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
WORKDIR /tools/AFL
RUN ls && make && make install
WORKDIR /tools/screen
RUN ls && ./configure && make
RUN echo $path
WORKDIR /
ENTRYPOINT [ "uwsgi", "--ini", "uwsgi.ini"]
