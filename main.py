import os
import json
import pprint


class Box:
    def __init__ (self):
        with open('data.json', 'r+') as fp:
            self.inventory = json.load(fp)

    def save(self, data):
        with open('data.json', 'w+') as fp:
            json.dump(data, fp)

    def checkCorrectInputToDecimal(self, inString):
        if '.' in inString:
            aux = int(inString[:inString.find('.')])
            aux += int(inString[inString.find('.')+1:inString.find('.')+2])/10
            inString = aux
        print(type(inString))
        return inString



    def addNew(self, ID):
        self.inventory[ID] = {}
        self.inventory[ID]["name"] = input('Enter product name: ')
        os.system('clear')
        self.inventory[ID]["weight"] = input('Enter product weigth: ')
        os.system('clear')
        self.inventory[ID]["price"] = input('Enter product price: ')
        os.system('clear')
        print('Your product: ')
        pprint.pprint(self.inventory[ID], width=1)
        print('We are done adding the product and description. Good bye!')
        save(self.inventory)

    def removeProduct(self,ID):
        del self.inventory[ID]

    def searchProduct(self, keyword):
        os.system('clear')
        count = 0
        for product in self.inventory.values():
            if keyword in product['product']:
                count += 1 
                print('\n' + str(count))
                print(product['product'])
                print('Precio de venta: '  + str(product['price']))
                if 'unitprice' in product.keys():
                    print('Precio de compra: ' + str(product['unitprice']))
                print('------------------------\n')
        print('\n He encontrado ' + str(count) + ' productos que coinciden con tu busqueda.')

    def addBoxPrice(self, ID):
        if ID in self.inventory.keys():
            os.system('clear')
            self.inventory[ID]['box'] = int(input('Ingresa el precio de la caja: '))
            self.inventory[ID]['ppb'] = int(input('Ingresa el numero de piezas que contiene: '))
            os.system('clear')
            self.inventory[ID]['unitprice'] = self.inventory[ID]['box']/self.inventory[ID]['ppb']
            print('El precio unitario de compra es de : ' + str(self.inventory[ID]['unitprice']))
        else:
            print('Lo siento, el producto no se encuentra en el inventario.')

    def addUnitPrice(self, ID):
        if ID in self.inventory.keys():
            os.system('clear')
            ieps = input('¿El precio incluye I.E.P.S? s/n: ')
            if ieps in ['Y', 'y', 'yes', 'Yes']:
                os.system('clear')
                self.inventory[ID]['unitprice'] = int(input('Ingresa el precio de compra unitario directamente: '))
                self.inventory[ID]['ppb'] = 1
                self.inventory[ID]['box'] = self.inventory['unitprice']
            elif ieps in ['N', 'n', 'No', 'no']:
                os.system('clear')
                unitprice_aux = int(input('Ingresa el precio que aparece en la lista de compra: '))
                ieps = int(input('¿Cual es el valor del I.E.P.S? '))/100
                self.inventory[ID]['unitprice'] = unitprice_aux*(1+ieps)
        else:
            print('Esta operacion solo es aplicable a productos del inventario: el que has ingresado no existe.')

    def actionOverItemFound(self, keyword):
        os.system('clear')
        count = {}
        i = 0
        for ID, product in self.inventory.items():
            if keyword in product['product']:
                i += 1
                count[str(i)] = [ID, product['product']]
        pprint.pprint(count, width=1)
        var = input('Sobre que producto deseas trabajar? ')
        print(count[var])
        option = input('Que accion deseas realizar? \n1- Anadir Precio de caja.\n2- Anadir precio de compra unitario.\n')
        if option == '1':
            self.addBoxPrice(count[var][0])
        elif option == '2':
            self.addUnitPrice(count[var][0])

    def sellProducts(self):
        os.system('clear')
        flag = True
        total = 0
        recipe = {}
        while flag:
            flag2 = True
            while flag2:
                ID = input('Lea el codigo de barras con el lector o manualmente: ')
                if len(ID) in [0, 8, 13]:
                    flag2 = False
                else:
                    print('El codigo no es valido, intente de nuevo. ')
            os.system('clear')
            if ID in self.inventory.keys():
                product = self.inventory[ID]
                total += product['price']
                recipe.setdefault(product['product'], 0)
                recipe[product['product']] += 1
                pprint.pprint(recipe, width=1)
                print('El total actual es de : ' + str(total))
            elif ID not in self.inventory.keys() and ID != '':
                print('El producto no se encuentra en el inventario.')
            elif ID == '':
                flag = False
        pprint.pprint(recipe, width=1)
        print('El total de la compra es de: ' + str(total))
