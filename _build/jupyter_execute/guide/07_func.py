# Funções

Funções definem blocos de código que podem ser reutilizados sempre que necessário. Assim como as funções matemáticas, as funções de Python recebem valores de entrada (chamados de parâmetros ou argumentos) e retornam valores de saída, no entanto não é obrigatório que elas recebam entradas nem que retornem saídas. Como um exemplo simples, vamos definir a função $f(x) = x^2$ em Python: 

def f(x):
    return x ** 2

f(3)

A definição de uma função começa com a palavra **def**, seguida do identificador da função (nesse caso, *f*) e da lista de parâmetros entre parênteses, terminando com o marcador de início de bloco (:). Note que, como a função define um bloco, as linhas seguintes devem ser indentadas. A definição de uma função cria uma variável com o nome da função, cujo valor é do tipo função. Portanto, é possível atribuir a função a uma outra variável. Isso pode ser usado como mecanismo de renomeação.

type(f)

square = f

square(4)

O "uso" da função após a sua definição é conhecido como "chamada" e requer valores para todos os parâmetros. A passagem de valores para os parâmetros pode ser feita de forma posicional (na ordem de declaração na lista de parâmetros) ou pelos seus nomes, sem necessidade de obedecer a uma ordem. Por exemplo:

def power(x, y):
    return x ** y

power(3, 2), power(y=2, x=3)

Agora vejamos uma função que não possui um comando **return**:

def power(x, y):
    print(x ** y)

power(3, 2)

À primeira vista, a função *power* acima seria chamada de procedimento em outras linguagens de programação, pois não retorna um valor. No entanto, todas as funções de Python possuem retorno. Portanto, quando uma função não possui um comando **return**, ou possui o comando sem associá-lo a um valor, a função retorna **None** (nulo). Nos exemplos abaixo, a chamada da função faz com que o comando **print** interno imprima o valor $3^2$ e depois a função retorna **None**.

print(power(3, 2))

def power(x, y):
    print(x ** y)
    return

print(power(3, 2))

É possível construir funções que retornam múltiplos valores em Python. Vejamos uma função que recebe dois inteiros e retorna o quociente e o resto da sua divisão:

def div(dividend, divisor):
    return dividend // divisor, dividend % divisor

div(7, 2)

Como se pode ver, os retornos da função *div* foram impressos entre parênteses, ou seja, na forma de uma tupla. Como vimos na Seção anterior, para definir uma tupla, basta declarar valores separados por vírgulas, ou seja, o comando **return** da função acima está declarando que retornará uma tupla contendo o quociente e o resto da divisão inteira dos valores *dividend* e *divisor*. Isso significa que Python emula retornos múltiplos de funções por meio do retorno de um único valor do tipo tupla. Essa abordagem permite desconstruir o retorno em múltiplas atribuições durante a chamada. Exemplo:

dividend, divisor = 7, 2
(quocient, remainder) = div(dividend, divisor)

quocient * divisor + remainder

## Declarando valores default

Funções podem ser definidas com valores default para seus parâmetros. Isso permite criar funções que podem ser chamadas com parâmetros omitidos. Por exemplo:

def power(x=3, y=2):
    return x ** y

power(), power(x=4), power(y=3), power(x=10, y=0), power(y=0, x=10)

É comum que uma função seja definida com parâmetros que possuem valores default e parâmetros que precisam ser informados. Nesse caso, é necessário declarar os parâmetros sem valor default primeiro. Como vimos acima, é possível passar valores para parâmetros sem valor default pelo seus nomes, não sendo necessário respeitar a ordem de declaração dos parâmetros. No entanto, caso um parâmetro não seja passado pelo seu nome, ele deve respeitar a ordem de declaração.

def power(x, y=2):
    return x ** y

power(3), power(y=2, x=3), power(3, y=2), power(3, 2)

## Quantidade indefinida de argumentos

É possível especifica um função que pode receber uma quantidade indefinida de argumentos. Esses parâmetros serão "empacotados" em uma tupla chamada *args*. No código abaixo, note que é preciso marcar a tupla *args* com um asterisco, para que Python saiba que deve alocar todos os parâmetros como elementos dela, na ordem que são passados.

def print_all(*args):
    for arg in args:
        print(arg)
        
print_all(1, 2, 'a', 1, 4, 'teste', -1)

Na definição de uma função com quantidade indefinida de argumentos, é possível declarar parâmetros normalmente antes da declaração \**args*. Quaisquer parâmetros passados além dos parâmetros definidos normalmente serão alocados em *args*:

def print_all(message, mean=0, variance=1, *args):
    print(message.format(mean, variance))
    for arg in args:
        print(message.format(arg, variance))

print_all('Gaussian with mean: {0} and variance: {1}')

print_all('Gaussian with mean: {0} and variance: {1}', 1)

print_all('Gaussian with mean: {0} and variance: {1}', 1, 4)

print_all('Gaussian with mean: {0} and variance: {1}', 1, 4, 0, 3, -1, 7)

print_all('Gaussian with mean: {0} and variance: {1}', mean=1, variance=4, 0, 3, -1, 7)

O código acima apresenta erro porque foram passados argumentos por nome antes de argumentos posicionais. Python também permite que uma função seja chamada com uma quantidade indefinida de parâmetros por nome. Para isso, é preciso declarar o parâmetro *kwargs*, que irá representar um dicionário em que Python irá alocar todos os parâmetros passados por nome que não foram pré-definidos na chamada da função. O parâmetro *kwargs* deve ser marcado por asteriscos duplos na definição da função. Exemplo:

def print_all(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])

print_all(param1=1, param2=2, param3=-1)

É possível definir uma função com parâmetros normais e quantidade indefinida de parâmetros posicionais e de parâmetros por nome, combinando \**args* e \*\**kwargs*. Nesse caso, é preciso declarar os parâmetros normais, *args* e *kwargs* nessa ordem.

def print_all(message, mean=0, variance=1, *args, **kwargs):
    print(message.format(mean, variance))
    for arg in args:
        print(message.format(arg, variance))
    for key in kwargs:
        print(key, kwargs[key])

print_all('Gaussian with mean: {0} and variance: {1}', 1, 4, 0, 3, -1, 7, param1=1, param2=2, param3=-1)

Esse tipo de declaração mais complexo é muito comum nas funções de geração de gráficos da biblioteca **matplotlib**, pois isso permite que o usário tenha bastante liberdade para customizar os gráficos.

Os operadores \* e \** também são úteis para chamar funções "desempacotando" listas/tuplas e dicionários para preencher argumentos posicionais e por nome, respectivamente. Exemplos:

args = [3, 10]
list(range(*args))

def print_sum(param1=1, param2=2, param3=-1):
    print(param1 + param2 + param3)
    
params = {
    'param1': 20, 
    'param2': 30, 
    'param3': 40
}

print_sum(**params)

## Passando funções como argumentos

Como mencionado acima, a definição de uma função cria uma variável com o mesmo nome, cujo valor é do tipo função. Portanto funções também podem ser passadas como parâmetros para outras funções. O código abaixo define uma função que recebe um valor *x* e uma função *oper*, que define que operação será realizada com o valor de *x*:

def square(x):
    return x ** 2

def perform_oper(x, oper):
    return oper(x)

perform_oper(3, square)

O segundo argumento passado para a função *perform_oper* foi a função *square* definida acima, que foi então chamada pelo código de *perform_oper* para retornar o quadrado de *x*.

## O operador lambda

Em Python, é possível usar o operador **lambda** para definir funções pequenas (que ocupam apenas uma linha). Isso pode ser útil para definir funções simples que não serão usadas em outros módulos ou em várias partes diferentes do código. O operador **lambda** retorna um valor do tipo função, portanto para usar a função assim definida, pode-se atribuí-la a uma variável:

cube = lambda x: x ** 3

cube(3)

Um dos casos de uso comuns do operador **lambda** é quando precisamos passar uma função simples como parâmetro para outra função de forma concisa. Exemplo:

def perform_oper(x, oper):
    return oper(x)

perform_oper(3, lambda x: x ** 4)

## Funções básicas

Python vem de fábrica com diversas [funções](https://docs.python.org/3.7/library/functions.html) que podem ser bastante úteis. Além das funções que já vimos e chamamos de operadores, como **list**(), **set**(), **tuple**(), **dict**(), **type**(), entre outras, temos também algumas operações, como:

* **sum**(): Soma os elementos de uma coleção;
* **min**(), **max**(): Determina o menor/maior valor em uma coleção;
* **pow**(x, y): Eleva *x* à *y*-ésima potência;
* **round**(): Arredonda o valor passado como parâmetro;
* **all**: Retorna **True** se todos os elementos da coleção passada como parâmetro avaliarem como **True**.
* **any**: Retorna **True** se algum dos elementos da coleção passada como parâmetro avaliar como **True**, caso contrário, retorna **False**.

Outras funções comumente úteis incluem as funções de entrada e saída e as funções **zip** e **enumerate**.

### Funções de entrada e saída

As principais funções de entrada e saída de Python são **input**, **print** e **open**. A função **input** pede que o usuário forneça um valor. Por exemplo, o código abaixo pede que o usuário digite seu nome e imprime uma saudação:

name = input('Digite seu nome: ')

print('Hello, ' + name)

O valor fornecido pelo usuário pode ser convertido para tipos diferentes, usando as funções como **int**, **bool**, **float**. Exemplo:

age = int(input('Digite sua idade: '))

print('Você se aposentará aos {0} anos'.format(age + 87))

A função **open** permite abrir um arquivo para escrita ou para leitura, com opções de abertura do arquivo sendo especificadas pelo parâmetro *mode*. Com *mode='r'*, o arquivo é aberto para leitura, enquanto *mode='w'* abre o arquivo para escrita. Outras opções podem ser vistas na [documentação de Python](https://docs.python.org/3.7/library/functions.html#open). Quando um arquivo é aberto para leitura, suas linhas podem ser acessadas iterativamente usando o operador de laço **for**. 

O código abaixo abre um arquivo chamado "samples.txt" para leitura e imprime seu conteúdo linha-a-linha. O código também introduz um nome tipo de bloco, chamado **with**. Esse bloco define uma região de código em que o arquivo será acessado. Ao final da execução do código dentro do **with**, o arquivo será fechado automaticamente. O bloco **with** também é muito útil para controlar conexões com servidores e bancos de dados.

with open('../data/samples.txt', mode='r') as file:
    for line in file:
        print(line, end='')

Para escrever em um arquivo, basta abrí-lo em modo de escrita e usar a função **print** apontando para o arquivo. O código abaixo irá ler o arquivo "samples.txt" e imprimir suas linhas no arquivo "copy.txt". Note os blocos **with** aninhados, para que os dois arquivos sejam fechados ao final do processamento.

with open('../data/samples.txt', mode='r') as samples:
    with open('../data/copy.txt', mode='w') as copy:
        for line in samples:
            print(line, file=copy, end='')

### Função zip

A função **zip** retorna os elementos de duas ou mais coleções em formato de tuplas, em que a i-ésima tupla contém os i-ésimos elementos de cada coleção. Exemplo:

means, variances = [1, -1, 0], [1, 4, 9]

for mean, var in zip(means, variances):
    print('Média: {0}, Variância: {1}'.format(mean, var))

### Função enumerate

Permite iterar pelos elementos de uma coleção e pelos seus índices simultaneamente. Exemplo:

for i, mean in enumerate(means):
    print('Índice: {0}, Média: {1}'.format(i, mean))

Como a função **zip** retorna uma coleção de tuplas, é possível usar a função **enumerate** para iterar sobre o resultado do **zip** (observe os parênteses para evitar ambiguidade entre as tuplas retornadas por **zip** e **enumerate**):

for i, (mean, var) in enumerate(zip(means, variances)):
    print('Índice: {0}, Média: {1}, Variância: {2}'.format(i, mean, var))

