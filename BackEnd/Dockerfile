FROM python:3.9

ENV MODE=PRODUCTION

COPY ./requirements.txt .
COPY ./uwsgi.ini .
COPY ./tools ./tools
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
# Install dependencies
RUN apt-get -qq update; \
    apt-get install -qqy --no-install-recommends \
        ca-certificates \
        autoconf automake cmake dpkg-dev file git make patch \
        libc-dev libc++-dev libgcc-8-dev libstdc++-8-dev  \
        dirmngr gnupg2 lbzip2 wget xz-utils libtinfo5; \
    rm -rf /var/lib/apt/lists/*

# Signing keys
ENV GPG_KEYS 09C4E7007CB2EFFB A2C794A986419D8A B4468DF4E95C63DC D23DD2C20DD88BA2 8F0871F202119294 0FC3042E345AD05D

# Retrieve keys
RUN gpg --batch --keyserver ha.pool.sks-keyservers.net --recv-keys $GPG_KEYS

# Version info
ENV LLVM_RELEASE 7
ENV LLVM_VERSION 7.0.1

# Install Clang and LLVM
COPY install.sh .
RUN ./install.sh
# WORKDIR /tools/
# RUN mkdir build
# WORKDIR /tools/build
# RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list && \
#     apt clean && \
#     apt update
# WORKDIR /tools/cmake
# RUN ls && chmod +x cmake-3.20.0-linux-x86_64.sh &&\
#     ./cmake-3.20.0-linux-x86_64.sh --prefix=/usr/local --exclude-subdir --skip-license &&\
#     rm ./cmake-3.20.0-linux-x86_64.sh
# WORKDIR /tools/build
# RUN cmake -G "Unix Makefiles" ../llvm-7.0.0.src
#--enable-optimized --enable-targets=host-only -DCMAKE_BUILD_TYPE=Release
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
