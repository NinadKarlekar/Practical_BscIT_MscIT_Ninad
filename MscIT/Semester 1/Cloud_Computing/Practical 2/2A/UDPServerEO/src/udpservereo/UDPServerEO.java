
package udpservereo;
import java.io.*;
import java.net.*; 

public class UDPServerEO {
 public static void main(String[] args) {
        int serverport = 2000;
        int clientport = 1000; 
        try {
            DatagramSocket ds = new DatagramSocket(serverport);
            byte b[] = new byte[1024];
            DatagramPacket dp = new DatagramPacket(b, b.length);
            ds.receive(dp);
            String str = new String(dp.getData(), 0, dp.getLength());
            System.out.println(str);
            int a = Integer.parseInt(str);
            String s = new String(); 
            if (a % 2 == 0) {
                s = "Number is even";
            } else {
                s = "number is odd";
            }
            byte b1[] = new byte[1024];
            b1 = s.getBytes();
            DatagramPacket dp1 = new DatagramPacket(b1, b1.length, InetAddress.getLocalHost(), clientport);
            ds.send(dp1);
        } catch (Exception e) {
            e.printStackTrace(); 
        } 
    }
}
