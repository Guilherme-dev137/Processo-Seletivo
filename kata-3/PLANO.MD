Seção 1 - Diagnóstico:

    -O endpoint de consulta de pedidos demora 8-12 segundos em horário de pico.
        •Causa mais provável desse problema:
            -Em horários de pico, devido a alta demanda do sistema o mesmo pode estar com uma sobrecarga
            várias requisições a API pode está gerando essa fila de espera.
        
        •O risco que representa:
            -Com a demora na consulta dos pedidos pode ocasionar o travamento do servidor devido a grande 
            quantidade de informações que estão sendo pedidas simultaneamente.
            -Para o negócio isso é ruim, pois o servidor pode ficar offline fazendo com que os usuários logados
            percam o acesso a plataforma e também pode acaretar na perca dos produtos que eles estajam realziando,
            caso o mesmo esteja realizando alguma compra nesse momento.

        •É um problema urgente ou importante?:
            -Segundo a Matriz de Eisenhower essa situação se enquadra como importante, mas não urgente, pois esse problema
            só ocorre nos horários de pico do sistema, com isso a equipe tem um certo tampo para planejar uma solução para
            esse problema e realizar a implementação da solução.

    -Dois pedidos foram criados em duplicitade na última semana.
        •Causa mais provável desse problema:
            -Pode ter ocorrido algum bug na hora da realização do pedido, os pedidos podem ter sido feitos no mesmo momento
            ou o sistema não realizou nenhuma validação nos pedidos já realziados ou o cliente fez o pedido, depois realizou 
            o cancelamento e realizou o pedido novamente, se o sistema não deletou o primeiro pedido ocorreu uma duplicidade 
            na hora do novo pedido.

        •O risco que representa:
            -Para o sistema isso pode prejudicar na disponibilidade desse produto no estoque da loja, pois como o pedido foi
            duplicado os itens vão ser removidos x2 do estoque do estabelecimento, com isso, tento que ajustar tanto os pedidos
            quando o estoque do estabelecimento.

            -Para o negócio, pode gerar uma cobrança duplicada para o cliente, como se o mesmo estivesse realizado duas compras nessa
            loja, por conta do pedido está duplicado. Isso pode deixar o cliente desconfiado em utilizar a plataforma novamente.

        •É um problema urgente ou importante?:
            -Segundo a Matriz de Eisenhower essa situação se enquadra como importante, mas não urgente, pois esse problema
            ocorreu apenas uma vez durante toda a semana, será preciso analisar melhor o que gerol esse erro para ser criado o planejamento
            para solucionar esse problema.

    -Um bug de cálculo de frete foi corrigido em produção diretamente (sem PR, sem teste).
        •Causa mais provável desse problema:
            -Foi realizado algum calculo errado, ou alguma equação estava escrita de uma forma e estava recebendo outro tipo de valor
            o que estava causando o bug no sistema na hora de realizar o calculo do frete.

        •O risco que representa:
            -Para o sistema esse erro gera muito impacto na hora de realizar o calculo da compra do cliente, como esse bug foi corrigido
            sem ser testado e sem ser documentado o que foi feito para resolver esse problema, isso pode gerar um novo bug onde a equipe
            demorará mais para solucionar esse novo bug.

            -Para o negócio é ruim pois o cliente ou irá ver um valor muito exorbitante ou um valor muito ameno, o que deixará o mesmo 
            desconfiado com o valor que está sendo cobrado no frete, podento até faze-lo procurar o mesmo produto em outro sites para 
            verificar a questão do frente.

        •É um problema urgente ou importante?:
            -Segundo a Matriz de Eisenhower essa situação se enquadra como urgente e importante, pois esse bug está afetando diretamente 
            a produção, mesmo o bug tendo sido resolvido como não foi documentado e nem testado, é valido estudar o que foi feito e realizar
            os teste para não gerar um problema maior futuramente.

    -O código da camada de negócio tem +4.000 linhas em um único arquivo.
        •Causa mais provável desse problema:
            -Como se trata de um sistema legado, é um sistema que está funcionando a muito tempo, e cada equipe que trabalhou nesse projeto
            apenas implementou novas funções, novas regras de negócio, diretamente na camada de negócio do projeto, o que com o tempo ocasionou
            um arquivo muito extenso.

        •O risco que representa:
            -Para o sistema isso representa um grande problema, pois caso seja preciso adicionar uma nova regra de negócio, não será simples
            e poderá gerar algum bug com as regras já presentes no sistema.

            -Para o usuário final ele não irá ser muito impactado devido ao sistema está com essa sobrecarga com as regras do negócio.

        •É um problema urgente ou importante?:
            -Segundo a Matriz de Eisenhower essa situação se enquadra como importante, mas não urgente, como o sistema continua funcionando 
            corretamente, a equipe consegue separar algum tempo para simplificar esse arquivo, tornando-o mais limpo e mais legível.

    -Não há testes automatizados. Nenhum.
        •Causa mais provável desse problema:
            -Por ser um sistema legado, pode utilizar uma tecnologia mais antiga que poucas pessoas tem domínio, e por o arquivo está
            com muitas informações implementar um teste automatizado pode demandar muito tempo e pode acabar atrapalhando o funcionamento
            do sistema.

        •O risco que representa:
            -Para o sitema isso é muito critico, pois como não tem nenhum teste os erros podem aparecer sem nenhuma explicação inicial
            e sem nenhuma medida paliativa para solucionar o problema que venha a aparecer.

            -O usuário não sentira a falta desses testes, pois o sistema como um todo continua funcionando normalmente.

        •É um problema urgente ou importante?:
            -Segundo a Matriz de Eisenhower essa situação se enquadra como urgente e importante, pois qualquer problema que possa aparecer
            e não esteja sendo tratado pode resultar em uma parada complete do sistema até a correção completa do sistema.

Seção 2 - Plano de ação:

    -Um bug de cálculo de frete foi corrigido em produção diretamente (sem PR, sem teste):
        •O que será feito em termos técnicos:
            -Inicialmente iremos verificar o que foi feito, depois será aplicado uma engenharia reversar para causar novamente o bug
            com o bug novamente no projeto, será analizado a melhor formula para realizar da forma, o projeto precisa da informação 
            de onde está o endereço do cliente, para assim realizar o calculo da distância de onde a mercadoria está para onde ela será 
            entrega, com esse calculo em mãos, será calculado quando a empressa cobra por KM para realizar essa entrga ao cliente, a 
            empressa pode utilizar também o calculo que o objeto que está sendo entregue, caso seja um produtor maior ou mais pesado
            pode influenciar no frete, com todos esses dados o sistema irá realizar a multiplicação do valor do KM x Deslocamento até
            o cliente + adicional pelo peso do produto.

        •Qual o esforço(horas/dias):
            -Estimo que em 7 dias essa solução estará entregue

        •Como saberá que o problema foi resolvido:
            -Os valores dos fretes começaram a aparecer com um certo padrão para o cliente final, além de não ocorrer de aparecer valores
            absortos ou valores nulos para o cliente.

    -Dois pedidos foram criados em duplicitade na última semana:
        •O que será feito em termos técnicos:
            -Será analisado a função responsável pela a inclusão do pedido no sistema, a função pode estar sendo executada duas vezes com o
            mesmo pedido, o bloco dessa função de pedido será isolado e será criado testes para verificar o que está causando a duplicidade,
            achando o erro vamos corrigir a função de pedido para que a mesma só tenha uma situação onde será executado a função de incluir 
            o pedido.

        •Qual o esforço(horas/dias):
            -Estimo que em 5 dias essa solução será entrgue

        •Como saberá que o problema foi resolvido:
            -Não irá ocorrer a duplicidade de nenhum pedido no sistema, ou seja, não teremos problema com o estoque e nem com o caixa da 
            empresa, pois não terá valores faltando.    

    -Não há testes automatizados. Nenhum:
        •O que será feito em termos técnicos:
            -Iremos realizar a análise nas partes críticas do sistema, com isso, irmos criando testes unitários para essas partes cíticas
            do sistema, cada teste automático que seja feito, será disparado um e-mail para o setor responsável pela manutenção do sistema,
            em caso de erro, a equipe já entrar em ação para solucionar o problema o mais breve possível, com isso podemos testandos mais partes
            do sistema, até cobrir todo o sistema.

        •Qual o esforço(horas/dias):
            -Estimo que em 12 dias essa solução será entregue

        •Como saberá que o problema foi resolvido:
            -A equipe responsável pelo sistema irá receber um e-mail em caso de erro ou em casso de sucesso nos testes, a equipe receberá um
            feedback de como está o sistema.    

Seção 3 - Decisão de arquitetura:

    •Opção A - Refatoração incremental:
        -Escolho essa opção por ser um mudança mais tranquila, como o sistema está em produção, e o time está muito ocupado,
        não estamos em uma situação favorável para correr riscos, se formos realziar toda a reescrita do módulo com testes e 
        uma arquitetura limpa, se ocorrer algum erro será necessário voltar tudo o que foi feito, o que impactará na disponibilidade do 
        sistema além de gerar um retrabalho para a equipe tento que voltar para uma versão que tinha sido removida do sistema.
        Extrair os módulos menores e ir realizando a oraganização sem para o sistema, por mais que seja um processo mais lento
        é um processo mais seguro pois a possibilidade de ocorrer um erro é quase nulo, e caso venha a ocorrer um erro no processo,
        por estar se tratanto de um módulo pequeno a correção não irá demandar muito tempo e será mais fácil pois está sendo trabalhado
        em uma parte específica do código.

Seção 4 - Requisitos Não Funcionais ignorados:

    •Requisitos Não Funcionais(RNF):
        -Validação dos endpoints
        -Persistência de dados
        -Manutenção e verificação de logs de erro
    
    •Os requisitos funcionais listados a cima, mostra pontos em que a equipe deve verificar, porque em horarios de pico o sistema
    apresenta uma lentidão no endpoint responsável por mostrar os pedidos, outro ponto é a persistência dos dados da plataforma
    como teve uma semana que ocoreu a duplicidade de um pedido, por fim, a realização de testes e a criação de um log para armazenar os
    erros do sistema, como atualmente o sistema não apresenta esses testes pode ocassionar um problema mais demorada para solucionar o 
    problema devido a não tem um log contendo os erros causados pelo sistema.

    •Deixar esses elementos em pauta para em uma reunião com a equipe seja mostrado esses pontos e deixar informado a equipe a necessidade
    de começar a implementar esses requisitos não funcionais, para melhorar a disponibilidade do sistema e manter o mesmo seguro contra
    possíveis falahas que venham a surgir.