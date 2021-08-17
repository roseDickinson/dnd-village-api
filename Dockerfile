FROM python:3.9

RUN mkdir -p /opt/dnd-village-api
WORKDIR /opt/dnd-village-api

COPY requirements.txt /opt/dnd-village-api/
RUN pip install -r requirements.txt

COPY ./ /opt/dnd-village-api/
RUN ln -fs /opt/dnd-village-api /site

ENV PORT 5000
EXPOSE ${PORT}

CMD ./run_app.sh