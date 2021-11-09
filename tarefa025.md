## Mateus da Silveira Batista – 201905543

### Padrão de projeto State
  <p>Ao termos um projeto onde o comportamento de algum objeto vária de acordo com o que podemos chamar de estados temos então uma oportunidade de, se forem poucos os estados, usar um padrão chamado State.</p>
	<p>Em projetos baseados em estados muitas vezes temos que fazer uma série de if-else’s para cada estado de um objeto, pra usar seus métodos corretamente, como por exemplo: Se uma conta-corrente está negativada, livre ou bloqueada. Assim teríamos várias linhas de código para verificar em cada método o estado dessa conta. Porém isso muda com o padrão State onde temos um objeto abstrato base onde tudo o que não se altera fica e usamos isso como base para criar interfaces para cada um dos estados.</p>
	<p>Tudo o que variar deve ser encapsulado, assim como métodos serem modificados para cada classe filha. Métodos novos não devem ser adicionados, e a classe deve ter apenas uma razão para mudar, no exemplo, uma conta que chega a saldo negativo muda para conta negativada, e somente por consequência disso.</p>
	<p>Os métodos devem se repetir até nas classes onde não fazem papel natural, apenas sendo levados a erros. Como por exemplo um saque na classe conta-corrente bloqueada, onde ele receberá um aviso que a conta não pode realizar transferências. Esse padrão melhora o desenvolvimento, deixando-o mais legível e menos repetitivo. As responsabilidades de cada estado estão distribuídas nas classes, cada uma com um encapsulamento e definidas apenas um estado para uma instância.</p>
  Passamos disso:

public class MaquinaRefrigerantes {
...

public void inseriuMoeda(){

if( estado == ESTADO_SEM_MOEDA ){

System.out.println( "OK: Moeda inserida com sucesso." );
estado = ESTADO_COM_MOEDA;
}
else if( estado == ESTADO_COM_MOEDA ){

System.out.println( "FALHOU: Você já inseriu uma moeda." );
}
else if( estado == ESTADO_VENDA ){

System.out.println( "FALHOU: Aguarde, já estamos liberando seu refrigerante." );
}
else if( estado == ESTADO_SEM_REFRIGERANTE ){

System.out.println( "FALHOU: Não há mais refrigerantes." );
}
...
} 

<p>para isso:</p>

abstract public class Estado {

protected MaquinaRefrigerantes maquinaRefrigerantes;

protected Estado( MaquinaRefrigerantes maquinaRefrigerantes ){

this.maquinaRefrigerantes = maquinaRefrigerantes;
}


public void inseriuMoeda(){

System.out.println( "FALHOU: Máquina em manutenção." );
}

public void solicitouMoeda(){

System.out.println( "FALHOU: Máquina em manutenção." );
}

public void despejarRefrigerante(){

System.out.println( "FALHOU: Máquina em manutenção." );
}

protected void despejar(){}

public void inserirRefrigerantes( int quantidadeRefrigerantes ){

int totalRefrigerantes = maquinaRefrigerantes.getQuantidadeRefrigerantes();
totalRefrigerantes += quantidadeRefrigerantes;
maquinaRefrigerantes.setQuantidadeRefrigerantes( totalRefrigerantes );
}

public void acionarManutencao(){

System.out.println( "FALHOU: Ainda em processamento, aguarde os estados ociosos para entrar em mnutenção." );
}

public void desacionarManutencao(){

System.out.println( "FALHOU: Máquina não está em mnutenção." );
}
} 

E podemos adicionar mais estados alterando e fatorando esse código.
