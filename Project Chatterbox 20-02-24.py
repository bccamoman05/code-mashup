#CHATBOT TESTING 29/11/23
# updated --> removed random text, started calculator, added "shutdown" and "quit" to pc.
#UPDATE 12/12/23
# beginning working calculator, plan to add some apps.
#20/12/23 - UPDATE
#added wordle, needs more words
# plan to add quiz + other games
# maybe add games section?
# random game support perhaps
#10/07/24 - Working on chatbot. Might attempt to utilise OpenAI to make it better.
#Also working on quiz section a little bit, as well as polishing up the login system with file handling, files will be in the onedrive/folder.
#FILES DO NOT WORK /!\ /!\ Will fix later as i do NOT have the mental capacity to handle it rn
# 10/12/24
# FIXED USERNAMES! Password fix coming soon
# really need to import chatbot stuffff

import time
import random 
import sys

clear = '\n' * 30
passAddress = 0
names = []
whileloop = 0
adminAccounts = ['OfficialBaconMan','BlakeMay','WilliamBri','SophiaMil']
operators = ['+','-','*','/','^']
print(clear)
print(clear)
print("Welcome!")
print("Select an option:\n1. Login\n2. Create New Account")
option = input("Enter 1 or 2: ").strip()

if option == "1":
    print("Logging in. What is your username?")
    
    while True:
        username = input("").strip()

        if username == "null":
            print("Username input was 'null'. Exiting.")
            exit()

        #opens file in context (SO SIGMA IK!!)
        with open("usernames.txt", "r") as f:
            names = [line.strip() for line in f]

        if username in names:
            passAddress = names.index(username)
            break
        else:
            print('Username not found. Please try again, or enter "null" to exit.')

    print(username + ", what is your password?")
    
    #pass test, 5 tries
    tries = 0
    while tries < 5:
        password = input("").strip()

        if password == "null":
          
            print("Goodbye!")
            exit()

        with open('passwords.txt', 'r') as passwordFile:
            passwords = [line.strip() for line in passwordFile]

        if passAddress < len(passwords):
            if password == passwords[passAddress]:
                print("Login successful!")
                break
            else:
                tries += 1
                print(f"Incorrect password. You have {5 - tries} attempts left.")
        else:
            print("Error: Password file does not match usernames.")
            exit()

    if tries == 5:
        print("Too many incorrect password attempts. Exiting.")
        exit()

elif option == "2":
    print("Creating a new account. Enter your desired username:")
    new_username = input("").strip()

    with open("usernames.txt", "r+") as f:
        names = [line.strip() for line in f]
        if "null" in names:
            names.remove("null")
        if new_username in names:
            print("Username already exists. Please choose a different one.")
            exit()
        names.append(new_username)
        f.seek(0)
        f.writelines(name + "\n" for name in names)

    print("Enter your desired password:")
    new_password = input("").strip()

    with open("passwords.txt", "r+") as pf:
        passwords = [line.strip() for line in pf]
        if "null" in passwords:
            passwords.remove("null")
        passwords.append(new_password)
        pf.seek(0)
        pf.writelines(password + "\n" for password in passwords)

    print("Account created successfully! You can now log in.")
    username = new_username
else:
    print("Invalid option. Please restart.")
    exit()


time.sleep(.5)
print("Logging in.")
time.sleep(1)
print("Logging in..")
time.sleep(1)
print("Logging in...")
while whileloop <3:
    time.sleep(1)
    print("Logging in.")
    time.sleep(1)
    print("Logging in..")
    time.sleep(1)
    print("Logging in...")
    whileloop = whileloop + 1
time.sleep(.5)
print("Welcome,",username)
total_loop = 1
if username in adminAccounts:
  print("ADMIN ACCOUNT")
  isAdmin = True
else:
    isAdmin = False
while total_loop == 1:
    time.sleep(3)
    print(clear)
    print(clear)
    time.sleep(1)
    print("What app would you like to use?")
    time.sleep(1)
    if isAdmin == False:
        print("\n CHATBOT \n\n CALCULATOR \n\n ROSHAMBO \n\n WORDLE \n\n QUIZ \n\n SHUTDOWN\n")
    else:
        print("\n CHATBOT \n\n CALCULATOR \n\n ROSHAMBO \n\n WORDLE \n\n QUIZ \n\n DELETE AN ACCOUNT \n\n SHUTDOWN\n")
    uinput = input("Choice Goes Here - ")
    uinput = uinput.lower()
    if uinput == 'CHATBOT' or uinput == 'Chatbot' or uinput == 'chatbot':
        print("Of Course! Entering CHATBOT Now!")
        randFeeling = random.randint(1,6)

        #RESPONSE SECTION
        
        greetings = ['BOT: Hey! Welcome in!',
                     'BOT: how you doing?',
                     'BOT: whatsup man!!!',
                     'BOT: ayup mate',
                     'BOT: whats poppin mannn']
        
        confused = ['BOT: Sorry?',
                    'BOT: huh???',
                    'BOT: not sure i understand...',
                    'BOT: huh wuh what',
                    'BOT: what do you mean???',
                    'BOT: what does that mean']
        
        british = ['BOT: ayup mate, howzit',
                   'BOT: ay styll fam innit',
                   'BOT: mate... you aint from croydon, are yas?']

        polish = ['BOT: hej man!',
                  'BOT: what you say man? ey scroow you man!!!',
                  'BOT: Oh, youre polish, are you?']
        
        feelings = ['BOT: im alright thanks!',
                    'BOT: honestly, im not that good. but thanks.',
                    'BOT: quite honestly, im really. REALLY. mad.',
                    'BOT: i feel quite gross rn. idk why.',
                    'BOT: im proper silly today!! :P',
                    'BOT: yeah im quite joyous today.']

        agree = ['BOT: oh cool!',
                 'BOT: oh sick!!',
                 'BOT: really? wow.',
                 'BOT: amazing. just amazing.']
        
        roast = ['BOT: roast? i can do that. you look more american than george washington.',
                 'BOT: roast? yeah, sure. roasted, but unlike your cooking, it wont be charred black.',]
        
        disagree = ['BOT: oh! thats not...',
                    'BOT: um. ok.']

        festive = ['BOT: MERRY CHRISTMAS!!!',
                   'BOT: WOOOHOOOOO ITS CRIMUH'
                   'BOT: Merry crisis!'
                   'BOT: Happy crismuh'
                   'BOT: Its chrysler']
        #chatbots make no sense :sob:

        #actually talking to it, what itll say to you

        time.sleep(1)
        print(clear)
        print(clear)
        time.sleep(3)
        print("BOT: Hey! Welcome to my chatroom! I am [BOT #47]. Type [QUIT] to leave!")
        lopsided=1
        while lopsided== 1:
            chatting = input("USER: ")
            chatting = chatting.lower()
            if "hey" in chatting or "hello" in chatting or "hi" in chatting:
                respond = random.choice(greetings)
                print(respond)
            elif "how are you" in chatting or "hows it going" in chatting:
                respond = feelings[randFeeling-1]
                print(respond)
            elif "ayup" in chatting:
                respond = random.choice(british)
                print(respond)
            elif "hej" in chatting:
                respond = random.choice(polish)
                print(respond)
            elif "yes" in chatting or "yeah" in chatting:
                respond = random.choice(agree)
                print(respond)
            elif "no" in chatting or "nah" in chatting:
                respond = random.choice(disagree)
                print(respond)
            elif "roast" in chatting:
                respond = random.choice(roast)
                print(respond)
            elif 'christmas' in chatting or 'festive' in chatting:
                respond = random.choice(festive)
                print(respond)
            elif chatting == 'quit':
                print("BOT: Oh, goodbye then!")
                lopsided = 0
            else:
                respond = random.choice(confused)
                print(respond)
    elif uinput == 'roshambo':
        print("Of course! Entering ROSHAMBO now!")
        time.sleep(1)
        print(clear)
        print(clear)
        time.sleep(3)
        print("ROSHAMBO MASTER: Welcome... To ROSHAMBO!")
        time.sleep(1)
        looperino = 1
        while looperino == 1:
            print("ROSHAMBO MASTER: Lets. Play. I've made my choice.")
            ai = random.randint(1,3)
            time.sleep(1)
            print("ROSHAMBO MASTER: What will you pick?")
            time.sleep(1)
            print('1 - Rock || 2 - Paper || 3 - Scissors')
            choice = int(input())
            time.sleep(1)
            print("ROSHAMBO MASTER: May the best player win.")
            time.sleep(1)
            print("ROSHAMBO MASTER: RO")
            time.sleep(1)
            print("ROSHAMBO MASTER: SHAM")
            time.sleep(1)
            print("ROSHAMBO MASTER: BO")
            time.sleep(0.5)
            if ai == choice:
                print("ROSHAMBO MASTER: It appears we have tied.")
            elif ai == 1 and choice == 2 or ai == 2 and choice == 3 or ai == 3 and choice == 1:
                print("ROSHAMBO MASTER: No...")
                time.sleep(1)
                print("ROSHAMBO MASTER: I have lost...")
                time.sleep(1)
            else:
                print("ROSHAMBO MASTER: YES! I AM VICTORIOUS!")
                time.sleep(1)
                print("ROSHAMBO MASTER: You will never defeat me...")
                time.sleep(1)
            print("Play again?")
            choice = input('Y/N - ')
            if choice == 'N' or choice == 'n':
                print("Goodbye!")
                looperino = 0
            else:
                print("Great choice!")
    elif uinput == 'calculator':
        print("Of course! Entering CALCULATOR now!")
        time.sleep(1)
        print(clear)
        print(clear)
        time.sleep(3)
        print("Welcome to calculator!")
        def calculate(n1,n2,op):
            if op not in operators:
                print("Not a valid operator.")
                result = "Failed Operation"
            if op == '+':
                result = n1+n2
            elif op == '-':
                result = n1-n2
            elif op == '*':
                result = n1*n2
            elif op == '/':
                result=n1/n2
            elif op == '^':
                result = n1**n2

            return result
        calculation = 0
        while calculation == 0:
            number1=float(input('Enter first number -  '))
            op = input("Enter operator (+,-,*,/,^) -  ")
            number2 = float(input("Enter second number -  "))
            print(number1,op,number2)
            result = calculate(number1,number2,op)
            print("=",result)
            print("Calculate again?")
            calculation = int(input("1 For no, 0 For yes - "))

    elif uinput == 'wordle':
        time.sleep(1)
        print("Entering Wordle Now!")
        time.sleep(3)
        print(clear)
        print(clear)
        wordle = 1
        def game_instruction():
            print("""Wordle is a single player game 
        A player has to guess a five letter hidden word 
        You have six attempts 
        Your Progress Guide "✔❌❌✔➕"  
        "✔" Indicates that the letter at that position was guessed correctly 
        "➕" indicates that the letter at that position is in the hidden word, but in a different position 
        "❌" indicates that the letter at that position is wrong, and isn't in the hidden word   """)

        words = ["wound","curve","first","peace","chain","stuff","sheep","chief","spray","admit","bowel","creed","pupil","ridge","voter","clear","shoot","party","eagle","peace","snail"]
        game_instruction()

        def check_word():
          hidden_word = random.choice(words)
          attempt = 6
          while attempt > 0:
            guess = str(input("Guess the word: "))
            if guess == hidden_word:
              print("You guessed the word correctly! You Win!")
              break
            else:
              attempt = attempt - 1
              print(f"you have {attempt} attempt(s) ,, \n ")
              for char, word in zip(hidden_word, guess):
                    if word in hidden_word and word in char:
                        print(word + " ✔ ")

                    elif word in hidden_word:
                        print(word + " ➕ ")
                    else:
                        print(" ❌ ")
              if attempt == 0:
                print(" Game over !!!! ")
                print("The word was",hidden_word,"!")

        check_word()
        while wordle == 1:
            redo = ''
            while redo not in ['yes','y','no','n']:
                print("play again?")
                redo = input("Y/N -  ")
                redo = redo.lower()
                if redo == 'y' or redo == 'yes':
                    print("OK!")
                    check_word()
                elif redo == 'n' or redo == 'no':
                    wordle = 0
                    print("Goodbye!")


                
    elif uinput == 'quiz':
        time.sleep(1)
        print("Of course! Entering QUIZ now!")
        time.sleep(1)
        print(clear)
        time.sleep(1)
        print("GAMEMASTER: Ladies and gentlemen,")
        time.sleep(2)
        print("GAMEMASTER: Boys and girls...")
        time.sleep(2)
        print("GAMEMASTER: WELCOME! To TRIVIA TRACK!")
        time.sleep(2)
        print("GAMEMASTER: The funtastic, gameshow for the whole family!")
        time.sleep(2)
    
        quiz_type = input("Choose quiz type (multiple_choice, true_or_false, fill_in_the_blanks): ").lower()
        
        if quiz_type == "multiple_choice":
            question = "What is the capital of France?"
            print(question)
            print("A) Paris", "B) London", "C) Berlin", "D) Madrid")
            user_answer = input("Your answer: ").upper()
            if user_answer == "A":
                print("Correct!")
            else:
                print("Wrong! The correct answer is A")

        elif quiz_type == "true_or_false":
            question = "The Earth is flat. (True/False)"
            print(question)
            user_answer = input("Your answer: ").capitalize()
            if user_answer == "False":
                print("Correct!")
            else:
                print("Wrong! The correct answer is False")

        elif quiz_type == "fill_in_the_blanks":
            question = "Python was created by ____ Van Rossum."
            print(question)
            user_answer = input("Your answer: ").capitalize()
            if user_answer == "Guido":
                print("Correct!")
            else:
                print("Wrong! The correct answer is Guido")

        else:
            print("Invalid quiz type")
            
    elif uinput in ['delete', 'delete an account', 'delete account'] and isAdmin:
        print("What account do you want to delete?")
        with open("usernames.txt", "r+") as f:
            names = [line.strip() for line in f]
        
        # display usernames
        print(names)
        delInput = ''
        while delInput != "null":
            delInput = input("Enter the account name to delete, enter 'null' to exit: ")
            # is name in list?
            if delInput == "null":
                break
            elif delInput not in names and delInput != 'null':
                print("Not found. Try again.")
            else:
                # get name index
                delAddress = names.index(delInput)
                # delete from names list cuz yea
                names.pop(delAddress)
                # open pass file and get it into a list
                with open("passwords.txt", "r") as g:
                    passwords = [line.strip() for line in g]
                # delete the password JUST FROM THE LIST. NOT the file.
                passwords.pop(delAddress)
                # writing back to files, deleting the accounts basically.
                with open("usernames.txt", "w") as f:
                    for name in names:
                        f.write(name + "\n")
                with open("passwords.txt", "w") as g:
                    for password in passwords:
                        g.write(password + "\n")
                print(f"Account {delInput} was deleted.")
                print(names)
        print("Exiting now...")
    elif uinput == 'shutdown':
        time.sleep(1)
        print("Goodbye!")
        time.sleep(3)
        print(clear)
        print(clear)
        total_loop=0
        sys.exit()