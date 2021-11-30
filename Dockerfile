# Hugo doesn't require Go to run, *except* if you're using Hugo Modules. It's
# much easier to install Node on the Go base image than vice-versa.
FROM golang:1.15-alpine

# the following version can be overridden at image build time with --build-arg
ARG HUGO_VERSION=0.89.4
# remove/comment the following line completely to build with vanilla Hugo:
ARG HUGO_EXTENDED=1

LABEL "com.github.actions.name"="Hugo Build"
LABEL "com.github.actions.description"="Hugo as an action, with extended support and legacy versions"
LABEL "com.github.actions.icon"="edit"
LABEL "com.github.actions.color"="gray-dark"

LABEL version="${HUGO_VERSION}${HUGO_EXTENDED:+-extended}"
LABEL repository="https://github.com/jakejarvis/hugo-build-action"
LABEL homepage="https://jarv.is/"
LABEL maintainer="Jake Jarvis <jake@jarv.is>"

# only install libc6-compat & libstdc++ if we're building extended Hugo
# https://gitlab.com/yaegashi/hugo/commit/22f0d5cbd6114210ba7835468facbdee60609aa2
RUN apk update && \
    apk add --no-cache \
      ca-certificates \
      git \
      nodejs \
      npm \
      python3 \
      py3-pip \
      ruby \
      ${HUGO_EXTENDED:+libc6-compat libstdc++} && \
    update-ca-certificates

# download Hugo and miscellaneous optional dependencies
RUN npm install --global tailwindcss postcss postcss-cli autoprefixer @babel/core @babel/cli && \
    echo $NODE_ENV && \
    pip3 install --upgrade Pygments==2.* && \
    gem install asciidoctor && \
    wget https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_EXTENDED:+extended_}${HUGO_VERSION}_Linux-64bit.tar.gz && \
    wget https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_checksums.txt && \
    grep hugo_${HUGO_EXTENDED:+extended_}${HUGO_VERSION}_Linux-64bit.tar.gz hugo_${HUGO_VERSION}_checksums.txt | sha256sum -c && \
    tar xf hugo_${HUGO_EXTENDED:+extended_}${HUGO_VERSION}_Linux-64bit.tar.gz && \
    mv ./hugo /usr/local/bin/ && \
    chmod +x /usr/local/bin/hugo && \
    rm -rf hugo_* LICENSE README.md

# fix potential stack size problems on Alpine
# https://github.com/microsoft/vscode-dev-containers/blob/fb63f7e016877e13535d4116b458d8f28012e87f/containers/hugo/.devcontainer/Dockerfile#L19
RUN go get github.com/yaegashi/muslstack && \
    muslstack -s 0x800000 /usr/local/bin/hugo

# verify everything's OK, fail otherwise
RUN hugo version && \
    hugo env && \
    echo "PostCSS Version:" &&\
    postcss --version && \
    tailwindcss -h && \
    autoprefixer --version && \
    babel --version && \
    pygmentize -V && \
    asciidoctor --version

COPY . /go/site

ENTRYPOINT ["/bin/sh"]