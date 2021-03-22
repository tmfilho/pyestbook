# Módulos e Importação

Frequentemente é necessário desenvolver um programa mais complexo, usando um editor de texto para preparar um arquivo e executando o arquivo usando o interpretador de Python. Esse arquivo é conhecido como *script*. À medida que o programa cresce, torna-se interessante dividí-lo em diversos arquivos, para facilitar a manutenção e a compreensão do código. Pode também ser necessário usar uma ou mais funções em diversos programas, sendo indesejável copiar o código da(s) função(ões) para cada programa.

Python atende esses requisitos por meio de *scripts* chamados módulos. Definições criadas em um módulo podem ser *importadas* em outros módulos ou no módulo principal (*main*), que é o módulo que contém as variáveis e funções definidas no *script* executado.

Um arquivo de módulo deve ter a extensão *.py*. Vejamos um exemplo retirado da [documentação de Python](https://docs.python.org/3/tutorial/modules.html). O código abaixo foi salvo em um arquivo chamado "fibo.py".

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

Para importar o módulo correspondente, fazemos:

import fibo

Após a importação, podemos usar as funções do módulo *fibo* da seguinte maneira:

fibo.fib(1000)

fibo.fib2(1000)

É possível importar as funções do módulo *fibo* diretamente. Assim, elas podem ser chamadas sem ser precedidas pelo nome do módulo:

from fibo import fib, fib2
fib(300)

Note que dessa forma, para ter acesso a todas as funções do módulo, seria necessário declarar cada um dos seus nomes. Isso pode ser feito de forma mais direta usando um asterisco: 

from fibo import *
fib2(300)

Isso irá importar todos os identificadores do módulo que não começam com *underline* (\_). A importação com asterisco não costuma ser muito usada, porque comumente resulta em código de difícil leitura. 

O comando *import* pode usar o operador *as* para atribuir um nome diferente ao módulo ou a uma função:

import fibo as f
f.fib(200)

from fibo import fib as fibonacci
fibonacci(100)

## Módulos da biblioteca padrão de Python

Python já vem de fábrica com uma enorme quantidade de módulos que podem ser importados para facilitar o trabalho de desenvolvimento. Recomendamos uma visita à lista de módulos da [biblioteca padrão](https://docs.python.org/3/library). Alguns módulos importantes:

   * **math**: Funções matemáticas
   * **statistics**: Funções estatísticas
   * **random**: Geração de números aleatórios
   * **datetime**: Tipos e funções básicos de datas
   * **os**: Funções de interação com o sistema operacional
   * **sqlite3**: Interface para bancos de dados SQLite
   * **itertools**: Funções para programação funcional
   * **multiprocessing**: Processamento paralelo
   * **urllib**: Funções para manipulação de URLs e requisições

