package chatserver;

import java.net.*;
import java.io.*;

public class ChatServer {

    public static void main(String[] args) {
        try {
            ServerSocket ss = new ServerSocket(8000);
            System.out.println("Waiting for client to connect...");
            Socket s = ss.accept();
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            DataOutputStream out = new DataOutputStream(s.getOutputStream());
            DataInputStream in = new DataInputStream(s.getInputStream());
            String receive, send;
            while ((receive = in.readLine()) != null) {
                if (receive.equals("STOP")) {
                    break;
                }
                System.out.println("Client Says : " + receive);
                System.out.println("Server Says : ");
                send = br.readLine();
                out.writeBytes(send + "\n");
            }
            br.close();
            in.close();
            out.close();
            s.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
