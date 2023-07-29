FROM jrottenberg/ffmpeg:3.2.16-ubuntu2004
WORKDIR /root/encoder
COPY requirements.txt .
RUN apt-get update \
  && apt-get install -y sudo \
  && apt-get -y install python3-pip \
  && pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["start.sh"]
ENTRYPOINT ["bash"]
