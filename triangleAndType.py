A = int(input("Enter angle A:"))
B =int(input("Enter angle B:"))
C =int(input("Enter angle C:"))
if (A+B+C==180) and (A>0) and (B>0) and (C>0):
    if(A==90) or (B==90)  or (C==90):
        print("IT IS RIGHT ANGLE TRIANGLE")
    elif((A>90) or (B>90)or (C>90)):
        print("IT IS OBTUSE ANGLED TRAIANGLE")
    else:
        print("IT IS ACUTE ANGLED TRAIANGLE")

else:
  print("NON VALID")

