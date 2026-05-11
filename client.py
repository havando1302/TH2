import xmlrpc.client


# Kết nối tới RPC Server
s = xmlrpc.client.ServerProxy('http://localhost:8000')

# Gọi các hàm từ xa
print("add(2, 3) =", s.add(2, 3))

print("mul(5, 2) =", s.mul(5, 2))

print("sub(10, 4) =", s.sub(10, 4))

print("div(20, 5) =", s.div(20, 5))

print("div(5, 0) =", s.div(5, 0))

# In danh sách method có sẵn
print("\nAvailable methods:")
print(s.system.listMethods())