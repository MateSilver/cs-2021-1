## Mateus da Silveira Batista – 201905543

### Injeção de Dependencias
  <p>Em configuração de software em tempo de execução temos a injeção de dependencias sendo um método de passar dependencias a um objeto ao inves de criar o objeto dentro de uma classe de por exemplo. Isso facilita testes e melhora o desempenho se você apenas quer realizar testes simples que não acessem as dependencias. O problema continua, podemos ter um objeto com acessos pesados à rede, porém agora temos o objeto passando como parametro para um construtor da classe, isso muda o problema de lugar e você pode simplesmente durante os testes passar como parametro um objeto simulação, mais leve ou menos complexo, de modo externo. Isso é somente um dos casos de injeção de dependencias.</p>

```	Public class someclass(){
		myObject = Factory.getObject();
	}
```
para:
```
     Public class someclass(class myObject){
          this.myObject	= myObject;
     }
```
  <p>A injeção de dependencias é um dos modos práticos de se usar o principio da inversão de controle, onde o chamados de dependencias é feito ao contrário, não criamos elas mas recebemos elas prontas para serem usadas, desse modo “terceirizamos”  o processo. Isso pode ser exemplificado com o wordpress e seus plugins ou mesmo os sistemas APIs de login do google e facebook que facilitam o cadastro de usuarios em novas contas, etc.</p>
	<p>Qualquer componente adicionado seria injetado na classe, de modo a ser enviado para ela, facilitando até mesmo a compreesão. Mas o motivo de uma classe com injeção de dependencias ser facil de fazer testes unitários é que a menor fração deles, o teste primario seria bem mais facil de fazer, como uma string vazia ou objeto vazio.</p>
