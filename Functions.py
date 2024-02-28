import requests #imports the requests module, for making HTTP requests.

def retrieve_data(url_tp_retrieve): #Function that Retrieve the information from the url 
    api_url = url_tp_retrieve
    response = requests.get(api_url)
    data = response.json()
    return data 

c_url=  "https://ddragon.leagueoflegends.com/cdn/13.23.1/data/en_US/champion.json" 
data= retrieve_data(c_url)


def welcome():
    print("==---------------------------==")
    print("Welcome to League of Legends, this interface can help you to know more about this game.")


def option():
    print("What do you want to do: ")
    print("1. Show all the Champions name")
    print("2. Show all the Champions Title")
    print("3. Show the champ LORE that you choose ")
    print("4. Compare 2 champs to know who is more difficult  ")
    print("5. Exit")

def show_names():#Show all the names 
    for c in data.get("data"):
            print(data.get("data").get(c).get("name")) #retrieve all the data. 

def name_title():
    title_champion={} # Initialize an empty dictionary to store name-title pairs
    for title in data.get("data"):
            champion_data = data.get("data").get(title)  # Get the champion data corresponding to the current title
            name = champion_data.get("name")  # Get the name 
            title = champion_data.get("title") # Get the tittle
            title_champion[name] = title  # Store the name-title pair in the dictionary
   
    for name, title in title_champion.items(): # iterate over each champ and print the name and tittle. 
        print(f"Name: {name}, Title: {title}")

def Lore_champ():
    Select_lore= input("About what champ you want to retrieve the Lore: ") #Input what ask the user 
    print("\n")
    lore_champ = data.get("data").get(Select_lore).get("blurb") # uses the input from the user to access the "blurb" attribute of the champ's data
    if Select_lore in lore_champ: # If the Lore is found, it is printed. 
         print(lore_champ)
    print("\n")

def stronger_champ ():
     print("Which champion do you want to selct first: ") #Ask the user for 2 champs in the list. 
     difficult_champ1= input("")
     print("Select the second champ what you want to compare: ")
     difficult_champ2= input("")
     comparative_difficult1= data.get("data").get(difficult_champ1).get("info").get("difficulty") #Get the difficulty of the 1st
     comparative_difficult2= data.get("data").get(difficult_champ2).get("info").get("difficulty")#Get the difficulty of the 2nd
     if comparative_difficult1 > comparative_difficult2: #both difficulties are compared 
          print(f"{difficult_champ1} is more difficult than {difficult_champ2}")
     elif comparative_difficult2 > comparative_difficult1:
          print(f"{difficult_champ2} is more difficult than {difficult_champ1}") # print the more difficult.
     
            

def exit_option():#Exit option, when the user finished.
     print("Thank you for your time, I hope you enjoyed League of Legends.")
     print("SEE YOU SOON!")
     exit()   #predefined function what quite the program 









