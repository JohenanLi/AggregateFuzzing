FROM python:3.9

ENV MODE=PRODUCTION

COPY ./requirements.txt .
COPY ./uwsgi.ini .
COPY ./tools ./tools
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
WORKDIR /tools/AFL
RUN ls && make && make install
WORKDIR /tools/screen-4.8.0
RUN ls && ./configure && make
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
    echo "deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse" >/etc/apt/sources.list && \
    echo "deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse" >>/etc/apt/sources.list 
RUN apt-get install screen
WORKDIR /
ENTRYPOINT [ "uwsgi", "--ini", "uwsgi.ini"]
