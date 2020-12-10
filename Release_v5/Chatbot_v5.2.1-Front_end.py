# link

# Import
import os
import random
import datetime
import calendar
import webbrowser
import Chatbot_Directory
from time import sleep
from datetime import date

# Clear Console
os.system('cls')

# .low statements
low_greetings = [x.lower() for x in Chatbot_Directory.greetings]
low_questions = [x.lower() for x in Chatbot_Directory.questions]
low_response = [x.lower() for x in Chatbot_Directory.response]
low_General = [x.lower()for x in Chatbot_Directory.General]
low_q1 = [x.lower() for x in Chatbot_Directory.q1]
low_a1 = [x.lower() for x in Chatbot_Directory.a1]
low_q2 = [x.lower() for x in Chatbot_Directory.q2]
low_a2 = [x.lower() for x in Chatbot_Directory.a2]
low_q3 = [x.lower() for x in Chatbot_Directory.q3]
low_a3 = [x.lower() for x in Chatbot_Directory.a3]
low_q4 = [x.lower() for x in Chatbot_Directory.q4]
low_a4 = [x.lower() for x in Chatbot_Directory.a4]
low_q5 = [x.lower() for x in Chatbot_Directory.q5]
low_q6 = [x.lower() for x in Chatbot_Directory.q6]
low_google = [x.lower() for x in Chatbot_Directory.google]
low_wiki = [x.lower() for x in Chatbot_Directory.wiki]
low_comments_q = [x.lower() for x in Chatbot_Directory.comments_q]
low_comments_a = [x.lower() for x in Chatbot_Directory.comments_a]
low_hangforsec = [x.lower() for x in Chatbot_Directory.hangforsec]
low_version = [x.lower() for x in Chatbot_Directory.version]
low_blank = [x.lower() for x in Chatbot_Directory.blank]
low_hastebin = [x.lower() for x in Chatbot_Directory.hastebin]
low_song = [x.lower() for x in Chatbot_Directory.song]
low_es1 = [x.lower() for x in Chatbot_Directory.es1]
low_er1 = [x.lower() for x in Chatbot_Directory.er1]
low_es2 = [x.lower() for x in Chatbot_Directory.es2]
low_calculator = [x.lower() for x in Chatbot_Directory.calculator]
low_rand_char = [x.lower() for x in Chatbot_Directory.rand_char]
low_cal = [x.lower() for x in Chatbot_Directory.cal]
low_clear = [x.lower() for x in Chatbot_Directory.clear]
low_rand_num = [x.lower() for x in Chatbot_Directory.rand_num]
low_say = [x.lower() for x in Chatbot_Directory.say]
low_var_quit = [x.lower() for x in Chatbot_Directory.var_quit]

# output display
run = True
while run:
    userInput = input(">>> ")
    low_userInput = userInput.lower()
    if low_userInput in low_greetings:
        random_greetings = random.choice(low_greetings)
        print(random_greetings)
    elif low_userInput in low_questions:
        random_response = random.choice(low_response)
        print(random_response)
    elif low_userInput in low_General:
        print('I am a basic Chatbot with a hard coded directory...')
    elif low_userInput in low_q1:
        random_a1 = random.choice(low_a1)
        print(random_a1)
    elif low_userInput in low_q2:
        random_a2 = random.choice(low_a2)
        print(random_a2)
    elif low_userInput in low_q3:
        random_a3 = random.choice(low_a3)
        print(random_a3)
    elif low_userInput in low_q4:
        random_a4 = random.choice(low_a4)
        print(random_a4)
    elif low_userInput in low_q5:
        today = date.today()
        print("Today's date is", today)
    elif low_userInput in low_q6:
        e = datetime.datetime.now()
        print(e.strftime("%H:%M:%S"))
    elif low_userInput in low_comments_q:
        random_comments_a = random.choice(low_comments_a)
        print(random_comments_a)
    elif low_userInput in low_google:
        print('Google.com')
        webbrowser.open_new('https://www.google.com/')
    elif low_userInput in low_wiki:
        print('Opening Wiki')
        webbrowser.open_new('https://www.wikipedia.org/')
    elif low_userInput in low_hangforsec:
        wait = int(input('Enter timer duration in seconds: '))
        sleep(wait)
        print('')
        print('Time Up!')
    elif low_userInput in low_version:
        webbrowser.open_new(
            'https://paste.pythondiscord.com/iqagetomip.shell')
    elif low_userInput in low_blank:
        today = date.today()
        Time = datetime.datetime.now()
        print("Date:", today)
        print(Time.strftime('Time: '+"%H:%M:%S"))
    elif low_userInput in low_hastebin:
        print('Opening Hastebin')
        webbrowser.open_new('https://hastebin.com/')
    elif low_userInput in low_es1:
        random_er1 = random.choice(low_er1)
        print(random_er1)
    elif low_userInput in low_song:
        def songs():
            print('Select song:')
            print('')
            print('1. Where no one goes - Httyd')
            print('2. Flying theme      - Httyd')
            print('3. Let it go         - Frozen')
            print('4. Into the unknown  - Forzen 2')
            print('5. Show your self    - Frozen 2')
            choice_of_song = int(input('Song number: '))
            if choice_of_song == 1:
                webbrowser.open_new(
                    'https://www.youtube.com/watch?v=BM8gC3Oj0OA')
            elif choice_of_song == 2:
                webbrowser.open_new(
                    'https://www.youtube.com/watch?v=SuX1SXRzQy4')
            elif choice_of_song == 3:
                webbrowser.open_new(
                    'https://www.youtube.com/watch?v=L0MK7qz13bU')
            elif choice_of_song == 4:
                webbrowser.open_new(
                    'https://www.youtube.com/watch?v=gIOyB9ZXn8s')
            elif choice_of_song == 5:
                webbrowser.open_new(
                    'https://www.youtube.com/watch?v=nrZxwPwmgrw')
        songs()
    elif low_userInput in low_es2:
        random_ending_response2 = random.choice(low_es2)
        print(random_ending_response2)
    elif userInput in low_var_quit:
        print('Terminating Programme')
        run = False
    elif userInput in low_say:
        run_say = True
        while run_say:
            sayinput = input('> ')
            var_say = sayinput

            if sayinput == 'quit':
                run_say = False
            else:
                print(var_say)
    elif low_userInput in low_calculator:
        num1 = float(input('number 1: '))
        num2 = float(input('number 2: '))

        def calc():
            print('Select Operation:')
            print('Add')
            print('Subtract')
            print('Multiply')
            print('Divide')
            print('')
            operator = str(input('Select operations from above: '))
            calculator_run = True
            while calculator_run:
                if operator == 'Add':
                    print(num1 + num2)
                    break
                elif operator == 'Subtract':
                    print(num1 - num2)
                    break
                elif operator == 'Multiply':
                    print(num1 * num2)
                    break
                elif operator == 'Devide':
                    print(num1 / num2)
                    break
                elif operator in low_var_quit:
                    calculator_run = False
        calc()
    elif low_userInput in low_rand_char:
        b = random.randint(1, 26)
        print(Chatbot_Directory.char[b])
    elif low_userInput in low_cal:
        dt = datetime.datetime.today()
        yy = dt.year
        mm = dt.month
        print(calendar.month(yy, mm))
    elif low_userInput in low_clear:
        def clear():
            return os.system('cls')
        clear()
    elif low_userInput == '22521':
        print('Launch code is correct!')
        print('Launching Code')
        print('')
        print('Terminating Programme...')
        os.startfile('C:\Program Files\Microsoft VS Code\Code.exe')
    elif userInput == 'Game-dev':
        os.system('python v5\gameDev.py')
    elif userInput in low_rand_num:
        n = str(random.randint(0, 100))
        print('Here is your random number between 0 and 100: ' + n)
    elif userInput in 'virus':
        print(
            "oh no! the corona virus has infected me and it is getting in my 1`s and 0`s")
    else:
        print('I did not understand what you said')
