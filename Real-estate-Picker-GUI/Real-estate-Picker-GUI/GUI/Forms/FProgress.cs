using Real_estate_Picker_GUI.Core.Config;
using Real_estate_Picker_GUI.Core.Interfaces;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Real_estate_Picker_GUI.DAO;
using System.Threading;

namespace Real_estate_Picker_GUI.GUI.Forms
{
    public partial class FProgress : Form, IWindow
    {
        private Dictionary<string, ResponseLinkTObject> progressDB = new Dictionary<string, ResponseLinkTObject>();
        private DictHandler dicthandler = new DictHandler();
        private Context ctx;
        private int index = 0;
        public FProgress(Context ctx)
        {
            this.ctx = ctx;
            InitializeComponent();
            this.initializeGUI();
            this.hookControls();

            Thread parseThread = new Thread(() => this.ParseMessage());
            parseThread.IsBackground = true;
            parseThread.Start();
        }


        public void initializeGUI()
        {
            this.cTopbar.Run.Visible = false;
        }

        public void hookControls()
        {
            this.cTopbar.Close.Click += new EventHandler(this.close);
            this.cTopbar.Minimize.Click += new EventHandler(this.minimize);
        }

        
        public void ParseMessage()
        {
            while(this.ctx.Nethandler.IsActive())
            {
                if (!this.ctx.Nethandler.IsActive()) { break; }

                string message = this.ctx.Nethandler.ReceivedMessage;

                if (message != null)
                {
                    if (message.Contains("Link"))
                    {
                        try
                        {
                            ResponseLinkTObject obj = JsonConvert.DeserializeObject<ResponseLinkTObject>(message);
                            this.Add(obj);
                        }
                        catch (Exception)
                        {

                        }
                    }
                }
            }
        }
        
        
        

        public void Add(ResponseLinkTObject obj)
        {
            this.index += 1;
            if (!this.dicthandler.Exists(this.progressDB, obj.Link))
            {
                if (this.cTable1.Table.InvokeRequired)
                {
                    this.cTable1.Table.Invoke(new MethodInvoker(delegate
                    {
                        this.cTable1.Table.Rows.Add(new object[] { index, obj.Link });
                        this.dicthandler.Add(this.progressDB, index.ToString(), obj);
                        return;
                    }));
                }
                else
                {
                    this.cTable1.Table.Rows.Add(new object[] { index, obj.Link });
                    this.dicthandler.Add(this.progressDB, index.ToString(), obj);
                    return;
                }
            }
        }

        public void minimize(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
        }

        public void close(object sender, EventArgs e)
        {
            this.Close();
        }
    }

    class DictHandler
    {
 
        public bool Exists(Dictionary<string, ResponseLinkTObject> dict, string key)
        {
            if (key != string.Empty)
            {
                foreach (KeyValuePair<string, ResponseLinkTObject> values in dict)
                {
                    if (values.Key.ToString() == key)
                    {
                        return true;
                    }
                }
            }
            return false;
        }

        public bool Add(Dictionary<string, ResponseLinkTObject> dict, string key, ResponseLinkTObject value)
        {
            if (dict != null && value != null && value.Link != string.Empty)
            {
                if (!this.Exists(dict, key))
                {
                    dict.Add(key, value);
                    return true;
                }
                //else
                //{
                //    return this.Update(dict, key, value);
                //}
            }
            return false;
        }

        public bool Update(Dictionary<string, ResponseLinkTObject> dict, string key, ResponseLinkTObject value)
        {
            if (dict != null && value != null && value.Link != string.Empty)
            {

                foreach (KeyValuePair<string, ResponseLinkTObject> values in dict)
                {
                    if (values.Key.ToString() == key)
                    {
                        dict[values.Key] = value;
                        return true;
                    }
                }
            }
            return false;
        }
    }
}
