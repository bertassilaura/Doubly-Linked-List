# Doubly-Linked-List
Trabalho 1 de Estrutura de Dados - UFSC

lista duplamente encadeada COM cursor.

As operações públicas que precisam estar implementadas são (no mínimo):

(elemento) acessarAtual() Leo e Laura
(void) InserirAntesDoAtual ( novo ) Leo
(void) InserirApósAtual ( novo ) Laura
(void) inserirNoFim ( novo ) --ok
(void) inserirNaFrente ( novo ) --ok
(void) inserirNaPosicao ( k, novo ) Leo
(void) ExcluirAtual () Laura
(void) ExcluirPrim () Leo
(void) ExcluirUlt () Laura
(void) ExcluirElem ( chave ) Laura
(void) ExcluirDaPos ( k ) Leo
(boolean) Buscar ( chave ) ??

As operações para controle do cursor (privadas) devem ser, no mínimo:

avançarKPosições( K ) --ok
retrocederKPosições ( K ) --ok
irParaPrimeiro() --ok
irParaUltimo() --ok

Outras (de apoio):

(boolean) Vazia()
(boolean) Cheia()
(INT) posiçãoDe(chave)

Criem um programa simples que sirva de demonstração básica da sua classe (p.ex. instancie ao menos 1 objeto ListaDuplamenteEncadeada e insira/retire/busque elementos...)

