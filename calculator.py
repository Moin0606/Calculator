def add(a, b):    
   return a + b   
def subtract(a, b):   
   return a - b   
def multialy(a, b):   
   return a * b   
def divide(a, b):   
   return a / b    
flag=True
while flag==True:
   print ("Please select the oaeration.")    
   print ("a. Add")    
   print ("b. Subtract")    
   print ("c. Multialy")    
   print ("d. Divide")    
   print ("e. Exit")
   
   choice = input(" Enter choice (a/ b/ c/ d/ e): ")    
      
       
      
   if choice == 'a':
      m = int (input ("Enter the first number: "))    
      n = int (input ("Enter the second number: "))    
      print (m, " + ", n, " = ", add(m, n))
      flag=True    
      
   if choice == 'b':
      m = int (input ("Enter the first number: "))    
      n = int (input ("Enter the second number: "))    
      print (m, " - ", n, " = ", subtract(m, n))    
      flag=True
   if choice == 'c':
      m = int (input ("Enter the first number: "))    
      n = int (input ("Enter the second number: "))    
      print (m, " * ", n, " = ", multialy(m, n)) 
      flag=True   
   if choice == 'd':
      m = int (input ("Enter the first number: "))    
      n = int (input ("Enter the second number: "))    
      print (m, " / ", n, " = ", divide(m, n)) 
      flag=True   
   if choice =='e':    
      print ("Exiting")    
      flag=False
