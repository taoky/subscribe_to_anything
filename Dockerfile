FROM debian:buster-slim

COPY requirements.txt /tmp
RUN sed -i \
    -e 's/deb.debian.org/mirrors.ustc.edu.cn/g' \
    -e 's/security.debian.org/mirrors.ustc.edu.cn/g' \
    /etc/apt/sources.list && apt update && apt install -y python3 python3-dev python3-pip libxml2-dev && rm -rf /var/lib/apt/lists/* && pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && pip3 install -r /tmp/requirements.txt

WORKDIR /app
CMD ["python3", "run.py"]
