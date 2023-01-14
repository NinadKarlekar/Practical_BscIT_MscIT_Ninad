package tcpserverprime;

import java.net.*;
import java.io.*;

public class Tcpserverprime {

    public static void main(String[] args) throws IOException {
        try {
            ServerSocket ss = new ServerSocket(8001);
            System.out.println("Server started.......");
            Socket s = ss.accept();

            DataInputStream in = new DataInputStream(s.getInputStream());
            int x = in.readInt();
            DataOutputStream otc = new DataOutputStream(s.getOutputStream());
            int y = x / 2;
            if (x == 1) {
                otc.writeUTF(x + " is not prime");
                System.exit(0);
            }
            boolean flag = true;
            for (int i = 2; i <= y; i++) {
                if (x % i == 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                otc.writeUTF(x + " is prime");
            } else {
                otc.writeUTF(x + " is not prime");
            }

        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }
}
