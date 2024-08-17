FROM python:3.10.12-bullseye

ARG USER=ocpuser
ARG GROUP=ocpgroup
ARG USER_ID=1000
ARG GROUP_ID=1000

RUN addgroup --system --gid $GROUP_ID $GROUP && \
    adduser --system --uid $USER_ID --ingroup $GROUP $USER

RUN apt-get -qq update
RUN apt-get -qq install -y --no-install-recommends \
    curl \
    wget \
    jq \
    nano \
    netcat \
    cron \
    binutils \
    libproj-dev \
    gdal-bin \
    gettext

RUN apt-get -qq clean

RUN mkdir -p /product /static

COPY ./requirements.txt /product/requirements.txt
WORKDIR /product

RUN chown -R $USER:$GROUP /product

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

STOPSIGNAL SIGQUIT

COPY . /product
RUN chown -R $USER:$GROUP /product

USER $USER

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=1
ENV STAGE=dev
