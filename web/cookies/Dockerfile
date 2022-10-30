FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3 python3-pip poppler-utils 
RUN pip3 install python-dotenv flask 

RUN useradd -s /bin/bash admin

COPY app /home/admin/app
WORKDIR /home/admin/app

#RUN chown -R admin:root /home/admin
USER admin

EXPOSE 1337
ENTRYPOINT ["flask", "run"]
