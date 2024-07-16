#CHATBOT TESTING 29/11/23
# updated --> removed random text, started calculator, added "shutdown" and "quit" to pc.
#UPDATE 12/12/23
# beginning working calculator, plan to add some apps.
#20/12/23 - UPDATE
#added wordle, needs more words
# plan to add quiz + other games
# maybe add games section?
# random game support perhaps
#16/07/24 - UPDATE
# Began work on roshambo improvement, will take ~a day
import time
import random
import sys
clear = ('\n'*40)
whileloop=1
print(clear)
print(clear)
print("Logging in. What is your username?")
username = input("")
if username == 'OfficialBaconMan':
    print("And what is your password?")
    password = input()
    if password == '020809':
        print("Welcome!")
    else:
        print("Wrong password. Reopen to try again.")
        sys.exit()
elif username == 'kapa888':
    print("And what is your password?")
    password = input()
    if password == '2020':
        print("Welcome!")
    else:
        print("Wrong password. Reopen to try again.")
        sys.exit()    
elif username == 'phenom':
    print("And what is your passsword?")
    password=input()
    if password =='wwww':
        print("Welcome!")
    else:
        print("Wrong password. Reopen to try again.")
        sys.exit()
elif username == 'skip' or username == 's' or username == 'w':
    whileloop=3

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
while total_loop == 1:
    time.sleep(3)
    print(clear)
    print(clear)
    time.sleep(1)
    print("What app would you like to use?")
    time.sleep(1)
    print("\n CHATBOT \n\n CALCULATOR \n\n ROSHAMBO \n\n WORDLE \n\n SHUTDOWN")
    uinput = input("Choice Goes Here - ")
    uinput = uinput.lower()
    if uinput == 'CHATBOT' or uinput == 'Chatbot' or uinput == 'chatbot':
        print("Of Course! Entering CHATBOT Now!")
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

        agree = ['BOT: oh cool!',
                 'BOT: oh sick!!',
                 'BOT: really? wow.',
                 'BOT: amazing. just amazing.']
        
        roast = ['BOT: roast? i can do that. you look more american than george washington.',
                 'BOT: roast? yeah, sure. roasted, but unlike your cooking, it wont be charred black.',]
        
        disagree = ['BOT: oh',
                    'BOT: um. ok.]

        festive = ['BOT: MERRY CHRISTMAS!!!',
                   'BOT: WOOOHOOOOO ITS CRIMUH'
                   'BOT: Merry crisis!'
                   'BOT: Happy crismuh'
                   'BOT: Its chrysler']
        #chatbots make no sense :sob:
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
        while calculation == 0:
            number1=float(input('Enter first number -  '))
            op = input("Enter operator (+,-,*,/,^) -  ")
            number2 = float(input("Enter second number -  "))
            print(number1,op,number2)
            result = calculate(number1,number2,op)
            print("=",result)
            print("Calculate again?")
            calculation = int(input("1 For no, 0 For yes"))

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
              print("You guessed the words correctly! WIN 🕺🕺🕺 ")
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
            print("play again?")
            redo = input("Y/N -  ")
            redo = redo.lower()
            if redo == 'y' or redo == 'yes':
                print("OK!")
                check_word()
            else:
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
        


    elif uinput == 'shutdown':
        time.sleep(1)
        print("Goodbye!")
        time.sleep(3)
        print(clear)
        print(clear)
        total_loop=0
        sys.exit()
