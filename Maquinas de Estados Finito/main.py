#Aluno: Mikael da Silva
""" Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
linguagem Python, C, ou C++. Este programa, quando executado, irá determinar se uma string de
entrada faz parte da linguagem 𝐿 definida por 𝐿 = {𝑥 | 𝑥 ∈ {𝑎, 𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏}
segundo o alfabeto Σ = {𝑎, 𝑏, 𝑐}.
    O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de
entrada. As linhas subsequentes contém uma string por linha. A seguir está um exemplo das linhas que
podem existir em um arquivo de testes para o programa que você irá desenvolver:

    3
    abbaba
    abababb
    bbabbaaab
    Neste exemplo temos 3 strings de entrada. O número de strings em cada arquivo será
representado por um número inteiro positivo. A resposta do seu programa deverá conter uma, e
somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado
da validação conforme o formato indicado a seguir:

    abbaba: não pertence.
    A saída poderá ser enviada para um arquivo de textos, ou para o terminal padrão e será
composta de uma linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída.
Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
contendo um número diferente de strings diferentes. Os arquivos de entrada criados para os seus testes
devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github. Observe que o professor
irá testar seu programa com os arquivos de testes que você criar e com, no mínimo um arquivo de
testes criado pelo próprio professor."""

linguagem = 'abb'

def verificaPrimeiraOcorrencia(divideLetra, i):
      if 'a' in divideLetra[i+1]:
        return False
      elif 'b' in divideLetra[i+1]:
        if 'b' in divideLetra[i+2]:
          if (i+3) < len(divideLetra):
            if 'a' in divideLetra[i+3]:
              i += 1     
            else:
              return True
          else:
            return True
        elif (i+2) < len(divideLetra):
          if 'a' in divideLetra[i+2]:
            return False

def verificaCadaLetra(caracter):
  divideLetra = list(caracter)
  i=0
  while i < len(divideLetra):
    if 'a' in divideLetra[i]:
      verificaPrimeiraOcorrencia(divideLetra, i)
      if verificaPrimeiraOcorrencia(divideLetra, i) == False:
        return False
    if 'b' in divideLetra[i]:
      if verificaPrimeiraOcorrencia(divideLetra, i) == False:
        return False
      elif verificaPrimeiraOcorrencia(divideLetra, i) == False and (i+1) < len(divideLetra): 
        i += 1
      else:
        return True
    else:
      i += 1

    

def verificaPalavra(texto):
  i = 0
  while i < len(texto):
    if 'c' in texto[i]:
      print(texto[i] + ": não pertence\n")
      i += 1
    else:
      if linguagem in texto[i]:
        if verificaCadaLetra(texto[i]) == True:
          print(texto[i] + ": pertence\n")
        else:
          print(texto[i] + ": não pertence\n")
      else:
        print(texto[i] + ": não pertence\n")
      i += 1


arq1 = open("dados.txt", "r")
arq2 = open("dados2.txt", "r")
arq3 = open("dados3.txt", "r")

ler1 = arq1.read()
ler2 = arq2.read()
ler3 = arq3.read()

texto1 = ler1.split()
texto2 = ler2.split()
texto3 = ler3.split()

#---colocar arquivo dentro das aspas vazias
#arq = open("", "r")
#ler = arq.read()
#texto = ler.split()

verificaPalavra(texto1)
verificaPalavra(texto2)
verificaPalavra(texto3)
#verificaPalavra(texto)



