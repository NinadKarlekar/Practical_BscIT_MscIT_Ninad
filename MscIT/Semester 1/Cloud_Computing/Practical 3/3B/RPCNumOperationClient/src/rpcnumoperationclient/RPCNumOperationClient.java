package rpcnumoperationclient;

import java.util.*;
import java.net.*;
import java.io.*;

public class RPCNumOperationClient {

    RPCNumOperationClient() {
        try {
            InetAddress ia = InetAddress.getLocalHost();
            DatagramSocket ds = new DatagramSocket();
            DatagramSocket ds1 = new DatagramSocket(1300);
            System.out.println("\nClient\n");
            System.out.println("1. Square = square\n2. Square root = squareroot\n3. Cube = cube\n4. Cube root = cuberoot");
            System.out.println("Enter method & number\n");
            while (true) {
                BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                String str = br.readLine();
                byte b[] = str.getBytes();
                DatagramPacket dp = new DatagramPacket(b, b.length, ia, 1200);
                ds.send(dp);
                dp = new DatagramPacket(b, b.length);
                ds1.receive(dp);
                String s = new String(dp.getData(), 0, dp.getLength());
                System.out.println("\nResult = " + s + "\n");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        new RPCNumOperationClient();
    }

}
