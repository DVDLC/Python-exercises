
import os
from time import sleep
from random import choice, shuffle

def timeout( time ):
    i = 0
    while i <= time:
        i += 1
        sleep(1)
    return  

def greet_player():

    os.system( 'clear' or 'cls' )

    print( '------------------------' )
    print( '  ¡Juego del ahorcado!  ' )
    print( '------------------------' )

    print( 'Bienvenido al juego del ahorcado, por favor dime tu nombre: ' )

    user_name = input("Your name: ")

    while len( user_name ) <= 1:
        os.system( 'clear' or 'cls' )
        print( 'Name is required' )
        user_name = input("Your name: ")
    
    return user_name


def choice_random_word():
    array_words = [
        'preguntar',
        'cortar', 
        'juicio', 
        'huracan', 
        'util', 
        'muñeca', 
        'pellizco', 
        'caridad', 
        'salvage', 
        'gravitacional', 
        'cifrado'
    ]
    
    shuffle( array_words )

    random_word = list( choice( array_words ) )
    blank_word = [ '-' for word in random_word ]
    

    return { 
        'random_word': random_word, 
        'blanks': blank_word
    }


def hangman_logic( random_word, blanks ):

    user_counter = 10

    while "".join( random_word ) != "".join( blanks ) and user_counter > 0:

        print( f"{' '.join(blanks) } \n "  )
        user_word = input( 'Escoge una letra: ' )
        while not user_word or len(user_word) > 1:
            os.system( 'clear' or 'cls' )
            user_word = input( 'Escoge una letra: \n' )
        
        for idx in range( len(random_word) ):

            if user_word == random_word[idx]:
                blanks[ idx ] = user_word 
                
        user_counter -= 1

        input( "Continar?....[enter]" )
        os.system( 'clear' or 'cls' )

    if "".join( random_word ) == "".join( blanks ):
        return True
    else: 
        return False                


def start_game(  ):

    # Saludar al jugador
    user_name = greet_player()

    # Explicar un poco y generar la palabra random
    print( 
        f'Hola { user_name } '
        'Tengo una palabra en la mente, ' 
        'te mostraré cuantos espacios corresponden por letra\n'
    )
    
    # Selección de palabra y sus espacion en blanco
    cpu_choice  = choice_random_word()

    random_word = cpu_choice['random_word']
    blanks      = cpu_choice['blanks']

    # Dar un tiempo para experiencia de usuario e imprimir los espacion en blanco
    timeout( 2 )

    game = hangman_logic( random_word, blanks )

    if game == True:
        print( f"!Genial¡, lo has logrado. La palabrá era: { ''.join( random_word ) }" )
    else:
        print( f"Has perdido, vuelve a intentarlo La palabrá era: { ''.join( random_word ) }" )

    return 


def main():
    start_game()

main()





