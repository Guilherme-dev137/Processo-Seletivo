Quais foram as principais decisões de tratamento que você tomou? (ex.: o que fazer com registros órfãos, como normalizar cidades):
    •As principais decisões de tratamento foram padronizar textos, corrigir datas e converter valores numéricos para um formato consistente. Também tratei campos vazios com valores padrão como nao_informado e NA, normalizei cidades removendo acentos e ajustando maiúsculas/minúsculas, e mantive registros órfãos usando left join para não perder pedidos sem cliente ou entrega correspondente.

Seu pipeline é idempotente? Ou seja, rodá-lo duas vezes produz o mesmo resultado? Justifique.
    •Sim, o pipeline é idempotente. Rodando duas vezes com os mesmos arquivos de entrada, ele gera o mesmo resultado, porque as transformações seguem regras fixas e os arquivos de saída são recriados com o mesmo conteúdo, sem acumular dados da execução anterior.

Se esse pipeline fosse executado diariamente com arquivos de 10 milhões de linhas, o que você mudaria na abordagem?
    •Para 10 milhões de linhas por dia, eu mudaria a abordagem para ganhar desempenho e memória. Usaria leitura em blocos ou ferramentas mais eficientes para grandes volumes, como polars, dask ou banco de dados, evitaria carregar tudo de uma vez na memória e separaria melhor as etapas de processamento e agregação.

Que testes você escreveria para garantir a qualidade das transformações?
    •Eu escreveria testes para validar leitura dos arquivos, normalização de texto, conversão de datas, conversão de valores monetários, cálculo de atraso, tratamento de nulos, manutenção de registros órfãos e geração correta dos indicadores finais. Também faria testes com casos limite, como campos vazios, datas inválidas e valores fora do padrão.








