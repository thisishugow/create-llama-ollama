FROM debian:latest

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends curl
RUN TZ=Asia/Taipei \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata 

# replace $PQ_USER, $PQ_PASSWORD, PQ_DBNAME in script.sql

# Install Python 3.11 and PIP
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget procps systemd
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3-dev gcc
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3.11 python3.11-distutils

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN mv /usr/lib/python3.11/EXTERNALLY-MANAGED /usr/lib/python3.11/EXTERNALLY-MANAGED.bk
RUN python3.11 get-pip.py
RUN pip3 install --upgrade setuptools
RUN curl -fsSL https://ollama.com/install.sh | sh
ENV OLLAMA_HOST=localhost:11434

RUN mkdir /app
RUN mkdir /app/data
RUN mkdir /app/chromadb
RUN mkdir cache_folder
COPY backend /app
COPY dist/requirements.txt /app
COPY dist/docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

WORKDIR /app
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "docker-entrypoint.sh" ]
EXPOSE 8080