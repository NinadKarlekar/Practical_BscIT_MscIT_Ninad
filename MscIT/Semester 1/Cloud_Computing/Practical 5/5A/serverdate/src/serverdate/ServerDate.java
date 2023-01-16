package serverdate;
import java.rmi.*;
import java.rmi.server.*;
import java.rmi.registry.*;
import java.util.*;
public class ServerDate extends UnicastRemoteObject implements InterDate{
   public ServerDate() throws RemoteException{
            
    }
    public static void main(String[] args) {
         try{
            Registry reg = LocateRegistry.createRegistry(1234);
            ServerDate s1 = new ServerDate();
            reg.rebind("PP", s1);
            System.out.println("Object registered....");
        }
        catch(RemoteException e){
            System.out.println("Exception:"+e);
        }
    }
    
    public String display() throws RemoteException
    {
        String str = "";
        Date d=new Date();
        str=d.toString();
        return str;
    }
}