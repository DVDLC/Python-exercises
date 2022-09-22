import os

class Employee:
    def __init__(self, name, sells):
        self.name = name
        self.sells = float(sells)
        self.commission_percentage = 13

    def get_commissions(self):
        result = round(
            (self.sells * self.commission_percentage) / 100,
            2
        )
        return result

os.system("clear")
print("--- Calculador de comisiones ---")

name = input('Ingresa tu nombre para hacer la busqueda en la db: ')
print(f'Bienvenido de nuevo {name} \n')
sells = input('Ingresa el total en pesos de las ventas realizadas esta semana: ')

employee = Employee(name, sells)
print(f'Tu total de comisiones: ${ employee.get_commissions() } MXN')