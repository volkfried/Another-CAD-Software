import os
import math
import sys

def xSurface():
	"Outputs a mesh of coordinates; X is the dependent variable"
	for stepy in range(0, Ysteps):
		Y = stepy*Delta + Ymin
		for stepz in range(0, ZSteps):
			Z = stepz*Delta + Zmin
			#X = Y^2 + Z^2
			#round()
			coord = "(" + str(X) + ", " + str(Y) + ", " + str(Z) + ")"
			print(coord)
			stepz = stepz +1
		stepy = stepy + 1

def ySurface():
	"Outputs a mesh of coordinates; Y is the dependent variable"
	for stepx in range(0, Xsteps):
		X = stepx*Delta + Xmin
		for stepz in range(0, ZSteps):
			Z = stepz*Delta + Zmin
			#Y = X^2 - Z
			#round()
			coord = "(" + str(X) + ", " + str(Y) + ", " + str(Z) + ")"
			print(coord)
			stepz = stepz +1
		stepx = stepx + 1

def zSurface():
	"Outputs a mesh of coordinates; Z is the dependent variable"
	for stepx in range(0, Xsteps):
		X = stepx*Delta + Xmin
		for stepy in range(0, YSteps):
			Y = stepy*Delta + Ymin
			Z = X - Y
			#round()
			coord = str(X) + "\t" + str(Y) + "\t" + str(Z)
			print(coord)
			stepy = stepy +1
		stepx = stepx + 1

#def round():

#Retrieves saved file from 3Dmodel.xml
with open("3Dmodel.xml", "r") as file_obj:
	content = file_obj.read()

#lines = content.splitlines()
#for line in lines:
#	print("[" + line + "]")

Xmax = 10
Xmin = 0
Ymax = 10
Ymin = 0

Delta = .5
dec = 1000000

X = Xmin
Y = Ymin

Z = X - Y

Xsteps = (Xmax - Xmin)/Delta + 1
YSteps = (Ymax - Ymin)/Delta + 1
Xsteps = math.floor(Xsteps)
YSteps = math.floor(YSteps)

zSurface()
