#cliente.py
class Cliente:
    def __init__(self, nome, rg, end, email, cidade):
        self.nome = nome
        self.rg = rg
        self.end = end
        self.email = email
        self.cidade = cidade

    def editaNome(self, novo_nome):
        self.nome = novo_nome
    
    def editaRg(self, novo_rg):
        self.rg = novo_rg
    
    def editaEndereco (self, novo_end):
        self.end = novo_end
    
    def editaEmail (self, novo_email):
        self.email = novo_email
    
    def editaCidade (self, nova_cidade):
        self.cidade = nova_cidade
    
    def retornaNome(self):
        return self.nome

    def retornaRg(self):
        return self.rg
    
    def retornaEndereco(self):
        return self.end

    def retornaEmail(self):
        return self.email
    
    def retornaCidade(self):
        return self.cidade