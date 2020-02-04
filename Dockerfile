FROM  python:3.7-alpine

LABEL maintainer=achillesrasquinha@gmail.com

ENV shank_PATH=/usr/local/src/shank

RUN apk add --no-cache \
        bash \
        git \
    && mkdir -p $shank_PATH

COPY . $shank_PATH
COPY ./docker/entrypoint.sh /entrypoint.sh

RUN pip install $shank_PATH

WORKDIR $shank_PATH

ENTRYPOINT ["/entrypoint.sh"]

CMD ["shank"]