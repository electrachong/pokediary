# developer version: remove emacs in future versions

FROM ubuntu:latest
MAINTAINER Electra Chong <electrachong@gmail.com>, Joe Greene <jggreene@gmail.com>
RUN apt-get update -y
RUN apt-get install -y git
WORKDIR /root/
RUN git clone https://github.com/electrachong/pokediary.git
RUN apt-get install -y python python-dev python-distribute python-pip
RUN pip install flask
RUN apt-get install -y emacs
WORKDIR /root/pokediary/app
ENTRYPOINT ["python"]
CMD ["app.py"]
# RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*