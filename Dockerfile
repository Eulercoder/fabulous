FROM 1science/alpine

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
RUN apk update
RUN apk add --update python3 python3-dev vim bash make curl \
    && curl "https://bootstrap.pypa.io/get-pip.py" | python3 \
    && pip install --upgrade pip setuptools     \
    && ln -s /usr/bin/python3 /usr/bin/python   \
    && mkdir -p /opt /app

ADD . /app
WORKDIR /app
RUN pip install -e .
CMD make repl