import openai
import sqlite3
from openai import OpenAI
import question_generator
import solution_generator
import solution_comparison

print("Come test your coding skills!") # Displays title of application

username = ""
password=""
score = 0
model = "gpt-3.5-turbo"

my_connection = sqlite3.connect("my3.db") # connects to existing database
cursor_object = my_connection.cursor()

# The commented lines below contain the code to create a new table 

#create_user_table = """CREATE TABLE users2 (username VARCHAR(30), password VARCHAR(30), score INTEGER);"""
#cursor_object.execute(create_user_table);

def authentication():
    global username
    global score    

    user_choice = input("Choose one of the following options: \n 1. Login \n 2. Don't have an account? Sign "
                        "Up \n\n ") 

    if (user_choice == "1"): #Prompts the user to login
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")        

        fetch_user_command = f"""SELECT * FROM users2 WHERE username = {username} AND password = {password};"""
        cursor_object.execute(fetch_user_command);

        user = cursor_object.fetchone()
        
        score = user[2]        

        if user is None:
            print("Invalid login details. Please try again.")
            authentication()

        else:
            score = user[2]
            question_generator.question_generator()
            solution_generator.solution_generator(username, score)
            solution_comparison.solution_comparison(username, score, cursor_object)

    elif(user_choice == "2"): # Prompts the user to sign up
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        print(f"Your username is {username} and password is {password}")

        insert_user_command = f'INSERT INTO users2(username, password, score) VALUES ({username}, {password}, 0);'
        cursor_object.execute(insert_user_command)
        my_connection.commit()

        score = 0

        question_generator.question_generator()
        solution_generator.solution_generator(username, score)
        solution_comparison.solution_comparison(username, score, cursor_object)
        
    
    else: # This condition is true if the user enters an invalid option
        user_choice = input("Invalid choice. Choose one of the following options: \n 1. Login \n 2. Sign Up \n ")
          

def main():
    authentication()


if __name__ == "__main__":
    main()    
