import os 

restalrante = ['pizza','xp'] # lista de nomes de restalrante

def exibir_nome_do_programa():
 print ("""sabor express
 """)
def exibir_opcoes():
 print ('1. cadastrar restalrante')
 print ('2. listar restalrante')
 print ('3. ativar restalrante')
 print ('4. sair')

def finaliza_app():
   exibir_subtitulo('finalizar app')

def voltar_ao_menu_principal():
   input('\n digite a tecla "enter" para voltar ao menu principal')
   main()



opcao_escolhida =int(input('escolha uma opcao: '))
#print('voce escolheu a opcao' , opcao_escolhida)
#print(f' voce escolheu a opcao {opcao_escolha}' )

def exibir_subtitulo(texto):
    os.system('cls') #os.system('clear')
    print(texto)
    print()

def escolher_opcao():

    if opcao_escolhida == 1:
        print('cadastrar restalrante')
    elif opcao_escolhida == 2:
        print(' listar restalrante')
    elif opcao_escolhida == 3:
        print('ativar restalrante')
    else:
        finaliza_app()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ =='_main_':
   main()
