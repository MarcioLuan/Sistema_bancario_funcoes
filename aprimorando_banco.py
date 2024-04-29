def menu():
    print (f"""\n
    ###### MENU ######  
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Criar usuario
    [5] Criar conta
    [6] Listar conta
    [0] Sair     
    """)
    opcao= int(input("Informe a opcao desejada: "))
    return opcao

def depositar (saldo, deposito, extrato, /):
    if deposito > 0:         
            saldo += deposito
            extrato += f"Depósito de R$ {deposito:.2f}\n"
            print (f"\nDeposito de R$ {deposito:.2f} realizado com sucesso!")
    else:
        print ("\nO valor de deposito informado não é válido")
    return saldo, extrato

def sacar (*,saldo, saque,valor_saque_limite, quantidade_saque, extrato, quantidade_limite_saque):
    excedeu_saldo = saque>saldo
    excedeu_limite = saque> valor_saque_limite
    excedeu_saques = quantidade_saque>= quantidade_limite_saque

    if excedeu_saldo:
        print ("\nNão foi possível completar o saque! Saldo insuficiente.")

    elif excedeu_saques:
        print ("\nNão foi possível completar o saque! Você excedeu o limite de 3 saques diários.")

    elif excedeu_limite:
        print ("\nNão foi possível completar o saque! Você excedeu o limite de R$500.00")

    elif saque>0:
        saldo = saldo - saque
        extrato = extrato + f"Saque de R$ {saque:.2f}\n"
        quantidade_saque = quantidade_saque + 1
        print (f"\nSaque de R$ {saque} realizado com sucesso.\nSaldo: R$ {saldo}")

    else:
            print ("\nOperação falhou! O valor de saque informado não é válido.")
    return saldo, extrato, quantidade_saque

def ver_extrato (saldo ,/, *,extrato):
     if extrato == "":
         print (f"######EXTRATO######\n{extrato}")
         print ("Não houve movimentações nessa conta")
         print (f"O saldo é de R$ {saldo:.2f}")
        
     else:
         print (f"###EXTRATO###\n {extrato}")
         print (f"O saldo é de R$ {saldo:.2f}")
     return saldo, extrato

def criar_usuario(usuarios):
    cpf = input ("Informe o CPF (apenas números): ")
    usuario =filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print ("Já existe usuário com esse CPF!")
        return
    
    nome= input ("\nInforme o nome do usuário: ")
    data_nascimento= input ("\nInforme a data de nascimento do usuário (dd/mm/aaaa): ")
    endereco= input ("\nInforme o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append ({"nome" : nome, "data_nascimento" : data_nascimento, "cpf" : cpf, "endereco": endereco})
    print ("Usuário cadastrado com sucesso!")

def filtrar_usuarios(cpf,usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados [0] if usuarios_filtrados else None

def criar_conta (agencia, numero_da_conta, usuarios):
     cpf = input ("Informe o CPF (apenas números): ")
     usuario= filtrar_usuarios (cpf, usuarios)

     if usuario:
          print ("Conta criada com sucesso!")
          return {"agencia":agencia, "numero_da_conta": numero_da_conta, "usuario":usuario}
     else:
          print ("É necessário criar um usuário para vincular à conta")
          return None

def listar_contas (contas):
     for conta in contas:
          print (f"""
                 Agencia: {conta["agencia"]}, Conta: {conta["numero_da_conta"]}, Titular: {conta ["usuario"]["nome"]}""") 

def main ():
    QUANTIDADE_LIMITE_SAQUE=3
    AGENCIA = "0001"
    
    saldo=0
    extrato=""
    quantidade_saque=0
    valor_saque_limite=500
    usuarios = []
    contas= []
    numero_da_conta=1

    while True:
        opcao= menu()
        if opcao ==1:
            deposito = float(input("\nInforme o valor do deposito: "))
            
            saldo,extrato = depositar (saldo, deposito, extrato)

        elif opcao ==2:
             saque = float(input("\nInforme o valor do saque: "))

             saldo, extrato, quantidade_saque= sacar (
                 saldo = saldo,
                 saque= saque,
                 valor_saque_limite=valor_saque_limite ,
                 quantidade_saque= quantidade_saque,
                 extrato = extrato,
                 quantidade_limite_saque=QUANTIDADE_LIMITE_SAQUE,)

        elif opcao==3:
             saldo,extrato= ver_extrato (saldo, extrato=extrato)

        elif opcao==4:
             criar_usuario(usuarios)
        
        elif opcao==5:
             conta= criar_conta (AGENCIA, numero_da_conta,usuarios)

             if conta:
                  contas.append (conta)
                  numero_da_conta +=1
        
        elif opcao==6:
             listar_contas(contas)

        elif opcao==7:
            break

        else:
             print ("Informe uma opção valida")
   
main()