# Lista

- Lista contígua de elementos
- dinâmico
- funciona bem como pilha
- não funciona bem como fila

| Complexidade | Operações |
| --- | --- |
| constant | [i], [i] = x, append, pop, len |
| linear | in, index, for, count, [begin:end], extend, +, *, reverse, remove, insert, shuffle, split, join |
| sublinear | sort, sorted |

`pop` é constante se retira último elemento, caso contrário é linear.

[Sessão IPython explorando operações e métodos](pratica/ipython_export/lista.txt).

[Código](pratica/listas/max_min_ordered.py):
- tudo em tempo constante

[Código](pratica/listas/max_min_for.py):
- é possível resolver passando uma única vez pela lista, conforme código
- algoritmo é O(n)
- as funções padrão `max` e `min` são lineares

# Recursão

Uma função recursiva é aquela que chama a si mesma.

Na matemática: f(n) = 1 se n <=1, senão n * f(n-1)

Há um critério de parada (o "se" na definição anterior).

Geralmente, há um parâmetro que é decrescido.

Como abordar:
- escrever contrato de alto nível
- tratar exceções
- inicializar estado
- delegar para função recursiva interna

Peculiaridades do Python:
- não possui otimização de pilha (*tail recursion optimization*)
    - https://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html
- pilha com limite de 1000 chamadas
- clojure com nonglobal
- sempre é possível transformar iteração em recursão
- sempre é possível transformar recursão em iteração

[Código](pratica/recursao/max_min_recursive.py):
- Tempo:
```
t(n) = 1 + t(n-1)
t(n) = 1 + 1 + t(n-2)
...
t(n) = n + 1 => O(n)
```

- Memória:
    - Python armazena todos os valores de cada chamada na pilha
    - m(m) = 1 + m(n-1) => O(n)
    - na resolução com for, era constante
    - a falta de otimização de pilha leva a isso
    
[Código](pratica/recursao/hanoi.py):
- Tempo:
    - é um somatório de PG

```
1 vem dos print
t(n) = 1 + 2(t(n-1))
t(n) = 1 + 2 + 4(t(n-2))
t(n) = 1 + 2 + 4 + 8(t(n-3))
...
t(n) = 1 + 2 + 4 + ... + 2^n (t(0)) => O(2^n)
```

- Memória:
    - m(n) = 1 + m(n - 1) - 1 + m(1) => O(n)


[Versão com generator](pratica/recursao/hanoi_generator.py).

[Versão iterativa](pratica/recursao/hanoi_iterative.py). Possui mesma complexidade.

# Lista duplamente ligada

- Dinâmica
- Funciona bem como pilha ou fila
- Funciona bem para iteração
- não funciona bem para acesso aleatório de elementos
- classe `

| Complexidade | Operações |
| --- | --- |
| Constant | append, appendleft, pop, popleft, len |
| Linear | [i], [i] = x, extend, extendleft |

Há o parâmetro `maxlen` que determina o tamanho máximo de elementos. Colocando mais elementos, remove do início ou do fim a depender de onde foi feita a inserção.

[Sessão IPython explorando operações e métodos](pratica/ipython_export/deque.txt).

[Código](pratica/double_ended_queue/binary_sum_pythonic.py)
- em Python, inteiros têm tamanho arbitrário, depende apenas do quanto de memória está disponível

[Código](pratica/double_ended_queue/binary_sum_zip_longest.py)
- supondo um contexto onde há limite de tamanho para inteiro. Ex.: 2^63 -1
- algoritmo linear, O(max(n, n2)).  

[Código](pratica/double_ended_queue/binary_sum_zip_cycle.py)
- definindo nosso próprio zip_longest, conhecendo `chain` e `cycle` de `itertools`

[Código](pratica/double_ended_queue/binary_sum_no_lib.py)
- definindo nosso próprio zip_longest sem usar zip nem qualquer método de `itertools`
- apenas `deque` foi importado

# Conjuntos

- Analogia com conjuntos matemáticos
- não possui elementos repetidos
- hash
    - números, string, tupla -> imutáveis
- estrutura boa para fazer backtrack
    - verificar se algum passo já foi feita
    
| Complexidade | Operações |
| --- | --- |
| Constant | add, remove, in |
| Linear | for (no order), union, -, intersection |

[Sessão IPython explorando operações e métodos](pratica/ipython_export/sets.txt).

[Código](pratica/conjuntos/dedup.py)
- procurar em um set é tempo constante com `in`, daí a vantagem de conferir no set e não na lista
- algoritmo linear em memória e tempo
- se fizesse a busca em `result`, seria quadrático

[Código](pratica/conjuntos/borders.py)
- O(m*n) em tempo e memória

# Dicionários

- Também chamado de mapa em outras linguagens
- Conecta chave a um valor
- Chaves precisam ser "hashable"
- Operações como as de um conjunto

| Complexidade | Operações |
| --- | --- |
| Constant | [k], [k] = v, pop, in |
| Linear | For (no order), keys(), values(), items() |

[Sessão IPython explorando operações e métodos](pratica/ipython_export/dicts.txt).

[Código](pratica/dicionarios/phoneword.py)
- O(3^n)<= ? <=O(4^n). Daí O(a^n), exponencial em tempo e memória.