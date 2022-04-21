#Variables
a = 0
b = 0

resultado = 0

a = int(input("Indica el valor de \"a\": "))
b = int(input("Indica el valor de \"b\": "))

operador = input("Indica el operador (+ - * /): ")

if(operador == "+"):
    resultado = a + b
elif(operador == "-"):
    resultado = a - b
elif(operador == "*"):
    resultado = a * b
elif(operador == "/"):
    resultado = a / b

print("El resultado es: {}".format(resultado))

