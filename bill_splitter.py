Name:Nsengiyumva Philbert
Registration Number:221012319
Department:Computer science
  
   codes of last work on project are:
      import random
num_friends = int(input("Enter the number of friends joining (including you):\n"))
if num_friends <= 0:
    print("No one is joining for the party")
else:
    friends = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        name = input()
        friends[name] = 0
    total_bill = float(input("Enter the total bill value:\n"))
    split_value = round(total_bill / num_friends, 2)
    for name in friends:
        friends[name] = split_value
    print("Do you want to use the randomizer? (yes/no)")
    res = input()
    if res.lower() == "yes":
        lucky = random.choice(list(friends.keys()))
        print("{} is the lucky one!".format(lucky))      
        for i in friends:
            friends.update({lucky: 0})
            if i == lucky:
                friends.update({lucky: 0})
            else:
                split_value = round(total_bill / (num_friends - 1), 2)
                friends.update({i: round(float(split_value), 2)})
        print(friends)
    else:
        print("No one is going to be lucky")
        print(friends)
