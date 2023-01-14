package chatclient;

import java.net.*;
import java.io.*;

public class ChatClient {

    public static void main(String[] args) {
        try {
            Socket s = new Socket("LocalHost", 8000);
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            DataOutputStream out = new DataOutputStream(s.getOutputStream());
            DataInputStream in = new DataInputStream(s.getInputStream());
            String msg;
            System.out.println("To stop chatting with server type STOP");
            System.out.println("Client says:");
            while ((msg = br.readLine()) != null) {
                out.writeBytes(msg + "\n");
                if (msg.equals("STOP")) {
                    break;
                }
                System.out.println("Server says:" + in.readLine());
                System.out.println("Client says: ");
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
