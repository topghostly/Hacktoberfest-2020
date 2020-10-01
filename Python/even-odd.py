num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

   // Code For Getting If The Number is A Prime Or Not
for i in range(2, num):
   if num % i == 0:
      print(f"{num} Is Not A Prime Number")
      break

else:
   print(f"{num} Is Also A Prime Number")
