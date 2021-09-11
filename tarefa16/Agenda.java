package agenda;
import java.util.List;
import calendario.Calendario;

public class Agenda {
    public ArrayList<Contato> contatos = new ArrayList<>();

    public Agenda(){}

    public void addContact(nome,telefone,email){
        private novo = new Contato(nome,telefone,email);
        contatos.add(novo);
    }

    public void consultContact (){
        try{
            contatos.forEach(contatos -> {
                System.out.println(contatos.nome);
                System.out.println(contatos.telefone);
                System.out.println(contatos.email);
                System.out.println();
            });
        }
        catch(FileNotFoundException erro){
            System.out.println("Sem contatos");
            erro.printStackTrace();
        }
    }
}