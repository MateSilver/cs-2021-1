<p style="text-align: center;"><font size="5"><b>Git <i>branching</i> (Exercícios:)</b></font></p1></p>
<DIV align="justify">

1. Qual o nome do branch padrão do Git?
  ```
  main
  ```
2. O que o comando **<code>git branch nome</code>** realiza?
  ```
  cria um novo branch com nome nome
  ```
3. Como criar um branch a partir de um commit específico?
  ```
  git checkout <ponto>
  ```
4. Em um repositório, qual o efeito do comando **<code>git checkout -b bugfix/234</code>**?
  ```
  recria uma nova branch a partir de bugfix/234/code
  ```
5. Qual o comando para se alternar para um branch de nome **experimento2**?
  ```
  git checkout experimento2
  ```
6. Em um repositório com dois branches, **b1** e **b2**, onde b1 é o corrente, qual o efeito do comando **<code>git branch</code>**?
  ```
  faz uma lista das branchs existentes
  ```
7. O que o comando **<code>git checkout -b</code>** nome faz?
  ```
  cria uma nova branch
  ```
8. Qual a função do <code>**comando git branch -d teste</code>**?
  ```
  exclui a branch atual
  ```
9. Durante o desenvolvimento de um software é comum, por exemplo, utilizar um novo recurso por meio de experimentação. Talvez uma nova tecnologia, uma nova biblioteca que pode ser útil ao que está em desenvolvimento, ou até mesmo uma nova versão de um produto já empregado. Para que o uso deste novo recurso não interfira com o que é considerado pronto, um branch pode ser criado para a experimentação. Código que for criado para a experimentação existirá apenas no branch criado. Se eventualmente o experimento demonstrar um resultado satisfatório, as alterações realizadas no branch poderão ser incorporadas no que é considerado pronto, ou seja, no branch principal (master). Esta última ação é conhecida por merge. Neste item, crie uma sequência de comandos que simula um caso simples de criação e uso seguido de merge empregando um branch para ilustrar uma experimentação conforme acima. A sequência deve incluir, obrigatoriamente: (a) criação de um ou mais branches; (b) chaveamento para pelo menos dois branches e (c) merge.
  ```
  git chekcout -b b1
  git chekcout -b b2
  git add --all
  git commit -m "primeiro commit"
  git add --all
  git commit -m "segundo commit"
  git checkout b1
  git merge b2
  git branch -d b2
```
</DIV/>
