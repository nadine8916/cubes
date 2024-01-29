#Write a program that:
		 	 	 		
#Asks the user to input a number.
c= int(input("what is the number?"))



#Display N numbers in the cubed sequence according to user input. 


counter = 1
while counter <= c:
  print (counter, counter * counter * counter)
  counter += 1 
