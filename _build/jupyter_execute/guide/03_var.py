# Variáveis

Variáveis são estruturas que permitem armazenar valores para leitura e uso posterior. Do ponto de vista computacional, elas funcionam como "apelidos", compreensíveis por humanos, para endereços de memória. Para facilitar a compreensão do conceito, podemos imaginar que a memória do computador é uma espécie de armário e as variáveis indicam as gavetas ou portas onde os valores estão armazenados.



:::{figure-md} cabinet
<img src="images/cabinet.svg" alt="Armário com variáveis"/>

Representação da memória como um armário e variáveis como endereços para as gavetas.
:::

## Nomes e Identificadores

Como na maior parte das linguagens, identificadores (nomes de variáveis, funções, classes, etc) permitem letras minúsculas e maiúsculas, dígitos e traço baixo ou _underline_ (\_). Identificadores não possuem limite de tamanho e diferenciam entre minúsculas e maiúsculas (_case sensitive_), ou seja _variavel_ é diferente de _Variavel_. Identificadores especiais costumam começar e terminar com duplos traços baixos, e.g. \_\_init\_\_. Seguem algumas convenções para nomeação de identificadores:

| Identificador        | Convenção           | Exemplo  |
|------------- |-------------| -----|
| Módulos/pacotes      | caracteres minúsculos | _projetopython_ |
| Métodos/funções/variáveis | minúsculos\_separados\_por\_underlines      |    _variavel_\__aleatoria_ |
| Globais/constantes      | maiúsculos\_separados\_por\_underlines     |   _CONSTANTE_ |
| Classes | Iniciais Maiúsculas      |    NormalDistribution |

## Atribuição de valores

Em Python não há um comando exclusivo para declaração de variáveis e seus tipos. Na verdade, não são as variáveis que tem tipo, mas sim os valores armazenados nelas por meio do operador de atribuição (*=*). Por exemplo, podemos criar uma variável *idade* e armazenar nela o valor 30. Se essa for a primeira vez que o identificador idade aparecer neste trecho de código, a variável será criada nesse momento. Como este material está escrito usando Jupyter Notebooks, para avaliar o valor da variável, basta digitar seu nome embaixo da declaração (em outras situações, será necessário usar o comando **print**, mas ainda veremos isso).  

idade = 30

idade

O símbolo *=* não está testando igualdade no comando acima. A operação deve ser lida como:

```
A variável idade recebe o valor 30.
```

Para verificarmos o tipo do valor armazenado na variável, podemos fazer:

type(idade)

Se mudarmos o valor armazenado para um texto, e.g. 'Estatística', veremos que não ocorrerá erro e a operação de verificação de tipo retornará o tipo correto.

idade = 'Estatística'

type(idade)

O código à direita do operador de atribuição não precisa ser apenas um valor, podendo conter uma expressão complexa (incluindo várias operações e chamadas de funções), cujo resultado será armazenado na variável. Como um exemplo simples, vamos adicionar *1* ao valor armazenado na variável *idade* e armazenar o resultado na própria variável, substituindo o valor anterior.

idade = 30
idade = idade + 1

idade

### Atribuições com operações

Assim como outras linguagens de programação, Python suporta atribuições associadas a certas operações, como soma ou concatenação (+=), subtração (-=), multiplicação (\*=), divisão (/=) e outras operações que veremos na próxima Seção. Quando essas atribuições especiais são usadas, a operação associada é realizada sobre os valores da expressão à direita do operador e da variável à esquerda e o novo valor é atribuído à mesma variável. Por exemplo, o código acima pode ser reescrito como:

idade = 30
idade += 1

idade

Outros exemplos:

idade = 30
idade -= 1

idade

idade = 30
idade *= 2

idade

idade = 30
idade /= 2

idade

### Atribuições múltiplas

Python permite que múltiplas atribuições sejam feitas na mesma linha de algumas formas. Primeiro, pode-se simplesmente usar vírgulas para separar os identificadores de variáveis à esquerda do operador de atribuição e os valores à direita do operador de atribuição. Na prática, essa operação de atribuição é realizada por meio de variáveis do tipo Tupla, que veremos mais à frente.

idade, altura = 30, 1.78

idade

altura

Pode-se também envolver os identificadores e os valores em colchetes \[ \]. Na prática, essa operação de atribuição é realizada por meio de variáveis do tipo Lista, que também veremos mais à frente.

[idade, altura] = [30, 1.78]

idade

altura