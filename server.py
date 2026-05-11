from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Giới hạn đường dẫn RPC
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Tạo XMLRPC Server
with SimpleXMLRPCServer(
        ('localhost', 8000),
        requestHandler=RequestHandler) as server:

    print("XML-RPC Server is running on port 8000...")

    # Cho phép introspection functions
    server.register_introspection_functions()

    # Hàm cộng
    def add(x, y):
        print(f"Client called add({x}, {y})")
        return x + y

    # Đăng ký hàm add
    server.register_function(add, 'add')

    # Class chứa các phương thức RPC
    class MyFunctions:

        def mul(self, x, y):
            print(f"Client called mul({x}, {y})")
            return x * y

        def sub(self, x, y):
            print(f"Client called sub({x}, {y})")
            return x - y

        def div(self, x, y):
            print(f"Client called div({x}, {y})")

            if y == 0:
                return "Cannot divide by zero"

            return x / y

    # Đăng ký instance
    server.register_instance(MyFunctions())

    # Chạy server
    server.serve_forever()