# Erros e Exceções

Mesmo quando um comando está sintaticamente correto, é possível que ocorram erros em sua execução. Esses erros que ocorrem em tempo de execução são chamados de exceções e, se não tratados, resultam no final fatal do programa. Alguns exemplos de exceções comuns:

1 / 0

mean * 3

'mean: ' + 1.

A última linha na mensagem de erro diz o que ocorreu e começa com o tipo de exceção, seguido de informações mais detalhadas que ajudam a entender e resolver a fonte do erro. A parte acima da mensagem de erro mostra o contexto em que o erro ocorreu, seguindo a execução do script através da pilha de chamadas (certa linha de código chamou certa função, que chamou outra função, etc).

Para evitar que programas falhem devido a exceções, é possível escrever códigos que se previnem contra a sua ocorrência. O exemplo abaixo pede que o usuário insira um número após o outro. Caso o usuário insira um valor inválido, o script avisa o usuário por meio de uma mensagem. Note que o exemplo executa em um laço infinito. No entanto, é possível pará-lo usando *Control-C*, caso esteja executando em um terminal, *Esc-i-i*, caso esteja usando *Jupyter Notebook*, ou algum comando de interrupção suportado pelo seu sistema operacional. Caso a execução seja interrompida usando um desses comandos, Python irá lançar a exceção *KeyboardInterrupt*.

while True:
    try:
        x = float(input('Digite um número: '))
    except ValueError:
        print('Número inválido. Tente novamente...')

O comando **try** funciona da seguinte maneira: 
   1. Os comandos definidos no bloco de código entre o **try** e o **except** são executados; 
   2. Se nenhuma exceção ocorrer o bloco do **except** é ignorado, terminando a execução do **try**; 
   3. Se uma exceção ocorrer, os comandos restantes do bloco **try** são ignorados;
      1. Se o tipo da exceção corresponder a algum tipo de exceção nomeado após o comando **except**, o bloco **except** é executado e a execução do *script* continua;
      2. Se a execução não corresponder aos tipos de exceção nomeados após o comando **except**, a exceção é lançada para escopos superiores, na tentativa de encontrar algum bloco que a trate;
         1. Se a exceção permanecer não tratada, a execução irá parar.

O comando **try** pode ser associado a mais de um **except**, para especificar tratamentos diferentes para diferentes tipos de exceção. Por exemplo, para evitar a mensagem de erro de *KeyboardInterrupt* ao interromper o código acima, podemos fazer:

while True:
    try:
        x = float(input('Digite um número: '))
    except ValueError:
        print('Número inválido. Tente novamente...')
    except KeyboardInterrupt:
        break

Além disso, Python também permite que um comando **except** seja associado a múltiplos tipos de exceções (nesse caso, o mesmo tratamento será dado às diferentes exceções):

try:
    pass
except (RuntimeError, TypeError, NameError):
    pass

## Exceções definidas pelo usuário

As exceções mencionadas até agora (RuntimeError, TypeError, NameError, ValueError e KeyboardInterrupt) e [muitas outras](https://docs.python.org/3.7/library/exceptions.html#bltin-exceptions) são disponibilizadas por padrão por Python. Todas elas são na verdade subclasses da classe *Exception*. Da mesma forma, é possível definir exceções customizadas que herdam de *Exception*. Por exemplo, o código abaixo continua o exemplo anterior, mas pede para o usuário digitar o número com vírgula como marcador de decimais. Caso não haja uma vírgula na *string* digitada, o código irá lançar o novo tipo de exceção chamado *InputError* (é convenção nomear exceções com a palavra *Error* no final). Caso haja uma vírgula, o código irá substituí-la por ponto e depois tentar converter a *string* resultante para *float*.

class InputError(Exception):
    def __init__(self, input_value, message):
        self.input_value = input_value
        self.message = message
        
while True:
    try:
        x = input('Digite um número (vírgula para decimais): ')
        if ',' not in x:
            raise InputError(x, 'Valor digitado não usou vírgula para decimais')
        else:
            print('Valor digitado: {}'.format(float(x.replace(',', '.'))))
    except ValueError:
        print('Número inválido. Tente novamente...')
    except KeyboardInterrupt:
        break

Note o uso do operador **raise** para lançar a exceção *InputError*. Além disso, o código não está tratando o *InputError*, o que faz com que o programa finalize com erro. Para tratar a nova exceção, iremos adicionar mais um **except**:

while True:
    try:
        x = input('Digite um número (vírgula para decimais): ')
        if ',' not in x:
            raise InputError(x, 'Valor digitado não usou vírgula para decimais')
        else:
            print('Valor digitado: {}'.format(float(x.replace(',', '.'))))
    except InputError as err:
        print(err.message + ': ' + err.input_value)
    except ValueError:
        print('Número inválido. Tente novamente...')
    except KeyboardInterrupt:
        break

Note o uso do operador **as** para atribuir a exceção capturada ao objeto *err*, permitindo o acesso aos atributos *message* e *input_value*.

## O operador **finally**

Além do **except**, o operador **try** pode ser associado a outro operador opcional, chamado **finally**, que é usado para definir ações que devem ser executadas sob quaisquer circunstâncias. Por exemplo, se uma conexão com um servidor for aberta, ela deve ser fechada após o seu uso, tendo ou não ocorrido erros. O bloco de código associado ao comando **finally** será sempre executado, mesmo que ocorra alguma exceção. Por exemplo:

try:
    raise ValueError('Lançando um erro')
finally:
    print('Adeus')