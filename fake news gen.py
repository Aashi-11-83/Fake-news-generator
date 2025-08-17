import random

film_names = ["Shahrukh Khan", "Shradha Kapoor", "Anjana Singh", "Madhuri", "Ram", "Sita", "Arjun"]
film_actions = ["eating", "dancing", "singing", "crying"]
film_places = ["at Red Fort", "in Mumbai", "Goa pool", "in Gujarat", "at Stupa"]

sports_names = ["Virat Kohli", "Rohit Sharma", "MS Dhoni", "Sachin Tendulkar"]
sports_actions = ["scored a century", "took 5 wickets", "won the match", "hit a six"]
sports_places = ["in Wankhede Stadium", "at Eden Gardens", "in Australia", "in World Cup"]

politics_names = ["Narendra Modi", "Rahul Gandhi", "Amit Shah", "Yogi Adityanath"]
politics_actions = ["gave a speech", "started a rally", "met supporters", "launched a scheme"]
politics_places = ["in Delhi", "in UP", "in Gujarat", "in Bihar"]


save_file = "Fake_news.txt"

def custom_category():
    print("\n create your own custom category ")
    names = input("Enter some names (seperated comma): ").split(",")
    actions = input("Enter some actions (seperated comma): ").split(",")
    places = input("Enter some places (seperated comma): ").split(",")

    return [ name.strip() for name in names], [action.strip() for action in actions],[place.strip() for place in places]

while True:

    print("\n CHoose a category : ")
    print("1. Film")
    print("2. sports")
    print("3. Politics")
    print("4. custom(create your own)")

    choice = input("Enter your choice(1/2/3/4): ").strip()

    if choice == "1":
        subject = random.choice(film_names)
        action = random.choice(film_actions)
        place = random.choice(film_places)

    elif choice == "2":
        subject = random.choice(sports_names)
        action = random.choice(sports_actions)
        place = random.choice(sports_places)

    elif choice =="3":
        subject = random.choice(politics_names)
        action = random.choice(politics_actions)
        place = random.choice(politics_places)

    elif choice == "4":
        custom_names,custom_action,custom_place = custom_category()
        subject = random.choice(custom_names)
        action = random.choice(custom_action)
        place = random.choice(custom_place)

    else:
        print("Invalid Choice1 Try again ")

    headline = f"breaking news: {subject} {action} {place}"
    print("\n " + headline)


    save = input("Do you want to save this headline file (yes/no):").strip().lower()

    if save == "yes":
        with open(save_file,"a") as f:
            f.write(headline+"\n")
        print(f"Headingline saved in {save_file}")


    user_input = input("Do you want more news to generate (yes/no): ").strip().lower()
    if user_input == "no":
        break

print("Thankyou for using the fake news generator!")

                    