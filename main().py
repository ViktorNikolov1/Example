from Functions import * #import everything from "Functions"
def main():
  
  user_selection = '' #  empty string
  title_champion = {}

  while user_selection != '4': #While the ser selection is not the 4th (exit) the programm still asking.
    user_selection= input(" **Select your option: ")

    #Depends of the user selection is executed each function. 
    if user_selection == '1':
      show_names()
    
    elif user_selection == '2':
      name_title()
    
    elif user_selection == "3":
      Lore_champ()
    
    elif user_selection =="4":
      stronger_champ()
    
    elif user_selection == "5":
      exit_option()

welcome()
option()

if __name__ == "__main__":
    main()  # Execute the main() function if the condition is met