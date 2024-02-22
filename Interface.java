import java.rmi.*;
import java.util.ArrayList;

public interface Interface extends Remote {
    public void storeString(String s) throws RemoteException;
    public ArrayList<String> listString() throws RemoteException;
    public String serverIP() throws RemoteException; 
    public String time() throws RemoteException;
}