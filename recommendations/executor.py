import logging

import grpc
from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        client = RecommendationsStub(channel)
        request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=2)
        response = client.Recommend(request)
    print(response)


if __name__ == "__main__":
    logging.basicConfig()
    run()
