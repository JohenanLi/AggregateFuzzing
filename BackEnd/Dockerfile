FROM python:3.9

ENV MODE=PRODUCTION

COPY ./requirements.txt .
COPY ./uwsgi.ini .
COPY ./tools ./tools
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
# LLVM dependencies:


# WORKDIR /tools/
# RUN mkdir build
# WORKDIR /tools/build
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list && \
    apt clean && \
    apt update
RUN apk --no-cache add \
	autoconf \
	automake \
	cmake \
	freetype-dev \
	g++ \
	gcc \
	libxml2-dev \
	linux-headers \
	make \
	musl-dev \
	ncurses-dev \
	python2
# WORKDIR /tools/cmake
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

ARG LLVM_VERSION=7.0.1
COPY install_llvm.sh /
WORKDIR /
RUN chmod +x install_llvm.sh && ./install_llvm.sh ${LLVM_VERSION} && rm install_llvm.sh

ENV CXX=clang++
ENV CC=clang
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
