import os
import pprint

# access the path environment variable
environment_var = os.environ

print("User environment variables: ")
pprint.pprint(dict(environment_var), width = 1)

print("----------------------------------------------------------------------------------")

home = os.environ['HOME']
path = os.environ['PATH']
print("HOME -> ", home)
print("HOME -> ", path)