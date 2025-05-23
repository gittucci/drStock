# drStock
Projeto TCC Usp/Esalq (protótipo de software)

Estudo feito com o método Event-Storming

O software DrStock é uma aplicação que gerencia o estoque de produtos.
Abaixo temos um resumo da composição:

### 1. Frontend
O frontend é a interface onde os usuários interagem com o sistema. Ele foi construído usando framework Next-Js.

### 2. Services
- Stock Service: Gerencia as operações relacionadas ao estoque, como consultar e atualizar quantidades.

- Entries Service: Lida com as entradas de produtos no estoque, registrando quando novos produtos são adicionados.

- Exits Service: Gerencia as saídas de produtos, registrando quando produtos são vendidos ou removidos do estoque.

- Catalog Service: Mantém o catálogo de produtos, incluindo informações detalhadas sobre cada produto.

- Suppliers Service: Gerencia informações sobre fornecedores, permitindo que os usuários adicionem e atualizem dados de fornecedores.

- Customers Service: Lida com informações sobre clientes, permitindo que os usuários gerenciem dados de clientes.

Cada um desses serviços tem suas próprias APIs, que são chamadas pelo frontend via API Gateway.

### 3. API Gateway
O API Gateway atua como um ponto de entrada único para todas as requisições feitas ao backend. Ele roteia as requisições para os serviços apropriados, gerencia autenticação e autorização, e pode implementar funcionalidades como caching e rate limiting. O uso de um API Gateway simplifica a comunicação entre o frontend e os serviços, permitindo que o frontend faça chamadas para um único endpoint em vez de múltiplos serviços.

### Para rodar o ambiente (tirar as quebras de página):
docker-compose
-f services/catalog/docker-compose.yml
-f services/customers/docker-compose.yml
-f services/entries/docker-compose.yml
-f services/exits/docker-compose.yml
-f services/gateway/docker-compose.yml
-f services/stock/docker-compose.yml
-f services/suppliers/docker-compose.yml
-f frontend/docker-compose.yml
### FIM ! 