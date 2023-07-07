class ContaCorrente:
    
    def __init__(self, numero, nomeCorrentista, saldo=0.0):
        self.numero = numero
        self.alterarNome(nomeCorrentista)
        self.saldo = saldo
        
    def alterarNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista
        
    def deposito(self, valor):
        self.saldo +=valor
        
    def sacar(self, saldo):
        self.saldo -=valor
    
    

class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, nomeCorrentista, saldo=0.0,limiteSaques=3):
        self.limiteSaques=limiteSaques
        super().__init__(numero, nomeCorrentista, saldo=0.0)
        
    def calculaTaxaJuros(self,selic,tr):
        if (selic>8.5):
            return 0.5+tr
        else:
            return selic*0.7+tr
            
    def saque(self,valor):
        if self.limiteSaques==0:
            print("Limites de saques atingidos!!!")
        else:
            self.limiteSaques-=1
            self.saldo -= valor
     
#TESTE DA CKASSE

cp=ContaPoupanca(200,"Arthur")
tx=cp.calculaTaxaJuros(2.12,1.7)
print(f"Taxa de Juros é {tx:.2f}%")
cp.deposito(200)
cp.saque(12)
cp.saque(12)
cp.saque(12)
cp.saque(12)
