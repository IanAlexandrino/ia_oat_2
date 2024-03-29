import random

class No:
    def __init__(self, chave):
        self.direita = None
        self.esquerda = None
        self.valor = chave

def main():
    def travessia_em_ordem(root):
        if root:
            travessia_em_ordem(root.esquerda)
            print(root.valor)
            travessia_em_ordem(root.direita)

    def insercao(root, chave):

        if root is None:
            return No(chave)
        
        else:

            if root.valor < chave:
                root.direita = insercao(root.direita, chave)

            else:
                root.esquerda = insercao(root.esquerda, chave)

        return root
    
    def busca(root, chave):

        if root is None or root.valor == chave:
            return root
        
        if root.valor < chave:
            return busca(root.direita, chave)
        
        return busca(root.esquerda, chave)
    
    root = None

    i = 0

    # Testando o método de inserção

    while i < 20:

        root = insercao(root, random.randint(1, 100))
        i += 1
    
    # Testando o método de travessia em ordem

    travessia_em_ordem(root)

    # Testando o método de busca

    valor = int(input("Escolha um valor para buscar na árvore: "))

    resultado = busca(root, valor)

    if resultado:
        print("Valor " + str(valor) + " encontrado na árvore.")

    else:
        print("Valor " + str(valor) + " não encontrado na árvore.")


if __name__ == "__main__":
    main()