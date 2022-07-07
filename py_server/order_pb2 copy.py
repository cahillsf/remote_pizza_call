# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: order.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0border.proto\x12\x05pizza\"\xd6\x02\n\nPizzaOrder\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\'\n\x06pizzas\x18\x03 \x03(\x0b\x32\x17.pizza.PizzaOrder.Pizza\x1a`\n\x05Pizza\x12)\n\x04size\x18\x01 \x01(\x0e\x32\x1b.pizza.PizzaOrder.PizzaSize\x12,\n\x08toppings\x18\x02 \x03(\x0e\x32\x1a.pizza.PizzaOrder.Toppings\"-\n\tPizzaSize\x12\t\n\x05LARGE\x10\x00\x12\n\n\x06MEDIUM\x10\x01\x12\t\n\x05SMALL\x10\x02\"q\n\x08Toppings\x12\r\n\tPEPPERONI\x10\x00\x12\x0b\n\x07SAUSAGE\x10\x01\x12\x0c\n\x08MUSHROOM\x10\x02\x12\x0b\n\x07PEPPERS\x10\x03\x12\n\n\x06ONIONS\x10\x04\x12\x0c\n\x08MEATBALL\x10\x05\x12\n\n\x06GARLIC\x10\x06\x12\x08\n\x04PARM\x10\x07\"C\n\x10PizzaOrderPriced\x12 \n\x05order\x18\x01 \x01(\x0b\x32\x11.pizza.PizzaOrder\x12\r\n\x05price\x18\x02 \x01(\x02\x32L\n\x0bOrderPricer\x12=\n\rGetOrderPrice\x12\x11.pizza.PizzaOrder\x1a\x17.pizza.PizzaOrderPriced\"\x00')



_PIZZAORDER = DESCRIPTOR.message_types_by_name['PizzaOrder']
_PIZZAORDER_PIZZA = _PIZZAORDER.nested_types_by_name['Pizza']
_PIZZAORDERPRICED = DESCRIPTOR.message_types_by_name['PizzaOrderPriced']
_PIZZAORDER_PIZZASIZE = _PIZZAORDER.enum_types_by_name['PizzaSize']
_PIZZAORDER_TOPPINGS = _PIZZAORDER.enum_types_by_name['Toppings']
PizzaOrder = _reflection.GeneratedProtocolMessageType('PizzaOrder', (_message.Message,), {

  'Pizza' : _reflection.GeneratedProtocolMessageType('Pizza', (_message.Message,), {
    'DESCRIPTOR' : _PIZZAORDER_PIZZA,
    '__module__' : 'order_pb2'
    # @@protoc_insertion_point(class_scope:pizza.PizzaOrder.Pizza)
    })
  ,
  'DESCRIPTOR' : _PIZZAORDER,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:pizza.PizzaOrder)
  })
_sym_db.RegisterMessage(PizzaOrder)
_sym_db.RegisterMessage(PizzaOrder.Pizza)

PizzaOrderPriced = _reflection.GeneratedProtocolMessageType('PizzaOrderPriced', (_message.Message,), {
  'DESCRIPTOR' : _PIZZAORDERPRICED,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:pizza.PizzaOrderPriced)
  })
_sym_db.RegisterMessage(PizzaOrderPriced)

_ORDERPRICER = DESCRIPTOR.services_by_name['OrderPricer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PIZZAORDER._serialized_start=23
  _PIZZAORDER._serialized_end=365
  _PIZZAORDER_PIZZA._serialized_start=107
  _PIZZAORDER_PIZZA._serialized_end=203
  _PIZZAORDER_PIZZASIZE._serialized_start=205
  _PIZZAORDER_PIZZASIZE._serialized_end=250
  _PIZZAORDER_TOPPINGS._serialized_start=252
  _PIZZAORDER_TOPPINGS._serialized_end=365
  _PIZZAORDERPRICED._serialized_start=367
  _PIZZAORDERPRICED._serialized_end=434
  _ORDERPRICER._serialized_start=436
  _ORDERPRICER._serialized_end=512
# @@protoc_insertion_point(module_scope)