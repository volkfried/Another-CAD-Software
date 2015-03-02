import os
import math
import sys

with open("cylinder.xml", "r") as file_obj:
	content = file_obj.read()

lines = content.splitlines()
for line in lines:
	print(line)
