import random

def enviar_mensagem():
    mensagens = [
        "Olá! Como posso ajudar você hoje?",
        "Bem-vindo ao nosso site de seguro de celulares!",
        "Se você tiver alguma dúvida, estou aqui para ajudar.",
        "Como posso fornecer assistência? É só me perguntar!",
        "Estou disponível para responder às suas perguntas.",
    ]
    return random.choice(mensagens)

def main():
    nome_cliente = input("Qual é o seu nome? ")
    print(f"Olá, {nome_cliente}! Bem-vindo(a) ao nosso site de seguro de celulares.")
    
    while True:
        mensagem = input("Digite sua mensagem (ou 'sair' para encerrar): ")
        
        if mensagem.lower() == 'sair':
            print("Obrigado por visitar nosso site. Até logo!")
            break
        
        resposta = enviar_mensagem()
        print(resposta)

if __name__ == "__main__":
    main()
