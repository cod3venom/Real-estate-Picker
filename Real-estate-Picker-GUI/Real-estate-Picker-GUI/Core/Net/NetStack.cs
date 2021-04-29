using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace Real_estate_Picker_GUI.Core.Net
{
    public class NetStack
    {
        public List<Socket> stack = new List<Socket>();
        

        public bool Exists(Socket sock)
        {
            if (sock != null)
            {
                foreach(Socket socket in this.stack)
                {
                    if (socket == sock) { return true; }
                }
            }
            return false;
        }

        public void Add(Socket sock)
        {
            if (!this.Exists(sock))
            {
                
                this.stack.Add(sock);
            }
        }

        public bool Delete(Socket sock)
        {
            if(this.Exists(sock))
            {
                return this.stack.Remove(sock);
            }
            return false;
        }

        public Socket SocketByEndpoint(EndPoint sockEndpoint)
        {
            foreach(Socket socket in this.stack)
            {
                if (socket.RemoteEndPoint == sockEndpoint)
                {
                    return socket;
                }
            }
            return null;
        }

        public Socket SocketByIP(string ipAddress)
        {
            foreach (Socket socket in this.stack)
            {
                string socketIp = socket.RemoteEndPoint.ToString().Split(':')[0];
                if (socketIp == ipAddress)
                {
                    return socket;
                }
            }
            return null;
        }

        public void Clear() { this.stack.Clear(); }
    }
}
