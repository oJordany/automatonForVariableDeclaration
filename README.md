
# AFD - Autômato Finito Determinístico 

A solução aqui apresentada visa a implementaçãode um software capaz de simular a verificação de declaração de variáveis em C++.

## 🚀 Começando

O desenvolvimento desse Software é referente à Terceira Prova da disciplina de Linguagens Formais, Autômatos e Computabilidade da Univerfidade Federal do Pará - UFPA, que solicitava a implementação de um Autômato Finito Determinístico para processar Tipos e Nomes de Variáveis da linguagem C++.

## 🛠️ Estrutura do AFD

#### Σ - Alfabeto de símbolos de Entrada;
#### Q – conjunto de estados possíveis do autômato;
#### δ - Função de Transição ou Programa;
#### q0 – estado inicial;
#### qf - estado final;

#### Representação 


## 🕹️ Funcionalidades

* Ler uma entrada em texto com as seguintes estruturas:
    
    - tipo_variavel nome_variavel;
    - tipo_variavel nome_variavel_1, nome_variavel_2, (...);

* **Processar a entrada** e **verificar se ela é aceita ou não**. Para isso, é verificado se o *tipo_variavel* é de algum tipo disponível na linguagem c++, que são : 
    - char
    - int
    - bool
    - float
    - double 
    
* Verifica se cada *nome_variave*l respeita as regras de nome das variáveis. 
    
* Verifica se a linha de entrada termina corretamente com ";".
    
## 📦 Pré-requisitos
~~~~Python
Python3+ 
~~~~

## 💻 Como Executar
Abra o Terminal no diretório do software e digite o seguinte comando: 
~~~Python
Python dfa.py
~~~
#### Entrada do usuário:
* Para uma única variável
~~~bash
tipo_variavel nome_variavel;
~~~
* Mais de uma variável
~~~bash
tipo_variavel nome_variavel_1, nome_variavel_2, (...);
~~~
#### Possíveis Retornos: 
~~~bash
palavra aceita
~~~
~~~bash
palavra recusada
~~~
~~~bash
Erro de Declaração de Tipo
~~~

## 🎮 Exemplos

~~~Python
Python dfa.py
~~~
* Palavra Aceita: 
~~~Python
int variavel1;
~~~
~~~Python
palavra aceita
Tipo primitivo: int
Variáveis: ['variavel1']
~~~

* Palavra Recusada
~~~Python
bool 1Var;
~~~

~~~Python
palavra recusada
~~~
* Erro de declaração de tipo:
~~~Python
chaars Var1;
~~~
~~~Python
Erro de Declaração de Tipo: chaars
~~~

* Para mais de uma declaração

~~~Python
bool var1, var1; char var 3
~~~
~~~Python
palavra aceita
Tipo primitivo: bool
Variáveis: ['var1', 'var1']
palavra recusada
~~~
## 👥 Equipe

#### 👤 Aimeê Miranda Ribeiro;
#### 👤Letícia Costa da Silva;
#### 👤Luiz Jordany de Sousa Silva;
#### 👤Syanne Karoline Moreira Tavares;