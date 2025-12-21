print("Enter a number (Numerator): ")
numn = int(input())
print("Enter a number (Denominator): ")
numd = int(input())
if numn%numd==0:
 print(f"{numn} is divisible by {numd}")
else:
 print(f"{numn} is not divisible by {numd}")