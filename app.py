import os 

restalrantes = ['pizza','xp'] # lista de nomes de restalrante

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

def opcao_invalida():
    print('opcao_invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls') #os.system('clear')
    print(texto)
    print()

def cadastrar_novo_restalrante():
   exibir_subtitulo('cadastro de novos restalrantes:')
   nome_do_restalrante = input('digite o nome do novo restalrante')
   restalrantes.append(nome_do_restalrante)
   print(f'o restalrante{nome_do_restalrante}foi cadastrado com sucesso!')
   voltar_ao_menu_principal()

   def listar_restalrante():
      exibir_subtitulo('listando os restalrantes')

      for restalrante in restalrantes:
         print(f'*{restalrante}')

   voltar_ao_menu_principal()

def escolher_opcao():
   try:
    opcao_escolhida =int(input('escolha uma opcao: '))

    if opcao_escolhida == 1:
       cadastrar_novo_restalrante()
    elif opcao_escolhida == 2:
       listar_restalrante()
    elif opcao_escolhida == 3:
        print('ativar restalrante')
    elif opcao_escolhida== 4:
       finaliza_app()
    else:
        finaliza_app()

   except:
    opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ =='_main_':
   main()
