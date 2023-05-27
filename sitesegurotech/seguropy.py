planos_seguro = [
    {"plano": "Básico", "cobertura": "Danos acidentais", "preco": 50.00},
    {"plano": "Intermediário", "cobertura": "Danos acidentais e roubo", "preco": 80.00},
    {"plano": "Completo", "cobertura": "Danos acidentais, roubo e perda", "preco": 100.00}
]

def mostrar_planos():
    print("Planos de Seguro Disponíveis:")
    for plano in planos_seguro:
        print(f"Plano: {plano['plano']}")
        print(f"Cobertura: {plano['cobertura']}")
        print(f"Preço: R${plano['preco']}\n")

mostrar_planos()
