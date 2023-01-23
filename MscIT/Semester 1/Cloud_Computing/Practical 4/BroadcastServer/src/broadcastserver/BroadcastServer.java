package broadcastserver;

import java.net.*;
import java.io.*;
import java.util.*;

public class BroadcastServer {

    public static final int PORT = 1234;

    public static void main(String args[]) throws Exception {
        MulticastSocket socket;
        DatagramPacket packet;
        InetAddress address;
        // set the multicast address to your local subnet
        address = InetAddress.getByName("239.1.2.9");
        socket = new MulticastSocket();
        // join a Multicast group and send the group
        socket.joinGroup(address);
        byte[] data = null;
        for (;;) {
            Thread.sleep(10000);
            System.out.println("Sending ");
            String str = ("This is ABC Calling....");
            data = str.getBytes();
            packet = new DatagramPacket(data, str.length(), address, PORT);

            socket.send(packet);
        }
    }
}
