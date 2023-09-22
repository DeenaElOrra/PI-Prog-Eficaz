[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12003102&assignment_repo_type=AssignmentRepo)
**Proj. Ágil - Frente Dev**

Insper 2023 - Segundo Semestre

### Nome Completo: 

## Instruções Gerais

A prova prática será entregue via Classroom. Não esqueça de fazer commits e push regularmente.

É permitido consultar os materiais da aula, suas APSs e o Google, desde que não utilize nenhuma extensão ou integração com qualquer tipo de IA.

É proibida a comunicação entre alunos. Qualquer tentativa de comunicação, seja pessoal ou virtual, será considerada fraude.

É proibido o uso de qualquer site, extensão ou programas que integrem IA ou que auxiliem no desenvolvimento de qualquer aspecto da prova.

Desabilite o Copilot. Caso seja identificado pelo Proctorio que o Copilot esteve ativo em qualquer momento da prova, será considerado fraude.

**O professor não ajudará com configurações de ambiente, Python, problemas de importação, entre outros. Ele poderá apenas esclarecer dúvidas sobre a interpretação do enunciado. A responsabilidade de ter um ambiente funcional para a prova é do aluno.**

Na pasta raiz da prova, há um arquivo requirements.txt. Crie um ambiente virtual para essa prova e instale os pacotes contidos nele. Para evitar o envio do ambiente virtual em um commit, crie-o na raiz com o nome "venv". Assim, ele será ignorado pelo Git, conforme configurado no .gitignore.

Sua prova utilizará o sistema de proctoring. Para realizá-la, é necessário:

Uso do navegador Google Chrome (apenas ele é compatível).
Ter a extensão da plataforma instalada (sem ela, o sistema não funcionará). Para instalar a extensão, acesse https://getproctorio.com/ pelo Google Chrome e siga os passos indicados.


## Exercício 1: Testes com Pytest (até 2.5 pontos)
Resolva e implemente este exercício dentro da pasta **"exercicio_1_pytest"** 

Você é um Quality Assurance (QA) na empresa "Tech Solutions". Recentemente, um dos desenvolvedores, conhecido por ser um pouco descuidado, entregou a implementação de algumas funções no arquivo funcoes_desenvolvidas_pelo_dev. Sua tarefa é criar testes para garantir que as funções desenvolvidas por ele estejam em conformidade com os requisitos especificados.

**Importante**: Seu trabalho como QA é garantir que o software funcione conforme os requisitos, e não conforme a implementação do desenvolvedor. Você deve basear seus testes estritamente nos requisitos fornecidos. Além disso, **lembre-se de que, como QA, você não deve, em hipótese alguma, alterar o arquivo desenvolvido pelo desenvolvedor. Qualquer modificação no arquivo funcoes_desenvolvidas_pelo_dev resultará em uma penalidade de 1 ponto.**

Crie um arquivo chamado **test_funcoes.py** e implemente os testes para os 9 requisitos apresentados a seguir. Se seus testes estiverem corretamente implementados, a implementação do "desenvolvedor descuidado" falhará em 2 desses requisitos.

### Implementações entregues pelo desenvolvedor e seus requisitos:

### **A**: Validação de Disponibilidade de Produto (até 1 ponto)
**Função:** `verifica_disponibilidade(produto_nome: str)`

Dada uma função que verifica a disponibilidade de um produto em um banco de dados SQLite, você deve implementar os testes para essa função considerando os seguintes requisitos:

1. Se o produto estiver disponível (ou seja, existir na base) e tiver estoque, a função deve retornar True. (0.25)
2. Se o produto não existir na base, a função deve retornar False. (0.25)
3. Se o produto existir na base, mas estiver sem estoque, a função deve retornar a string "sem estoque". (0.25)
4. Se o produto existir, tiver estoque, mas o preço for menor ou igual a zero (indicando um erro humano no cadastro), a função deve retornar False. (0.25)

**Utilize a marcação do pytest "estoque" para os testes relacionados a essa função.**

Para facilitar, aqui estão os dados cadastrados na base. Use-os em seu teste.

**Produtos cadastrados na base de dados**:

| Nome       | Preço | Quantidade em Estoque |
|------------|-------|-----------------------|
| Produto A  | 20.5  | 10                    |
| Produto B  | 0     | 5                     |
| Produto C  | 15.0  | 0                     |

### **B**: Consulta de CEP (até 1.5 ponto)
Função: `consulta_cep(cep: str)`

Dada a função consulta_cep que recebe um CEP no formato de uma string e retorna uma string com a sigla do estado, você deve implementar os testes para essa função considerando os seguintes requisitos:

A função recebe como parâmetro de entrada um CEP no formato de uma string (somente dígitos, ex.: "09320330").
1. Se o CEP for válido, a função deve retornar o estado ao qual aquele CEP pertence (por exemplo, "SP", "MT", etc.). (0.2)
2. Se o CEP não for uma string, a função deve retornar False. (0.2)
3. Se o CEP tiver mais de 8 dígitos, a função deve retornar False. (0.3)
4. Se o CEP tiver menos de 8 dígitos, a função deve levantar uma exceção genérica. (0.5)
5. Se o CEP for válido, mas não existir na API consultada, a função deve retornar False. (0.3)

Utilize a marcação do pytest "cep" para os testes relacionados a essa função.

**Penalidades - caso não implementado**

- Crie os marcadores. (-0.2)
- Crie corretamente o arquivo de configuração do pytest para que os marcadores sejam reconhecidos e não gerem *warnings* ao testar. (-0.2)



## Exercício 2: Web Service POX para Cardápio de Restaurante (até 1.0)


O "desenvolvedor descuidado" da empresa "Tech Solutions" criou um web service POX para um cardápio de restaurante, e mais uma vez, ele deixou algumas coisas inacabadas. Ele não seguiu as convenções REST, optando por um design POX (Plain Old XML) com verbos nas rotas.

O web service não está funcionando devido à ausência da base de dados!

**Sua tarefa:**

1. Analise o código fornecido no arquivo `app.py` para identificar onde (em que pasta) e como a base de dados deve ser criada.
2. Crie a base de dados `cardapio.db` no local correto para que o web service funcione corretamente.
3. Implemente e execute o arquivo/script `criar_cardapio.py` para criar a tabela necessária na base de dados.
4. Teste o web service usando a coleção POSTMAN fornecida, assim você pode verificar se a base que você criou esta no local correto e funcionando corretamente.

**Especificações do Web Service:**

O web service, fornecido no arquivo `app.py`, oferece funcionalidades para:

- Inserir um novo prato
- Atualizar um prato existente
- Deletar um prato
- Buscar informações de um prato específico
- Buscar informações de vários pratos

Cada prato contém as seguintes informações:

- Título
- Descrição
- Categoria (por exemplo, "entrada", "prato principal", "sobremesa")
- Preço

**Atenção:**

- Este web service não é RESTful. Certifique-se de não usar sua estrutura como referência em futuros projetos que exijam REST.
- Uma coleção POSTMAN foi fornecida para você testar o web service. O web service só funcionará corretamente quando a base de dados estiver configurada no local correto, com a tabela e o nome corretos.
- **Não altere de forma alguma o arquivo `app.py` fornecido pelo desenvolvedor descuidado.**
- Sua entrega deve conter o arquivo **`criar_cardapio.py`** que você usou para criar a base de dados, e deve estar localizado na pasta raiz do exercício 2.





# Web Service REST - Aluguel de Bicicletas Compartilhadas (até 4.5 pontos)

Com o avanço da economia compartilhada, cada vez mais empresas estão buscando soluções sustentáveis e econômicas que atendam às demandas da sociedade moderna. Uma dessas soluções é o aluguel de bicicletas compartilhadas, que tem ganhado popularidade em muitas cidades ao redor do mundo, oferecendo uma alternativa ecológica e saudável aos meios de transporte tradicionais.

Uma startup inovadora no ramo de aluguel de bicicletas contratou você para desenvolver um sistema de gerenciamento para sua operação. Eles precisam de um web service REST de nível 2 de Richardson que permita gerenciar usuários, bicicletas e empréstimos.

Você deverá criar todo o web service dentro da pasta **`exercicio_3_REST`**.

## Requisitos

### Usuários
- Cada usuário deve ter um nome (str), CPF (str) e data de nascimento (formato string mesmo, não precisa usar date).
- O CPF é único para cada usuário.
- O CPF não pode ser uima string vazia também.
- Todas as informações são obrigatórias. Se qualquer informação estiver faltando ao criar ou atualizar um usuário, o sistema deve retornar um status HTTP condizente.

Para facilitar: considere que para atualizar as infos e um usuário todos os campos serão enviados novamente, não somente o que será atualizado, mas você precisa verificar se todos os campos estão presentes.

### Bicicletas
- Cada bicicleta deve ter uma marca, modelo e a cidade onde está alocada.
- Todas as informações são obrigatórias. Se qualquer informação estiver faltando ao criar ou atualizar uma bicicleta, o sistema deve retornar um status HTTP condizente.

Para facilitar: considere que para atualizar as infos e uma bicicleta todos os campos serão enviados novamente, não somente o que será atualizado, mas você precisa verificar se todos os campos estão presentes.

### Empréstimos
- Cada empréstimo relaciona uma bicicleta a um usuário.
- Esta tabela deve ter o id do usuário que está alugando e o id da bicicleta que esta sendo alugada.
- Crie uma rota que receba o id da bicicleta e o id do usuario e registre o aluguel. Mas lembre-se que uma bicicleta que já esta alugada, não pode ser alugada novamente. Restrição apenas para bicicleta e não para o usuário.

Para facilitar: implemente ler todos emprestimos, inserir e deletar um emprestimo.

## Rotas

- Para usuários. (até 1.5)
    - Ler todos usuários (/usuarios)
    - Ler apenas um úsuario dado um id (/usuarios/\<id_usuario\>)
    - Inserir um usuário (/usuarios)
    - Atualizar um usuário dado um id (/usuarios/\<id_usuario\>)
    - Deletar um usuário dado um id (/usuarios/\<id_usuario\>)
- Para bicicletas. (até 1.5)
    - Ler todas bicicletas (/bikes)
    - Ler apenas uma bicicleta dado um id (/bikes/\<id_bike\>)
    - Inserir uma bicicleta (/bikes)
    - Atualizar uma bicicleta dado um id (/bikes/\<id_bike\>)
    - Deletar uma bicicleta dado um id (/bikes/\<id_bike\>)
- Para empréstimos. (até 1.0)
    - Ler todos emprestimos (mostrando apenas os ids - do usuário, da bicicleta e do emprestimo) (/emprestimos)
    - Inserir um emprestimo dado um id de usuario e id da bicicleta (/emprestimos/usuarios/\<id_usuario\>/bikes/\<id_bike\>)
    - Deletar um emprestimo dado um id de empréstimo (/emprestimos/\<id_emprestimo\>)
    
## Nível 2 de maturidade
- Garanta que seja utilizado os métodos HTTP corretos para cada operação
- Utilize corretamente os status code HTTP para um web service REST. Para facilitar a lista é: (200, 201, 400, 404 e 500)
- Utilize recuso nas rotas. Para facilitar, tem uma collection do Postman para vocês utilizarem.

## Instruções

1. A base já foi fornecida e o arquivo `app.py` também, programe nele.
2. Implemente as rotas conforme especificado.
3. Garanta que todos os erros sejam tratados corretamente e que os status codes HTTP sejam retornados conforme a especificação REST.
4. Para te auxiliar nos testes, fornecemos uma coleção do Postman. Use-a para garantir que seu web service esteja funcionando corretamente.

Este é um web service REST de nível 2 de Richardson. Siga as boas práticas e convenções REST para nomeação de rotas, uso de verbos HTTP e tratamento de erros. Obviamente que cada aspecto da implementação fora do REST, será penalizado.

## Sobre a correção

Lembre-se de que só serão avaliadas as rotas que estiverem em conformidade com as requisições da collection fornecida no exercício. Portanto, use-a para garantir o correto funcionamento das rotas. Evite alterar o nome das rotas ou o corpo das requisições. Altere apenas o conteúdo a ser inserido para que você realize seus testes.

Ao invés de abordar diversas tarefas simultaneamente, foque em finalizar completamente cada rota. Isso ajudará você a maximizar sua nota, caso não haja tempo para concluir todo o exercício.



Boa Prova!
# PI-Prog-Eficaz
