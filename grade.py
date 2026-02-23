Subject1 =int(input("enter marks of subject 1 : " ))
Subject2 =int(input("enter marks of subject 2 : " ))
Subject3 =int(input("enter marks of subject 3 : " ))

sum=Subject1 + Subject2 + Subject3
average=sum/3

if(average>=70 and average <=100) :
    print("your grade is an A.")
elif(average>=60 and average <=69) :
    print("your grade is a B.")
elif(average>=50 and average <=59) :
    print("your grade is a C.")
elif(average>=40 and average <=49) :
    print("your grade is a D.")
elif(average>=0 and average <=39) :
    print("your grade is an E.")
else:
    print("enter valid marks")

print("your average grade is",grade)
