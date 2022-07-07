https://grpc.io/docs/languages/python/quickstart/

for generating the files from 
```
.proto python3 -m grpc_tools.protoc -I=/Users/stephen.cahill/Desktop/pygrpc --python_out=/Users/stephen.cahill/Desktop/pygrpc --grpc_python_out=/Users/stephen.cahill/Desktop/pygrpc /Users/stephen.cahill/Desktop/pygrpc/order.proto
```

Idea is to :

- have a web UI that passes a pizza order to the gRPC client 
- client hosts the routes to receive front end call, then makes a gRPC call to the gRPC server (PizzaOrder)
- gRPC server calculates the price of the pizza order based on "market conditions (some sort of pseudo random number generator", then returns that to the clien  (PizzaOrderPriced)
- client passes along the priced order to the front end which reflects the updated price


{
	"showModal": false,
	"name": "sdfd",
	"email": "sdf",
	"pizza": {
		"size": "large",
		"toppingslist": ["PEPPERS", "SAUSAGE"]
	},
	"pizzas": [{
		"size": "large",
		"toppingslist": ["PEPPERS", "SAUSAGE"]
	}, {
		"size": "large",
		"toppingslist": ["ONIONS", "PARM"]
	}]
}