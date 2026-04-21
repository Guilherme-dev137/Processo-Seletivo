No backend, organizei o projeto em camadas simples: rotas para os endpoints, controllers para validações e regras da API, e model para manipular os dados. Isso deixa o código mais organizado e fácil de manter.

Para a API ser confiável em produção, eu trocaria o armazenamento em memória por um banco de dados real, adicionaria logs estruturados para acompanhar erros e uso da aplicação, e monitoramento com health checks e métricas de desempenho.

Se o sistema precisasse de múltiplos usuários com autenticação, eu adicionaria login, tokens ou sessão, uma tabela de usuários no banco e vínculo entre cada tarefa e seu usuário. Assim, cada pessoa veria e alteraria apenas as próprias tarefas.