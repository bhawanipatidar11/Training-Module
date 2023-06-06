Physics = int(input("Enter the physics marks "))
Chemistry = int(input("Enter the Chemistry marks "))
Maths = int(input("Enter the Maths marks "))

aver = (Physics + Chemistry + Maths)/3
print("Average of three number is :" , aver)

pro = (Physics + Chemistry + Maths)/300 * 100
print("percentage of three number is :" , pro)

if Physics>100 and  Chemistry>100 and  Maths>100:
    print("Invalid marks")

elif pro>=80:
    print("Passed by first division")

elif pro>=70:
    print("Passed by Second division")

elif pro>=50:
    print("Passed by Third division")

else:
    print("Grade D")
