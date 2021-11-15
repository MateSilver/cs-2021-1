package testeagenda;
import agenda.Agenda;

public class AgendaTeste implements Agenda {
    NovaAgenda = new Agenda();

    NovaAgenda.addContact("Joao","40028922","Joaopao@hotmail.com");
    NovaAgenda.addContact("Ze","32228950","ZZZ@gmail.com");
    NovaAgenda.addContact("Liz","32245565","LadyLizzz@gmail.com");

    try {
        NovaAgenda.consultContact();
    }
    catch(FileNotFoundException nexc){
        System.out.println("Sem contatos!");
    } 
    catch(NullPointerException nexc){
        System.out.println("Sem contatos!");
    } finally {
        NovaAgenda.remove(0);
    }

}