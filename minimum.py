A = int(input("Enter num A:"))
B =int(input("Enter num B:"))
C =int(input("Enter num C:"))
if (A<B) and (A<C):
    print(A,"IS MINIMUM")
elif (B<C) and (B<A):
   print(B, "IS MINIMUM")

else:
  print(C,"IS MINIMUM")

