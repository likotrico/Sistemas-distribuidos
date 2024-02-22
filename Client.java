import java.rmi.Naming;
import java.util.ArrayList;

public class Client {
    private static Interface a = null;

    public static void main(String[] args) {
        try {
            a = (Interface) Naming.lookup("rmi://10.0.84.186:11099/RMIInterface");
            System.out.println(String.valueOf(a.time()));
            System.out.println(a.serverIP());
            String s = "Likotrico";
            a.storeString(s);
            ArrayList<String> array = null;
            array = a.listString();
            for (String aString : array) {
                System.out.println(aString);
            }

        }
        catch (Exception e) {
            System.out.println("Trouble: " + e);
        }
    }
}