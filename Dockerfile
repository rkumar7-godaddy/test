FROM debian:11

RUN apt-get update && \
apt-get upgrade
RUN useradd -ms /bin/bash rohan
USER rohan
WORKDIR /home/rohan
RUN touch test.txt
CMD ls -al

