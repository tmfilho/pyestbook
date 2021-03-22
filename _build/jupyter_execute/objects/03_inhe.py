# Herança e Polimorfismo

Herança é um mecanismo que permite basear uma classe em outra, mantendo uma implementação similar e formando uma hierarquia de classes. A classe derivada é chamada de subclasse enqunto a classe base é chamada de super classe. Um objeto de uma subclasse mantém todos os atributos e métodos definidos na super classe. O mecanismo de herança é útil quando certos comportamentos (métodos) iguai são esperados para objetos de diferentes tipos ou para facilitar o reuso de código. É importante diferenciar herança de composição de objetos. A composição se dá quando um objeto contém outro(s) objeto(s), ou seja, há uma relação de posse de um objeto para outro.

Vejamos o exemplo abaixo:

import math

class DiscreteDistribution:
    
    def __init__(self, params):
        self.params = params
        
    def pmf(self, x):
        pass
    
    def cdf(self, x):
        total = 0
        for v in range(x + 1):
            total += self.pmf(v)
        return total
    
    def mean(self):
        pass
    
    def variance(self):
        pass
    
class BinomialDistribution(DiscreteDistribution):
    
    def pmf(self, x):
        
        n, p = self.params['n'], self.params['p']
        
        def factorial(n):
            prod = 1
            for i in range(1, n + 1):
                prod *= i
            return prod

        def combination(n, x):
            return factorial(n) / (factorial(x) * factorial(n - x))

        return combination(n, x) * p ** x * (1.0 - p) ** (n - x) 
    
    def mean(self):
        return self.params['n'] * self.params['p']
    
    def variance(self):
        return self.params['n'] * self.params['p'] * (1 - self.params['p'])

class PoissonDistribution(DiscreteDistribution):
    
    def pmf(self, x):
        
        l = self.params['lambda']
        
        def factorial(n):
            prod = 1
            for i in range(1, n + 1):
                prod *= i
            return prod

        return (l ** x * math.e ** (-l)) / factorial(x)
    
    def mean(self):
        return self.params['lambda']
    
    def variance(self):
        return self.params['lambda']

binomial = BinomialDistribution(params={'n': 5, 'p': 0.7})
print('################## Binomial ##################')
print('Média: {}'.format(binomial.mean()))
print('Variância: {}'.format(binomial.variance()))
print('PMF de 2: {}'.format(binomial.pmf(2)))
print('CDF de 2: {}'.format(binomial.cdf(2)))

print()

poisson = PoissonDistribution(params={'lambda': 5})
print('################## Poisson ##################')
print('Média: {}'.format(poisson.mean()))
print('Variância: {}'.format(poisson.variance()))
print('PMF de 2: {}'.format(poisson.pmf(2)))
print('CDF de 2: {}'.format(poisson.cdf(2)))

O código acima define uma classe base, chamada *DiscreteDistribution*, cujo único atributo se chama *params* (uma coleção de parâmetros) e cujos métodos incluem o cálculo da função massa de probabilidade, da função distribuição acumulada, da média e da variância. O único método implementado nesta classe é o cálculo da função distribuição e o construtor. Os outros métodos possuem apenas a sua assinatura.

Como subclasses dessa classe base (note o **nome da super classe entre parênteses** após o nome da subclasse), temos *BinomialDistribution* e *PoissonDistribution*. Ambas implementam os métodos *pmf*, *mean* e *variance* de acordo com a distribuição de probabilidade representada. Após declarar as subclasses, o código cria um objeto de cada uma delas e executa seus métodos. Note que, apesar de as subclases não declarararem o método *cdf* ambos, os objetos podem chamá-lo. Isto ocorre porque as subclasses herdam este método da sua superclasse. Note que, internamente, o método *cdf* chama o método *pmf*, cuja implementação ficou sob responsabilidade das subclasses. Isso significa que parte do comportamento do método *cdf* é modificado pelas implementações das subclasses. Em programação orientada a objetos, esse conceito (comportamentos parcialmente diferentes entre subclasses) é chamado de **polimorfismo**.

Uma subclasse pode modificar a implementação de um método da superclasse total ou parcialmente. No exemplo abaixo, a subclasse PoissonDistribution irá modificar o método *cdf* para avisar que o cálculo foi feito usando a função massa da Poisson.

class PoissonDistribution(DiscreteDistribution):
    
    def pmf(self, x):
        
        l = self.params['lambda']
        
        def factorial(n):
            prod = 1
            for i in range(1, n + 1):
                prod *= i
            return prod

        return (l ** x * math.e ** (-l)) / factorial(x)
    
    def cdf(self, x):
        print('Calculado usando pmf da Poisson')
        total = 0
        for v in range(x + 1):
            total += self.pmf(v)
        return total
    
    def mean(self):
        return self.params['lambda']
    
    def variance(self):
        return self.params['lambda']

poisson = PoissonDistribution(params={'lambda': 5})
print('CDF de 2: {}'.format(poisson.cdf(2)))

Note que todo o código da implementação do método *pmf* da superclasse foi copiado e apenas a linha *print('Calculado usando pmf da Poisson')* foi adicionada. Essa abordagem de codificação resultaria em muitos códigos copiados, o que é uma má prática. Para evitar isso, Python fornece um atalho para reutilizar a implementação de um método da superclasse: o operador **super**. Veja abaixo:

class PoissonDistribution(DiscreteDistribution):
    
    def pmf(self, x):
        
        l = self.params['lambda']
        
        def factorial(n):
            prod = 1
            for i in range(1, n + 1):
                prod *= i
            return prod

        return (l ** x * math.e ** (-l)) / factorial(x)
    
    def cdf(self, x):
        print('Calculado usando pmf da Poisson')
        return super().cdf(x)
    
    def mean(self):
        return self.params['lambda']
    
    def variance(self):
        return self.params['lambda']

poisson = PoissonDistribution(params={'lambda': 5})
print('CDF de 2: {}'.format(poisson.cdf(2)))

Note que a função *factorial* foi definida duas vezes no nosso código: dentro do método *pmf* das duas subclasses. Para evitar essa cópia de código, podemos definí-la no escopo global: 

def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod
        
class BinomialDistribution(DiscreteDistribution):
    
    def pmf(self, x):
        
        n, p = self.params['n'], self.params['p']        

        def combination(n, x):
            return factorial(n) / (factorial(x) * factorial(n - x))

        return combination(n, x) * p ** x * (1.0 - p) ** (n - x) 
    
    
    def cdf(self, x):
        print('Calculado usando pmf da Poisson')
        return super().cdf(x)
    
    def mean(self):
        return self.params['n'] * self.params['p']
    
    def variance(self):
        return self.params['n'] * self.params['p'] * (1 - self.params['p'])

class PoissonDistribution(DiscreteDistribution):
    
    def pmf(self, x):
        
        l = self.params['lambda']

        return (l ** x * math.e ** (-l)) / factorial(x)
    
    def mean(self):
        return self.params['lambda']
    
    def variance(self):
        return self.params['lambda']

binomial = BinomialDistribution(params={'n': 5, 'p': 0.7})
print('################## Binomial ##################')
print('Média: {}'.format(binomial.mean()))
print('Variância: {}'.format(binomial.variance()))
print('PMF de 2: {}'.format(binomial.pmf(2)))
print('CDF de 2: {}'.format(binomial.cdf(2)))

print()

poisson = PoissonDistribution(params={'lambda': 5})
print('################## Poisson ##################')
print('Média: {}'.format(poisson.mean()))
print('Variância: {}'.format(poisson.variance()))
print('PMF de 2: {}'.format(poisson.pmf(2)))
print('CDF de 2: {}'.format(poisson.cdf(2)))

## Herança múltipla

Uma classe pode ser subclasse de várias classes ao mesmo tempo. Para isso, basta declarar os nomes das super classes separados por vírgulas. O código abaixo declara uma classe, chamada *Printable*, que possui apenas um método **__str__**, que retorna os parâmetros do objeto em uma string formatada. O método **__str__** é chamado por Python quando um objeto é passado como parâmetro para a função **print**. Após declarar a classe *Printable*, as classes das distribuições são declaradas novamente, dessa vez herdando de *DiscreteDistribution* e de *Printable*. Note que ambas as classes agora redefinem o construtor, adicionando o atributo *name*.

class Printable:
    def __str__(self):
        s = self.name + ' com parâmetros '
        for key in self.params:
            s += '{0}: {1} '.format(key, self.params[key])
        return s

class BinomialDistribution(DiscreteDistribution, Printable):
    
    def __init__(self, params):
        self.name = 'Binomial'
        super().__init__(params)
        
    def pmf(self, x):
        
        n, p = self.params['n'], self.params['p']        

        def combination(n, x):
            return factorial(n) / (factorial(x) * factorial(n - x))

        return combination(n, x) * p ** x * (1.0 - p) ** (n - x) 
    
    
    def cdf(self, x):
        print('Calculado usando pmf da Poisson')
        return super().cdf(x)
    
    def mean(self):
        return self.params['n'] * self.params['p']
    
    def variance(self):
        return self.params['n'] * self.params['p'] * (1 - self.params['p'])

class PoissonDistribution(DiscreteDistribution, Printable):
    
    def __init__(self, params):
        self.name = 'Poisson'
        super().__init__(params)        
    
    def pmf(self, x):
        
        l = self.params['lambda']

        return (l ** x * math.e ** (-l)) / factorial(x)
    
    def mean(self):
        return self.params['lambda']
    
    def variance(self):
        return self.params['lambda']

binomial = BinomialDistribution(params={'n': 5, 'p': 0.7})
print(binomial)
poisson = PoissonDistribution(params={'lambda': 5})
print(poisson)

