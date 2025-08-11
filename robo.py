import nltk
from nltk.chat.util import Chat, reflections

# Usando a lista de pares mais completa e robusta do seu segundo trecho
pares = [
    [
        r"oi| Ola| hey| Hello",
        ["Ola","oi","hey","Hello" ],
    ],
    [
        r"Qual e o seu nome ?",
        ["Meu nome é chatbot",'Eu sou o Chatbot!'],
    ],
    [
        r"Como voce está ?| Como voce esta ?| como estas se sentindo",
        ["Estou bem obrigado, e voce ?", "Estou otimo", "Vou bem", "haha que isso teteu da dando mole p mim é"]
    ],
    [
        r"Tchau | adeus| flw pai",
        ["Etchauzinho", "até mais", "ate a proxima painho", "seu fofo tchau"]
    ]
]

# Definindo a função para iniciar o chatbot
def chatbot():
    print("Olá! Eu sou o chatbot. Vamos conversar!")
    # Criando a instância do chatbot usando a classe Chat e a lista de pares
    chat = Chat(pares, reflections)
    while True:
        try:
            respost = chat.respond(input())
            print(respost)
        except KeyboardInterrupt:
            break
    # Iniciando a conversa
    chat.converse()

# Chamando a função para rodar o chatbot
if __name__ == "__main__":
    chatbot()