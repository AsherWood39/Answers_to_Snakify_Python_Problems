
# This program validates file operations against a set of allowed operations and prints "OK" for valid requests or "Access denied" for invalid ones based on the given filesystem permissions.

operations = {
    "write" : "W",
    "read" : "R",
    "execute" : "X"}
permissions={}
for i in range(int(input())):
    file, *o = input().strip().split()
    permissions[file] = set(o)
for i in range(int(input())):
    o, file = input().strip().split()
    if operations[o] in permissions[file]:
        print("OK")
    else:
        print("Access denied")
