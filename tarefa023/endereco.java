public class Endereco {
    private String tipoEndereco; //comercial, residencial, etc.
    private String tipoLogradouro; //rua, avenida, alameda, marginal, via, viela, travessa, etc.
    private String nomeLogradouro;
    private int numero;
    private String complementoNumero; //exemplo 13-A, o complemento é -A.
    private String complementoEndereco; //quadra, lote, apartamento, etc.

    public Endereco(String tipoEndereco, String tipoLogradouro, String nomeLogradouro, int numero, String complementoNumero, String complementoEndereco){
        this.tipoEndereco = tipoEndereco;
        this.tipoLogradouro = tipoLogradouro;
        this.nomeLogradouro = nomeLogradouro;
        this.numero = numero;
        this.complementoNumero = complementoNumero;
        this.complementoEndereco = complementoEndereco;
    }
}