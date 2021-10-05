import numpy as np

x = 1.0 	#define a float
y = 2.0 	#define another float

#exponents and logarithms
print(np.exp(x))		#e^x
print(np.log(x))		#ln x
print(np.log10(x))		#log_10 x
print(np.log2(x))		#log_2 x

#min/max/misc
print(np.fabs(x))		#Absolute val as a float
print(np.fmin(x,y))		#min f x and y
print(np.fmax(x,y))		#max of x and y

#populate arrays
n = 100 						#define an int
z = np.arange(n,dtype=float)	#get an array [0.0,float(n-1)]
z *= 2.0*np.pi /float(n-1)		
sin_z = np.sin(z)				#an array sin(z)

#interpolation
print(np.interp(.075,z,sin_z))
print(np.sin(0.75))