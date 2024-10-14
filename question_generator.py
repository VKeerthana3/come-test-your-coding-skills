import openai
import sqlite3
from openai import OpenAI

client = OpenAI(api_key="...") # Please add your API key here.
model = "gpt-3.5-turbo"

username = ""
password=""
score = 0


def question_generator():
    """Generates the question for both types of questions for all three topics and displays it to the user. 
    Contains the necessary prompts instructing the model to generate the required content"""
    global question_type
    global generated_text
    
    topic_choice = input("\n Choose the topic: \n 1. Variables \n 2. Loops & Branches \n 3. Functions \n \n")

    if (topic_choice == "1"):
        question_type = input("\n Choose question type: \n 1. Short aswers \n 2. Coding \n")
        if (question_type == "1"):
            prompt = """
            Given a c++ program, the user will have to write what would be the output of the program. Below are 
            two independent examples. Start the question with, Type the program's output,
            follwed by the c++ program. User should be able to type the solution in one line.

        1. Type the progam's output
        #include <iostream>
        using namespace std;

        int main() {
            int x;
            int y;

            x = 7;
            y = 4;
   
             cout << x << " " << y;

            return 0;
        }

        2. Type the program's output
        #include <iostream>
        using namespace std;

        int main() {
            int x;
            int y;

            y = 10;
            x = y + 5;
   
            cout << x << " " << y;

            return 0;
        }

        For the above examples, I have provided a short prompt of 'Type the program's output' followed by the 
        c++ program. Please generate one question in a similar style as an exercise and present it to 
        the users to test their coding skills. Do not provide example solutions or provide steps to do it. 
        Do not provide questions whose solutions have 'endl'. """
            
        elif(question_type == "2"):
            prompt = """
            Below are two independent examples of prompts for coding exercises. 

            1. Declare an integer variable numBirds initialized to 5.

            2. Given the sideA, sideB, and sideC of a triangle, assign triPerimeter with the perimeter of the 
            triangle.

            For the above examples, I have provided a short prompt. I would like to generate one question in a 
            similar style as an exercise and present it to the users to test their coding skills only in C++. 
            Make sure you explicitly tell the user what the required variable names should be. Do not provide example 
            solutions or provide steps to do it and start your answer with : 'Here is an exercise for you'.
            Do not provide any hints and clues to the solution. Also, make sure not to include how 
            the solution should look like. Make sure to ask the user to generate a c++ program
            for the answer."""

    elif (topic_choice == "2"):
        question_type = input("Please choose which kind of question to practice: \n 1. Short aswers \n "
                              "2. Coding \n")
        if (question_type == "1"):
            prompt = """
            Given a c++ program, the user will have to write what would be the output of the program. Below are 
            two independent examples. Start the questio with, Type the program's output,
            follwed by the c++ program.

        1. Type the program's output
            #include <iostream>
            using namespace std;

            int main() {
                int g;
                g = 0;
                
                while (g <= 1) {
                    cout << g << " ";
                    g = g + 1;
                }
               return 0;
            }

            2. Type the program's output
            #include <iostream>
            using namespace std;

            int main() {
                int i;
   
                for (i = 0; i < 3; ++i) {
                cout << (i * 2);
            }

                return 0;
            }

        For the above examples, I have provided a short prompt of 'Type the program's output' followed by the 
        c++ program. Please generate one question in a similar style as an exercise and present it to 
        the users to test their coding skills. Do not provide example solutions or provide steps to do it. 
         Also, do not provide questions whose solutions have 'endl'. """
            
        elif(question_type == "2"):
            prompt = """
            Below are two independent examples of prompts for coding exercises. 

            1. Given positive integer numInsects, write a while loop that prints, then doubles, numInsects each 
            iteration. Print values < 200. Follow each number with a space.

            2. Integer valCount is read from input representing the number of integers to be read next. Use a 
            loop to read the remaining integers from input into variable value. For each integer from 0 to 
            valCount minus 1, inclusive, output the integer followed by " eagles". 

            For the above examples, I have provided a short prompt. I would like to generate one question in a 
            similar style as an exercise and present it to the users to test their coding skills. Make sure you 
            explicitly tell the user what the required variable names should be. Do not provide example 
            solutions and start your answer with : 'Here is an exercise for you'.
            Do not provide any hints and clues to the solution. Also, make sure not to include how 
            the solution should look like. Make sure to ask the user to generate a c++ program
            for the answer. Do not provide steps to solve the answer."""

    elif (topic_choice == "3"):
        question_type = input("Please choose which kind of question to practice: \n 1. Short aswers \n "
                              "2. Coding \n")
        if (question_type == "1"):
            prompt = """
            Given a c++ program, the user will have to write what would be the output of the program. Below are 
            two independent examples. Start the questio with, Type the program's output,
            follwed by the c++ program.

        1. Type the program's output
        #include <iostream>
        using namespace std;

        int ChangeValue(int x) {
            return x + 3;
        }

        int main() {
            cout << ChangeValue(1) << endl;
   
            return 0;
        }

        2. Type the program's output
            #include <iostream>
            using namespace std;

            int ChangeValues(int x, int y) {
                int result;
                result = x + y;

                return result;
            }

            int main() {
                cout << ChangeValues(4, 2) << endl;
                return 0;
            }

        For the above examples, I have provided a short prompt of 'Type the program's output' followed by the 
        c++ program. Please generate one question in a similar style as an exercise and present it to 
        the users to test their coding skills. Do not provide example solutions or provide steps to do it. 
         Also, do not provide questions whose solutions have 'endl'. """
            
        elif(question_type == "2"):
            prompt = """
            Below are two independent examples of prompts for coding exercises. 

            1. Complete the function definition to return the hours given minutes. 

            2. Define a function CalculateNum() that takes one integer parameter and returns the parameter plus 5. 

            For the above examples, I have provided a short prompt. I would like to generate one different and independent question in a 
            similar style as an exercise and present it to the users to test their coding skills. Make sure you 
            explicitly tell the user what the required variable names should be. Do not provide example 
            solutions or provide steps to do it and start your answer with : 'Here is an exercise for you'.
            Do not provide any hints and clues to the solution. Also, make sure not to include how 
            the solution should look like. Make sure to ask the user to generate a c++ function
            for the answer."""



    response = client.chat.completions.create(model=model, 
                                              messages=[
        {"role": "system", "content": "You are a coding question generator. You carefully come up with simple, yet "
         "good coding exercises for beginner students to help improve their coding skills."},
        {"role": "user", "content": prompt}],         
        temperature=1, max_tokens=250, top_p=1, frequency_penalty=0, presence_penalty=0)

    
    generated_text = response.choices[0].message.content

    print("\n")
    print(generated_text)
