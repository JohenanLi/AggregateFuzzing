FROM python:3.9

ENV MODE=PRODUCTION

COPY ./requirements.txt .
COPY ./uwsgi.ini .
COPY ./tools ./tools
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
WORKDIR /tools/AFL
RUN ls && make && make install
#ncurses
# WORKDIR /tools/ncurses
# RUN ./configure --prefix=$HOME/.local && make && make install
#libevent
WORKDIR /tools/libevent

RUN sudo apt-get install libevent-dev

#tmux
WORKDIR /tools/tmux
RUN ./configure CFLAGS="-I$HOME/.local/include -I$HOME/.local/include/ncurses" LDFLAGS="-L$HOME/.local/lib -L$HOME/.local/include/ncurses -L$HOME/.local/include" CPPFLAGS="-I$HOME/.local/include -I$HOME/.local/include/ncurses" LDFLAGS="-static -L$HOME/.local/include -L$HOME/.local/include/ncurses -L$HOME/.local/lib"  && make 
RUN cp tmux /bin
WORKDIR /
ENTRYPOINT [ "uwsgi", "--ini", "uwsgi.ini"]
