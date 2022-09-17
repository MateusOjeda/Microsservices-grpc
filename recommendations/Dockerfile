FROM python

RUN mkdir /service

COPY recommendations/requirements.txt /service/recommendations/requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r /service/recommendations/requirements.txt
COPY protobufs/ /service/protobufs/
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/recommendations.proto

COPY recommendations/ /service/recommendations/
WORKDIR /service/recommendations


EXPOSE 50051
ENTRYPOINT [ "python", "recommendations.py" ]