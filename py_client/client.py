from flask import Flask, jsonify, request, Response, make_response
from flask_cors import CORS
import logging
import grpc
import sys
import order_pb2
import order_pb2_grpc
from ddtrace import config, patch_all, Pin, patch, tracer
config.env = "dev"      # the environment the application is in
config.service = "grpc-client"  # name of your application
config.version = "0.0.1"  # version of your application
patch_all()

app = Flask(__name__)
# CORS(app, origins=["http://localhost:8080"], headers=['Content-Type'], expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True)
CORS(app)

def codify_toppings(toppings):
    int_toppings= []
    for topping in toppings:
        int_toppings.append(order_pb2.PizzaOrder.Toppings.Value(topping))
    return int_toppings


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    # while (True):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = order_pb2_grpc.OrderPricerStub(channel)
        response = stub.GetOrderPrice(order_pb2.PizzaOrder(name="Stephen"))
    print("Greeter client received: " + str(response.order) + " " + str(response.price))

@app.route('/api/test', methods=['GET', 'POST'])
def testRoute():
    print("test route", file=sys.stderr)
    app.logger.info("test route")
    if request.method == 'POST':
        print(request.data, file=sys.stderr)
        print(request.json['name'], file=sys.stderr)
    # with grpc.insecure_channel('pyserver:50051') as channel:
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = order_pb2_grpc.OrderPricerStub(channel)
        order = order_pb2.PizzaOrder(name=request.json['name'], email=request.json['email'])
        clean_pizzas = []
        for pizza in request.json['pizzas']: 
            toppings = codify_toppings(pizza['toppingslist'])
            clean_pizza = order_pb2.PizzaOrder.Pizza(size=pizza['size'], toppings=toppings)
            clean_pizzas.append(clean_pizza)
        order.pizzas.extend(clean_pizzas)
        response = stub.GetOrderPrice(order)
    print("Greeter client received: " + str(response.order) + " " + str(response.price), file=sys.stderr)
    return "OKAY", 200

# if __name__ == '__main__':
#     # logging.basicConfig()
#     run()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)