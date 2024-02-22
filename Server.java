import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class Server extends UnicastRemoteObject implements Interface{

    private ArrayList<String> stringStore;

    public Server() throws RemoteException {
        super();
        this.stringStore = new ArrayList<String>();
    }

    

    @Override
    public void storeString(String s) {
        this.stringStore.add(s);
    }


    @Override
    public ArrayList<String> listString() {
        return this.stringStore;
    }


    @Override
    public String serverIP() {
        return "10.0.84.186";
    }



    @Override
    public String time() {
        DateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        Date date = new Date();
        return dateFormat.format(date);
    }

    public static void main(String[] args) {
        try {
            Server server = new Server();
            System.out.println("Server is running...");
            Naming.rebind("rmi://10.0.84.186:11099/RMIInterface", new Server());
        } catch (Exception e) {
            System.out.println("Trouble: " + e);
        }
    }

}