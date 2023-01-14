package tcpfileserver;
import java.net.*;
import java.io.*;

public class Tcpfileserver {

    public static void main(String[] args) throws IOException {
      try{
            ServerSocket ss = new ServerSocket(8001);
            System.out.println("Server Started");
            Socket s = ss.accept();
            System.out.println("Conection");            
            DataInputStream in = new DataInputStream(s.getInputStream());         
            DataOutputStream out = new DataOutputStream(s.getOutputStream());
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String fname = in.readUTF();            
            if(fname.equals("hello"))
            {
                System.out.println("File exists");
                BufferedReader d = new BufferedReader(new FileReader("F:\\MSC IT\\Practical\\Cloud Computing\\FileServer\\src\\fileserver\\hello.txt"));                
                String line;
                while((line = d.readLine())!=null){
                    out.writeUTF(line);
                    //System.out.println(line);
                }                
            }            
            else
            {
                System.out.println("File does not exists");
            } 
            br.close();
            in.close();
            out.close();
            ss.close();            
        }        
        catch(Exception e){
            System.out.println(e);
        }        
    }    
}
