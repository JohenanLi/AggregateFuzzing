FROM python:3.9

ENV MODE=PRODUCTION

COPY ./requirements.txt .
COPY ./uwsgi.ini .
COPY ./tools ./tools
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
RUN apt-get update && apt-get install -y build-essential curl xz-utils && \
  rm -rf /var/lib/apt/lists/* && \
  curl -SL http://releases.llvm.org/7.0.0/clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04.tar.xz | tar -xJC . && \
  mv clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04 clang_7.0.0 && \
  echo 'export PATH=/clang_7.0.0/bin:$PATH' >> ~/.bashrc && \
  echo 'export LD_LIBRARY_PATH=/clang_7.0.0/lib:LD_LIBRARY_PATH' >> ~/.bashrc
WORKDIR /tools/afl
RUN make
WORKDIR /
RUN cat ~/.bashrc && cat ~/.zshrc &&clang --version
WORKDIR /tools/afl/mm_metric
RUN make
#ncurses
# WORKDIR /tools/ncurses
# RUN ./configure --prefix=$HOME/.local && make && make install
#libevent
RUN apt-get install libevent-dev

#tmux
WORKDIR /tools/tmux
RUN ./configure CFLAGS="-I$HOME/.local/include -I$HOME/.local/include/ncurses" LDFLAGS="-L$HOME/.local/lib -L$HOME/.local/include/ncurses -L$HOME/.local/include" CPPFLAGS="-I$HOME/.local/include -I$HOME/.local/include/ncurses" LDFLAGS="-static -L$HOME/.local/include -L$HOME/.local/include/ncurses -L$HOME/.local/lib"  && make 
RUN cp tmux /bin
WORKDIR /
ENTRYPOINT [ "uwsgi", "--ini", "uwsgi.ini"]
