# Rest - API
## o que é uma API
Uma API, do inglês: _Aplication programing interface_, é um conjunto de protocolos e regrinhas para acesso a um programa ou serviço web, seus dados e integrar-se com esse programa. Quando fazemos duas aplicações trabalharem entre sí usamos uma API. de modo que, por exemplo, os dados captados por um programa ou pagina web possam aparecer e ser acessados por um aplicativo mobile completamente diferente, ou função, ou banco de dados. Eles se comunicam, compartilham dados através de códigos. É fácil imaginar esse processo como um serviço entre um cliente 
## o que é Rest?
Do inglês: _Representational State Transfer_, o REST foi criado pelo cientista da computação Roy Fielding, é um protocolo de arquitetura de informação em aplicações web de qualquer tipo, sendo regras e restrições de boas praticas de hierarquia de código, deixando assim ele mais leve e fácil de se integrar, deste modo qualquer API escrita sobre esse protocolo consegue facilmente se integrar a _web-services_ independente da linguagem usada ou seu objetivo. Quanto mais facil se integrar, mais versátil é a API, podendo ser mais rentável, rápida e eficiente.
## API Rest
O protocolo Rest usa princípios básicos e rápidos, como o princípio de "comunicação stateless". Que permite comunicação e transferencia de dados entre navegadores e outras API usando comandos como Get, put, etc. usando caminhos através de http ou até mesmo de https. Assim podemos por exemplo, captar através de formulários um novo cliente e integra-lo à um banco de dados automaticamente, realizar checagem de estoque e pagamentos em e-commerce's. emissão de notas fiscais. Tudo a um clique, a comunicação das Rest API's leva dados a outros serviços como correios, gerencia estoque de Empresas, acessa sistemas internos e outros dados. E até mesmo envia seu endereço de e-mail para o marketing que prontamente te bombardeará com mensagens que caem em sua caixa de _spam_.
Para uma API ser considerada API_REST ela precisa:
* Ter arquitetura Client/Server, com clientes servidores e recursos. tendo solicitações gerenciadas através de HTTP
* Ter a comunicação _Stateless_, onde nenhum dado de cliente é armazenado entre informações get.
* Armazenar dados em cache.
* Ter um interface uniforme, padronizada.
* Ter um sistema de camada de servidor com hierarquia de dados protegidos do client.
Embora todas essas conformidades devam ser cumpridas as API-Rest são as mais rápidas e fáceis de se integrar. As informações podem ser retornadas do banco de dados por arquivos .JSON, .XML ou até .txt sendo fáceis para o computador e pessoas lerem.
## Exemplos
Voce pode encontrar varias API Rest no seu dia-a-dia, como por exemplo API do google e facebook que permite que voce se autentique em serviços externos automaticamente usando "login com facebook" ou "login com google". é criada uma requisição da API como um GET, que usará HTTP para se comunicar ao banco de dados do facebook ou do google, que retornarão através dessa mesma HTTP dados requisitados em formato .JSON
### requisições:
Considerando que temos pessoa como um recurso, com atributos idade, nome, id. e temos sob dominio a API minhaAPI. usando o método `get` em `https://minhaAPI/pessoa` podemos ter o retorno de todas as pessoas cadastradas:
```
{
   "status":200,
   "data":[
      {
         "id":1,
         "nome":"John Doe",
         "idade":20
      },
      {
         "id":2,
         "nome":"Mary Ann",
         "idade":25
      },
      etc...
   ]
}
```
Deste modo podemos também usar um `get{id}` para retorno atraves da API de uma pessoa com o {id} requisitado, como por exemplo usando `https://minhaAPI/pessoas/1` 
```
{
   "status":200,
   "data":[
      {
         "id":1,
         "nome":"John Doe",
         "idade":20
      }
   ]
}
```
Do mesmo modo `POST` irá adicionar uma pessoa.
```
{
   "Name": "Peter Jones",
   "age":20
}
```
retorno será:
```
{
  "status":200,
  "sucess":True
}
``` 
e por ai vai. use os comando PUT e DELETE a exemplo deles.
## criando APIs
Para criar API's precisamos ter conhecimento do protocolo HTTP, e linguagens de programação web, como o Python. Ainda assim podemos ainda precisar de JavaScript lidando com sites e outros recursos web. Sempre esbarramos em JavaScript. Precisamos antes mesmo de implementar a aplicação, é preciso saber quais dados voce quer captar e gerenciar. Podemos criar APIs usando frameworks como NextJS.
