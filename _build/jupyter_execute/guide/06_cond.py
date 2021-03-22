# Condições e Laços

Nesta Seção, veremos os primeiros tipos de blocos de códigos que podem ser definidos em Python. Blocos são regiões de código que realizam uma tarefa ou um conjunto de tarefas relacionadas. Essas regiões podem definir operações condicionais, iterações (operações repetidas), funções e tipos de dados. Blocos podem ser aninhados, ou seja, é possível definir blocos dentro de blocos, o que equivale à definição de sub-tarefas. Na maior parte das linguagens, os blocos de código são delimitados por algum marcador, como um par de chaves {} ou marcadores de início (*begin*) e fim (*end*), mas Python adota uma abordagem diferente.

## Blocos e indentação

A principal diferença de Python para outras linguagens, como R, C e Java, é a representação de blocos de código usando níveis de indentação, dispensando o uso de chaves para marcar o início e o fim dos blocos. Essa diferença pode ser vista nos blocos de código abaixo, representando a mesma função para calcular a média aritmética de dois valores. O primeiro código está escrito em R e o segundo contém exatamente a mesma função escrita em Python.

```R
mean <- function(value1, value2) {
  result <- (value1 + value2) / 2
  return(result)
}
```

def mean(value1, value2):
    result = (value1 + value2) / 2
    return result

O uso de indentação para indicar estrutura tem vários benefícios, incluindo:

   1. Reduz a necessidade de padrões de código extra: a indentação sempre será de 4 espaços e a IDE usada para escrever o código cuidará de manter essa consistência;
   2. Códigos de diferentes fontes são forçados a seguir o mesmo estilo de indentação;
   3. Reduz trabalho, pois não é necessário se preocupar com o padrão das chaves **e** da indentação;
   4. Mantém um código mais limpo;
   5. O código só executará se a indentação estiver correta, portanto, se o código parece correto, ele está correto;
   6. Não há como confundir escopos de blocos de código aninhados.

## Condições

Os operadores condicionais **if** (se), **elif** (senão se) e **else** (senão) são usados para definir blocos de código que serão executados apenas se certas condições forem satisfeitas, sendo, portanto, blocos de **controle de fluxo**, pois alteram o fluxo de execução do código, como mostra o fluxograma da {numref}`flow-if`.

:::{figure-md} flow-if
<img src="images/flow-if.svg" alt="Fluxograma com estrutura condicional"/>

luxograma com estrutura condicional.
:::

O fluxograma acima simula uma entrevista de emprego em que a única pergunta é se a pessoa que se candidatou à vaga entende de Python ou não. Em caso afirmativo, a pessoa é imediatamente contratada. Caso contrário, continuará desempregada. Esse tipo de situação pode ser lido como "**se** (**if**) a pessoa sabe Python, então está contratada; **senão** (**else**), está desempregada. Isso pode ser escrito em Python da seguinte forma:

knows_python = True

if knows_python == True:
    situation = 'hired'
else:
    situation = 'unemployed'

situation

Note que a variável *situation* não foi definida antes do bloco condicional. Isso não resulta em erro porque só há dois fluxos possíveis para o código, i.e. *knows_python ==* **True** ou *knows_python ==* **False**. Caso uma variável não seja definida em todos os fluxos possíveis, é possível que ocorra um erro. Por exemplo, suponha que, caso seja contratada, a pessoa receberá um salário de R$10000,00. Se a pessoa não souber Python e tentarmos acessar o salário, causaremos um erro.

knows_python = False

if knows_python == True:
    situation = 'hired'
    salary = 10000
else:
    situation = 'unemployed'

salary

Perceba que a linha que define o bloco condicional inicia com o operador **if**, seguido de uma expressão, e termina com dois pontos. A linha que define o caso contrário contém apenas **else:**. De um modo geral, o **if** testa se a expressão que o segue é **True** ou **False** e executa o bloco de código associado apenas se o resultado da expressão for **True**. Note que, como o operador **if** verifica se a expressão associada é **True**, o código acima é redundante e equivale ao seguinte teste: (*knows_python ==* **True**) *==* **True**. Em outras palavras, a condição poderia ser definida de forma mais simples da seguinte forma:

knows_python = True

if knows_python:
    situation = 'hired'
else:
    situation = 'unemployed'

situation

Ao dispensar a necessidade de escrever o teste de igualdade explicitamente, Python faz com que o código resultante seja escrito de forma próxima à linguagem natural.

Como vimos, o código acima testa se o valor de uma variável booleana é verdadeiro ou falso. Mas, curiosamente, Python também permite testar **True** ou **False** para outros tipos de valores, algo que, apesar de não muito intuitivo, mostra-se frequentemente útil. Os valores que testam **False** incluem **None** (nulo), o valor *0* de qualquer tipo numérico e coleções vazias , i.e. *''*, *()*, *\[ \]*, *{}*, **set**(), **range**(*0*). Todos os outros valores testam **True**.

if '':
    result = 'tested True'
else:
    result = 'tested False'

result

if None:
    result = 'tested True'
else:
    result = 'tested False'

result    

Isso permite testar facilmente se uma lista tem ou elementos ou não. Por exemplo:

if []:
    result = 'lista com elementos'
else:
    result = 'lista vazia'

result

A expressão associada ao **if** pode ser tão complexa quanto necessário, usando os operadores que vimos na [Seção 1.3](https://tmfilho.github.io/pyestbook/guide/04_oper.html) e chamadas de funções, que veremos na [Seção 1.6](https://tmfilho.github.io/pyestbook/guide/07_func.html). O código abaixo testa se a média de três valores é maior do que 3 (note que a expressão aritmética é avaliada antes da comparação):

x1 = 1
x2 = 4
x3 = 7

if (x1 + x2 + x3) / 3 > 3:
    result = 'Greater than 3'
else:
    result = 'Less than or equal to 3'

result

### Múltiplas condições

Os códigos acima todos testaram apenas situações binárias, ou seja, só há duas respostas possíveis. Para testar mais situações no mesmo bloco condicional, existem duas abordagens: testes com mais de uma situação usando o comando **elif** ou **ifs** aninhados. O comando **elif** equivale ao **else if** de outras linguagens de programação e pode ser lido como *senão se*. Vamos imaginar que a entrevista de emprego que simulamos acima não pergunte apenas se há ou não conhecimento de Python, mas quais linguagens de programação são dominadas pela pessoa que se candidatou. Se a pessoa não dominar linguagem alguma, ela continuará desempregada. Caso domine Python e R, será contratada como cientista de dados. Caso ela domine quaisquer linguagens, incluindo Python ou R (mas não as duas juntas), ela será contratada como desenvolvedora de software. Essa entrevista poderia ser escrita em Python da seguinte forma:

languages = ['Python', 'R']

if not languages:
    situation = 'unemployed'
elif 'Python' in languages and 'R' in languages:
    situation = 'data scientist'
else:
    situation = 'developer'

situation

languages = ['Python', 'JavaScript', 'C']

if not languages:
    situation = 'unemployed'
elif 'Python' in languages and 'R' in languages:
    situation = 'data scientist'
else:
    situation = 'developer'

situation

Agora vamos supor que a empresa irá categorizar seu novo cientista de dados como júnior, pleno ou sênior, dependendo da sua experiência. Se o candidato tiver menos de 3 anos de experiência, será contratado como cientista de dados júnior, com pelo menos 3 anos e menos de 5 será contratado como cientista de dados pleno e, com pelo menos 5 anos, cientista de dados sênior. Assim, o código Python da entrevista seria:

languages = ['Python', 'R']
experience = 4

if not languages:
    situation = 'unemployed'
elif 'Python' in languages and 'R' in languages:
    if experience < 3:
        situation = 'junior data scientist'
    elif experience < 5:
        situation = 'full data scientist'
    else:
        situation = 'senior data scientist'
else:
    situation = 'developer'

situation

## Laços

Os blocos condicionais alteram o fluxo do programa, mas são executados apenas uma vez. Para executar um bloco de código repetidas vezes, é necessário usar os operadores de laço, como **while** (enquanto) e **for** (para cada). 

### O comando while
O comando **while** executa um bloco de código enquanto uma expressão associada for avaliada como **True**, ou seja, ele funciona como um **if** que se repete. É preciso tomar cuidado ao usá-lo, pois se a expressão associada nunca deixar de ser avaliada como **True**, o código entrará em um laço infinito. Suponha que desejemos remover os elementos de uma lista e somá-los, de forma que, ao final da execução, a lista estará vazia e a variável *total* irá conter a soma desses valores. A operação *pop(0)* remove o primeiro elemento da lista (índice 0) e o retorna, nesse caso atribuindo-o à variável *value*.

l = [3, 1, 3, 5, 6]

total = 0

while l:
    value = l.pop(0)
    total = total + value

total

l

Note que a expressão testada pelo **while** é apenas a lista *l*. Como vimos anteriormente, uma lista é avaliada como **False** apenas quando está vazia, portanto, o laço **while** irá repetir até que a lista *l* torne-se vazia. Assim como o **if**, o **while** também pode ter um "caso contrário", i.e. um bloco definido pelo operador **else**, que irá executar apenas quando a expressão associada ao **while** for avaliada como **False**.

l = [3, 1, 3, 5, 6]

total = 0
message = 'the list is not empty'

while l:
    value = l.pop(0)
    total = total + value
else:
    message = 'the list is empty'
    
message

A execução do laço **while** pode ser afetada por dois comandos: **break** e **continue**. O comando **break** termina a execução do laço completamente, ou seja, nem mesmo o bloco associado ao **else** é executado. No código abaixo, se o valor 5 for encontrado enquanto a lista está sendo processada, a execução irá parar. Note que a variável *message* permanecerá inalterada, pois seu valor só é modificado no **else**. Além disso, a variável *total* irá conter apenas o valor 7 (3 + 1 + 3).

l = [3, 1, 3, 5, 6]

total = 0
message = 'the list is not empty'

while l:
    value = l.pop(0)
    if value == 5:
        break
        
    total = total + value
else:
    message = 'the list is empty'
    
message

total

O comando **continue**, por outro lado, faz o **while** voltar imediatamente para a avaliação da sua expressão associada, ignorando os passos restantes do seu bloco de código. No código abaixo, se o valor 5 for encontrado, ele será ignorado. Portanto, a variável *total* irá conter o valor 13 (3 + 1 + 3 + 6). A execução do **else** não é afetada.

l = [3, 1, 3, 5, 6]

total = 0
message = 'the list is not empty'

while l:
    value = l.pop(0)
    if value == 5:
        continue
        
    total = total + value
else:
    message = 'the list is empty'
    
message

total

### O comando for

O comando **for** é usado para iterar sobre os elementos de uma coleção (como uma lista, tupla ou string). Seu significado é "**para cada** elemento **na** coleção **faça**. O bloco de código associado é executado uma vez para cada elemento retornado pela coleção, na ordem em que os objetos são retornados. Quando os elementos acabam, as iterações terminam e, se houver um bloco **else** associado ao **for**, ele é executado. 

Assim como no **while**, é possível usar os comandos **break** e **continue**, mas seu uso neste contexto não é considerado boa prática, pois o **for** deve ser usado quando a quantidade de iterações é controlada, i.e. pela quantidade de elementos na lista. 

O **for** é comumente associado a coleções do tipo **range** que, como vimos na Seção anterior, define uma sequência de valores. Por exemplo, para somar todos os elementos em \[0, 5), pode-se fazer:

total = 0

for i in range(5):
    total += i

total

Para somar todos os elementos de uma lista, pode-se fazer (note que a lista continua preenchida):

l = [3, 1, 3, 5, 6]
total = 0

for i in l:
    total += i

total

l

Cada iteração do código acima atribui o novo elemento retornado pela lista à variável *i*, portanto ao final das iterações, *i* permanecerá com o último valor que lhe foi atribuído.

i

Naturalmente, se o laço não chegar a executar, a variável nunca receberá um valor. Por exemplo:

total = 0

for j in []:
    total += 0

j

Vimos, na Seção anterior, que coleções podem conter outras coleções. Isso significa que os elementos retornados pela coleção nas iterações do **for** podem ser outras coleções. Isso pode ser útil ao iterar sobre linhas de matrizes. Por exemplo:

matrix = [[2, 1], [3, 2]]

for row in matrix:
    print(row)

É possível realizar atribuições múltiplas para acessar os elementos individuais:

matrix = [[2, 1], [3, 2]]

for [i, j] in matrix:
    print(i + j)

Quando iteramos sobre strings, acessamos cada caractere sequencialmente:

for c in 'Estatística':
    print(c)

Quanto iteramos sobre dicionários, acessamos suas chaves:

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

for key in distributions:
    parameters = distributions[key]
    print(parameters)

### Compreensão de listas

Compreensão de lista (*list comprehension*) é um mecanismo que permite construir coleções de forma concisa a partir dos resultados de operações sobre cada membro de outras coleções. Por exemplo, o código abaixo gera uma lista com os quadrados dos valores em **range**(10), usando **for**, como vimos acima:

squares = []
for x in range(10):
    squares.append(x**2)
    
squares

A mesma lista pode ser criada usando compreensão de listas como segue:

squares = [x**2 for x in range(10)]

squares

A compreensão de listas usa um **for** para atribuir cada elemento do **range** à variável *x*, cujo quadrado é então colocado na nova lista *squares*. Ao final das iterações, a variável *x* mantém o último valor que lhe foi atribuído.

x

Não é necessário que a coleção resultante da compreensão de listas tenho o mesmo número de elementos da coleção original. Por exemplo, o código abaixo só calcula os quadrados dos elementos pares (note o **if** aninhado no **for**):

squares = [x**2 for x in range(10) if x % 2 == 0]

squares

Também é possível usar o operador **else** em compreensão de listas. Nesse caso, o **if** e o **else** devem vir antes do **for**, formando uma estrutura conhecida como operador ternário (<valor\> **if** <expressão\> **else** <outro_valor\>):

squares = [x**2 if x % 2 == 0 else x for x in range(10)]

squares

Note que o **if** só vem antes do **for** se for parte de um operador ternário, i.e. **if** sem **else** antes do **for** provoca erro de sintaxe:

[x**2 if x % 2 == 0 for x in range(10)]

