
package tcpfileclient;
import java.net.*;
import java.io.*;

public class Tcpfileclient {
     public static void main(String[] args) {
        try {
            Socket cs = new Socket("LocalHost",8001);
            BufferedReader infu = new BufferedReader(new InputStreamReader(System.in));
            DataInputStream in = new DataInputStream(cs.getInputStream());
            DataOutputStream out = new DataOutputStream(cs.getOutputStream());
            
            String fname;            
            System.out.println("Enter file name");
            fname = infu.readLine();
            out.writeUTF(fname);
            FileWriter fw = new FileWriter("F:\\MSC IT\\Practical\\Cloud Computing\\FileClient\\src\\fileclient\\hello.txt");
            String temp;
            System.out.println("\n\nFile Content");
            while(!(temp = in.readUTF()).equals("EOF"))
            {
                System.out.println(temp);
                fw.write(temp+"\n");
            }
            fw.close();            
            System.out.println("File transfer Completed");
            infu.close();
            out.close();
            cs.close();            
        } 
        catch (Exception e) {
            System.out.println(e);
        }
    }    
}
