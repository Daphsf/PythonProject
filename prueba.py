operacion = 0

num1 = 0

num2 = 0




class Calculadora:

    def __init__(self):

        self.resultado = 0

    def Suma(self,num1,num2):

        self.resultado = num1 + num2

    def Resta(self,num1,num2):

        self.resultado = num1 - num2

    def Mult(self,num1,num2):

        self.resultado = num1 * num2

    def Div(self,num1,num2):

        self.resultado = num1 / num2

    def Pot(self,num1,num2):

        self.resultado = num1 ** num2

    def resul(self):

        return self.resultado





class menu:

    def __init__(self):

        self.resul = 0

    def Cal(self,operacion, num1, num2):

        while(operacion != 6):

           

            operacion = int(input("""

            Indique Que operacion desea hacer:

            1. Suma

            2. Resta

            3. Multiplicacion

            4. Division

            5. Potencia

            6. Salir

           

            """))

            if operacion != 6:

               

                if operacion == 1:

                    num1 = int(input("""Indique un número: """))

                    num2 = int(input("""Indique un segundo número: """))

                    Operacion.Suma(num1,num2)

                elif operacion == 2:

                    #valor = int(input("Indique el numero: "))

                    num1 = int(input("""Indique un número: """))

                    num2 = int(input("""Indique un segundo número: """))

                    Operacion.Resta(num1,num2)

                elif operacion == 3:

                    num1 = int(input("""Indique un número: """))

                    num2 = int(input("""Indique un segundo número: """))

                    Operacion.Mult(num1,num2)

                elif operacion == 4:

                    num1 = int(input("""Indique un número: """))

                    num2 = int(input("""Indique un segundo número: """))

                    Operacion.Div(num1,num2)

                elif operacion == 5:

                    num1 = int(input("""Indique un número: """))

                    num2 = int(input("""Indique un segundo número: """))

                    Operacion.Pot(num1,num2)

                print(f"""

--------------------------

El resultado es: {Operacion.resul()}

--------------------------

""")

            else:  

                print("""-------------

Adios

-------------""")




Men = menu()

Operacion = Calculadora()

Men.Cal(operacion, num1, num2)






# while(valor > 0):

#     valor = int(input("Indique el numero: "))

#     Sum.suma(valor)

#     print(Sum.resul())