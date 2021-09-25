import contato.Contato;

public class ContatoNaoEncontrado {
    public contato; 
    contato = new Contato('mateus','899898','40028922');
    public ContatoNaoEncontrado(){}

    public void exibe() throws erro{
        if(!contato){
            erro("sem contatos");
        }
        System.out.println(contato.nome);
        System.out.println(contato.telefone);
        System.out.println(contato.email);
    }
    public static void main(String[] args) {
        try{
            ContatoNaoEncontrado();
        } catch(erro sem){
            sem.getMessage();
        }
    }
}