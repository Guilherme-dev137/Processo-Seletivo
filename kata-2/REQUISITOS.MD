Descrição informada pelo cliente:
    "Preciso de uma tela onde eu veja minhas tarefas. Cada tarefa tem um título e uma situação.
    Quero poder criar novas, marcar como feita e deletar as que não preciso mais.
    Ah, e precisa ter um filtro pra eu ver só as pendentes ou só as concluídas.
    Se der, queria também uma prioridade nas tarefas. Mas isso pode ficar pra depois."

Análise de requisitos:

As informações faltantes que identifiquei foram essas:
    O cliente não informou quem pode verificar esse painel
    O cliente não deixou claro se só ele irá utilizar o painel ou se será compartilhado com outras pessoas
    O cliente também não expecificou quem pode fazer a adição de novas tarefas, ou a modificação da mesma

Perguntas que eu faria ao cliente referênte as informações faltantes:
    Esse sistema será para ser utilizado somente para você ou para toda a equipe?
    Caso o sistema seja para toda a equipe, quem estiver vendo pode verificar todas as tarefas ou só algumas tarefas em expecífico?
    Se o sistema seja implementado para toda a equipe, quem além de você, quem mais pode realizar modificações nas tarefas do painel?

Decisões que tomaria na ausência das respostas
    Na criação do projeto, eu implementaria somente o front-end de um botão para ser realizado o login no sistema, inicialmente o projeto irá mostrar
    todas as informações das tarefas como solicitado pelo cliente, mas antes de realizar a entrga do sistema, mostraria uma versão de homologação
    para o cliente validar todo o sistema, caso ele queira implementar essas funções que foram perguntadas, o front-end estaria pronto, com isso iria criar
    toda a lógica do banck-end para validar os usuários no sistema.

Requisitos funcionais(RF):
    -O sistema deve mostrar uma tela inicial com as informações das tartefas
    -O sistema deve mostrar nos cards das tarefas o titulo, a situação e o status da tafera
    -O sistema deve criar novas tarefas
    -O sistema deve filtrar as tarefas, todas as tarefas concluídas ou todas as tarefas pendentes
    -O sistema deve possibilitar marcar as tarefas como concluídas ou deletar as tarefas
    -O sistema deve possibilitar alterar a prioridade das tarefas(O cliente informou que pode ficar para depois)

Requisitos não funcionais(RNF):
    -O sistema deve ser seguro com as informações das tarefas
    -O sistema deve ser responsivo para o acesso em diversos dispositivos
    -O sistema deve ser otimizado para realizar as operações(criar, deletar, trocar status)
    -O sistema deve ser organizado para realizar consultas mais precisas

O requisito que o cliente informou que "pode ficar para depois", eu acrescentei o mesmo aos requisitos funcionais do projeto,
porem deixei o mesmo com uma observação, fiz isso para não esquecer do mesmo e quando o cliente pedir a implementação dessa
função não ser algo que passou despercebido por mim.


