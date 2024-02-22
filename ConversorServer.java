import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class ConversorServer extends UnicastRemoteObject implements Conversor{
    public ConversorServer() throws RemoteException {
        super();
    }

    @Override
    public float realParaEuro(float a) throws RemoteException {
        return(a * (float) 0.19);
    }

    @Override
    public float euroParaReal(float a) throws RemoteException {
        return(a * (float) 5.35);
    }

    @Override
    public float realParaDolar(float a) throws RemoteException {
        return(a * (float) 0.2);
    }

    @Override
    public float dolarParaReal(float a) throws RemoteException {
        return(a * (float) 4.94);
    }

    public static void main(String[] args) {
        try {
            ConversorServer server = new ConversorServer();
            System.out.println("ConversorServer is running...");
            Naming.rebind("rmi://127.0.0.1:11099/RMIInterface", server);
        } catch (Exception e) {
            System.out.println("Erro: " + e);
        }
    }
}