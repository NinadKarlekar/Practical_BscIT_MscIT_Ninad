package rpcnumoperationserver;

import java.util.*;
import java.net.*;
import java.io.*;

public class RPCNumOperationServer {

    DatagramSocket ds;
    DatagramPacket dp;
    String str, methodName, result;
    int val;

    RPCNumOperationServer() {
        try {
            ds = new DatagramSocket(1200);
            byte b[] = new byte[4096];
            while (true) {
                dp = new DatagramPacket(b, b.length);
                ds.receive(dp);
                str = new String(dp.getData(), 0, dp.getLength());
                if (str.equalsIgnoreCase("q")) {
                    System.exit(1);
                } else {
                    StringTokenizer st = new StringTokenizer(str, " ");
                    int i = 0;
                    while (st.hasMoreTokens()) {
                        String token = st.nextToken();
                        methodName = token;
                        val = Integer.parseInt(st.nextToken());
                    }
                }
                System.out.println(str);
                InetAddress ia = InetAddress.getLocalHost();
                if (methodName.equalsIgnoreCase("square")) {
                    result = "" + square(val);
                } else if (methodName.equalsIgnoreCase("squareroot")) {
                    result = "" + squareroot(val);
                } else if (methodName.equalsIgnoreCase("cube")) {
                    result = "" + cube(val);
                } else if (methodName.equalsIgnoreCase("cuberoot")) {
                    result = "" + cuberoot(val);
                }
                byte b1[] = result.getBytes();
                DatagramSocket ds1 = new DatagramSocket();
                DatagramPacket dp1 = new DatagramPacket(b1, b1.length, InetAddress.getLocalHost(), 1300);
                System.out.println("result : " + result + "\n");
                ds1.send(dp1);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public double square(int a) throws Exception {
        double ans;
        ans = a * a;
        return ans;
    }

    public double squareroot(int a) throws Exception {
        double ans;
        ans = Math.sqrt(a);
        return ans;
    }

    public double cube(int a) throws Exception {
        double ans;
        ans = a * a * a;
        return ans;
    }

    public double cuberoot(int a) throws Exception {
        double ans;
        ans = Math.cbrt(a);
        return ans;
    }

    public static void main(String[] args) {
        new RPCNumOperationServer();
    }
}
