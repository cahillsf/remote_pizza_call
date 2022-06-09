from concurrent import futures
import logging
import grpc
import order_pb2
import order_pb2_grpc
from ddtrace import config, patch_all, Pin, patch, tracer
config.env = "dev"      # the environment the application is in
config.service = "grpc-server"  # name of your application
config.version = "0.0.1"  # version of your application
patch_all()


class Pricer(order_pb2_grpc.OrderPricerServicer):

    def GetOrderPrice(self, request, context):
        return order_pb2.PizzaOrderPriced(order=order_pb2.PizzaOrder(name= request.name,
        email=request.email,
        pizzas=request.pizzas,
        ), price=10.00)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderPricerServicer_to_server(Pricer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()