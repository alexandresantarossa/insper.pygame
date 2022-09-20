Projeto Final de Dessoft - 2021.2

Integrantes:

Alexandre Rodrigues Santarossa 

Gustavo Mendes da Silva

Kevin Nagayuki Shinohara 

O nosso projeto final da matéria de Dessoft é programar um jogo totalmente em Python, utilizando a biblioteca Pygame!
O jogo escolhido para o nosso projeto foi o Bomberman, deste modo, criamos o incrível Bomb Smash, um jogo para dois jogadores
que envolve muita habilidade e diversão que vai definir de uma vez por todas qual é o melhor Hulk, o verde ou o vermelho!

Confira no Youtube: https://www.youtube.com/watch?v=LnG8Jyq3QeE


Com o objetivo de melhorar a arquitetura do nosso codigo realizamos as seguintes mudanças 

- Foi criado a classe block é a classe wood que estende a classe block, melhoramos a coesão do nosso codigo quando realizamos a abstração ao transformar duas classes com mesmas propriedade em uma classe mãe e uma herdeira. 

-  A segunda mudança foi unir classes separadas para player 1 e player 2, ambas possuiam os mesmo objetivos, então utilizar uma classe apenas e apenas direcionar para qual player quermos que a realize, traz uma melhor coesão, legibilidade e facilidade para futuras alterações. 

- A ultima alteração feita é semelhante a descrita anteriormente, já que apenas juntamos as janelas de vitoria, no lugar de termos duas, uma pra cada cenario, temos uma que analisa o resultado e nós diz o mesmo.