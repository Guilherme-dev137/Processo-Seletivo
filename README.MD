======== INFORMAÇÕES PESSOAIS ========
* Guilherme Gonçalves Soares         *
* (81) 9 9329 - 8501                 *
* guilhermegoncalves1720@gmail.com   *
======================================

========= Stack(s) utilizadas ========
PYTHON | SQLITE | REACT | BOOTSTRAP | NODE.JS | JAVASCRIPT | EXPRESS | CORS | VITE | PANDAS |


============== Kata-1 ================

Para resolver o desafio proposto no campo do kata-1, foram utilizadas as Stacks Python e SQLite
Utilizei o Python pois é uma linguagem propria para a análise de dados, além de possuír uma linguagem mais
próxima a nossa linguagem tornandoa mais simples, sem contar com as bibliotecas que ela tem disponível o que 
ajuda muito a filtrar, organizar e tratar dados.

Outro motivo para eu ter escolhido o Python para esse projeto, foi pensnado em futuras melhorias para o sistema,
utilizar os dados para criar um dashboard, para melhorar a visualização das informações, tanto para os pacientes 
terem uma noção de como está o atendimento quanto para os médicos terem uma base de como está o dia, utilizar o mesmo 
como um back-end e um front-end para ser registrados novos pacientes tudo isso vinculado a um banco de dados para manter as 
informações salvas e principalmente sincronizadas.

O SQLite foi utilizado por ser uma versão mais simples do banco SQL, inicialmente o projeto "VERSAODB.PY" conta com o salvamento
da lista que foi ordenada em um banco de dados, fazendo com que os dados não sejam perdidos mediante a alguma falha no sistema,
foi utilizado pois tem uma proposta mais simples e que futuramente pode ser atualizado para o banco de dados SQL tornando o sistema 
mais robusto, e o banco de dados SQLite tem integração com a linguagem Python o que facilitou a implementação desse banco.

==== Como executar o programa localmente ====

O aplicativo executa diretamente pelo terminal, é preciso ter o python instalado na máquina, segue o passo-a-passo:

1º- Abrir o terminal do Windows, prescione as teclas: "win" + "r", depois digite: "cmd", depois aperte "enter"
2º- Com o terminal aberto localize a pasta do arquivo, a mesma está salva como "kata-1"
3º- Entre na pasta utilizando o comando: "cd kata-1"
4º- Dentro da pasta execute o comando: "python ordenaFila.py" para executar o aplicativo inicial, o mesmo já conta com uma base de dados para ser ordenada

Caso queira realziar os testes, na mesma pasta execute o comando: "python testesUnitarios.py"

Se quiser executar a versão com o banco de dados, na mesma pasta execute o comando: "python versaoDB.py"



============== Kata-2 ================

Para resolver o desafio do kata-2, foram utilizados as tecnologias: 
    Para o front-end:
        React | Bootstrap | Vite | JavaScript

    Para o back-end:
        Node.js | Express | Cors 

Optei por utilizar o React nesse projeto devido as integrações que essa tecnologia possúi, tanto com o back-end quanto para possíveis melhorias desse projeto,
como por exemplo evoluir esse projeto para um aplicativo mobile, além disso, o React tem uma alta performace, isso ajuda na hora de evoluir o projeto com a implementação
de mais funções junto a isso utilizei o Vite para a otimizar a criação do front-end, o Vite utilizado com o React simplifica a configuração e consecultivamente diminui o 
tempo para a inicialização do servidor, tornando a aplicação mais rápida para aplicar as mudanças realizadas no desenvolvimento do sistema.

O javaScript foi utilizado devido a utilização do back-end ser em Node.js e a utilização do React que funciona com o proprio JavaScript, além de tornando mais fácil a integração 
do front-end com o back-end, por utilizar a mesma linguagem tanto no front-end quanto no back-end.

Já o Bootstrap foi utilizado para otimizar o tempo da estilização, no lugar de criar um arquivo CSS para estilizar todo o projeto, utilizei o Bootstrap que contém estilos 
prontos para serem utilizados diretamente no HTML.

Como estou utilizando o React para o front-end, o próprio React precisa utilizar um servidor em Node para ser executado, aproveitando disso criei o servidor desse projeto com
o próprio Node.js com os frameworks Express, nativo do Node e o Cors que é um mecanismo de segurança que utiliza cabeçalhos HTTP, como o mesmo também tem compatibilidade com
o Node foi mais fácil realizar a implementação dessas tecnologias, para subir o servidor desse projeto.

==== Como executar o programa localmente ====

Para executar esse projeto é preciso ter o Node.js instalado na máquina,
Todo o arquivo foi disponibilizado no github, segue passo-a-passo:

1º- Baixar o arquivo do Github para a máquina
2º- Abrir um terminal no Windows,  prescione as teclas: "win" + "r", depois digite: "cmd", depois aperte "enter"
3º- Navegue até a pasta do arquivo que foi copiado e colado na máquina
4º- Dentro da pasta "kata-2/" acesse o diretório: "backend", comando para acessar o diretório: "cd backend"
5º- Instale as dependências do projeto, no caminho: "kata-2/backend/", execute o comando: "npm install"
6º- Depois das dependências instaladas, execute o servidor com o comando: "npm run dev", com isso o back-end estará ativo
7º- Abra outro terminal do Windows para executar o front-end
8º- Com o segundo terminal aberto, navegue até a pasta: "kata-2/frontend/"
9º- Dentro da pasta será preciso baixar as dependências com o comando: "npm install"
10º- Depois basta executar o front-end com o comando: "npm run dev"
11º- Para validar o front-end basta acessa por meio do navegador esse endereço: "http://localhost:5173"
12º- Para validar o back-end basta acessar por meio do navegador esse endereço: "http://localhost:3000/health"

Os arquivos estão sendo armazenados por meio do back-end, o projeto não conta com um banco de dados, quando o servidor é reiniciado os dados voltam para os valores padrão.



============== Kata-3 ================

Dentro da pasta kata-3 encontra-se o arquivo PLANO.MD com todas as seções respondidas



============== Kata-4 ================

Para solucionar o desafio do kata-4 eu utilizei novamente o Python com a biblioteca pandas, o Python é uma tecnologia muito boa para análise de dados além disso possui muitas bibliotecas que auxiliam nisso, a exemplo temos a biblioteca Pandas, que é uma excelente biblioteca par trabalhar com planilhas, por isso utilizei o Python para realizar toda a análise dos dados assim como o tratamento dos dados e a geração dos arquivos.

A estrutura que utilizei foi uma pasta com todas as informções em CSV, pasta com o nome "valores_iniciais" e todo os resultados estão sendo salvos na pasta "Resultados", como solicitado, o primeiro arquivo gerado é a união de todos os dados que estão presentes na pasta "valores_iniciais" esse arquivo CSV recebe o nome de analise_inicial, pois além de juntar os arquivos é realizado um tratamento nos dados, pois alguns campos não possuem valores, o formato de alguns valores não estão em nenhum padrão o que dificulta caso seja preciso realizar alguma consulta, o que pode oassionar em uma entrega de valores errados. o segundo arquivo gerado é dependente do primeiro, no segundo arquivo é análisado os valores que estão presentes no primeiro e é realizado cálculos médios, da quantidade de pedidos, rank de qual estado realizou mais pedidos, qual a média de entrega de produtos com atraso, entre outras informações.

==== Como executar o programa localmente ====
Para executar esse projeto será necessário ter o Python instalado na máquina, além disso é preciso instalar a biblioteca Pandas, com o Python já instalado na máquina execute esse comando para instalar a biblioteca:

1º- Aperte a tecla "Win" 
2º- Digite PowerShell, e execute como adminstrador
3º- Digite esse comando no terminal: py -m pip install pandas
4º- Depois aperte enter que a biblioteca será instalada

Com a biblioteca instalada na máquina junto ao próprio Pthon, basta copiar toda a pasta kata-4 para a máquina, com isso acesse a pasta por meio do terminal:

1º- Aperte as teclas "Win" + "r", e digite cmd, depois aperte enter
2º- Navegue até a pasta "kata-4/"
3º- Dentro da pasta "kata-4" exceute esse comando: python pipeline_tratamento_dados.py
4º- Resultado da execução do script ficará disponível em "kata-4/resultados"

Esse passo-a-passo irá executar o script que foi desenvolvido para realizar todos os tratamentos dos dados disponibilizados.