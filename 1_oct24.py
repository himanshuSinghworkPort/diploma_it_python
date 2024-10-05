str=''' *********************
* 		 *
* 	welcome	 *
* 		 *
*		 *		
****************************
himanshu'''
print(str)

x = 0b1111111 #Binary Literals  
y = 100 #Decimal Literal   
z = 0o215 #Octal Literal  
u = 0x12d #Hexadecimal Literal  
  
#Float Literal  
float_1 = 100.5   
float_2 = 1.5e2  
  
#Complex Literal   
a = 5+3.14j  
  
print(x, y, z, u)  
print(float_1, float_2)  
print(a, a.imag, a.real)

x = (1 == True)  
y = (2 == False)  
z = (3 == True)  
a = True + 10  
b = False + 10  
  
print("x is", x)  
print("y is", y)  
print("z is", z)  
print("a:", a)  
print("b:", b)  