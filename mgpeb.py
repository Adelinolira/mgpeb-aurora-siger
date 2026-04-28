import random

fila_pouso = []
pousados = []
alerta = []

clima_ok = random.choice([True, False])
sensores_ok = random.choice([True, True, True, False])

print("CONDIÇÕES DO SISTEMA:")
print("Clima favorável:", clima_ok)
print("Sensores operacionais:", sensores_ok)
print("-" * 40)

modulos = [
    {"nome": "Habitação", "prioridade": random.randint(3,5), "combustivel": random.randint(40,100)},
    {"nome": "Energia", "prioridade": random.randint(3,5), "combustivel": random.randint(40,100)},
    {"nome": "Laboratório", "prioridade": random.randint(1,4), "combustivel": random.randint(40,100)},
    {"nome": "Logística", "prioridade": random.randint(1,3), "combustivel": random.randint(40,100)},
    {"nome": "Médico", "prioridade": random.randint(3,5), "combustivel": random.randint(40,100)}
]

for m in modulos:
    fila_pouso.append(m)

fila_pouso.sort(key=lambda x: x["prioridade"], reverse=True)

def buscar_menor_combustivel(lista):
    menor = lista[0]
    for m in lista:
        if m["combustivel"] < menor["combustivel"]:
            menor = m
    return menor

def autorizar_pouso(modulo):
    combustivel_ok = modulo["combustivel"] > 50
    prioridade_alta = modulo["prioridade"] >= 4

    if (combustivel_ok and sensores_ok and clima_ok) or prioridade_alta:
        return True
    else:
        return False

print("\nINICIANDO GERENCIAMENTO DE POUSO\n")

while fila_pouso:
    modulo = fila_pouso.pop(0)

    print("Analisando módulo:", modulo["nome"])

    if autorizar_pouso(modulo):
        print("Pouso autorizado\n")
        pousados.append(modulo)
    else:
        print("Pouso negado - enviado para alerta\n")
        alerta.append(modulo)

print("\nMódulos pousados:")
for m in pousados:
    print(m["nome"])

print("\nMódulos em alerta:")
for m in alerta:
    print(m["nome"])

menor = buscar_menor_combustivel(modulos)
print("\nMódulo com menor combustível:", menor["nome"])
