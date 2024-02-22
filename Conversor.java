import java.rmi.*;

public interface Conversor extends Remote {
    public float realParaEuro(float a) throws RemoteException;
    public float euroParaReal(float a) throws RemoteException;
    public float dolarParaReal(float a) throws RemoteException;
    public float realParaDolar(float a) throws RemoteException;
}