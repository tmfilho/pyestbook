# Coleções

Coleções são estruturas que permitem armazenar múltiplos valores, que podem ser do mesmo tipo ou não. Os principais tipos de coleções são: listas (*list*), tuplas (*tuple*), intervalos (*range*), textos (*str*), conjuntos (*set*) e dicionários (*dict*). As coleções podem ser de dois tipos, dependendo das operações permitidas sobre seus valores: mutáveis e imutáveis. 

## Listas

As listas são coleções mutáveis normalmente (mas não obrigatoriamente) usadas para armazenar itens homogêneos. Uma lista pode ser criada de várias formas:

   1. Para criar uma lista vazia: \[ \] ou **list**()
   2. Para criar uma lista com valores: \[*1*, *5*, *2*\]
   3. A partir de outra coleção: **list(colecao)**
      * Esta operação irá construir uma lista cujos itens são os mesmos e na mesma ordem que os itens da coleção original

### Verificando a presença de um item

Para verificar se um valor *x* pertence à lista ou vetor *s*, usa-se o operador **in**, que equivale à notação matemática $x \in \vec{s}$, como mostra o código abaixo.

s = [1, 2, -1]

2 in s

Por outro lado, para verificar se o elemento não pertence à lista, i.e. $x \notin \vec{s}$:

3 not in s

### Concatenando listas

Dadas duas listas *s1* e *s2*, pode-se concatená-las, produzindo uma terceira lista, usando-se o operador de adição:

s1 = [1, 2]
s2 = [3, 4]

s1 + s2

O operador de multiplicação tem o efeito de repetir *s1* um número de vezes igual a *n*:

n = 2

s1 * n

### Obtendo o tamanho da lista

Para obter o tamanho da lista, basta usar o operador **len**:

len(s1)

### Acessando elementos da lista

Listas tem acesso direto aos seus elementos por meio de índices inteiros, com o índice *0* correspondendo ao primeiro elemento.

s = [4, 5, 0, 2, 3, 9, 7, 1, 12]

s[0]

Listas permitem acessar fatias (*slices*) dos seus valores, e.g para obter a fatia da lista *s* compreendida entre os índices \[*1*, *3*):

s[1:3]

Note que o lado direito do intervalo dos índices é aberto. Também é possível definir o intervalo da fatia com início, fim e incremento. O código abaixo seleciona os índices {*1*, *3* e *5*}.

s[1:7:2]

Nenhum dos três valores para definição da fatia é obrigatório. Se o início não for fornecido, a fatia irá iniciar do índice *0*. Se o fim não for definido, a fatia irá até a última posição da lista. Por fim, se o incremento não for informado, ele receberá o valor *1*.

s[:3]

s[2:]

Python também permite que os elementos sejam acessados usando índices negativos. Para entender esses índices, basta imaginar que a origem deixa de ser o *0* e passa a ser o tamanho da lista, **len**(*s*). Por exemplo, o índice *-1* corresponderá a **len**(*s*) - *1*, ou seja, a última posição da lista. O índice *-2* equivalerá à penúltima posição da lista, i.e. **len**(*s*) - *2*. Além disso, incrementos de fatias também podem ser negativos.

s[-1]

s[-2]

s = [4, 5, 0, 2, 3, 9, 7, 1, 12]

s[5:2:-1]

### Modificando a lista

Como mencionado acima, listas são coleções mutáveis, portanto seus valores podem ser modificados ou removidos e novos valores podem ser adicionados. As operações discutidas nesta Seção são implementadas apenas pelas coleções mutáveis. Para modificar um valor da lista, basta atribuir um novo valor a sua posição:

s[2] = 11

s

Uma fatia inteira pode ser substituída pelos valores de uma outra lista do mesmo tamanho, como mostra o código abaixo.

s[1:3] = [2, 8]

s

O operador **del** permite remover uma fatia inteira da lista, reduzindo seu tamanho:

del s[2:7:2]

s

Para adicionar novos elementos pode-se usar as operações **append** (adiciona elemento ao final da lista), **insert** (adiciona elemento na posição desejada) e **extend** (adiciona elementos de outra lista ao final da lista).

s.append(3)

s

s.insert(1, 5)

s

s.extend([6, 7])

s

## Tuplas

Tuplas são coleções imutáveis, tipicamente usadas para armazenar dados heterogêneos. Essas estruturas são bastante usadas para permitir o retorno de múltiplos valores em funções. Uma tupla pode ser criada de várias formas:

   1. Para criar uma tupla vazia: () ou **tuple**()
   2. Para criar uma tupla com valores: *1*, 'a', *2* ou (*1*, 'a', *2*)
   3. A partir de outra coleção: **tuple(colecao)**
      * Esta operação irá construir uma tupla cujos itens são os mesmos e na mesma ordem que os itens da coleção original

Como se pode ver no item 2 acima, parênteses na definição da tupla com valores são opcionais, exceto para evitar situações de ambiguidade, e.g. **func**(*1*, *2*, *3*), ou seja uma chamada de função com três parâmetros, é diferente de **func**((*1*, *2*, *3*)), i.e. uma chamada de função com apenas com parâmetro do tipo tupla.

As tuplas implementam todas as operações de coleções que não modificam valores, incluindo **in**, **not in**, concatenação, **len** e acesso de elementos por fatias de índices.

## Intervalos

Coleções do tipo **range** são imutáveis e contêm sequências de números que são comumente usados em laços com quantidades definidas de repetições (**for**). Intervalos são construídos de forma parecida com as fatias de índices, i.e. por meio de três valores inteiros que definem início, fim (intervalo aberto) e incremento do intervalo. Também de forma similar, se o início for omitido, ele recebe o valor *0* e se o incremento não for informado, assume-se *1*. De forma geral, o **range** $r$, com início $j$, fim $k$ e incremento $t$ retornará os elementos $r = \left\{j \leq r_i < k~|~r_i =j + t * i, i \geq 0\right\}$.

Um detalhe importante das coleções **range** é que ele sempre ocupa a mesma quantidade de memória, independente do tamanho do intervalo. Isso é possível porque ele apenas armazena os valores de início, fim e incremento. Todos os valores que pertencem ao intervalo são calculados apenas quando necessário. Isso significa que para obter os elementos do **range**, é preciso acessá-los explicitamente. Por exemplo, o código abaixo cria um **range** \[*0*, *10*). Diferente das outras coleções, o retorno do comando que cria o **range** não imprime todos os elementos.

range(10)

Para imprimir todos os elementos, pode-se criar uma lista a partir do intervalo:

list(range(0, 10))

Uma fatia de um **range** também é um **range**, mantendo a vantagem de usar pouca memória. Por outra lado, valores únicos podem ser acessados diretamente usando seus índices.

range(1,12)[2:6:2]

list(range(1,12)[2:6:2])

range(1,12)[4]

## Textos

Dados do tipo texto, também chamados de *strings* são representados por variáveis do tipo **str**, que são coleções imutáveis de caracteres Unicode. Existem três formas de definir variáveis do tipo **str**, diferenciadas pelo tipo de aspas:

   1. Aspas simples: 
       ```python
           'nesse caso, as aspas "internas" devem ser duplas'
       ```
   2. Aspas duplas:
       ```python
           "nesse caso, as aspas 'internas' devem ser simples"
       ```
   3. Três aspas simples ou duplas:
       ```python
''' 
    strings neste formato
    podem ocupar múltiplas linhas e
    incluem todos os espaços em branco    
'''
       ```


Caracteres e fatias de *strings* podem ser acessados, assim como em listas e tuplas. Não há um tipo específico para caracteres, como em outras linguagens de programação. Assim, um caractere é apenas uma *string* de tamanho *1*.

'Estatística'[2]

'Estatística'[2::-1]

Assim como as tuplas, as *strings* suportam todas as operações de sobre coleções que não modificam seus valores. Além dessas operações comuns a todos os tipos de coleções, as *strings* também implementam várias operações que facilitam o processamento de texto. Aqui, listaremos algumas dessas operações. Mais opções estão disponíveis na [documentação de Python](https://docs.python.org/3.7/library/stdtypes.html#string-methods).

### Verificando a presença de caracteres

Diferente das outras coleções, o operador **in** e sua negação **not in** funcionam não só para checar se um caractere pertence à *string*, mas também pode checar se uma *string* menor pertence ou não a outra, ou seja se uma *string* é *substring* da outra ou não. Note que essas operações diferenciam minúsculas e maiúsculas.

'a' in 'Estatística'

'b' not in 'Estatística'

'Est' in 'Estatística'

'est' in 'Estatística'

### Concatenando *strings*

*Strings* podem ser concatenadas usando o operador de adição ou colocando apenas um espaço branco entre elas. Além disso, é possível usar a operação **join** para concatenar *strings*, intercalando-as com a *string* sobre a qual faz-se a operação.

'ciência ' + 'de ' + 'dados' 

'ciência ' 'de ' 'dados' 

', '.join(['pêra', 'uva', 'maçã', 'salada mista'])

### Formatando *strings*

Uma das operações mais frequentes sobre *strings* é a formatação, que permite inserir certos valores em posições pré-definidas de uma *string*. Existem duas formas principais de fomatar *strings* em Python. A primeira e mais flexível é a operação **format**. A segunda, que não cobriremos neste material, é baseada no comando **printf** de *C*. Para começar, considere a seguinte *string*, que poderia ser usada para descrever os parâmetros de uma distribuição Normal:

s = 'Média: 1, Variância: 4'

Suponha que, em uma aplicação, fosse necessário listar os parâmetros de várias Normais diferentes. As únicas partes que precisariam mudar na *string* acima seriam os valores associados aos parâmetros. Assim, seria interessante definir a *string* *s* como um modelo, com lacunas que serão preenchidas plos valores de média e variância. Para isso, podemos definir *s* como:

s = 'Média: {0}, Variância: {1}'

Uma vez definida a *string* modelo, basta aplicar a operação **format**:

s.format(2, 9)

Em detalhes, as chaves delimitam campos que serão preenchidos. Os números *0* e *1* dentro das chaves indicam a ordem de preenchimento dos valores. Se tivéssemos definido o campo relacionado à média com *{1}* e o da variância com *{0}*, a ordem de preenchimento teria sido trocada:

s = 'Média: {1}, Variância: {0}'

s.format(2, 9)

Também é possível marcar os valores que serão preenchidos por meio de palavras-chave, por exemplo:

s = 'Média: {mean}, Variância: {var:.2f}'

s.format(mean=2.576, var=9.375)

Note que no caso da variância, o valor foi arredondado para duas casas decimais. Há muitas opções de formatação diferentes, incluindo a limitação do número de casas decimais, formatação específica para datas, porcentagens, opções estéticas, etc. A [documentação de Python](https://docs.python.org/3.7/library/string.html#formatstrings) especifica todas as opções.

### Outras operações com *strings*

Outras operações comuns com *strings* incluem **split**, **replace**, **find**, **lower**, **upper**, **title**. A operação **split** divide a *string* em uma lista contendo *substrings* delimitadas pela *string* *sep*. Caso *sep* não seja informada, espaços em branco consecutivos serão tratados como delimitadores.

'Média: 1, Variância: 4'.split(sep=', ')

'Média: 1,     Variância: 4'.split()

As operações podem ser encadeadas, sendo executadas em ordem. Por exemplo, o código abaixo formata uma *string* e depois a separa em *substrings* delimitadas por uma vírgula seguida de um espaço em branco.

'Média: {mean}, Variância: {var:.2f}'.format(
    mean=2.576, var=9.375
).split(
    sep=', '
)

A operação **replace** substitui todas as ocorrências de uma *substring* por uma nova *substring* e dá como resultado a *string* modificada. Opcionalmente, pode-se informar quantas substituições deseja-se fazer.

'Média: 1, Variância: 4'.replace(': ', '=')

'Média: 1, Variância: 4'.replace(': ', '=', 1)

A operação **find** permite encontrar o índice da primeira ocorrência de uma *substring* em uma *string* ou em uma fatia de uma *string*.

'Estatística'.find('t')

'Estatística'.find('t', 3, 7)

Note que o código acima não retorna o mesmo resultado que o código abaixo:

'Estatística'[3:7].find('t')

Isso acontece porque o primeiro código busca a *substring* na *string* original, porém desconsidera qualquer ocorrência fora da fatia especificada. Por outro lado, o segundo código primeiro extrai a fatia entre os índices \[*3*, *7*), gerando uma nova *string*, e só depois aplica a operação **find**.

As operações **lower**, **upper**, **title** servem para modificar a caixa dos caracteres de uma *string*.

   1. **lower**: coloca todos os caracteres em caixa baixa (minúsculas)
   2. **upper**: coloca todos os caracteres em caixa alta (maiúsculas)
   3. **title**: coloca a *string* em formato de título, i.e. as primeiras letras das palavras ficam maiúsculas e as demais minúsculas (note que o algoritmo faz essa transformação em todas as palavras da *string*)

'CIÊNCIA DE DADOS'.lower()

'ciência de dados'.upper()

'ciência de dados'.title()

## Conjuntos 

Coleções do tipo conjunto (**set**) são exatamente o que se espera: uma coleção não-ordenada de elementos únicos que suporta operações matemáticas em conjuntos, como união, interseção, diferença, etc.  

   1. Para criar um conjunto vazio: **set**()
   2. Para criar um conjunto com valores: {*1*, *5*, *2*}
   3. A partir de outra coleção: **set(colecao)**
      * Esta operação irá construir um conjunto composto pelos valores únicos da coleção original, característica que pode ser usada para remover duplicatas em uma coleção

S = set('Estatística')

S

Por não ser uma coleção ordenada, não é possível acessar elementos por seus índices, mas naturalmente é possível testar se um elemento pertence a um conjunto.

'b' in S

'b' not in S

'a' in S

### Comparações de conjuntos

Os operadores relacionais <=, <, >= e > tem outros significados quando usados para comparar conjuntos permitindo testar se $S_1 \subseteq S_2$, $S_1 \subset S_2$,  $S_1 \supseteq S_2$ e $S_1 \supset S_2$, respectivamente.

S1 = {1, 2}
S2 = {1, 2, 3, 4}

S1 <= S2

S1 < S2

S1 >= S2

S1 > S2

A comparação de igualdade de dois conjuntos só retorna **True** sse $S_1 \subseteq S_2$ e $S_1 \supseteq S_2$, i.e. se ambos os conjuntos possuem exatamente os mesmos elementos:

{1, 2} == {1, 2}

Também pode ser útil verificar se dois conjuntos são disjuntos:

S1 = {0, 8}
S2 = {1, 2, 3, 4}

S1.isdisjoint(S2)

### Operações em dois ou mais conjuntos

Python também oferece operadores para realizar a união (|), interseção (&) e a diferença (-) de dois ou mais conjuntos e a diferença simétrica (^) entre dois conjuntos.

S1 = {1, 2, 3}
S2 = {2, 3, 4}
S3 = {5, 3, 4}

S1 | S2 | S3

S1 & S2 & S3

S1 - S2 - S3

S1 ^ S2

### Modificando um conjunto

Conjuntos são coleções mutáveis (há um outro tipo de conjunto, chamado **frozenset** que é imutável e pode ser útil em algumas situações), portanto suportam operações pra adicionar e remover elementos, no entanto os operadores **append**, **insert** e **del** que podem ser usados para as listas não suportados, pois assumem coleções ordenadas. Assim, para adicionar novos elementos a um conjunto, deve-se usar a operação **add** e para remover, pode-se usar **remove** (resulta em erro do tipo **KeyError**, se o elemento não pertencer ao conjunto) ou **discard** (executa apenas se o elemento pertencer ao conjunto).

S1.add(4)

S1

S1.remove(2)

S1

S1.remove(2)

S1.discard(3)

S1

S1.discard(3)

S1

## Dicionários

O último tipo de coleção que cobriremos neste livro são os dicionários (**dict**), coleções mutáveis que permitem realizar mapeamento de valores usando chaves únicas, que podem ser de vários tipos, mas são comumente *strings* ou números. Dicionários com chaves do tipo *string* são muito parecidos e facilmente convertidos de/para objetos do tipo *JSON*, muito utilizados em arquivos de configuração e para comunicação entre serviços Web. Um dicionário pode ser criado de várias formas, incluindo, mas não limitado a:

   1. Para criar um dicionário vazio: {} ou **dict**()
   2. Para criar um dicionário com valores: 
      1. {'one': *1*, 'two': *2*, 'three': *3*}
      2. **dict**(one=*1*, two=*2*, three=*3*)
      3. **dict**(\[(one, *1*), (two, *2*), (three, *3*)\])

### Operações em dicionários

Valores armazendos em dicionários são inseridos, acessados e removidos pelas suas chaves.

d = {'one': 1, 'two': 2, 'three': 3}

d

d['four'] = 4

d

d['two']

d['four'] = d['four'] + 1

d

del d['four']

d

A operação **del** retorna erro do tipo **KeyError** se a chave não existir no dicionário.

del d['four']

Para evitar esse erro, é importante checar se a chave existe dentro do dicionário. Como sempre, para checar pertinência, pode-se usar os operadores **in** e **not in**, que nesse caso operam sobre as chaves do dicionário.

'one' in d

'four' not in d

O erro **KeyError** também acontece ao tentar acessar uma chave que não existe no dicionário. Para evitar esse erro, pode-se usar a operação **get**, que retorna um valor padrão, caso a chave não esteja disponível. Caso o valor padrão não seja informado, **get** retorna o valor **None**, também conhecido como **null** em outras linguagens de programação.

d['four']

d.get('four', 0)

print(d.get('four'))

A operação **keys** retorna todas as chaves de um dicionário em um tipo de coleção (**dict_keys**), que nada mais é do que uma lista que atualiza automaticamente se as chaves do dicionário forem modificadas. No código abaixo, as chaves do dicionário serão obtidas e depois um novo mapeamento vai ser adicionado ao dicionário, modificando a lista de chaves obtida anteriormente.

keys = d.keys()

d['five'] = 5

keys

A operação **values** é similar à operação **keys**, mas retorna os valores dos mapeamentos do dicionário em um tipo de coleção (**dict_values**) que também se mantém atualizado quando o dicionário é modificado. No código abaixo, os valores do dicionário serão obtidos e depois um novo mapeamento vai ser adicionado, modificando a lista de valores obtida anteriormente.

values = d.values()

d['six'] = 6

values

Por fim, a operação **items** retorna os mapeamentos do dicionário em forma de tuplas em um tipo de coleção (**dict_items**) que também se mantém atualizado quando o dicionário é modificado. No código abaixo, os itens do dicionário serão obtidos e depois um novo mapeamento vai ser adicionado, modificando a lista de itens obtida anteriormente.

items = d.items()

d['seven'] = 7

items

## Coleções de coleções

Coleções podem armazenar valores de todos os tipos, incluindo outras coleções. Assim, podemos ter uma matriz representada por uma lista de listas. 

matrix = [[2, 0], [3, 1]]

Para acessar os elementos dessas coleções compostas, é preciso usar os índices ou chaves de cada nível. Por exemplo, para acessar o elemento de valor *0* presente na primeira lista (i.e. primeira linha), na segunda posição (segunda coluna), da matriz acima, podemos fazer:

matrix[0][1]

Outro exemplo comum é um dicionário que mapeia outros dicionários para configuração de experimentos (note as quebras de linha para deixar o código mais legível):

distributions = {
    'Gaussian': {
        'mean': 0,
        'variance': 1
    },
    'Beta':{
        'alfa': 1,
        'beta': 1
    }
}

distributions['Gaussian']['variance']

