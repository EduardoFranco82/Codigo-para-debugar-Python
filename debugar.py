class EmailDeBoasVindas:
    def __init__(self):
        self.pessoas = ['Cristian', 'Robert', 'Eduardo', 'Ana']

    def Iniciar(self):
        print('Olá bem vindo a este site!')
        emails_apresentacao = self.MontarCredencial(self.pessoas)
        for email in emails_apresentacao:
            print(email)

    def MontarCredencial(self, pessoas):
        credenciais = []
        for pessoa in pessoas:
            credenciais.append(f'A empresa gostaria de dar boas vindas para o(a) {pessoa}')
        return credenciais

email = EmailDeBoasVindas()
email.Iniciar()

#f5 Começar a debugar o código
#f10 Analisar linha sem entrar no código interno
#f11 Analisar linha e entrar no código interno
#Shift-f11 air do bloco de código atual e continuar a execução


