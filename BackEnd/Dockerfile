FROM python:3.9

ENV MODE=PRODUCTION

COPY ./requirements.txt .
COPY ./uwsgi.ini .
COPY ./tools ./tools
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
WORKDIR /tools/AFL
RUN ls && make && make install
RUN tmux
WORKDIR /tools/screen
RUN ls && ./configure && make && cp ./screen /bin && ls /bin/screen
WORKDIR /
ENTRYPOINT [ "uwsgi", "--ini", "uwsgi.ini"]
