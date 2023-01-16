package serverdate;

import java.rmi.*;

public interface InterDate extends Remote {

    public String display() throws RemoteException;

}
