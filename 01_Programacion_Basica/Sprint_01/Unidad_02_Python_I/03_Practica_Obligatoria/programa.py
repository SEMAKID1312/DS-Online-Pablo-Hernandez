precio_fam = 8.95
precio_med = 9.95

print("Buenas tardes, bienvenido al servicio de pedido online. \n"
        "El precio de nuestra pizzas es de 8,95€ para la familiar o de 9,90€ para la mediana ¿Cuántas pizzas  familiares desea?")
pizz_familiar = int(input("¿Cuántas pizzas familiares desea? "))

pizz_mediana = int(input("Estupendo, ¿Cuántas pizzas medianas desea? "))

print(f"Estupendo, se están preparando {pizz_familiar} pizzas familiares y {pizz_mediana} pizzas medianas. Digame su dirección")
direcc = input("Dígame su dirección, porfavor ")

total_pizzas = pizz_familiar + pizz_mediana
total = (precio_fam * pizz_familiar) + (precio_med * pizz_mediana)

print(f"Le mandaremos las {total_pizzas} pizzas a {direcc}. Será un total de {total:.2f}€. Muchas gracias por su pedido")