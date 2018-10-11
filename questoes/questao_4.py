## QUESTÃO 4 ##
#
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data 
# será inserida em formato numérico com três instruções de entrada separadas; 
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
   n = int(input('Digite uma dia'))
   n1 = int(input('Digite um mes'))
   n2 = int(input('digite um ano'))
   print('O sucessor da data {}-{}-{} é {}-{}-{}'.format (n, n1, n2, (n <= 28), (n1 + 1), (n2 + 1)))


  if n2 % 400:
    if n1 == 2:
           print('O sucessor é {}-{}-{}'.format (n, n1, n2, (n), (n1), (n2 % 400)))
    else:
            print('O sucessor é {}-{}-{}'.format((n % 2), (n1 + 2), (n2 + 1)))
  else:
    print('O sucessor é {}-{}-{}'.format((n % 2), (n1 + 2), (n2 + 1)))


    
if __name__ == '__main__':
    main()
