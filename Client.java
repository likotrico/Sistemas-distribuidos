import java.rmi.Naming;

public class Client {
    private static Interface a = null;

    public static void main(String[] args) {
        try {
            a = (Interface) Naming.lookup("rmi://10.0.84.186:11099/RMIInterface");
            System.out.println(String.valueOf(a.time()));
        }
        catch (Exception e) {
            System.out.println("Trouble: " + e);
        }
    }
}