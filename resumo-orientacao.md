# Resumos do livro de Orientação a Objetos

### Linguagem de alto nível -> 
- disponiliza comandos bem próximos de uma linguagem natural. 
- melhoria no processo chamado tempo de compilação, tornou-se possível detectar de forma mais rápida se o código inicialmente feito conseguiria realizar os passos desejados com sucesso.
### Linguagem de baixo nível -> 
- utilizava cartões perfurados para conversar com o computador.
### Paradigma Estruturado
- C e Pascal são as mais famosas, pois são simples de manipular e exigem baixo 	poder computacional para serem executadas;
- Defende que é possível resolver qualquer problema com sequência, decisão e iteração;
### Paradigma Orientado a Objetos tem como principal característica uma melhor e maior expressividade das necessidade do nosso dia a dia;
> possibilita criar unidades de código mais próximas da forma como pensamos e agimos, facilitando o processo de transformação das necessidades diárias para uma linguagem orientada a objetos;

### Histórico
#### Simulação com Keith Tocher (1967)
- Discrete Events Simulation - usa modelos lógicos e matemáticos para retratar mudanças de estado através do tempo, assim como os relacionamentos que levaram a essas mudanças.
#### SIMULA 67 com Kristen Nygaard e Ole-Johan Dahl
- Era uma linguagem de simulação de eventos discretos
- Linguagem orientada a problemas e não a computadores
- Baseada em Fortran e depois em ALGO 60
- Originou a OO
- Rodava somente em UNIVAC 1107
#### Smalltalk-80 com Alan Kay (Década de 70)
- Tornou a OO conhecida
- Para pcs
- IDE, interface gráfica amigável
- Tudo que a linguagem manipulava era objeto

### REÚSO
Em uma linguagem estruturada é possível reutilizar:
- Dados com struct, porém é preciso definir struct dentro de struct e o código fica repleto de redefinições;
- Comportamentos com funções, porém elas se limitam à unidade de código em que são definidas. Para isso existem as headers que podem ser reutilizadas em mais de um Módulo Principal e os próprios módulos. Entretanto, isso exige uma grande quantidade de estruturas e código fica mais propenso a falhas;
 > Para	suprir	tais	dificuldades,	a	OO	disponibiliza	dois
 mecanismos	para	reúso	de	código:	a	herança	e	a	associação.	A
 partir	deles,	é	possível	criarmos	unidades	de	código	que
 compartilham	códigos	de	forma	estrutural,	ou	seja,	não	são	blocos
 de	código	dispersos.	Eles	criam	um	relacionamento	que,	além	de
 possibilitar	o	reúso	de	forma	mais	prática	e	menos	propícia	a	erros,
 ainda	gera	uma	modelagem	mais	próxima	do	mundo	real.

A Orientação a objetos preconiza que os dados relativos a uma entidade do mundo real devem somente estar juntos de suas operações, quais são responsáveis por manipular - exclusivamente - tais dados. 

### COESÃO
Cada unidade de código deve executar tarefas e possuir informações que dizem respeito ao conceito que ela representa. É possível utilizar structs, headres e módulos para separar esses conceitos, porém todos aqueles problemas voltam a aparecer. A OO disponibiliza conceitos de classe e associação, por meio do uso de métodos e atributos, para definir unidades de código que são responsáveis somente por tarefas e conceitos que dizem repeito a elas. 

### ACOPLAMENTO
> Acoplamento é o nível de interdependência entre os códigos de um programa de computador

Esse termo é usado para medir o relacionamento entre unidades de código que são unidas, acopladas, para que a aplicação consiga executar suas atividades da forma desejada. Em linguagens estruturas, o acoplamento pode se tornar um problema devido ao processo de compilação dessas linguagens. Os conceitos de classe e associação facilitam a criação de códigos mais autocontidos e coesos.

### GAP SEMÂNTICO
Existe uma limitação da linguagem estrutura em representar o mundo real, pois há uma desassociação entre os dados e os comportamentos e o que eles representam no código.

### Perguntas
- Podemos dizer que a OO trouxe o reúso de códigos?
  Não trouxe o reúso, pois ele já era possível mesmo dentro do paradigma estruturado, porém facilitou a reutilização de unidades de código.
- Qual a importância da coesão?
  Com a coesão é possível ter um controle melhor do código e uma melhor organização, a divisão de responsabilidades é essencial para construir um sistema complexo e restringir o que pode ser manipulado e onde.
- Discorra	sobre	a	seguinte	frase:	"Uma	das	vantagens	da	OO	é
 que	ela	evita	se	ter	códigos	acoplados."
  Ela não evita o acoplamento, porém ela faz com que o processo de acoplamento de unidades de códigos não seja um problema e utiliza técnicas que facilitam o processo de programar e tornam o código mais profissional e de alto nível.
- O	que	vem	a	ser	um	"gap	semântico",	no	contexto	da
 programação?
  É a diferença entre a representação de um contexto do conhecimento em linguagens de programação.

### Abstração

### Reúso
#### Herança

#### Associação

### Encapsulamento

#### Classe

O	objetivo	de	uma classe	é	definir,	servir	de	base,	para	o	que	futuramente	será	o objeto.	É	através	dela	que	criamos	o	"molde"	aos	quais	os	objetos deverão	seguir. Este	"molde"	definirá	quais	informações	serão trabalhadas	e	como	elas	serão manipuladas. Classe	também	pode	ser definida	como	uma	abstração	de	uma	entidade.

#### Atributo
Atributos são características que vão definir quais informações as classes poderão armanezar e manipular. 
> Atributo	é	o	elemento	de	uma	classe	responsável	por	definir	sua
 estrutura	de	dados.	O	conjunto	destes	será	responsável	por
 representar	suas	características	e	fará	parte	dos	objetos	criados	a
 partir	da	classe.

#### Método
O método é responsável por identificar e executar as operações que a classe fornece.
> Método	é	uma	porção	de	código	(sub-rotina)	que	é disponibilizada	pela	classe.	Esta	é	executado	quando	é	feita	uma requisição	a	ela.	Um	método	serve	para	identificar	quais	serviços, ações,	que	a	classe	oferece.	Eles	são	responsáveis	por	definir	e realizar	um	determinado	comportamento.

##### Construtor
O	construtor	é	responsável	por	criar	objetos	a	partir	da classe	em	questão.	

##### Destrutor
É usado para eliminar os objetos criados. A funcionalidade Garbage	Collector	é responsável	por	automaticamente	identificar	objetos	que	não mais	estão	sendo	usados	e	eliminá-los.	É	neste	processo	de eliminação	que	o	Garbage	Collector	usa	os	destrutores.

### Objeto
	É	a	instanciação de	uma	classe
 >  Um	objeto	é	a	representação	de	um	conceito/entidade	do	mundo
 real,	que	pode	ser	física	(bola,	carro,	árvore	etc.)	ou	conceitual
 (viagem,	estoque,	compra	etc.)	e	possui	um	significado	bem	definido
 para	um	determinado	software.	Para	esse	conceito/entidade,	deve
 ser	definida	inicialmente	uma	classe	a	partir	da	qual	posteriormente
 serão	instanciados	objetos	distintos.

- Todo objeto é único
- Os objetos possuem estados
- 

### Curiosidades
Lambda	Expressions	e	Method	Reference	para	Java ou	Method	Group	para	C#;
Membros se referecem a atributos e métodos de uma classe/objeto;
