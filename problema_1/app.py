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


if __name__ == "__main__":
    main()