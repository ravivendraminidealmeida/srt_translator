FROM python:3.12-alpine

WORKDIR /server

COPY requirements.txt requirements.txt

COPY . .

RUN pip3 install -r requirements.txt
RUN chmod u+x ./entrypoint.sh

EXPOSE 80

ENTRYPOINT [ "./entrypoint.sh" ]




