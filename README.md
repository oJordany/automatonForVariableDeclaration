
# AFD - Autômato Finito Determinístico 

A solução aqui apresentada visa a implementaçãode um software capaz de simular a verificação de declaração de variáveis em C++.

<h2>&#x2714 Conteúdos</h2>
<ul type="pointer">
  <li><a href="#começando">Começando</a></li>
  <li><a href="#estrutura do afd">Estrutura do AFD</a></li>
    <ul>
    <li><a href="#alfabeto">Σ - Alfabeto de símbolos de Entrada;</a></li>
    <li><a href="#estados">Q – conjunto de estados possíveis do autômato;</a></li>
    <li><a href="#transicoes">δ - Função de Transição ou Programa;</a></li>
    <li><a href="#estado inicial">Estado Inicial;</a></li>
    <li><a href="#estado final">Conjunto de estados finais;</a></li>
    <li><a href="#representacao">Representação</a></li>
  </ul>
  
   <li><a href="#funcionalidades">Funcionalidades</a></li>
  <li><a href="#pre-requisitos">Pré-Requisitos</a></li>
  <li><a href="#como executar">Como Executar</a></li>
  <li><a href="#exemplos">Exemplos</a></li>
  <ul>
    <li><a href="#palavra aceita">Palavra Aceita</a></li>
    <li><a href="#palavra recusada">Palavra Recusada</a></li>
    <li><a href="#erro de declaração de tipo">Erro de Declaração de Tipo</a></li>
  </ul>
  <li><a href="#equipe">Equipe</a></li>
 
  
</ul>

<h2><a name="começando">🚀 Começando</a></h2>

O desenvolvimento desse Software é referente à Terceira Prova da disciplina de Linguagens Formais, Autômatos e Computabilidade da Univerfidade Federal do Pará - UFPA, que solicitava a implementação de um Autômato Finito Determinístico para processar Tipos e Nomes de Variáveis da linguagem C++.

<h1></h1>

<h2><a name="estrutura do afd">🛠️ Estrutura do AFD</a></h2>
<h3><a name="alfabeto">Σ - Alfabeto de símbolos de Entrada;</a></h3> 

~~~Python
import strings
I = {*(string.ascii_letters + "_")}
M = {*(string.ascii_letters + string.digits + "_")}
MDI = M.difference(I)
IUM = I.union(M)
~~~
<h3><a name="estados">Q – conjunto de estados possíveis do autômato;</a></h3> 

~~~Python
{q0,q1,qf}
~~~

<h3><a name="transicoes">δ - Função de Transição ou Programa;</a></h3> 

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

<h3><a name="estado inicial">Estado inicial;</a></h3> 

~~~Python
{q0}
~~~
<h3><a name="estado final">Conjunto de estados finais;</a></h3> 

~~~Python
{qf}
~~~

<h3><a name="representacao">Representação.</a></h3>

<div align="center">
<img src="https://user-images.githubusercontent.com/87232098/206476992-11bdb4c4-c763-4051-bb25-037f926c5477.jpeg" width="700px" />
</div>

<h1></h1>

<h2><a name="funcionalidades">🕹️ Funcionalidades</a></h2>

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

<h1></h1>

<h2><a name="pre-requisitos">📦 Pré-requisitos</a></h2> 

~~~Python
Python3+ 
~~~

<h1></h1>

<h2><a name="como executar">💻 Como Executar</a></h2> 

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
<h1></h1>

<h2><a name="exemplos">🎮 Exemplos</a></h2> 

~~~Python
Python dfa.py
~~~
<h3><a name="palavra aceita">Palavra Aceita</a></h3> 

~~~Python
int variavel1;
~~~
~~~Python
palavra aceita
Tipo primitivo: int
Variáveis: ['variavel1']
~~~

<h3><a name="palavra recusada">Palavra Recusada</a></h3> 

~~~Python
bool 1Var;
~~~

~~~Python
palavra recusada
~~~
<h3><a name="erro de declaração de tipo">Erro de Declaração de tipo</a></h3> 

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

<h1></h1>

<h2><a name="equipe">👥 Equipe</a></h2> 

#### 👤[Aimeê Miranda Ribeiro](https://github.com/Eemiaa) | 202104940014
 
#### 👤[Letícia Costa da Silva](https://github.com/leticiacostt) | 202104940017
#### 👤[Luiz Jordany de Sousa Silva](https://github.com/oJordany) | 202104940005
#### 👤[Syanne Karoline Moreira Tavares](https://github.com/syannekaroline) | 202104920029
