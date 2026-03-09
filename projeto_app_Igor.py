'''
CRUD



'''




print("\n== GESTÃO DO SALÃO ===")
print("1. Agendar Cliente")
print("2. Ver Agenda")
print("3. Mudar Serviço")
print("4. Cancelar Agendamento")
print("5. Relatorio de Serviços")
print("0. Sair")

while True:

    escolha = input("\nEscolha uma opcão:")  
    
    if escolha =='1':

        print("Cadastrar cliente...")
        nome_cliente = input("Digite o nome do Cliente")
        cliente_telefone = input("Digite o nome do cliente: ")

        print("Cadastro concluido com sucesso?\n")
        
    elif escolha == '2':

        print("mostrar os horarios cadastrados")
        horario_cliente = input("Esolha um horario:")
        periodo_cliente = input("Escolha o periodo:")

        print("Horario Cadastrado com sucesso\n")
     
    if escolha == '3':

        print("Alterar serviço do cliente")
        serviço_cliente = input("digite o novo serviço (corte / barba / Corte + Barba): ")
        print("Serviço alterado com sucesso!")

    elif escolha == '4':

        print
    

        
