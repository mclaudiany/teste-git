class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def unir_nomes(self):
        self.nome_completo = self.nome + ' ' + self.sobrenome
        print(f'{self.nome_completo}')
        
        