FROM python:3.9

ENV MODE=PRODUCTION

COPY ./requirements.txt .
COPY ./uwsgi.ini .
COPY ./tools ./tools
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
WORKDIR /tools/
RUN mkdir build
WORKDIR /tools/build
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list && \
    apt clean && \
    apt update
RUN apt install cmake
RUN cmake -G "Unix Makefiles" --enable-optimized --enable-targets=host-only -DCMAKE_BUILD_TYPE=Release  ../llvm-7.0.0.src
WORKDIR /tools/afl
RUN make
WORKDIR /tools/afl/mm_metric
RUN make
# WORKDIR /tools/aflGithub
# RUN ls && make && make install
# WORKDIR /tools/aflGithub/llvm_mode
# RUN make

#libevent
RUN apt-get install libevent-dev

#tmux
WORKDIR /tools/tmux
RUN ./configure CFLAGS="-I$HOME/.local/include -I$HOME/.local/include/ncurses" LDFLAGS="-L$HOME/.local/lib -L$HOME/.local/include/ncurses -L$HOME/.local/include" CPPFLAGS="-I$HOME/.local/include -I$HOME/.local/include/ncurses" LDFLAGS="-static -L$HOME/.local/include -L$HOME/.local/include/ncurses -L$HOME/.local/lib"  && make 
RUN cp tmux /bin
WORKDIR /
ENTRYPOINT [ "uwsgi", "--ini", "uwsgi.ini"]
