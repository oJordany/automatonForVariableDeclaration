
# AFD - Autômato Finito Determinístico 

A solução aqui apresentada visa a implementaçãode um software capaz de simular a verificação de declaração de variáveis em C++.

<h2>&#x2714 Conteúdos</h2>
<ul type="pointer">
  <li><a href="#Começando">Começando</a></li>
  <li><a href="#Estrutura do AFD">Estrutura do AFD</a></li>
   <li><a href="#Funcionalidades">Funcionalidades</a></li>
  <li><a href="#Pré-Requisitos">Pré-Requisitos</a></li>
  <li><a href="#Como Executar">Como Executar</a></li>
  <li><a href="#Exemplos">Exemplos</a></li>
  <ul>
    <li><a href="#Palavra Aceita">Palavra Aceita</a></li>
    <li><a href="#Palavra Recusada">Palavra Recusada</a></li>
    <li><a href="#Erro de Declaração de Tipo">Erro de Declaração de Tipo</a></li>
  </ul>
  <li><a href="#Equipe">Equipe</a></li>
 
  
</ul>

## 🚀 Começando

O desenvolvimento desse Software é referente à Terceira Prova da disciplina de Linguagens Formais, Autômatos e Computabilidade da Univerfidade Federal do Pará - UFPA, que solicitava a implementação de um Autômato Finito Determinístico para processar Tipos e Nomes de Variáveis da linguagem C++.

## 🛠️ Estrutura do AFD

#### Σ - Alfabeto de símbolos de Entrada;
~~~Python
import strings
I = {*(string.ascii_letters + "_")}
M = {*(string.ascii_letters + string.digits + "_")}
MDI = M.difference(I)
IUM = I.union(M)
~~~
#### Q – conjunto de estados possíveis do autômato;
~~~Python
{q0,q1,qf}
~~~
#### δ - Função de Transição ou Programa;
~~~Python
{"estado atual": {"símbolo processado": "estado alcançado"}}

transitions = {
    "q0":{
        "a": "q1", "b": "q1", ... ,"z": "q1", "A": "q1", "B": "q1", ... ,"Z": "q1", "_": "q1"
        },
    "q1":{
        "a": "q1", "b": "q1", ... ,"z": "q1", "A": "q1", "B": "q1", ... ,"Z": "q1", "_": "q1", 
        "0":"q1", "1": "q1", ... ,"9":"q1", ",": "q0", ";":"qf"
        },
    "qf":{
        "a": None, "b": None, ... ,"z": None, "A": None, "B": None, ... ,"Z": None, "_": None,
        "0": None, "1": None, ... ,"9": None, ",": None, ";": None
        }
    }
~~~
#### Estado inicial;
~~~Python
{q0}
~~~
#### Conjunto de estados finais;
~~~Python
{qf}
~~~

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

#### 👤[Aimeê Miranda Ribeiro;](https://github.com/Eemiaa)
 
#### 👤[Letícia Costa da Silva;](https://github.com/leticiacostt)
#### 👤[Luiz Jordany de Sousa Silva;](https://github.com/oJordany)
#### 👤[Syanne Karoline Moreira Tavares](https://github.com/syannekaroline)