import os 

restaurantes = [{'nome':'restaurante xp','categoria':'alimento','ativo':False},
                {'nome':'santa','categoria':'carne','ativo':True},
                {'nome':'cwb','categoria':'sushi','ativo':False}]

def exibir_nome_do_programa():
   '''Essa funcao e responsavel por exibir nome do programa'''
print ("""sabor express
 """)
def exibir_opcoes():
 '''essa funçao e responsavel por exibir as opçoes'''
 print ('1. cadastrar restaurante')
 print ('2. listar restaurante')
 print ('3. ativar restaurante')
 print ('4. sair')

def finaliza_app():
   '''Essa funcao e responsavel por finalizar o programa'''
   exibir_subtitulo('finalizar app')

def voltar_ao_menu_principal():
   '''Essa funcao e responsavel por voltar ao menu principal
   inputs:
   -enter
   
   outputs:
   voltar ao menu principal
   '''
   
   input('\n digite a tecla "enter" para voltar ao menu principal')
   main()

def opcao_invalida():
    '''essa funcao e responsavel por invalidar as opçoes'''
    print('opcao_invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa funcao e responsavel por exibir subtitulo'''
    os.system('clear') 
    linha = '*'*(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
   '''Essa funcao e responsavel por cadastrar um novo restaurante
   inputs:
   -nome do restaurante
   -categoria

   output:
   -adicionar um novo restauante a lista de restaurantes
   '''
   
   exibir_subtitulo('cadastro de novos restaurantes:')
   nome_do_restaurante = input('digite o nome do novo restaurante:')
   categoria = input(f'digite a categoria do restalrante {nome_do_restaurante}: ')
   dado_do_restaurante = {'nome':nome_do_restaurante, 'categoria': categoria, 'ativo': False}
   restaurantes.append(dado_do_restaurante)
   print(f'o restaurante{nome_do_restaurante}foi cadastrado com sucesso!')
   voltar_ao_menu_principal()

def listar_restaurante():
   '''Essa funcao e responsavel por listar um novo restaurante
   inputs:
   -listar restaurante
   -categoria

   output:
   -adicionar um novo restauante a lista de restaurantes
   '''

   exibir_subtitulo('listando os restaurantes')

   print(f'{"nome do restaurante".ljust(22)} |{"categoria".ljust(20)} | satus')
   for restaurante in restaurantes:
       nome_restaurante = restaurante ['nome']
       categoria = restaurante ['categoria']
       ativo = 'ativado' if restaurante ['ativo'] else  'desativado'
       print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

   voltar_ao_menu_principal()

def alterar_estado_restaurante():
   '''Essa funcao e responsavel por alterar o estado do novo restaurante
   inputs:
   -alterar estado do restaurante
   -categoria

   output:
   -adicionar um novo restauante a lista de restaurantes
   '''
    
   exibir_subtitulo('alternando estado do restaurante')
   nome_restaurante = input('digite o nome do restaurante que deseja alterar o estado:')
   restaurante_encontrado = False

   for restaurante in restaurantes:
         if nome_restaurante == restaurante ['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante ['ativo']
            mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
            print (mensagem)

   if not restaurante_encontrado:
      print('o restaurante nao foi encontrado')
   voltar_ao_menu_principal()

def escolher_opcao():
   '''essa funçao e responsavel por mescolher as opçoes'''
   try:
    opcao_escolhida =int(input('escolha uma opcao: '))

    if opcao_escolhida == 1:
       cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
       listar_restaurante()
    elif opcao_escolhida == 3:
        alterar_estado_restaurante()
    elif opcao_escolhida== 4:
       finaliza_app()
    else:
         opcao_invalida()

   except:
    opcao_invalida()

def main():
    '''essa funcao e a principal responsavel por apresentar as opçoes'''
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
 main()
 