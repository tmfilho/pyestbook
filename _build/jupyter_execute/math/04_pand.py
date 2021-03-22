# Pandas 

O pacote *pandas* é uma das ferramentas de *Python* mais importantes para cientistas e analistas de dados atualmente. Ele é a base da maior parte dos projetos que incluem leitura, manipulação, limpeza e escrita de dados. O nome *pandas* é derivado do termo *panel data* (dados em painel), que é um termo econométrico que descreve dados compostos de múltiplas observações através do tempo para os mesmos indivíduos.

*Pandas* foi desenvolvido como uma camada acima do *NumPy*, mas boa parte de suas funcionalidades de análise estatística são feitas pelo *SciPy*, além do uso do *Matplotlib* para funções de visualização. Dessa forma, *pandas* simplifica o uso de diversas bibliotecas úteis para estatísticos e cientistas de dados.

Os dois principais objetos de *pandas* são as séries (*Series*) e as tabelas (*DataFrame*). Uma *Series* é basicamente uma coluna, enquanto uma *DataFrame* é uma tabela multidimensional composta de uma coleção de Series. Exemplo:

import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])

s

A Series acima foi criada por meio de uma lista de valores, incluindo o valor *NaN* (*not a number*), que equivale a uma posição nula. A lista de valores foi passada para o construtor *pd.Series* e *pandas* criou um índice númerico para cada linha e determinou o tipo de  que melhor se representaria os dados (*float64*). Note que todos os valores passados foram inteiros, menos o *NaN*, cujo valor é tratado como *float64*. A criação de *DataFrames* também é muito simples, porém muito versátil. No exemplo abaixo, criamos uma *DataFrame* composta por uma matriz de inteiros. Após a chamada ao construtor *pd.DataFrame*, *pandas* cria um índice númerico para cada linha e atribui um número como título de cada coluna.

pd.DataFrame(np.arange(12).reshape(4, 3))

Podemos passar mais informações ao construtor da *DataFrame*, como um nome para cada coluna:

pd.DataFrame(
    np.arange(12).reshape(4, 3),
    columns=['A', 'B', 'C']
)

Podemos também criar um índice customizado para cada linha. Por exemplo, vamos criar um índice com um intervalo de datas:

dates = pd.date_range(
    '20200101', periods=4
)  # experimente trocar a string da data por 'today'

pd.DataFrame(
    np.arange(12).reshape(4, 3),
    index=dates,
    columns=['A', 'B', 'C']
)

Uma outra forma de criar uma *DataFrame* é passar um dicionário com objetos que podem ser convertidos a objetos do tipo *Series*.

df = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': list('abcd')
})

df

Note que as colunas resultantes tem tipos diferentes:

df.dtypes

## Acessando os dados

O pacote oferece diversas formas de acessar os dados contidos em uma *DataFrame*. Por exemplo, para acessar as primeiras linhas, usa-se o método *head*:

df2 = pd.DataFrame(
    np.arange(200).reshape(40, 5),
    columns=list('ABCDE')
)

df2.head()

Se o método *head* for chamado sem parâmetro algum, ele irá retornar as cinco primeiras linhas da *DataFrame*. Caso receba um número inteiro, o método irá retornar a quantidade desejada.

df2.head(2)

De forma similar, podemos acessar as últimas linhas da *DataFrame*:

df2.tail()

df2.tail(3)

Para listar o índice e as colunas:

df2.index

df2.columns

Para verificar o formato da tabela, usa-se o atributo *shape*:

df2.shape

O método *to_numpy* fornece uma representação dos dados na forma de um *array* de *NumPy*. Isso pode ser uma operação simples, caso os dados da *DataFrame* sejam homogêneos:

df2.to_numpy()

No entanto, como *arrays* de *NumPy* devem ser homogêneos, no caso de *DataFrames* heterogêneas, a operação pode ser custosa, porque *pandas* vai precisar encontrar o tipo que melhorar representará todos os dados em um *array*. Por vezes, esse tipo pode terminar sendo *object*. 

df.to_numpy()

Note que o índice e os nomes das colunas não aparecem na saída de *to_numpy*. Para transpor a *DataFrame*, basta accessar o atributo *T*:

df2.T

Para acessar uma única coluna, retornada como uma *Series*, podemos usar notação de colchetes ou de atributo:

df['E']

df.E

Para acessar linhas pelos seus índices, podemos usar o atributo *loc*:

dates = pd.date_range(
    '20200101', periods=6
)

df3 = pd.DataFrame(
    np.arange(18).reshape(6, 3),
    index=dates,
    columns=['A', 'B', 'C']
)

df3.loc[dates[0]]

O atributo *loc* também permite acessar listas de índices, bem como especificar quais colunas devem ser retornadas:

df3.loc[[dates[2], dates[4]]]

df3.loc[[dates[2], dates[4]], ['A', 'C']]

Se apenas um índice e uma coluna forem especificados, *pandas* retornará o valor correspondente da tabela:

df3.loc[df3.index[0], 'B']

Note a diferença de comportamento se a única coluna for informada dentro de uma lista:

df3.loc[df3.index[0], ['B']]  # retorna uma Series com apenas um elemento

Para acessar apenas um valor de forma mais rápida, o atributo *loc* pode ser substituído por *at*:

df3.at[df3.index[0], 'B']

Similar ao *loc*, o atributo *iloc* também permite acessar os dados da *DataFrame*, porém ao invés de acessar através dos valores dos índices, ele permite acessar pelas posições das linhas. Exemplo:

df3.iloc[0]  # equivale a df3.loc[df3.index[0]]

As colunas também são tratadas numericamente por *iloc*. Inclusive, é possível usá-lo para acessar fatias da tabela, assim como em um *array* de *NumPy*:

df3.iloc[0, [0, 2]]

df3.iloc[0, 0]

df3.iloc[0:2, 0:2]  # exclui o final

Continuando as similaridades com *arrays*, também é possível acessar os dados de uma *DataFrame* usando condições booleanas:

df2[df2.A % 2 == 0]  # apenas as linhas em que a coluna A é par

df2[df2 % 2 == 0]  # Apenas os valores pares

O método *isin* permite filtrar dados:

df[df['F'].isin(['a', 'd'])]

Além de acessar dados, *loc*, *iloc*, *at* e *iat* permitem atribuir valores às posições indicadas:

df3.iloc[2] = 1

df3

df3.loc['20200101', 'C'] = 10

df3

df3.iat[2, 2] = -5

df3

Também é possível usar máscaras booleanas para atribuir valores:

df2[df2 % 2 == 0] = -df2

df2

Para adicionar uma nova coluna, basta usar a notação de colchetes com o nome da nova coluna:

df2['F'] = 1

df2

## Estatística descritiva

O pacote *pandas* oferece diversas funções para análise de Estatística descritiva. A mais geral dessas funcionalidades é o método *describe*, que computa uma variedade de medidas:

df2.describe()

É possivel selecionar os percentis que serão incluídos (a mediana é sempre retornada por padrão):

df2.describe(percentiles=[.05, .25, .75, .95])

Para colunas não-númericas, *describe* retorna um sumário mais simples:

df['E'].describe()

Numa *DataFrame* com tipos mistos, *describe* irá incluir apenas as colunas numéricas:

frame = pd.DataFrame({'a': ['Yes', 'Yes', 'No', 'No'], 'b': range(4)})

frame.describe()

Esse comportamento pode ser controlado pelos argumentos *include* e *exclude*:

frame.describe(include=['object'])

frame.describe(include=['number'])

frame.describe(include=['object', 'number'])

frame.describe(include='all')

Cada uma das funções separadas de estatística descritiva pode ser calculada para um dado eixo (*axis*), assim como *NumPy*:

df = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
    'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
    'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})

df

df.mean(0)

df.mean(1)

Diferente de *NumPy*, se o eixo não for informado, o padrão é *axis=0* (*NumPy* calcula a média para o *array* todo).

df.mean()

Note que os valores *NaN* são descartados. Isso pode ser controlado pelo argumento *skipna*, que é *True* por padrão:

df.mean(0, skipna=False)

Combinando comportameto aritmético e *broadcasting*, é possível realizar operações estatísticas, como a padronização (média 0 e desvio 1), de forma concisa:

df_stand = (df - df.mean()) / df.std()

df_stand.std()

df_stand = df.sub(df.mean(1), axis=0).div(df.std(1), axis=0)

df_stand.std(1)

Métodos como *cumsum* (soma acumulada) e *cumprod* (produto acumulado) preservam a posição de valores *NaN*:

df.cumsum()

df.cumprod(1)

A tabela abaixo oferece um sumário de funções comumente usadas:


| Função        | Convenção           |
|------------- |-------------|
| *count*      | número de observações não-*NaN* |
| *sum* | soma dos valores      |
| *mean*      | média dos valores     |
| *mad* | desvio absoluto médio      |
| *median* | mediana dos valores      |
| *min* | mínimo      |
| *max* | máximo     |
| *mode* | moda      |
| *abs* | valores absolutos      |
| *prod* | produto dos valores      |
| *std* | desvio padrão amostral      |
| *var* | variância amostral      |
| *skew* | assimetria amostral      |
| *kurt* | curtose amostral    |
| *quantile* | quantis amostrais    |
| *cumsum* | soma acumulada    |
| *cumprod* | produto acumulado    |
| *cummax* | máximo acumulado    |
| *cummin* | mínimo acumulado  |

As funções *idxmin* e *idxmax* retornam os índices dos menores e maiores valores, respectivamente, através do eixo informado:

df.idxmin(0)

df.idxmax(1)

Os objetos do tipo *Series* disponibilizam um método chamado *value_counts* (que também pode ser usado como uma função) que computa um histograma de um *array* unidimensional:

data = np.random.randint(0, 7, size=50)

data

s = pd.Series(data)

s.value_counts()

pd.value_counts(data)

Valores contínuos podem ser discretizados usando as funções *cut* (intervalos baseados nos valores) e *qcut* (intervalos baseados nos quantis).

arr = np.random.randn(20)

factor = pd.cut(arr, 4)

factor

factor = pd.cut(arr, [-5, -1, 0, 1, 5])

factor

pd.value_counts(factor)

factor = pd.qcut(arr, [0, .25, .5, .75, 1])

factor

pd.value_counts(factor)

## Ordenando valores

Três formas de ordenação estão disponíveis em *pandas*: pelos índices, pelas colunas e pelas duas coisas. Os métodos *Series.sort_index()* e *DataFrame.sort_index()* são usados para ordenar objetos *pandas* pelos seus índices:

df = pd.DataFrame({
     'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
     'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
     'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})

df

df.sort_index(ascending=False)

df.sort_index(axis=1)

df['three'].sort_index(ascending=False)

O método *Series.sort_values()* é usado para ordenar uma *Series* pelos seus valores. Já o método *DataFrame.sort_values()* pode ser usado para ordenar uma *DataFrame* pelos valores das linhas ou das colunas e tem um parâmetro opcional *by=* que serve para especificar uma ou mais colunas para determinar a ordem.

df1 = pd.DataFrame({'one': [2, 1, 1, 1],
                    'two': [1, 3, 2, 4],
                    'three': [5, 4, 3, 2]})

df1

df1.sort_values(by='two')

df1[['one', 'two', 'three']].sort_values(by=['one', 'two'])

Esses métodos tem um tratamento especial para valores faltantes, por meio do parâmetro *na_position*:

s = pd.Series(
    ['A', 'B', np.nan, 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'],
    dtype="object"
)

s.sort_values()

s.sort_values(na_position='first')

Strings passadas para o argumento *by=* podem se referir a colunas ou nomes de índices. Aliás, esse é um bom momento para introduzir índices múltiplos:

idx = pd.MultiIndex.from_tuples(
    [('a', 1), ('a', 2), ('a', 2), ('b', 2), ('b', 1), ('b', 1)]
)

idx.names = ['first', 'second']

df_multi = pd.DataFrame(
    {'A': np.arange(6, 0, -1)},
    index=idx
)

df_multi

df_multi.sort_values(by=['second', 'A'])

*Series* também oferece os métodos *nsmallest()* e *nlargest()*, que retornam os menores ou maiores *n* valores, o que pode ser bem mais eficiente do que ordenar a *Series* toda só para chamar *tail(n)* ou *head(n)* no resultado. Esses métodos também são oferecidos por *DataFrames* e é preciso informar a(s) coluna(s) desejada(s).

s = pd.Series(np.random.permutation(10))

s

s.sort_values()

s.nsmallest(3)

s.nlargest(2)

df = pd.DataFrame({'a': [-2, -1, 1, 10, 8, 11, -1],
                   'b': list('abdceff'),
                   'c': [1.0, 2.0, 4.0, 3.2, np.nan, 3.0, 4.0]})
df

df.nlargest(3, 'a')

df.nsmallest(5, ['a', 'c'])

## Combinando *Series* e *DataFrames*

*Pandas* oferece diversas formas para combinar objetos *Series* e *DataFrames*, usando lógica de conjuntos para os índices e colunas e álgebra relacional para operações do tipo *join* (que remetem a operações de bancos de dados SQL).

A função *concat* faz o trabalho de concatenação ao longo de um eixo (*axis*), usando lógica de conjuntos (união ou interseção) dos índices ou colunas no outro eixo, se o outro eixo existir (*Series* tem apenas um eixo). Um exemplo:

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])
 

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7])
 

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])


frames = [df1, df2, df3]
result = pd.concat(frames)
result

Suponha que você queira associar chaves específicas para os dados que pertenciam a cada *DataFrame* original. Para isso, pode-se usar o argumento *keys*:

result = pd.concat(frames, keys=['x', 'y', 'z'])
result

O mesmo efeito pode ser obtido passando um dicionário com as *DataFrames* parciais:

pieces = {'x': df1, 'y': df2, 'z': df3}

result = pd.concat(pieces)

result

O objeto resultante da concatenação passou a ter um índice múltiplo e hierárquico, o que permite selecionar cada bloco original usando o atributo *loc*. Note que no *jupyter notebook*, ao passar o ponteiro do *mouse* sobre um dos índices, as linhas que pertencem a ele são destacadas.

result.loc['y']

result.index.levels

O uso da função *concat* realiza uma cópia dos dados, então ela não deve ser usada iterativamente, i.e. se seus dados são gerados por um processo repetido, o ideal é guardar as *DataFrames* parciais em uma lista e aplicar *concat* uma única vez.

Ao juntar múltiplas *DataFrames*, é possível escolher como lidar com os outros eixos de duas formas usando o argumento *join*:

  1. Tomando a união, i.e. *join='outer'*. Essa é a opção padrão e nunca resulta em perda de informação.
  2. Tomando a interseção, i.e. *join='inner'*.

Primeiro vejamos um exemplo de *join='outer'*:

df1

df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']},
                    index=[2, 3, 6, 7])
df4

result = pd.concat([df1, df4], axis=1, sort=False)
result

result = pd.concat([df1, df4], axis=0, sort=False)
result

result = pd.concat([df1, df4], axis=1, join='inner')
result

result = pd.concat([df1, df4], axis=0, join='inner')
result

Para *DataFrames* que não possem índices importantes, é possível concatená-las e ignorar os índices originais, o que pode ser útil quando existem índices repetidos, como no exemplo acima. Para isso, usa-se o argumento *ignore_index*.

result = pd.concat([df1, df4], axis=0, ignore_index=True, join='inner')
result

result = pd.concat([df1, df4], axis=1, ignore_index=True, join='inner')
result

É possível concatenar uma mistura de objetos *Series* e *DataFrame*. Internamente, *pandas* transforma a(s) *Series* em *DataFrame(s)* com apenas um coluna com o(s) mesmo(s) nome(s) da(s) *Series*.

s1 = pd.Series(['X0', 'X1', 'X2', 'X3'], name='X')

pd.concat([df1, s1], axis=1)

Caso a(s) *Series* não tenha(m) nome, o(s) nome(s) será(ão) atribuído(s) numericamente e consecutivamente:

s2 = pd.Series(['_0', '_1', '_2', '_3'])

pd.concat([df1, s2, s2, s2], axis=1)

pd.concat(
    [df1, s1], axis=1, ignore_index=True
)  # todas as colunas perdem seus nomes

O argumento *keys* tem um uso interessante que é sobrescrever os nomes das colunas quando uma nova *DataFrame* é criada por meio da concatenação de várias *Series*. Note que o comportamento padrão, como vimos acima, é que a *DataFrame* resultante use o nome de cada *Series* como nome para a coluna resultante (caso a *Series* tenha nome).

s3 = pd.Series([0, 1, 2, 3], name='foo')

s4 = pd.Series([0, 1, 2, 3])

s5 = pd.Series([0, 1, 4, 5])

pd.concat([s3, s4, s5], axis=1)

pd.concat([s3, s4, s5], axis=1, keys=['red', 'blue', 'yellow'])

Mesmo não sendo muito eficiente (porque um novo objeto precisa ser criado), é possível adicionar um única linha nova a uma *DataFrame* passando uma *Series* para o método *append*.

s2 = pd.Series(['X0', 'X1', 'X2', 'X3'], index=['A', 'B', 'C', 'D'], name='t')
df1.append(s2)

Caso a *Series* não tenha nome, é necessário usar o argumento *ignore_index*:

s2 = pd.Series(['X0', 'X1', 'X2', 'X3'], index=['A', 'B', 'C', 'D'])
df1.append(s2, ignore_index=True)

## Iterando sobre objetos

O comportamento de iteração em objetos *pandas* depende do tipo. Ao iterar sobre uma *Series*, o comportamento é igual a um *array* unidimensional, produzindo os seus valores.

for value in s2:
    print(value)

No caso de *DataFrames*, *pandas* itera sobre as colunas, como se estivesse iterando sobre as chaves de um dicionário.

for col in df1:
    print(col)

Para iterar sobre as linhas de uma *DataFrame*, *pandas* oferece os seguintes métodos: *iterrows()* e *itertuples()*. O método *iterrows()* retorna as linhas de uma *DataFrame* como pares (índice, *Series*). Como cada linha é retornada como uma *Series*, valores de colunas com tipos diferentes são convertidos para o tipo mais geral.

df = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c']})

for row_index, row in df.iterrows():
    print(row_index, row, sep='\n')

O método *itertuples()*, por outro lado, retorna uma tupla nomeada para cada linha da *DataFrame*. O primeiro elemento da tupla será o índice e cada elemento seguinte corresponderá ao valor em cada coluna na linha. Caso o nome da coluna não possa ser convertido para um identificador Python válido, ele será substituído para um nome posicional. Se o número de colunas for maior do 255, tuplas comuns são retornadas. 

for row in df.itertuples():
    print(row)

df = pd.DataFrame({'1': [1, 2, 3], '2': ['a', 'b', 'c']})

for row in df.itertuples():
    print(row)

## Dividindo um objeto em grupos

Objetos *pandas* podem ser divididos através de qualquer de seus eixos por meio de um mapeamento de valores para nomes de grupos. Essa operação cria um objeto do tipo *GroupBy*.

df = pd.DataFrame([('bird', 'Falconiformes', 389.0),
                   ('bird', 'Psittaciformes', 24.0),
                   ('mammal', 'Carnivora', 80.2),
                   ('mammal', 'Primates', np.nan),
                   ('mammal', 'Carnivora', 58)],
                  index=['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
                  columns=('class', 'order', 'max_speed'))

df

grouped = df.groupby('class')
print(grouped)

Note que objetos do tipo *GroupBy* não têm comportamento definido de impressão. Eles existem para facilitar operações agrupadas. No entanto, é possível iterar sobre os diferentes grupos:

for name_of_the_group, group in grouped:
    print(name_of_the_group)
    print(group)
    print()

grouped = df.groupby('order', axis='columns')

for name_of_the_group, group in grouped:
    print(name_of_the_group)
    print(group)
    print()

grouped = df.groupby(['class', 'order'])

for name_of_the_group, group in grouped:
    print(name_of_the_group)
    print(group)
    print()

Por padrão, as chaves dos grupos são ordenadas para realizar o agrupamento, mas é possível desativar esse comportamento usando *sort=False* para aumentar a performance da operação.

df2 = pd.DataFrame({'X': ['B', 'B', 'A', 'A'], 'Y': [1, 2, 3, 4]})

df2.groupby(['X']).sum()

df2.groupby(['X'], sort=False).sum()

Apesar de ordenar as chaves dos grupos por padrão, o agrupamento mantém a ordem original das observações em cada grupo.

df3 = pd.DataFrame({'X': ['A', 'B', 'A', 'B'], 'Y': [1, 4, 3, 2]})

df3.groupby(['X']).get_group('A')

df3.groupby(['X']).get_group('B')

Uma vez que um objeto *GroupBy* é criado, é possível usá-lo para realizar diversas operações de agregação de forma bastante eficiente, usando os métodos *aggregate* e *agg*.

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]


index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
    
    
df = pd.DataFrame({'A': [1, 1, 1, 1, 2, 2, 3, 3],
                   'B': np.arange(8)},
                   index=index)

grouped = df.groupby('A')

grouped.aggregate(np.sum)

grouped.aggregate([np.sum, np.mean, np.std])

Outra operação agregada simples pode ser feita usando o método *size* que retorna a quantidade de elementos em cada grupo:

grouped.size()

É possível controlar o nome das colunas resultantes das operações de agregação por meio de um sintaxe especial no método *agg()*, chamada de agregação nomeada. Nesse caso, os argumentos serão os nomes das colunas resultantes e os valores dos argumentos serão tuplas, cujo primeiro elemento é a coluna a ser agregada e o segunda é a função de agregação a ser aplicada. A função de agregação pode ser passada como *string* ou pelo seu nome (e també pode ter sido criada pelo usuário).

animals = pd.DataFrame({'kind': ['cat', 'dog', 'cat', 'dog'],
                        'height': [9.1, 6.0, 9.5, 34.0],
                        'weight': [7.9, 7.5, 9.9, 198.0]})




animals.groupby("kind").agg(
    min_height=pd.NamedAgg(column='height', aggfunc='min'),
    max_height=pd.NamedAgg(column='height', aggfunc='max'),
    average_weight=pd.NamedAgg(column='weight', aggfunc=np.mean),
)

## Lendo e escrevendo dados

*Pandas* consegue ler e escrever arquivos de diversos tipos, incluindo *csv*, *excel*, *json*, *HDF5*, *SAS*, *SPSS* e outros. Os tipos disponíveis podem ser visualizados na [documentação de entrada e saída](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html). De uma maneira geral, as funções de leitura tem assinatura *read_tipo*, e.g. *read_csv*, e podem ler arquivos locais ou remotos, enquanto os métodos de escrita tem assinatura *to_tipo*, e.g. *to_csv*. O código abaixo lê um arquivo *csv* hospedado em um repositório do *Github* e calcula as correlações entre as colunas. O parâmetro *index_col* indica qual coluna do arquivo *csv* deve ser usada como índice da tabela. Por padrão, supõe-se que cada coluna de um arquivo *csv* é separada por vírgulas. Isso pode ser modificado por meio do parâmetro *sep*. 

url = 'https://tmfilho.github.io/pyestbook/data/google-trends-timeline.csv'
trends = pd.read_csv(url, index_col=0, parse_dates=True, sep=',')

trends

trends.corr(method='spearman')  # method é opcional

Os dados lidos são compostos por séries temporais com 260 observações, que representam o interesse mundial por quatro tópicos de buscas no Google: Python, R, aprendizagem de máquina e ciência de dados. A quantidade de buscas de cada tópico foi medida semanalmente. O argumento *parse_dates* indica que as datas no índice da *DataFrame* devem ser tratadas como objetos *datetime*, não como *strings*.

trends.index

trends.index[0].weekday()

O argumento *parse_dates* pode receber diferentes valores, tendo comportamentos diferentes:

  1. boolean: Se True -> tentar tratar o índice;
  2. list de inteiros ou nomes: Se [1, 2, 3] -> tentar tratar colunas 1, 2 e 3 como colunas separadas de datas;
  3. list de lists: Se [[1, 3]] -> combinar colunas 1 e 3 e tratar como uma única coluna de datas;
  4. dict: Se {‘foo’ : [1, 3]} -> tratar colunas 1 e 3 como datas e chamar a coluna resultante de *foo*.

Se uma das colunas especificadas ou um índice possuir um valor não tratável ou uma mistura de fusos horários, seus valores serão retornados não-tratados com tipo *object*.

Para escrever uma *DataFrame* em um arquivo *csv*, pode-se usar o método *to_csv*:

trends.to_csv('google-trends-timeline.csv')

Se nenhum diretório for especificado, a *DataFrame* será escrita em um arquivo com o nome informado, localizado no mesmo diretório do *script* *Python* que chamou o método. Caso o método tenha sido chamado em um *script* interno de um projeto, o arquivo será salvo no mesmo diretório do *script* que contém o *main*.

## Tabelas pivotadas

*Pandas* fornece a função *pivot_table()* para pivotar tabelas agregando dados numéricos. A ação de pivotar envolve um agrupamento (*GroupBy*) seguido da aplicação de função(ões) de agregação. A função *pivot_table()* recebe os seguintes argumentos:


  1. data: uma *DataFrame*.
  2. values: uma coluna ou lista de colunas cujos valores serão agregados.
  3. index: coluna(s), um objeto do tipo *Grouper* ou *array* que será usado como índice para as linhas da tabela resultante.
  4. columns: coluna(s), um objeto do tipo *Grouper* ou *array* que define as colunas da tabela resultante.
  5. aggfunc: função(ões) para realizar a agregação, com *numpy.mean* por padrão.

Exemplo:

import datetime

df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 6,
                   'B': ['A', 'B', 'C'] * 8,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 4,
                   'D': np.random.randn(24),
                   'E': np.random.randn(24),
                   'F': [datetime.datetime(2013, i, 1) for i in range(1, 13)]
                   + [datetime.datetime(2013, i, 15) for i in range(1, 13)]})


df

pd.pivot_table(
    df, 
    values='D', 
    index=['A', 'B'], 
    columns=['C']
)

pd.pivot_table(
    df, 
    values='D', 
    index=['B'], 
    columns=['A', 'C'], 
    aggfunc=np.sum
)

pd.pivot_table(
    df, 
    values=['D', 'E'], 
    index=['B'], 
    columns=['A', 'C'], 
    aggfunc=np.sum
)

O objeto resultante é uma *DataFrame* com índices e colunas potencialmente hieráquicos. Se o argumento *values* não for especificado, a tabela pivotada irá conter todas as colunas que podem ser agregadas em um nível adicional de hierarquia nas colunas:

pd.pivot_table(df, index=['A', 'B'], columns=['C'])

Um objeto *Grouper* pode ser usado para os argumentos *index* e *columns*. No código abaixo, *Grouper* é usado para definir um agrupamento mensal das datas da coluna *'F'*. Para mais possibilidades de frequência e agrupamento, ver a [documentação de Grouper](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases).

pd.pivot_table(
    df, 
    values='D', 
    index=pd.Grouper(freq='M', key='F'),
    columns='C'
)

Para imprimir a tabela resultante usando uma representação mais interessante para os dados faltantes, pode-se usar o método *to_string*:

table = pd.pivot_table(df, index=['A', 'B'], columns=['C'])

print(table.to_string(na_rep=''))

print(table.to_string(na_rep='X'))

A função *pivot_table()* é frequentemente usada para agregar resultados de experimentos. Exemplo:

df = pd.DataFrame(
    {
        'accuracy': np.random.rand(40),
        'cross-entropy': np.random.rand(40) * 5,
        'method': ['LR'] * 10 + ['DT'] * 10 + ['SVM'] * 10 + ['NB'] * 10
    }
)


df

results = pd.pivot_table(
    df, 
    values=['accuracy', 'cross-entropy'], 
    index='method',
    aggfunc=[np.mean, np.std]
)

results

Após a geração da tabela pivotada com os resultados, pode-se gerar a tabela em formato de código *LaTeX*, para inclusão em artigos e relatórios:

results.to_latex()

O retorno de *to_latex()* inclui barras duplas e quebras de linhas com *\n* pois elas são necessárias para retornar barras dentro de *strings* Python.

\begin{tabular}{lrrrr}
\toprule
{} & \multicolumn{2}{l}{mean} & \multicolumn{2}{l}{std} \\
{} &  accuracy & cross-entropy &  accuracy & cross-entropy \\
method &           &               &           &               \\
\midrule
DT     &  0.365762 &      2.227704 &  0.326730 &      1.327534 \\
LR     &  0.314544 &      2.995433 &  0.250636 &      1.146052 \\
NB     &  0.439088 &      2.596552 &  0.286103 &      1.748327 \\
SVM    &  0.631967 &      2.153559 &  0.296118 &      1.059571 \\
\bottomrule
\end{tabular}

## Reindexando e alterando rótulos

Suponha que você tem dados provenientes de fontes diferentes. As tabelas tem colunhas e linhas em comum e outras diferentes. Você quer trabalhar com os dados em comum, e preencher os valores faltantes de alguma forma. Além disso, você quer que os dados estejam dispostos em uma ordenação específica através dos índices e das colunas. Tudo isso pode ser realizado por meio do método *reindex()*, que é a forma principal de "realinhar" dados em *pandas*. Reindexar significa ajustar os dados a um dado conjuntode rótulos através de um eixo. Isso permite reordenar os dados existentes, inserir posições faltantes onde não existem dados para os rótulos passados e preencher esses dados faltantes. Exemplo:

s = pd.Series(
    np.random.randn(5), 
    index=['a', 'b', 'c', 'd', 'e']
)

s

s.reindex(['e', 'b', 'f', 'd'])

Note que o rótulo 'f' não estava presente na *Series*, aparecendo como *NaN* no resultado. No caso de *DataFrames*, é possível reindexar índices e colunas simultaneamente:

df = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
    'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
    'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})

df

df.reindex(
    index=['c', 'f', 'b'], 
    columns=['three', 'two', 'one']
)

O método *reindex()* também pode ser usado com o argumento *axis*:

df.reindex(['c', 'f', 'b'], axis='index')

df.reindex(['c', 'f', 'b'], axis='columns')

df.reindex(['three', 'two', 'one'], axis='columns')

df.reindex(['three', 'two', 'one'], axis='index')

Objetos do tipo *Index* podem ser compartilhados entre objetos *Series* e *DataFrame* por meio do método *reindex*:

rs = s.reindex(df.index)

rs

rs.index is df.index

Para reindexar um objeto, de forma que ele fique perfeitamente "alinhado" com outro, pode-se usar o "atalho" *reindex_like()*:

df

df2 = pd.DataFrame({
    'two': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
    'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
})

df2

df.reindex_like(df2)

A operação de reindexação torna-se mais importante quando é necessário escrever códigos cujo desempenho é fator essencial. Diversas operações são realizadas mais rapidamente sobre dados pré-alinhados, como as operações aritméticas, que precisam disparar um realinhamento interno, se os dados não estiverem alinhados.

Caso seja interessante alinhar dois objeto simultaneamente, pode-se usar o método *align* (ao invés de duas chamadas ao método *reindex*). O método *align* retorna uma tupla com os dois objetos realinhados e aceita o argumento *join* para indicar a forma como os objetos serão alinhados:

  1. join='outer': toma a união dos índices (default);
  2. join='left': usa o índice do objeto que chama o método;
  3. join='right': usa o índice do objeto passado como parâmetro;
  4. join='inner': toma a interseção do síndices.

Exemplos:

s = pd.Series(
    np.random.randn(5), 
    index=['a', 'b', 'c', 'd', 'e']
)

s1 = s[:4]
s2 = s[1:]
s1.align(s2)

s1.align(s2, join='inner')

s1.align(s2, join='left')

Para *DataFrames*, o *join* é aplicado aos índices e às colunas por padrão:

df

df2

df.align(df2, join='inner')

Usando o argumento *axis*, é possível especificar a qual eixo o *join* deve ser aplicado:

df.align(df2, join='inner', axis=0)

Ao passar uma *Series* ao método *align* de uma *DataFrame*,é possível escolher alinhas ambos os objetos de acordo com o índice ou com as colunas da *DataFrame*, usando o argumento *axis*:

df.align(df2.iloc[0], axis=1)

### Preenchendo valores faltantes

O método *reindex* pode receber um parâmetro opcional que determina uma forma de preencher dados faltantes. Os valores possíveis para esse argumento são:

  1. pad/ffill: preenche os valores para a frente;
  2. bfill/backfill: preenche os valores para trás;
  3. nearest: preenche com os valores do índice mais próximo.
  
Exemplos:

rng = pd.date_range('1/3/2000', periods=8)

ts = pd.Series(np.random.randn(8), index=rng)

ts2 = ts[[0, 3, 6]]

ts

ts2

ts2.reindex(ts.index)

ts2.reindex(ts.index, method='ffill')

ts2.reindex(ts.index, method='bfill')

ts2.reindex(ts.index, method='nearest')

Note que esses métodos de preenchimento precisam que os índices estejam ordenados (em ordem ascendente ou decrescente). Caso seja desejável limitar o preenchimento de dados faltantes, para evitar que valores muito distantes sejam usados, pode-se usar os argumentos *limit* e *tolerance*. *Limit* especifica o número máximo de preenchimentos consecutivos:

ts2.reindex(ts.index, method='ffill', limit=1)

*Tolerance* especifica o intervalo máximo entre o índice faltante e o índice que será usado para preenchê-lo.

ts2.reindex(ts.index, method='ffill', tolerance='1 day')

Resultados parecidos de preenchimento podem ser obtidos pelo método *fillna*:

ts2.reindex(ts.index).fillna(method='ffill')

O método *fillna* pode ser bastante útil por permitir o preenchimento usando um objeto *pandas* ou um dicionário que seja alinhável, ou seja, as chaves do dicionário ou índice da *Series* precisam se ajustar às colunas da *DataFrame* que será preenchida. Um caso de uso muito comum para isso é preencher dados faltantes com a média ou a mediana das colunas correspondentes:

dff = pd.DataFrame(np.random.randn(10, 3), columns=list('ABC'))

dff.iloc[3:5, 0] = np.nan

dff.iloc[4:6, 1] = np.nan

dff.iloc[5:8, 2] = np.nan

dff

dff.mean()

dff.fillna(dff.mean())

dff.fillna(dff.median())

dff.fillna(dff.mean()['B':'C'])

Dados faltantes também podem ser preenchidos usando interpolação, por meio do método [*interpolate*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html#pandas.DataFrame.interpolate):

rng = pd.date_range('1/3/2000', periods=100)

ts2 = pd.Series(np.random.randn(100), index=rng)

ts2[np.random.choice(100, size=34, replace=False)] = np.nan

ts2

ts2.count()

ts2.plot()

ts3 = ts2.interpolate()

ts3

ts3.count()

ts3.plot()

O método interpolate pode levar em consideração os valores dos índices (caso eles não sejam regularmente intervalados):

ser = pd.Series([0.0, np.nan, 10], index=[0., 1., 10.])

ser

ser.interpolate()

ser.interpolate(
    method='values'
)

Também é possível interpolar *DataFrames*:

dfi = pd.DataFrame({'A': [1, 2.1, np.nan, 4.7, 5.6, 6.8],
                   'B': [.25, np.nan, np.nan, 4, 12.2, 14.4]})

dfi

dfi.interpolate()

O argumento *method* flexibiliza *interpolate* para poder usar diferentes métodos de interpolação:

np.random.seed(2)

ser = pd.Series(np.arange(1, 10.1, .25) ** 2 + np.random.randn(37))

missing = np.array([4, 13, 14, 15, 16, 17, 18, 20, 29])

ser[missing] = np.nan

methods = ['linear', 'quadratic', 'cubic']

dfi = pd.DataFrame({m: ser.interpolate(method=m) for m in methods})

dfi.plot()

## Removendo rótulos

Caso a intenção ao usar *reindex* seja apenas remover certos rótulos, o ideal é usar o método *drop*:

df

df.drop(['a', 'd'], axis=0)

df.reindex(
    df.index.difference(
        ['a', 'd']
    )
)  # o mesmo resultado, mas usando reindex

df.drop(['one'], axis=1)

## Renomeando rótulos

Para renomear índices e colunas, *pandas* fornece o método *rename()*, que pode receber como parâmetros um dicionário, uma *Series* ou uma função. Caso uma função seja usada, ela deve retornar um valor único e válido para cada rótulo renomeado.

s

s.rename(str.upper)

Ao renomear usando um mapeamento, os rótulos que não forem especificados não são renomeados. Além disso, se o mapeamento contiver rótulos inexistentes, eles são apenas ignorados sem erro.

df

df.rename(
    columns={'one': 'foo', 'two': 'bar'},
    index={'a': 'apple', 'b': 'banana', 'd': 'durian'}
)

## Substituindo valores

Frequentemente é necessário substituir certos valores em uma *DataFrame* ou *Series*. O método *replace* é uma forma simples e eficiente de realizar essa operação. Em uma *Series*, é possível substituir um único valor ou uma lista de valores por outros valores:

ser = pd.Series([0., 1., 2., 3., 4.])

ser.replace(0, 5)

ser.replace([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])

Também é possível especificar um dicionário de substituições:

ser.replace({0: 10, 1: 100})

Para *DataFrames*, é possível determinar substituições por coluna:

df = pd.DataFrame({'a': [0, 1, 2, 3, 4], 'b': [5, 6, 7, 8, 9]})

df.replace({'a': 0, 'b': 5}, 100)

df.replace({'a': [0, 2], 'b': 5}, 100)

Ao invés de substituir por valores específicos, é possível tratar todos os valores dados como faltantes e preencher ou interpolar:

ser

ser.replace([2, 3], method='ffill')

## Aplicando funções

Funções arbitrárias podem ser aplicadas a um eixo de uma *DataFrame* usando o método *apply()*, que recebe um argumento opcional de eixo (*axis*).

df = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
    'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
    'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})

df

df.apply(np.mean)

df.mean()  # equivalente ao resultado acima

df.apply(np.mean, axis=1)

df.mean(axis=1)  # equivalente ao resultado acima

df.apply(lambda x: x.max() - x.min())

df.apply(np.exp)

O tipo de retorno da função usada no *apply()* influencia o tipo da saída. Se a função aplicada retornar uma *Series*, o resultado será uma *DataFrame*, caso contrário, o resultado será uma *Series*. O método *apply* pode ser usado de formas criativas para responder perguntas sobre um conjunto de dados. Por exemplo: suponha que queiramos saber a data onde o valor mínimo ocorreu para cada coluna:

tsdf = pd.DataFrame(
    np.random.randn(1000, 3), 
    columns=['A', 'B', 'C'],
    index=pd.date_range('1/1/2000', 
                        periods=1000)
)


tsdf.apply(lambda x: x.idxmax())

Também pode ser útil passar argumentos posicionais ou nomeados para o método *apply*. Exemplo:

def subtract_and_divide(x, sub, divide=1):
    return (x - sub) / divide

df.apply(subtract_and_divide, args=(5,), divide=3)

Por último, *apply* pode receber o argumento *raw*, que é *False* por padrão. Caso ele seja passado como *True*, cada linha ou coluna é convertido para um objeto *array* de *NumPy* antes de realizar as operações o que pode trazer um impacto positivo de performance, caso as funcionalidades de indexação sejam desnecessárias.

