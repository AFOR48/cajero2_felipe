dinero = float(input("¿Cuanto dinero desea retirar?: "))
print("Su retiro es de: ")
billetes_valor = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]
for n in range(11):
    if billetes_valor[n] <= dinero:
        numero_billetes = dinero//billetes_valor[n]
        residuo = dinero%billetes_valor[n]
        if billetes_valor[n] > 500:
            tipo = " billete"
        else:
            tipo = " moneda"
        if numero_billetes >= 2:
            cantidad = "s"
        else:
            cantidad = ""
        print(str(numero_billetes)+ tipo + cantidad + " de " + str(billetes_valor[n]) + " pesos")
        
    dinero = residuo
print("Muchas gracias por utilizar nuestro servicio.")