import random
from colorama import Fore, Style

def read_jokes_from_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

knock_jokes_list = read_jokes_from_file("C:\\Users\\pinsa\\Desktop\\IT\\ReDI\\Python Foundation s23\\final project\\knock_jokes.txt")
dad_jokes_list = read_jokes_from_file("C:\\Users\\pinsa\\Desktop\\IT\\ReDI\\Python Foundation s23\\final project\\dad_jokes.txt")
programming_jokes_list = read_jokes_from_file("C:\\Users\\pinsa\\Desktop\\IT\\ReDI\\Python Foundation s23\\final project\\programming_jokes.txt")

name=input("Hello, Welcome to the joke bot! Please type in your name: " )

def joke_bot():
    category=input(f"""
                     Dear {name}, Please choose a joke category.
                     You can choose between three categories:
                     For knock-knock jokes, type 'knock knock' 
                     For dad jokes, type 'dad'
                     For programming jokes, type 'programming' """).lower()
    if category=="knock knock":
        if len(knock_jokes_list)>0:
            a=random.choice(knock_jokes_list)
            knock_jokes_list.remove(a)
            print (Fore.GREEN + f"\n{a}\n" + Style.RESET_ALL)
        else:
            print ("\nSorry, we have no more knock knock jokes left ):\n")
    elif category=="dad":
        if len(dad_jokes_list)>0:
            b=random.choice(dad_jokes_list)
            dad_jokes_list.remove(b)
            print (Fore.BLUE + f"\n{b}\n" + Style.RESET_ALL)
        else:
            print ("\nSorry, we have no more dad jokes left ):\n")
    elif category=="programming":
        if len(programming_jokes_list)>0:
            c=random.choice(programming_jokes_list)
            programming_jokes_list.remove(c)
            print (Fore.RED + f"\n{c}\n" + Style.RESET_ALL)
        else:
            print ("\nSorry, we have no more programming jokes left ):\n")
    else:
        print ("\nPlease only choose between 'knock knock', 'dad' or 'programming', otherwise we can't move forward :)")
        return joke_bot()

    again=input("""
              Would you like another joke? Then type 'yes'
              If you had enough laughs for today, type 'done'
              """).lower()
    if again=='yes':
        return joke_bot()
    elif again=='done':
        print ("\nThank you for using the joke bot!")
    else:
        print ("\nPlease type either 'yes' or 'done'\n")
        return joke_bot()

joke_bot()
