package udpclientfact;

import java.io.BufferedReader;
import java.io.*;
import java.net.*;

public class UDPclientFACT {

    public static void main(String[] args) {

        int serverport = 2000;
        int clientport = 1000;
        try {
            DatagramSocket ds = new DatagramSocket(clientport);
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Enter a number");
            String num = br.readLine();
            byte b[] = new byte[1024];
            b = num.getBytes();

            DatagramPacket dp = new DatagramPacket(b, b.length, InetAddress.getLocalHost(), serverport);
            ds.send(dp);
            byte b1[] = new byte[1024];

            DatagramPacket dp1 = new DatagramPacket(b1, b1.length);
            ds.receive(dp1);

            String str = new String(dp1.getData(), 0, dp1.getLength());
            System.out.println(str);

        } catch (Exception e) {
            e.printStackTrace();

        }
    }
}
