
user_input = input( 'Escribe una frase, palabra o poema: \n' ).lower()
words_to_search = input( '3 palabras que quieres buscar separador por comas: ' ).lower().split(',')
count_words = []


is_python_in_user_input = 'python' in user_input


for word in words_to_search:
    count_words.append({ word: user_input.count( word ) })

print( 'El largo de la frase es de: ' + str(len( user_input )) )
print( 'Primera letra: ' + user_input[0],
       'Ultima letra: ' + user_input[-1] )
print( 'Tu frase en orden inverso es: ' + user_input[::-1] )
print( 'Las palabras que elejiste aparecen un total de: ' + str(count_words))

if( is_python_in_user_input != False ):
    print('Python es una palabra que aparece en tu input 🐍')
else:
    pass
