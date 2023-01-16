package serverdate;

import java.rmi.*;
import java.rmi.registry.*;

public class ClientDate {

    public static void main(String[] args) {
        try {
            Registry reg = LocateRegistry.getRegistry("localhost", 1234);
            String s1;
            InterDate h1 = (InterDate) reg.lookup("PP");
            s1 = h1.display();
            System.out.println(s1);
        } catch (NotBoundException | RemoteException e) {
            System.out.println("Exception" + e);
        }
    }
}
