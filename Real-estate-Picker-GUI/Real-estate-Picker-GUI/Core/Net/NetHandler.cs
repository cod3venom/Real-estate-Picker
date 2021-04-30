using Real_estate_Picker_GUI.Core.Config;
using Real_estate_Picker_GUI.Core.Handlers;
using Real_estate_Picker_GUI.GUI.Forms;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Real_estate_Picker_GUI.Core.Net
{
    public class NetHandler: NetStack
    {
        Home parent;
        private Context ctx;
        public NetMessageHandler netMessageHandler = new NetMessageHandler();
        private HListBox hListobx;
        private bool isActive;

        private Thread threadWatch;
        private Socket socketWatch;
        private IPEndPoint ipEndpoint;
        public Socket client;
        public EndPoint clientEndpoint;

        private Dictionary<EndPoint, Socket> sockDict = new Dictionary<EndPoint, Socket>();
        private Dictionary<EndPoint, Thread> threadDict = new Dictionary<EndPoint, Thread>();
        

        public string ReceivedMessage { get; set; }
        public void  setListbox(ListBox box) 
        {
            this.hListobx = new HListBox(box);
        }


        public NetHandler(Home parent, Context ctx)
        {
            this.parent = parent;
            this.ctx = ctx;
            this.isActive = false;

        }

        public bool IsActive() {return this.isActive;}
        
        public void Start()
        {
            this.isActive = true;
            this.ipEndpoint = new IPEndPoint(IPAddress.Parse(this.ctx.Settings.localIp), this.ctx.Settings.localPort);
            this.socketWatch = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            try
            {
                this.socketWatch.Bind(this.ipEndpoint);
                this.socketWatch.Listen(10);
            }
            catch(SocketException sockex) { MessageBox.Show(sockex.ToString()); }
            catch (Exception ex) { MessageBox.Show(ex.ToString()); }

            this.threadWatch = new Thread(this.Listen);
            this.threadWatch.IsBackground = true;
            this.threadWatch.Start();
        }
         
        public void Listen()
        {
            try
            {
                while (this.isActive)
                {
                    if (!this.isActive) { break; }
                        this.client = this.socketWatch.Accept();
                        this.clientEndpoint = client.RemoteEndPoint;
                   
                    if (!this.Exists(client) && this.ctx.Settings.maxConnectionLimit -1 == this.stack.Count)
                    {
                        if(this.hListobx != null) {
                            this.hListobx.addOnThread(clientEndpoint.ToString());
                        }
                        this.Add(client);
                        Thread recvThread = new Thread(() => this.Receive(client));
                        recvThread.IsBackground = true;
                        recvThread.Start();
                        this.threadDict.Add(clientEndpoint, recvThread);
                    }
                }
            }
            catch (SocketException) {   }
            catch (Exception ex) { MessageBox.Show(ex.ToString()); }
        }
        public void Stop()
        {
            if(this.isActive)
            {
                this.isActive = false;
                this.socketWatch.Close();
                this.sockDict.Clear();
                this.threadDict.Clear();
                this.hListobx.clear();
                this.Clear();
            }
        }

        public bool Send(string message, EndPoint IpEndpoint = null, string ipAddress = "", Socket client = null)
        {
            try
            {
                if (message != string.Empty)
                {
                    byte[] messageBytes = Encoding.UTF8.GetBytes(message);
                    byte[] messageSize = Encoding.UTF8.GetBytes(messageBytes.Length.ToString());
                    if (IpEndpoint != null)
                    {
                        client = this.SocketByEndpoint(IpEndpoint);
                        if (client != null)
                        {
                            client.Send(messageSize);
                            client.Send(messageBytes);
                        }
                        return true;
                    }
                    if (ipAddress != string.Empty)
                    {
                        client = this.SocketByIP(ipAddress);
                        if (client != null)
                        {
                            client.Send(messageSize);
                            client.Send(messageBytes);
                        }
                    }
                    if (client != null)
                    {
                        if (client.Connected)
                        {
                            client.Send(messageSize);
                            client.Send(messageBytes);
                        }
                    }
                }
                return false;
            }
            catch (SocketException){ return false; }
            catch(Exception) { return false; }
        }

        public void Receive(Socket client)
        {
            while(this.isActive)
            {
                byte[] buffer = new byte[1024];
                int receiveLength = -1;

                try
                {
                    receiveLength = client.Receive(buffer);
                }
                catch (SocketException) 
                {
                    this.OnDisconnect(client);
                }
                catch (Exception ex) { MessageBox.Show(ex.ToString()); }

              
                if (receiveLength > 0)
                {
                    string received = Encoding.ASCII.GetString(buffer, 0, receiveLength);

                    if (received != this.ReceivedMessage)
                    {
                        this.ReceivedMessage = received;
                        Console.WriteLine(this.ReceivedMessage);
                    }
                }
            }
        }

        private void OnDisconnect(Socket client)
        {
            sockDict.Remove(client.RemoteEndPoint);
            threadDict.Remove(client.RemoteEndPoint);
            this.Delete(client);
            this.hListobx.delete(client.RemoteEndPoint.ToString());

        }
    }
}
