#Diego Espinola
#10.07.19
#else and if exercise. 
#test
people= 30
cars= 40
trucks=15

if cars>people:
    print("We shoould take the cars")
elif cars<people:
    print("We should not take the cars.")
else:
    print("We cant decide.")

if trucks > cars:
    print("That is too many trucks")
elif trucks < cars:
    print("Maybe we could take the trucks")
else:
    print("We still can not decide.")

if people > trucks:
    print("Alright, let's just take the trucks")

else:
    print("Fine, let's stay home then")
