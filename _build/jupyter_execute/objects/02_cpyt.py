# Classes em Python

Todos os valores são objetos em Python, dos mais básicos, como inteiros e booleanos, aos tipos mais complexos definidos por usuários, incluindo as funções (objetos do tipo função). Como vimos anteriormente, objetos são instâncias de classes, então para criar objetos, é preciso antes definir as classes. Para definir classes em Python, usa-se o operador **class**, seguido do nome da classe e dois pontos. No bloco de código associado à classe, pode-se declarar variáveis e funções. O código abaixo declara a classe *MyClass* com uma variável e uma função interna, chamadas *my_variable* e *my_func* respectivamente. O parâmetro **self** declarado na função *func* será explicado mais à frente. 

class MyClass:
    my_variable = 10
    
    def my_func(self):
        print('hello world')

Para criar um objeto da classe *MyClass*, usa-se a mesma sintaxe de chamada de funções:

my_object = MyClass()

Com isso, a variável *my_object* agora representa uma instância, i.e. um objeto, da classe *MyClass*. Portanto, *my_object* tem acesso tanto à variável *my_variable*, quanto à função *my_func*, sendo possível acessá-las como segue:

print(my_object.my_variable)

my_object.my_func()

É possível criar múltiplos objetos da mesma classe. Cada um deles conterá cópias independentes das variáveis e funções definidas na classe. Por exemplo, podemos criar mais um objeto da classe *MyClass*, chamado *b* e mudar o valor de *my_variable*:

b = MyClass()
b.my_variable += 5

print(my_object.my_variable, b.my_variable)

Assim, *my_variable* representa um atributo dos objetos da classe *MyClass*. Como é esperado que diferentes objetos tenham valores diferentes em seus atributos, seria incoveniente se fosse necessário modificar os valores dos atributos após a criação de cada objeto, em outras palavras seria mais interessante que o valor dos atributos pudesse ser informado no momento da criação do objeto. Para isso, usa-se um método especial, chamado **\_\_init\_\_**, também conhecido como construtor. Uma classe com construtor pode ser definida da seguinte forma: 

class MyClass:
    def __init__(self, value):
        self.my_variable = value
    
    def my_func(self):
        print('hello world')

Quando uma classe é definida com um método **\_\_init\_\_**, a criação de novos objetos da classe automaticamente invoca **\_\_init\_\_** para cada novo objeto. Assim, uma nova instância pode ser criada como: 

b = MyClass(3)
print(b.my_variable)

O primeiro parâmetro dos métodos **\_\_init\_\_** e *my_func* é o mesmo: **self**. O parâmetro **self** é uma referência ao próprio objeto, permitindo acesso aos identificadores definidos no *namespace* do objeto. No método **\_\_init\_\_**, a linha *self.my_variable = value* cria o atributo *my_variable* no *namespace* do objeto, com o valor passado como argumento. É isso que permite que o valor do atributo seja acessado como *b.my_variable*. Se uma outra variável fosse declarada dentro do método **\_\_init\_\_**, mas sem associá-la ao **self**, ela não ficaria acessível fora do método. Exemplo:

class MyClass:
    def __init__(self, value):
        self.my_variable = value
        other_variable = 10
    
    def my_func(self):
        print('hello world')

b = MyClass(3)
print(b.other_variable)

Note que ao chamar um método de um objeto, não se deve passar um valor para o parâmetro **self**. Quando o método é chamado, **self** automaticamente se torna uma referência ao objeto associado. Além disso, **self** não é uma palavra reservada e não é obrigatório que o primeiro parâmetro chame-se **self**. Isso é apenas uma convenção.

class MyClass:
    def __init__(self, value):
        self.my_variable = value
        other_variable = 10
    
    def my_func(self):
        print('hello world')
    
    def my_other_func(test, value):
        print('hi {}'.format(value))
        
b = MyClass(3)
b.my_other_func('everyone')

Caso um método seja definido sem parâmetros, não haverá um primeiro parâmetro para atribuir a referência do objeto. Como consequência, o método não fará parte do *namespace* do objeto. Nesses casos, o método fica associado apenas ao *namespace* da classe. Exemplo:

class MyClass:
    def __init__(self, value):
        self.my_variable = value
        other_variable = 10
    
    def my_func(self):
        print('hello world')
    
    def my_other_func(test, value):
        print('hi {}'.format(value))
    
    def my_third_func():
        print('hi world')
    
    def my_fourth_func(value1, value2):
        print(value1 + value2)
        
b = MyClass(3)
b.my_third_func()

MyClass.my_third_func()

O quarto método acima, *my_fourth_function*, possui dois parâmetros. Portanto, se ele for chamado por meio de um objeto, o primeiro parâmetro será atribuído à referência do objeto, o que gerará um erro de quantidade incorreta de parâmetros:

b.my_fourth_func(10, 5)

Note que o método existe no *namespace* do objeto, mas nesse caso ele associa o parâmetro *value1* à referência do objeto e espera apenas que o parâmetro *value2* receba algum valor. No *namespace* da classe, no entanto, o método pode ser chamado com um valor para cada parâmetro:

MyClass.my_fourth_func(10, 5)

Python permite a "injeção" dinâmica de atributos. Ou seja, é possível atribuir um valor a um atributo que não foi declarado na definição da classe. Exemplo:

b.new_attribute = 23

print(b.new_attribute)

