

 
# 1. ATM Pin Code Attempt System
# - User has 3 chances to enter the correct 4-digit ATM pin.
# - If the pin is correct, show "Welcome!"
# - If wrong 3 times, show "Card Blocked!"


pin=1234
userAttempt=3

while userAttempt>0:
    userPin=int(input('enter your pin:'))
    if userPin==pin:
        
        print('Welcome')
        break
    else:
        userAttempt=userAttempt-1
        print('Card Blocked')


# 2. FizzBuzz (Modified)
# - Loop through numbers from 1 to 50.
# - Print:
#   - "Fizz" if number divisible by 3
#   - "Buzz" if number divisible by 5
#   - "FizzBuzz" if divisible by both 3 and 5
#   - Else just print the number itself.


for numbers in range(1,51):
    if(numbers%3==0 and numbers%5==0 ):
        print('FizzBuzz')
    elif(numbers%3==0):
        print('Fizz')
    elif(numbers%5==0):
        print('Buzz')
    else:
        print(numbers)


# 3. Voting System for 5 People
# - Ask 5 users their age.
# - If age >= 18, print "Eligible to Vote"
# - Else print "Not Eligible"
# - After all users, print how many were eligible.



for i in range(5):
    userAge=int(input('enter your age:'))
    if userAge>=18:
        print('Eligible to Vote')
    else:
        print('Not Eligible')



# 4. Guess the Secret Code
# - There’s a secret number (like 7).
# - Give the user 5 chances to guess it.
# - After each wrong guess, tell:
#   - "Too High" if guess is bigger.
#   - "Too Low" if guess is smaller.
# - If they guess right, stop the game and show "You found the secret code!"




secretNumber=7
userAttempt=5

while userAttempt>0:
    userGuess=int(input('enter your guess:'))
    if userGuess==secretNumber:
        print('You found the secret code!')
        break
    elif userGuess>secretNumber:
        print('Too High')
    else:
        print('Too Low')
    userAttempt=userAttempt-1


# 5. Traffic Light Simulation
# - Loop 3 times, ask user to input a traffic light color (red, yellow, green).
# - Based on input:
#   - Red → "Stop"
#   - Yellow → "Slow down"
#   - Green → "Go"
#   - Anything else → "Invalid color!"


for i in range(3):
    trafficLight=input('enter traffic light color')
    if trafficLight=='red':
        print('Stop')
    elif trafficLight=='yellow':
        print('Slow down')
    elif trafficLight=='green':
        print('Go')
    else:
        print('Invalid color!')


