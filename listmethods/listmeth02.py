
#!/usr/bin/env python3

# This line is describing proto as a list-object.
proto = ["ssh", "http", "https"]

# This line is describing protoa as a list-object
protoa = ["ssh", "http", "https"]

# This line explains what we're saying in the print function.
saying = ["These are common port functions"]

# This line prints the objects int he list "proto"
print(saying + proto)

# This line will add "dns" to the end of our list
proto.append("dns")

# This line will add "dns" to the end of our list.
protoa.append("dns")

# This line will print the objects in the list "proto"
print(proto)

# This is a list of common port numbers
proto2 = [ 22, 80, 443, 53 ]

# This line passes proto2 as an argument to the extend method.
proto.extend(proto2)

# This line prints the objects in the list for proto.
print(proto)

# This line passes proto2 as an argument to the append mthod
protoa.append(proto2)
# This line prints the objects in the list protoa
print(protoa)
