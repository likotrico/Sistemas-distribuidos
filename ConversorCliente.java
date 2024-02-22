import java.rmi.Naming;

public class ConversorCliente {
    private static Conversor calc = null;

    public static void main(String[] args) {
        try {
            calc = (Conversor) Naming.lookup("rmi://10.0.84.187:11099/RMIInterface");
            System.out.println(String.valueOf(calc.realParaDolar(1)));
            System.out.println(String.valueOf(calc.dolarParaReal(1)));
            System.out.println(String.valueOf(calc.realParaEuro(1)));
            System.out.println(String.valueOf(calc.euroParaReal(1)));
        }
        catch (Exception e) {
            System.out.println("Trouble: " + e);
        }
    }
}