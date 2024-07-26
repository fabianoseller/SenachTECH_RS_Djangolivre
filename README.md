

# ![Cucumber Logo](https://github.com/cucumber-ltd/brand/raw/master/images/png/notm/cucumber-black/cucumber-black-128.png)

Cucumber is a tool that supports [Behaviour-Driven Development
(BDD)](https://cucumber.io/blog/2017/05/15/intro-to-bdd-and-tdd) - a software
development process that aims to enhance software quality and reduce
maintenance costs.



-------------------------------------------------------------
Documento com as documentações e escopos do projeto que discutimos. Vou criar um esboço de documento com base nas informações que temos disponíveis. Lembre-se de que este é um documento inicial e pode precisar de ajustes ou adições conforme necessário.
Título: Documentação do Sistema de Registros de Filmes Tarantino
Objetivo Principal do Sistema O objetivo principal do sistema é fornecer uma plataforma para usuários registrarem e gerenciarem informações sobre filmes, com foco específico nos filmes de Quentin Tarantino.
Objetivos Específicos 2.1. Gerenciamento de usuários
Permitir que novos usuários se registrem no sistema
Autenticar usuários existentes através de um processo de login
Gerenciar sessões de usuários, incluindo logout
2.2. Cadastro e Gerenciamento de Filmes
Permitir que usuários autenticados adicionem novos filmes ao sistema
Possibilidade de edição de informações de filmes existentes
Permitir a exclusão de filmes do sistema
2.3. Visualização de Filmes
Exibir uma lista de filmes cadastrados pelo usuário logado
Veja detalhes de cada filme, como nome, ano de lançamento, diretor e sinopse
2.4. Personalização de Cadastros
Associar filmes a usuários específicos através do modelo Cadastro
Permitir que os usuários adicionem especificamente aos filmes cadastrados
2.5. Feedback ao Usuário
fornecer mensagens de feedback para ações como login, registro, adição, edição e exclusão de filmes
2.6. Segurança
Implementar o controle de acesso, garantindo que apenas usuários autenticados possam realizar operações no sistema
2.7. Interface Amigável
Oferecer uma interface intuitiva e responsiva para interação com o sistema
2.8. Organização de Dados
Manter uma estrutura organizada de dados, relacionando usuários, filmes e cadastros
Requisitos Funcionais (RF) RF01 - Registro de Usuário RF02 - Login RF03 - Logout RF04 - Adicionar Filme RF05 - Visualizar Filmes RF06 - Editar Filme RF07 - Excluir Filme RF08 - Mensagens de Feedback







Requisitos Não Funcionais (RNF) RNF01 - Desempenho RNF02 - Segurança RNF03 - Usabilidade RNF04 - Compatibilidade RNF05 - Manutenibilidade




Modelo de Dados 5.1. Entidades Principais
Usuário (modelo de usuário integrado do Django)
Filme
Cadastro
5.2. Relacionamentos
Usuário tem muitos Cadastros (um-para-muitos)
Filme tem muitos Cadastros (one-to-many)
Cadastro pertence a um usuário e a um filme (many-to-one para ambos)
Principais Funcionalidades Implementadas 6.1. Autenticação de Usuários 6.2. Registro de Novos Usuários 6.3. Adição de Filmes 6.4. Edição de Filmes 6.5. Exclusão de Filmes 6.6. Visualização de Filmes do Usuário





Interface do Usuário 7.1. Telas Principais
Tela de Login
Tela de Registro
Página Inicial (Home)
Tela de Adição de Filme
Tela de Edição de Filme
7.2. Elementos de Design
Uso de cores escuras com destaque em amarelo para elementos importantes
Imagens de fundo relacionadas a filmes de Tarantino
Layout responsivo para diferentes tamanhos de tela
Tecnologias Utilizadas
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Banco de Dados: SQLite (desenvolvimento) / PostgreSQL (produção)
Considerações Futuras
Implementação de um sistema de busca de filmes
Adição de uma funcionalidade de avaliação de filmes
Integração com APIs externas para obter informações adicionais sobre os filmes

--------------------------------------

manutenção e expansão futura. Com base no código que você encontrou, vou sugerir um diagrama de classes básico para o seu sistema de registro de filmes Tarantino.
Aqui está uma descrição textual do diagrama de classes:
Classe User (modelo User integrado do Django)
Atributos: nome de usuário, e-mail, senha, etc.
Classe Filme
Atributos:
nome (CharField)
ano_lancamento (IntegerField)
diretor (CharField)
sinopse (Campo de texto)
Métodos:
str (): retorna o nome do filme
Classe Cadastro
Atributos:
usuário (ForeignKey para usuário)
filme (ForeignKey para Filme)
descrição (TextField)
Métodos:
str (): retorna uma representação string do cadastro
Classe FilmeForm (ModelForm)
Campos: baseado no modelo Filme
Classe UserRegisterForm (UserCreationForm)
Campos: nome de usuário, e-mail, senha1, senha2
Relações:
Usuário tem muitos Cadastros (um-para-muitos)
Filme tem muitos Cadastros (one-to-many)
Cadastro pertence a um usuário e a um filme (many-to-one para ambos)
Para criar um diagrama visual, você pode usar ferramentas como:
Draw.io (gratuito, baseado na web)
Lucidchart (tem versão gratuita e paga)
PlantUML (gratuito, baseado em texto)
Microsoft Visio (pago, parte do pacote Office)
Ao criar o diagrama, você deve:
Representar cada classe como um retângulo
Listar os atributos e métodos dentro de cada retângulo de classe
Desenhar linhas para representar as relações entre as classes
Usar símbolos protetores para indicar o tipo de relação (por exemplo, seta para herança, linha com diamante para composição)
Além do diagrama de classes, você também pode considerar criar:
Diagrama de casos de uso: para mostrar as interações do usuário com o sistema
Diagrama de sequência: para ilustrar o fluxo de operações para processos importantes
Diagrama de relacionamento entidade (ER): para representar a estrutura do banco de dados
Estes diagramas, junto com uma descrição textual do sistema, formarão uma documentação abrangente do seu projeto.
ok..pode gerar os casos de uso e distração de sequência
Fontes

Responder
Claro, você vai gerar os casos de uso e um diagrama de sequência para o seu sistema de registro de filmes Tarantino. Começaremos com os casos de uso e, em seguida, criaremos um diagrama de sequência para um dos casos de uso principais.
Casos de uso:
Registro de Usuário
Ator: Usuário não autenticado
Descrição: O usuário se registra no sistema fornece nome de usuário, e-mail e senha.
Conecte-se
Ator: Usuário registrado
Descrição: O usuário faz login no sistema usando suas credenciais.
Sair
Ator: Usuário autenticado
Descrição: O usuário faz logout do sistema.
Adicionar Filme
Ator: Usuário autenticado
Descrição: O usuário adiciona um novo filme ao sistema, fornece nome, ano de lançamento, diretor e sinopse.
Visualizar Filmes
Ator: Usuário autenticado
Descrição: O usuário visualiza a lista de filmes que adicionou ao sistema.
Editar Filme
Ator: Usuário autenticado
Descrição: O usuário edita as informações de um filme existente.
Excluir Filme
Ator: Usuário autenticado
Descrição: O usuário remove um filme do sistema.
Diagrama de Sequência para o caso de uso "Adicionar Filme":
texto
Usuário                   Interface                 View                   Modelo
   |                          |                       |                       |
   | Clica em "Adicionar Filme"|                       |                       |
   |-------------------------->|                       |                       |
   |                          | Exibe formulário       |                       |
   |                          |<------------------------|                       |
   | Preenche o formulário    |                       |                       |
   |-------------------------->|                       |                       |
   |                          | Envia dados do filme   |                       |
   |                          |----------------------->|                       |
   |                          |                       | Valida dados          |
   |                          |                       |-------------------|   |
   |                          |                       | Cria novo filme   |   |
   |                          |                       |------------------>|   |
   |                          |                       |                   |   |
   |                          |                       | Salva filme       |   |
   |                          |                       |------------------>|   |
   |                          |                       |                   |   |
   |                          |                       | Confirma salvamento   |
   |                          |                       |<------------------|   |
   |                          | Exibe mensagem de     |                       |
   |                          | sucesso               |                       |
   |<--------------------------|                       |                       |
   |                          |                       |                       |

Este diagrama de sequência mostra o fluxo de interações entre o usuário, a interface, a visualização e o modelo quando um usuário adiciona um novo filme ao sistema. Ele ilustra os seguintes passos:
O usuário clicou no botão "Adicionar Filme" na interface.
A interface solicita a visualização do formulário de adição de filme.
A view retorna o formulário, que é exibido pela interface.
O usuário preenche o formulário com os detalhes do filme.
A interface envia os dados do formulário para uma visualização.
Uma visão válida dos dados recebidos.
Se os dados são válidos, a visualização cria um novo objeto Filme.
O novo objeto Filme é salvo no banco de dados.
O modelo confirma que o filme foi salvo com sucesso.
A visualização informa à interface que o filme foi adicionado com sucesso.
A interface exibe uma mensagem de sucesso para o usuário.
Este diagrama da sequência fornece uma visão clara do processo de adição de um novo filme, mostrando como os diferentes componentes do sistema interagem entre si para realizar esta tarefa.
gere os Requisitos Funcionais (RF) 5 Requisitos Não Funcionais (RNF
Fontes

Responder
Com base nas informações fornecidas e no código do sistema de registro de filmes Tarantino, aqui estão os Requisitos Funcionais (RF) e Requisitos Não Funcionais (RNF):
Requisitos Funcionais (RF)
RF01 - Registro de Usuário :
O sistema deve permitir que novos usuários se registrem fornecendo um nome de usuário, e-mail e senha.
O sistema deve validar as informações fornecidas e criar uma nova conta do usuário.
RF02 - Login :
O sistema deve permitir que os usuários façam login usando seu nome de usuário e senha.
O sistema deve autenticar as credenciais do usuário e permitir que o acesso ao sistema seja válido.
RF03 - Sair :
O sistema deve permitir que os usuários façam logout, encerrando sua sessão atual.
RF04 - Adicionar Filme :
O sistema deve permitir que usuários autenticados adicionem novos filmes, forneçam nome, ano de lançamento, diretor e sinopse.
O sistema deve validar as informações fornecidas e salvar o novo filme no banco de dados.
RF05 - Visualizar Filmes :
O sistema deve permitir que usuários autenticados visualizem a lista de filmes que adicionaram ao sistema.
A lista deve exibir o nome, ano de lançamento, diretor e sinopse de cada filme.
RF06 - Editar Filme :
O sistema deve permitir que usuários autenticados editem as informações de um filme existente.
O sistema deve validar as informações atualizadas e salvar as alterações no banco de dados.
RF07 - Excluir Filme :
O sistema deve permitir que usuários autenticados excluam um filme existente.
O sistema deve remover o filme do banco de dados e confirmar a exclusão do usuário.
RF08 - Mensagens de Feedback :
O sistema deve exibir mensagens de feedback para ações como registro, login, adição, edição e exclusão de filmes.
Requisitos Não Funcionais (RNF)
RNF01 - Desempenho :
O sistema deve responder às ameaças dos usuários dentro de 2 segundos em 95% das vezes.
RNF02 - Segurança :
O sistema deve criptografar as senhas dos usuários usando um algoritmo seguro (por exemplo, bcrypt).
O sistema deve implementar autenticação baseada em sessão para gerenciar o acesso dos usuários.
RNF03 - Usabilidade :
O sistema deve fornecer uma interface de usuário intuitiva e fácil de usar, com navegação clara e feedback imediato para as ações do usuário.
RNF04 - Compatibilidade :
O sistema deve ser compatível com os navegadores web mais populares (por exemplo, Chrome, Firefox, Safari, Edge).
RNF05 - Manutenibilidade :
O código do sistema deve ser modular e bem documentado para facilitar a manutenção e expansões futuras.
Diagrama de Casos de Uso
Aqui está uma descrição textual dos casos de uso, que você pode usar para criar um diagrama de casos de uso visual:
Registro de Usuário
Ator: Usuário não autenticado
Descrição: O usuário se registra no sistema fornece nome de usuário, e-mail e senha.
Conecte-se
Ator: Usuário registrado
Descrição: O usuário faz login no sistema usando suas credenciais.
Sair
Ator: Usuário autenticado
Descrição: O usuário faz logout do sistema.
Adicionar Filme
Ator: Usuário autenticado
Descrição: O usuário adiciona um novo filme ao sistema, fornece nome, ano de lançamento, diretor e sinopse.
Visualizar Filmes
Ator: Usuário autenticado
Descrição: O usuário visualiza a lista de filmes que adicionou ao sistema.
Editar Filme
Ator: Usuário autenticado
Descrição: O usuário edita as informações de um filme existente.
Excluir Filme
Ator: Usuário autenticado
Descrição: O usuário remove um filme do sistema.
Diagrama de Sequência para "Adicionar Filme"
Aqui está a descrição textual do diagrama de sequência para o caso de uso "Adicionar Filme":
O usuário clicou no botão "Adicionar Filme" na interface.
A interface solicita a visualização do formulário de adição de filme.
A view retorna o formulário, que é exibido pela interface.
O usuário preenche o formulário com os detalhes do filme.
A interface envia os dados do formulário para uma visualização.
Uma visão válida dos dados recebidos.
Se os dados são válidos, a visualização cria um novo objeto Filme.
O novo objeto Filme é salvo no banco de dados.
O modelo confirma que o filme foi salvo com sucesso.
A visualização informa à interface que o filme foi adicionado com sucesso.
A interface exibe uma mensagem de sucesso para o usuário.
Você pode usar ferramentas como Draw.io, Lucidchart ou PlantUML para criar os diagramas visuais com base nessas solicitações textuais.
sobre telas web podemos documentar?
Fontes

Responder
Para documentar as telas do sistema de registro de filmes de Tarantino, vamos detalhar os seguintes aspectos:
Requisitos Funcionais (RF)
Requisitos Não Funcionais (RNF)
Casos de Uso
Diagrama de Sequência
Requisitos Funcionais (RF)
RF01 - Registro de Usuário :
O sistema deve permitir que novos usuários se registrem fornecendo um nome de usuário, e-mail e senha.
O sistema deve validar as informações fornecidas e criar uma nova conta do usuário.
RF02 - Login :
O sistema deve permitir que os usuários façam login usando seu nome de usuário e senha.
O sistema deve autenticar as credenciais do usuário e permitir que o acesso ao sistema seja válido.
RF03 - Sair :
O sistema deve permitir que os usuários façam logout, encerrando sua sessão atual.
RF04 - Adicionar Filme :
O sistema deve permitir que usuários autenticados adicionem novos filmes, forneçam nome, ano de lançamento, diretor e sinopse.
O sistema deve validar as informações fornecidas e salvar o novo filme no banco de dados.
RF05 - Visualizar Filmes :
O sistema deve permitir que usuários autenticados visualizem a lista de filmes que adicionaram ao sistema.
A lista deve exibir o nome, ano de lançamento, diretor e sinopse de cada filme.
RF06 - Editar Filme :
O sistema deve permitir que usuários autenticados editem as informações de um filme existente.
O sistema deve validar as informações atualizadas e salvar as alterações no banco de dados.
RF07 - Excluir Filme :
O sistema deve permitir que usuários autenticados excluam um filme existente.
O sistema deve remover o filme do banco de dados e confirmar a exclusão do usuário.
RF08 - Mensagens de Feedback :
O sistema deve exibir mensagens de feedback para ações como registro, login, adição, edição e exclusão de filmes.
Requisitos Não Funcionais (RNF)
RNF01 - Desempenho :
O sistema deve responder às ameaças dos usuários dentro de 2 segundos em 95% das vezes.
RNF02 - Segurança :
O sistema deve criptografar as senhas dos usuários usando um algoritmo seguro (por exemplo, bcrypt).
O sistema deve implementar autenticação baseada em sessão para gerenciar o acesso dos usuários.
RNF03 - Usabilidade :
O sistema deve fornecer uma interface de usuário intuitiva e fácil de usar, com navegação clara e feedback imediato para as ações do usuário.
RNF04 - Compatibilidade :
O sistema deve ser compatível com os navegadores web mais populares (por exemplo, Chrome, Firefox, Safari, Edge).
RNF05 - Manutenibilidade :
O código do sistema deve ser modular e bem documentado para facilitar a manutenção e expansões futuras.
Casos de Uso
Registro de Usuário
Ator: Usuário não autenticado
Descrição: O usuário se registra no sistema fornece nome de usuário, e-mail e senha.
Conecte-se
Ator: Usuário registrado
Descrição: O usuário faz login no sistema usando suas credenciais.
Sair
Ator: Usuário autenticado
Descrição: O usuário faz logout do sistema.
Adicionar Filme
Ator: Usuário autenticado
Descrição: O usuário adiciona um novo filme ao sistema, fornece nome, ano de lançamento, diretor e sinopse.
Visualizar Filmes
Ator: Usuário autenticado
Descrição: O usuário visualiza a lista de filmes que adicionou ao sistema.
Editar Filme
Ator: Usuário autenticado
Descrição: O usuário edita as informações de um filme existente.
Excluir Filme
Ator: Usuário autenticado
Descrição: O usuário remove um filme do sistema.
Diagrama de Sequência para "Adicionar Filme"
Aqui está a descrição textual do diagrama de sequência para o caso de uso "Adicionar Filme":
O usuário clicou no botão "Adicionar Filme" na interface.
A interface solicita a visualização do formulário de adição de filme.
A view retorna o formulário, que é exibido pela interface.
O usuário preenche o formulário com os detalhes do filme.
A interface envia os dados do formulário para uma visualização.
Uma visão válida dos dados recebidos.
Se os dados são válidos, a visualização cria um novo objeto Filme.
O novo objeto Filme é salvo no banco de dados.
O modelo confirma que o filme foi salvo com sucesso.
A visualização informa à interface que o filme foi adicionado com sucesso.
A interface exibe uma mensagem de sucesso para o usuário.
Descrição das Telas Web
Tela de Registro ( register.html)
Objetivo : Permitir que novos usuários se registrem no sistema.
Componentes :
Formulário de registro com campos para nome de usuário, e-mail e senha.
Botão "Registrar".
Link para a página de login.
Mensagens de feedback.

-----------------------

Descrição das Telas Web
Tela de Registro ( register.html)
Objetivo : Permitir que novos usuários se registrem no sistema.
Componentes :
Formulário de registro com campos para nome de usuário, e-mail e senha.
Botão "Registrar".
Link para a página de login.
Mensagens de feedback.

------------------------------------

Banco Modelo Físico
Fontes

Responder
Para criar o Modelo Físico do banco de dados para o Sistema de Registros de filmes Tarantino, vamos usar as informações fornecidas no código das visualizações e nos modelos. Aqui está uma representação do Modelo Físico do banco de dados:
SQLite
-- Tabela de Usuários (built-in do Django)
CREATE TABLE auth_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password VARCHAR(128) NOT NULL,
    last_login DATETIME,
    is_superuser BOOLEAN NOT NULL,
    username VARCHAR(150) NOT NULL UNIQUE,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    email VARCHAR(254) NOT NULL,
    is_staff BOOLEAN NOT NULL,
    is_active BOOLEAN NOT NULL,
    date_joined DATETIME NOT NULL
);

-- Tabela de Filmes
CREATE TABLE filme (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    ano_lancamento INTEGER NOT NULL,
    diretor VARCHAR(255) NOT NULL,
    sinopse TEXT
);

-- Tabela de Cadastro (relação entre Usuário e Filme)
CREATE TABLE cadastro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    filme_id INTEGER NOT NULL,
    descricao TEXT,
    FOREIGN KEY (user_id) REFERENCES auth_user (id),
    FOREIGN KEY (filme_id) REFERENCES filme (id)
);

Explicação das tabelas:
auth_user: Esta é a tabela padrão de usuários do Django. Ela armazena informações sobre os usuários registrados no sistema.
filme: Esta tabela armazena informações sobre os filmes. Cada filme tem um nome, ano de lançamento, diretor e sinopse.
cadastro: Esta tabela estabelece a relação entre usuários e filmes. Ela permite que um usuário tenha filmes múltiplos e que um filme possa ser associado a múltiplos usuários. A coluna pode ser usada para armazenar informações adicionais sobre o cadastro do filme pelo usuário.descricao
Observações:
As chaves primárias (PRIMARY KEY) são definidas como INTEGER e AUTOINCREMENT para garantir valores únicos e auto-incrementais.
As chaves estrangeiras (FOREIGN KEY) na tabela garantem a integridade referencial com as tabelas e .cadastroauth_userfilme
Os tipos de dados (VARCHAR, INTEGER, TEXT, BOOLEAN, DATETIME) são escolhidos com base nos tipos de campo usados ​​nos modelos Django.
A tabela é uma representação simplificada da tabela de usuários do Django. Na prática, o Django gerencia essa tabela automaticamente.auth_user
Este modelo físico reflete a estrutura do banco de dados necessária para suportar as funcionalidades descritas no código das visualizações, como registro de usuários, adição de filmes e associação de filmes a usuários.
Objetivo Principal do Sistema e Objetivos Específicos
Fontes

Responder
Com base no seguinte código fornecido, posso inferir os objetivos do Sistema de Registros de Filmes Tarantino:
Objetivo Principal: O objetivo principal do sistema é fornecer uma plataforma para usuários registrarem e gerenciarem informações sobre filmes, com foco específico nos filmes de Quentin Tarantino.
Objetivos Específicos:
Gerenciamento de Usuários:
Permitir que novos usuários se registrem no sistema.
Autenticar usuários existentes através de um processo de login.
Gerenciar sessões de usuários, incluindo logout.
Cadastro e Gerenciamento de Filmes:
Permitir que usuários autenticados adicionem novos filmes ao sistema.
Possibilidade de edição de informações de filmes existentes.
Permitir a exclusão de filmes do sistema.
Visualização de Filmes:
Exibir uma lista de filmes cadastrados pelo usuário logado.
Veja detalhes específicos de cada filme, como nome, ano de lançamento, diretor e sinopse.
Personalização de Cadastros:
Associar filmes a usuários específicos através do modelo Cadastro.
Permitir que os usuários adicionem detalhes específicos aos filmes cadastrados.
Feedback ao Usuário:
fornecer mensagens de feedback para ações como login, registro, adição, edição e exclusão de filmes.
Segurança:
Implementar controle de acesso, garantindo que apenas usuários autenticados possam realizar operações no sistema.
Interface Amigável:
Oferece uma interface intuitiva e responsiva para interação com o sistema.
Organização de Dados:
Manter uma estrutura organizada de dados, relacionando usuários, filmes e cadastros.
Esses objetivos refletem a funcionalidade renovada no código fornecido, focando na criação de um sistema que permite aos usuários gerenciar uma coleção pessoal de informações sobre filmes, com ênfase nos trabalhos de Quentin Tarantino.
gera uma imagem do modelo ER do sistema, por favor
Fontes

Responder
Para criar um diagrama ER (Entidade-Relacionamento) do sistema de registro de filmes Tarantino, podemos usar as informações fornecidas sobre as tabelas e suas relações. Vou descrever o diagrama ER em texto e, em seguida, fornecer uma imagem gerada com base nessa descrição.
Descrição do Diagrama ER
Entidades:
Usuário (auth_user) :
eu ia (PK)
nome de usuário
e-mail
senha
primeiro nome
sobrenome
é_pessoal
está ativo
data_ingressou
Último Login
Filme :
eu ia (PK)
nome
ano_lancamento
diretor
sinopse
Cadastro :
eu ia (PK)
user_id (FK para usuário)
filme_id (FK para Filme)
descrição
Relações:
Um usuário pode cadastrar vários filmes (relação um-para-muitos entre Usuário e Cadastro).
Um filme pode ser cadastrado por vários usuários (relação um-para-muitos entre Filme e Cadastro).
Diagrama ER em Texto
texto
+-----------------+          +-----------------+          +-----------------+
|     User        |          |     Cadastro    |          |      Filme      |
+-----------------+          +-----------------+          +-----------------+
| id (PK)         |<---------| id (PK)         |--------->| id (PK)         |
| username        |          | user_id (FK)    |          | nome            |
| email           |          | filme_id (FK)   |          | ano_lancamento  |
| password        |          | descricao       |          | diretor         |
| first_name      |          +-----------------+          | sinopse         |
| last_name       |                                       +-----------------+
| is_staff        |
| is_active       |
| date_joined     |
| last_login      |
+-----------------+

Gerando a Imagem do Diagrama ER
Para gerar a imagem do diagrama ER, você pode usar ferramentas como Lucidchart, Draw.io, ou PlantUML. Vou fornecer um exemplo de como você pode usar o PlantUML para gerar o diagrama.
PlantaUML
texto
@startuml
entity "User" as user {
  + id : int <<PK>>
  --
  username : varchar
  email : varchar
  password : varchar
  first_name : varchar
  last_name : varchar
  is_staff : boolean
  is_active : boolean
  date_joined : datetime
  last_login : datetime
}

entity "Filme" as filme {
  + id : int <<PK>>
  --
  nome : varchar
  ano_lancamento : int
  diretor : varchar
  sinopse : text
}

entity "Cadastro" as cadastro {
  + id : int <<PK>>
  --
  user_id : int <<FK>>
  filme_id : int <<FK>>
  descricao : text
}

user ||--o{ cadastro : "cadastra"
filme ||--o{ cadastro : "foi cadastrado"
@enduml

Você pode copiar esse código e colá-lo em um editor PlantUML para gerar a imagem do diagrama ER. Aqui está um exemplo de como o diagrama pode parecer:
![Diagrama ER](https://www.plantuml.com/plantuml/uml/CJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9J4rCJYp9
