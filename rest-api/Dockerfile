FROM python:3-alpine
MAINTAINER Argon <argon.l@inwinstack.com>

ARG VERSION="2.16.0"
ARG KUBE_VERSION="1.16.6"

ENV KUBECONFIG=/etc/kubernetes/admin.conf
ENV BASE_URL="https://get.helm.sh"
ENV TAR_FILE="helm-v${VERSION}-linux-amd64.tar.gz"

RUN apk add --update ca-certificates && \
    apk add --update -t deps curl && \
    curl -L https://storage.googleapis.com/kubernetes-release/release/v$KUBE_VERSION/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl && \
    curl -L ${BASE_URL}/${TAR_FILE} |tar xvz && \
    mv linux-amd64/helm /usr/bin/helm && \
    chmod +x /usr/bin/helm && \
    chmod +x /usr/local/bin/kubectl && \
    rm -rf linux-amd64 && \
    apk del --purge deps && \
    rm /var/cache/apk/* && \
    mkdir -p /usr/src/app &&\
    mkdir -p /etc/kubernetes

COPY admin.conf /etc/kubernetes

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

# Expose the Flask port
EXPOSE 5000

CMD [ "python", "./app.py" ]



