FROM python:slim-buster

# Repo Clone

RUN git clone https://github.com/jaaat4u/Simple-Telethon-Userbot /root/userbot

# Workdir 

WORKDIR /root/userbot

# Install Requirements

RUN pip3 install --no-cache-dir requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
