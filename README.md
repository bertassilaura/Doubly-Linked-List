# Doubly-Linked-List
Trabalho 1 de Estrutura de Dados - UFSC

lista duplamente encadeada COM cursor.

As operações públicas que precisam estar implementadas são (no mínimo):

(elemento) acessarAtual()
(void) InserirAntesDoAtual ( novo )
(void) InserirApósAtual ( novo )
(void) inserirNoFim ( novo ) --ok
(void) inserirNaFrente ( novo ) --ok
(void) inserirNaPosicao ( k, novo )
(void) ExcluirAtual ()
(void) ExcluirPrim ()
(void) ExcluirUlt ()
(void) ExcluirElem ( chave )
(void) ExcluirDaPos ( k )
(boolean) Buscar ( chave )

As operações para controle do cursor (privadas) devem ser, no mínimo:

avançarKPosições( K )
retrocederKPosições ( K )
irParaPrimeiro() --ok
irParaUltimo() --ok

Outras (de apoio):

(boolean) Vazia()
(boolean) Cheia()
(INT) posiçãoDe(chave)

Criem um programa simples que sirva de demonstração básica da sua classe (p.ex. instancie ao menos 1 objeto ListaDuplamenteEncadeada e insira/retire/busque elementos...)