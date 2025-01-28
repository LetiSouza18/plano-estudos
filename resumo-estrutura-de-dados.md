
## Lista linear

### Pilha
É uma lista linear em que todas as inserções e remoções são feitas numa mesma extremidade da lista linear. Esta extremidade se denomina topo (em inglês “top”) ou lado aberto da pilha. Como o último elemento que entrou na pilha será o primeiro a sair da pilha, a pilha é conhecida como uma estrutura do tipo LIFO (“Last In First Out”). Exemplos: pilhas de pratos numa cafeteria (acréscimos e retiradas de pratos sempre feitos num mesmo lado da pilha- lado de cima).

![image](https://github.com/user-attachments/assets/a7d70ec1-12b2-4e6b-909e-935f04c8bf39)


### Fila
É uma lista linear em que todas as inserções de novos elementos são realizadas numa extremidade da lista e todas as remoções são feitas na outra extremidade. Uma fila é uma estrutura do tipo FIFO (“First In First Out”). Elementos novos são inseridos no lado In (fim da fila) e a retirada ocorre no A lista duplamente encadeada é formada por nós similares ao da lista encadeada simples, porém com um
atributo adicional: um apontador para o nó anterior. Dessa forma, é possível percorrer esse tipo de lista em
ambas as direções. A Figura 1 redefine a estrutura “nó” vista anteriormente para adicionar o novo apontador
e simplificar o armazenamento de dados, uma vez que a chave não é realmente necessária. lado Out (frente ou começo da fila). Exemplo: Num sistema operacional, os processos prontos para entrar em execução (aguardando apenas a disponibilidade da CPU) são geralmente mantidos numa fila.

![image](https://github.com/user-attachments/assets/986d26d1-9243-4e5f-931e-61a8ec31d5c5)



## Lista encadeada
A lista encadeada simples usando apontadores é uma estrutura que, diferentemente da lista linear usando vetores, tem sua ordem definida pelo apontador contido em cada nó. As operações definidas para as listas lineares devem ser suportadas por listas encadeadas e são facilmente adaptáveis. 

![image](https://github.com/user-attachments/assets/7b366ae9-95e7-42a5-96ff-44ffbdb985f0)

## Lista duplamente encadeada
A lista duplamente encadeada é formada por nós similares ao da lista encadeada simples, porém com um atributo adicional: um apontador para o nó anterior. Dessa forma, é possível percorrer esse tipo de lista em ambas as direções. 

![image](https://github.com/user-attachments/assets/721cfce4-b837-492b-809c-795adff8fe90)

## Árvore
 É um tipo abstrato de dados que armazena elementos de forma hierárquica, ou seja, não linear;
 - Cada elemento de uma árvore tem um elemento pai e zero ou mais elementos filhos;
 - Nodo do topo = pai ou raiz
 - Nodos do pai = filhos
 - Nodos do mesmo pai = irmãos
 - Nodo externo = não tem filhos (também chamados de folhas)
 - Nodo interno = tem filhos
 - Armazena elementos em posições;
 - As posições são seus nodos, e as posições vizinhas satisfazem as relações pai-filho que definem uma árvore válida.

 ### Árvores Binárias
 É uma árvore ordenada na qual cada nó tem no máximo dois filhos;
 - Árvore binária é dita **própria** se todo nodo interno tiver dois filhos;
 - Cada um dos **nodos internos** de uma árvore binária é rotulado como sendo o filho da esquerda ou o filho da direita;
 - Os filhos são ordenados de maneira que o filho da esquerda venha antes do filha da direita.

![image](https://github.com/user-attachments/assets/3aaaf869-aceb-4175-b7fd-0ae5ad52c0f9)

#### Conceitos
![image](https://github.com/user-attachments/assets/e67fd1b8-d5b1-4505-b4d9-020177ccf790)


### Árvore de Busca Binária
Possui uma propriedade fundamental: 
- O valor associado à raiz é sempre maior que o valor associado a qualquer nó da esquerda;
- O valor associado à raiz é sempre menor que o valor associado a qualquer nó da direita
 
![image](https://github.com/user-attachments/assets/6c42393d-411d-45c3-95b7-da3968e74b10)

#### Inserir

![image](https://github.com/user-attachments/assets/76e58f3f-2f93-4ef2-bc51-5c505cdf2251)


#### Remover

Existem 3 situações possíveis: 

1ª) Quando se deseja retirar uma raiz que é folha: basta liberar a memória alocada pelo elemento;

2ª) Quando a raiz a ser retirada possui um único filho;

3ª) Quando a raiz a ser retirada tem dois filhos:
 - Encontrar o elemento que precede a raiz na ordenação: isto equivale a encontrar o elemento mais à direita da subárvore à esquerda;
 - Trocar a informação da raiz com a informação do nó encontrado;
 - Retirar da subárvore à esquerda o nó encontrado.
 
![image](https://github.com/user-attachments/assets/9d68065f-9901-4619-b369-2f9f9aff591e)
