
import os
from random import *

os.system('clear')
print( '-----------------------  ' )
print( '   GUESS THE NUMBER   ' )
print( '-----------------------  \n' )

user_name = str( input( 'What is your name: ' ) )
os.system('clear')

user_response = input( f'Welcome { user_name }, are you ready? [y/n]: \n' ).lower()

while user_response != 'n' and user_response != 'y':
    os.system('clear')
    user_response = input( f'Welcome { user_name }, are you ready? [y/n]: \n' ).lower()


match user_response:
    case 'y':
        os.system('clear')

        user_tries = 8
        user_input = False
        cpu_random = randint( 0, 100 )

        print( "I'm thinking of a number from 1 to 100, do you can tell what it is? " )
        user_input = int(input( "Try it!: " ))
        
        while user_input != cpu_random and user_tries != 1:

            if user_input > cpu_random:
                os.system('clear')
                user_tries -= 1
                user_input = int(input( f"No, your number is bigger. Try again, you have { user_tries } attempts left:  " ))

            elif user_input < cpu_random:
                os.system('clear')
                user_tries -= 1
                user_input = int(input( f"No, your number is lower. Try again, you have { user_tries } attempts left:  " ))

            elif user_input > 100 or user_input < 0:
                os.system('clear')
                user_tries -= 1
                user_input = int(input( f"What are you doing? this is not an accepted number xD, you have { user_tries } attempts left:  " ))

        if user_tries <= 1:
            print( f"Uy I'm sorry, you has lose, you don't have any tries :c. My number: { cpu_random }" )
        elif user_input == cpu_random:
            print( f'Congrats! You did it! My number: { cpu_random } your number: { user_input }' )
        else:
            pass
    
        
    case 'n':
        os.system('clear')
        print( f'See you later {user_name}' )
