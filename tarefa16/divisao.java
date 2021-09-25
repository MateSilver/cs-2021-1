import java.util.Scanner;

public class Divisao {

    private static Scanner sc = new Scanner(System.in);

    public static int divide(int dividendo, int divisor) throws erro{
        if(divisor == 0){
            throw new erro("divisor 0");
        }
        return dividendo/divisor;
    }

    public static void main (String args[]) {

        System.out.println("Informe o valor do dividendo: ");
        int dividendo = sc.nextInt();
        System.out.println("Informe o valor do divisor: ");
        int divisor = sc.nextInt();
        try{
            System.out.println(divide(dividendo, divisor));
        }
        catch(erro){
            System.out.println(erro.getMessage());
            System.out.println(erro.printStackTrace());
        }
    }

}