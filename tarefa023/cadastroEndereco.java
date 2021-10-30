public class CadastroEndereco {
    private String tipoEndereco; //comercial, residencial, etc.
    private String tipoLogradouro; //rua, avenida, alameda, marginal, via, viela, travessa, etc.
    private String nomeLogradouro;
    private int numero;
    private String complementoNumero; //exemplo 13-A, o complemento é -A.
    private String complementoEndereco; //quadra, lote, apartamento, etc.
    private String bairro;
    private Integer CEP;
    private String cidade;
    private String estado;
    private String pais;

    public CadastroEndereco(String logradouro,int numero, String complementoNumero, String complementoEndereco, String bairro, Integer CEP, String cidade, String estado, String pais){
        this.nomeLogradouro = Logradouro(logradouro);
        this.numero = Numero(numero);
        this.complementoNumero = complementoNumero;
        this.complementoEndereco = complementoEndereco;
        this.bairro = Bairro(bairro);
        this.CEP = CEP;
        this.cidade = Cidade(cidade);
        this.estado = Estado(estado);
        this.pais = Pais(pais);
    }
    public getLogradouro(){
        return this.nomeLogradouro;
    }
    public getnumero(){
        return this.numero;
    }
    public getcomplementoNumero(){
        return this.complementoNumero;
    }
    public getcomplementoEndereco(){
        return this.complementoEndereco;
    }
    public getBairro(){
        return this.bairro;
    }
    public getCEP(){
        return this.CEP;
    }
    public getCidade(){
        return this.cidade;
    }
    public getEstado(){
        return this.estado;
    }
    public getPais(){
        return this.pais;
    }
}