FROM python:3.9

ENV MODE=PRODUCTION

RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list && \
    apt clean && \
    apt update
RUN apt-get install cmake -y

ARG LLVM_VERSION=7.0.0
COPY install_llvm.sh /
WORKDIR /
RUN chmod +x install_llvm.sh && ./install_llvm.sh ${LLVM_VERSION} && rm install_llvm.sh

COPY ./requirements.txt .
COPY ./uwsgi.ini .
COPY ./tools ./app/tools
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
# LLVM dependencies:


# WORKDIR /app/tools/
# RUN mkdir build
# WORKDIR /app/tools/build

# WORKDIR /app/tools/cmake
# ARG CMAKE_VERSION=3.4.3
# # #https://github.com/Kitware/CMake/releases/download/v3.16.0/cmake-3.16.0-Linux-x86_64.sh
# RUN wget https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}-Linux-x86_64.sh \
#       -q -O /tmp/cmake-install.sh \
#       && chmod u+x /tmp/cmake-install.sh \
#       && mkdir /usr/bin/cmake \
#       && /tmp/cmake-install.sh --skip-license --prefix=/usr/bin/cmake \
#       && rm /tmp/cmake-install.sh
# RUN ls && chmod +x cmake-3.4.3-linux-x86_64.sh &&\
#         ./cmake-3.4.3-linux-x86_64.sh --prefix=/usr/local --exclude-subdir --skip-license &&\
#         rm ./cmake-3.4.3-linux-x86_64.sh

#https://github.com/JohenanLi/AggregateFuzzing/commit/361347b0353b2d5eaafb9052b2beb89311858320a
# ENV PATH="/usr/bin/cmake/bin:${PATH}"


# ENV CXX=clang++
# ENV CC=clang
ENV LLVM_CONFIG /usr/local/bin/llvm-config

# ENV CC /usr/local/bin/clang
# ENV CXX /usr/local/bin/clang++
# RUN echo 'export LLVM_CONFIG=/usr/local/bin/llvm_config' >> /etc/profile  \
# && echo 'export CC=/usr/local/bin/clang' >> /etc/profile \
# && echo 'export CXX=/usr/local/bin/clang++' >> /etc/profile \
# && /bin/bash -c 'source /etc/profile'

WORKDIR /app/tools/afl-2.52b
RUN ls && make
WORKDIR /app/tools/afl-2.52b/llvm_mode
RUN ls /usr/local/bin && make


WORKDIR /app/tools/AFL-2.57b 
RUN ls && make  
WORKDIR /app/tools/AFL-2.57b/llvm_mode
RUN make

WORKDIR /app/tools/TortoiseFuzz-master
RUN make


WORKDIR /app/tools/collafl-master 
RUN  chmod 777 afl-gcc && make
ENV CC /usr/local/bin/clang
ENV CXX /usr/local/bin/clang++
WORKDIR /app/tools/collafl-master/llvm_mode 
RUN make



#libevent
RUN apt-get install libevent-dev

#tmux
WORKDIR /app/tools/tmux
RUN ./configure CFLAGS="-I$HOME/.local/include -I$HOME/.local/include/ncurses" LDFLAGS="-L$HOME/.local/lib -L$HOME/.local/include/ncurses -L$HOME/.local/include" CPPFLAGS="-I$HOME/.local/include -I$HOME/.local/include/ncurses" LDFLAGS="-static -L$HOME/.local/include -L$HOME/.local/include/ncurses -L$HOME/.local/lib"  && make 
RUN cp tmux /bin
WORKDIR /
ENTRYPOINT [ "uwsgi", "--ini", "uwsgi.ini"]
