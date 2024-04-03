import os 

print ("""sabor express
       """)

print ('1. cadastrar restalrante')
print ('2. listar restalrante')
print ('3. ativar restalrante')
print ('4. sair')
#https://fsymbols.com/pt/letras/

opcao_escolhida =int(input('escolha uma opcao: '))
#print('voce escolheu a opcao' , opcao_escolhida)
#print(f' voce escolheu a opcao {opcao_escolha}' )

def finaliza_app():
    os.system('cls') #os.system('clear')
    print('encerrando o programa\n')

if opcao_escolhida == 1:
    print('cadastrar restalrante')
 elif opcao_escolhida == 2:
    print(' listar restalrante')
elif opcao_escolhida == 3:
    print('ativar restalrante')
else:
    finaliza_app()