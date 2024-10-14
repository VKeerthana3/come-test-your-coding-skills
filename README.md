Come Test Your Coding Skills!

This application is called Come Test Your Coding Skills! It is a command-line application and game developed in Python. It is a coding-theme game which is designed to help users, especially beginners improve their coding skills. This application makes use of Open AI API’s GPT-3.5 model and sqlite3 database to store information the username, password, as well as the score of the user.

It consists of four python modules, final.py, question_generator.py, solution_generator.py, and solution_comparison.py. The github repo also contains the text file where the user can enter their code for the coding exercise, and sqlite database file created for the application.

ARCHITCTURE DIAGRAM image

The user will be first prompted to either signup or login. Next, the user will be asked to choose one among three topics that they would wish to practice their coding skills in, Variables, Loops and Branches, and Functions. Next, it prompts the user to choose two kinds of questions they would like to test their skills in. Short answer programs will provide the user with a code and ask for the output. Coding exercise presents the user with a prompt asking them to write the code.

FINAL.py – This file contains the code for authentication and has the main function. It also contains the code necessary for database connection. Once the user has been successfully authenticated, the other three modules will be called.

QUESTION GENERATOR.py - The question_generator.py file contains the code required to generate the question for the user. It contains the six prompts used to generate the question for the user for each type of question within all three topic choices. Sample examples of questions are given to the model to give it an idea of questions to generate. It is also provided with instructions as to how it should present the question to the user. For short answer questions, I have mentioned that it should generate the question such that user can type the answer in one line as writing multiple lines on terminal without terminating the program is tricky.

SOLUTION_GENERATOR.py - The solution_generator.py file contains the prompt needed for the model to generate the solution for both types of questions. In order to achieve this, the question generated by the prompt from the question_generator is fed into the prompt for the solution_generator. In addition to this, we also provide the models with examples as done earlier along with a few instructions to explicitly tell it to generate the required content.

SOLUTION_COMPARISON.py - The solution_comparison.py file contains the prompt needed to compare the user’s solution to that generated by the model. For this purpose, the solution generated by the model using the solution generator will be fed into the prompt. Also, the user’s answer will also be passed to the prompt. Moreover, the prompt will instruct the model to check if the two snippets of code or output values provided earlier both perform the same functionality and check if they both utilise the same variable names. If the answer is correct, the user’s score will be updated in the database. Otherwise, the user will be prompted to either quit the game or play again.

CHALLENGES One of the challenges of this application is designing the prompts to instruct the model explicitly what content had to be generated. A deeper insight to the code shows that instructions also were provided to instruct the model of what should not be generated too. For instance, the prompt for the question generator specifies the model not to generate hints, clues, or steps to write the code.

LIMITATIONS One of the limitations of this application is that it solely relies on AI to generate all the content and in some cases, although not quite often, it could provide wrong answers or judgements. This can be mitigated by having a human being manually check the user’s solution or by using an IDE to further validate the answer. Another limitation is that since the examples provided in the prompts used for the question_generator are quite simple, it presents simple questions to the user too.

FUTURE WORK It can be enhanced by converting it to a web application. It can also be improved by refining the prompts and providing it with either examples of question with various difficulty levels or by providing it with precise prompts instructing it about the difficulty level of the questions that are to be generated. Moreover, it can be enhanced by making it generate test input and output values along with the coding exercise question and prompting it to check whether the user’s code will run successfully against those values too.

COMPILE / RUN: Please make sure you provide your API key in the space provided in the question_generator.py, solution_generator.py, and solution_comparison.py files. Next, run the command: python3 final.py to run the application from Linux. To check the database value, enter the following commands: sqlite3 my3.db select * from users2;
