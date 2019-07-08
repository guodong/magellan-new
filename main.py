import ast
import astunparse
from threading import Thread
from flow_program import FlowProgram
from node_visitor import NodeVisitor

from grpc_server import serve
from compiler import compile

if __name__ == '__main__':
    # t = Thread(target=serve, args=(fp)).start()
    serve()


