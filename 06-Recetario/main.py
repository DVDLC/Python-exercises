import os
from pathlib import Path
from unicodedata import category

# GLOBAL HELPERS
MY_RECIPE_PATH = Path( 'Recipe book' )

def greet_player():

    os.system( 'clear' or 'cls' )

    print( '-------------------------------' )
    print( '  ¡Bienvenido a tu recetario!  ' )
    print( '-------------------------------' )

    print( 'Por favor dime tu nombre: ' )

    user_name = input("Your name: ")

    while len( user_name ) <= 1:
        os.system( 'clear' or 'cls' )
        print( 'Name is required' )
        user_name = input("Your name: ")
    
    return user_name

# Función que crea "Recipe book sino existe"
def recipe_book():
    if os.path.exists( MY_RECIPE_PATH ) == False:
        os.mkdir( MY_RECIPE_PATH )
        return
    return

# Funcion para validar dirs y archivos
def valid_dirs_and_files( category = '' ):

    # Declaro mis variables
    idx = 0
    list_to_print = []
    files_list = os.listdir( Path( MY_RECIPE_PATH, category ) )
    is_valid = False

    # Genero una lista que será impresa en consola
    for file in files_list :
        list_to_print.append( f'[{idx}] - {file}' )
        idx += 1

    # Generamos un bucle validando los datos proporcionados por el cliente
    while not is_valid and len( files_list ) > 0:

        os.system('clear' or 'cls')

        try:
            print( 'Elije una opción: \n' )
            for file in list_to_print:
                print( file )

            user_choice = int( input('') )
            
            return files_list[user_choice]
        except ValueError:
            pass
        except IndexError:
            pass

    # Sino existe algun archivo retornamos 
    os.system('clear' or 'cls')
    print( 'No existen archivos, en esta categoria' )
    input( 'Enter para continuar ":D"' )
    return False

# Crear categorias
def create_dir_category( dir_name ):
    try:
        dir_name = dir_name.lower()

        os.mkdir( Path( MY_RECIPE_PATH , dir_name ) )
        print( f'Nuevo recetario creado: { dir_name }' )
        input('Enter para continuar')
        return True
        
    except FileExistsError:
        print( f'Archivo con nombre: { dir_name } es incorrecto o ya existe\n' )
        input('Enter para continuar')
        return False 
    except AttributeError:
        print( 'Nombre invalido, intentalo de nuevo\n' )
        input('Enter para continuar')
        return False

# Crear receta
def create_file_recipe( file_info ):

    dir_name = file_info["dir_name"]
    file_name = file_info["file_name"]
    recipe_desc = file_info["recipe_desc"]

    recipe_dir = Path( MY_RECIPE_PATH, dir_name )
    recipe_file = Path( MY_RECIPE_PATH, dir_name, f'{file_name}.txt' )
    
    if recipe_dir.exists() == True and recipe_file.exists() == False:

        new_recipe_file = open( recipe_file, 'w' )
        new_recipe_file.write( recipe_desc )
        new_recipe_file.close()

        print( 'Archivo creado! Ya puedes leerlo, actualizarlo y/o borrarlo' )
        input('Enter para continuar')
        return True

    else: 
        if recipe_dir.exists() == False:
            os.system('clear' or 'cls')
            print( f'El directorio { dir_name }, no existe' )
            
        elif recipe_file.exists() == True:
            os.system('clear' or 'cls')
            print( f"{ file_name } file, ya existe" )
            
        input('Enter para continuar')
        return False

# CREATE - crear categoria
def create_category():

    category_is_created = False
    while not category_is_created:

        user_input = str( input( 'Que nombre le quieres dar a la categoria: ' ) )
        category_is_created = create_dir_category( user_input )

# CREATE - crear receta
def create_recipe():

    dir_name = valid_dirs_and_files()
    os.system('clear' or 'cls')
    file_name = str( input( 'Nombre del archivo: ' ) )
    os.system('clear' or 'cls')
    recipe_desc = str( input( 'Contenido del archivo:\n' ) )

    user_input = {
        "dir_name"    : dir_name,
        "file_name"   : file_name,
        "recipe_desc" : recipe_desc
    }

    return create_file_recipe( user_input )

# READ - leer receta
def read_recipe():

    cetegory_choice = ''

    cetegory_choice = valid_dirs_and_files()
    file_choice = valid_dirs_and_files( cetegory_choice )

    if file_choice != False: 
        os.system('clear' or 'cls')
        my_recipe_file = open( Path( MY_RECIPE_PATH, cetegory_choice, file_choice ), 'r' )
        print( my_recipe_file.read() )
        my_recipe_file.close()
        input( 'Enter para continuar:' )
    else: 
        return False

# TODO: Esta mal el borrar la categoria y la receta

def delete_category():

    category_to_delete = valid_dirs_and_files()
    complete_path = Path( MY_RECIPE_PATH, category_to_delete )
    user_input = ''

    os.system('clear' or 'cls' )
    print( f'Oh oh.... veo que quieres eliminar: { category_to_delete }'  )
    if len(os.listdir( complete_path )) > 0:
        print( f'Aún tienes archivos importantes en { category_to_delete }' )
    
    print('\n')
    
    while True :
        user_input = str( input( 'Seguro quieres borrarlo [S/N]: ' ) ).lower()
        os.system('clear' or 'cls' )

        if user_input == 's':
            os.rmdir( complete_path )
            print( 'Se ha borrado exitosamente la categoria' )
            break
        elif user_input == 'n':
            print( 'Genial!' )
            break
        else: 
            pass

    return True

def delete_recipe():
    cetegory_choice = ''
    user_input = ''

    cetegory_choice = valid_dirs_and_files()
    file_choice = valid_dirs_and_files( cetegory_choice )

    if file_choice != False: 
        os.system('clear' or 'cls')
        complete_path = Path( MY_RECIPE_PATH, cetegory_choice, file_choice )

        print( f'Oh oh.... veo que quieres eliminar: { file_choice }\n'  )

        while True :
            user_input = str( input( 'Seguro quieres borrarlo [S/N]: ' ) ).lower()
            os.system('clear' or 'cls' )

            if user_input == 's':
                os.remove( complete_path )
                print( 'Se ha borrado exitosamente la receta' )
                break
            elif user_input == 'n':
                print( 'Genial!' )
                break
            else: 
                pass

        input( 'Enter para continuar:' )
        return True
    else: 
        return False

# Función CRUD
def CRUD( user_input ):
    
    match user_input:
        case 'create_recipe':
            if len( os.listdir( MY_RECIPE_PATH ) ) > 0:
                create_recipe()
            else: 
                os.system('clear' or 'cls')
                print( 'Aún no existen categorias' )
                input('Enter para continuar')
                return False
        case 'create_category':
            create_category()
        case 'read':
            if len( os.listdir( MY_RECIPE_PATH ) ) > 0:
                read_recipe()
            else: 
                os.system('clear' or 'cls')
                print( 'Aún no existen recetas' )
                input('Enter para continuar')
                return False
        case 'delete_category':
            delete_category()
        case 'delete_recipe':
            delete_recipe()

# APP
def app():

    app_options = [ 
        '[0] - create_recipe', 
        '[1] - create_category', 
        '[2] - read', 
        '[4] - delete_category', 
        '[5] - delete_recipe',
        '[q] - quit' 
    ]

    # Saludar al cliente
    user_name  = greet_player()
    os.system('clear' or 'cls')
    print( f'Hola, {user_name}' )
    print( "Este es tu recetario acontinuación se creara un archivo" )
    print( "donde estarán registrados todas las categorias y recetas que hagas\n" )
    input( 'Enter para continuar :D' )

    # Crear el recetario sino existe
    recipe_book()

    # Logica del CRUD
    while True:

        os.system('clear' or 'cls')
        print( 'Escoge una opción: \n' )
        for option in app_options:
            print( option ) 
        user_input = input('') 

        if user_input.lower() == 'q':
            os.system('clear' or 'cls')
            print('Gracias por usar nuestros servicio')
            break

        try:
            CRUD( app_options[ int(user_input )].split('-')[1].strip() )
        except IndexError:
            pass
        
# MAIN
def main():
    app()
main()


