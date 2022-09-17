FROM python

RUN mkdir /service

COPY marketplace/requirements.txt /service/marketplace/requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r /service/marketplace/requirements.txt
COPY protobufs/ /service/protobufs/
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/recommendations.proto

COPY marketplace/ /service/marketplace/
WORKDIR /service/marketplace

EXPOSE 5000
ENV FLASK_APP=marketplace.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]