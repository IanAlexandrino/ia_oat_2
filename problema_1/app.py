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


if __name__ == "__main__":
    main()