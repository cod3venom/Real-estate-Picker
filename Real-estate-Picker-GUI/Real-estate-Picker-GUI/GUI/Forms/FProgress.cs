using Real_estate_Picker_GUI.Core.Config;
using Real_estate_Picker_GUI.Core.Interfaces;
using Real_estate_Picker_GUI.DAO;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Windows.Forms;
using System.Threading;
using Real_estate_Picker_GUI.Core.Vendors;

namespace Real_estate_Picker_GUI.GUI.Forms
{
    public partial class FProgress : Form, IWindow
    {
        private Context ctx;
        private TableHandler tableHandler;
        private int index = 0;
        public FProgress(Context ctx)
        {
            this.ctx = ctx;
            InitializeComponent();
            this.initializeGUI();
            this.hookControls();
            this.tableHandler = new TableHandler(this.ctx, this.cTable1.Table);
            
            Thread parseThread = new Thread(() => this.ParseMessage());
            parseThread.IsBackground = true;
            parseThread.Start();
        }
        public void initializeGUI() {
            this.cTopbar.Run.Visible = false;
            this.cTopbar.Title = this.ctx.Texts.getText(12);
            this.cTable1.TotalTitle = this.ctx.Texts.getText(15);
        }
        public void hookControls() {
            this.cTopbar.Close.Click += new EventHandler(this.close);
            this.cTopbar.Minimize.Click += new EventHandler(this.minimize);
        }
        public void minimize(object sender, EventArgs e) { this.WindowState = FormWindowState.Minimized; }
        public void close(object sender, EventArgs e) {
            if (this.InvokeRequired)
                this.Invoke(new MethodInvoker(delegate { this.Close(); }));
            else
                this.Close();
        }

        public void ParseMessage() 
        {
            while(this.ctx.Nethandler.IsActive())
            {
                if (!this.ctx.Nethandler.IsActive()) { break; }

                string message = this.ctx.Nethandler.ReceivedMessage;
                if (message != null)
                {
                    if (message.Contains(VendorMessageKeys.Folder))
                    {
                        ResponseLinkTObject obj = JsonConvert.DeserializeObject<ResponseLinkTObject>(message);
                        this.index += 1;
                        this.tableHandler.Add(index, obj);
                    }

                    if (message.Contains(JobActions.Finish))
                    {
                        MessageBox.Show(this.ctx.Texts.getText(13), this.ctx.Texts.getText(12),MessageBoxButtons.OK, MessageBoxIcon.Information);
                        break;
                    }
 
                }
            }
        }
  
    }

    class TableHandler
    {
        private Dictionary<int, ResponseLinkTObject> progressDB = new Dictionary<int, ResponseLinkTObject>();
        private Context ctx;
        private DataGridView table;
        
        public TableHandler(Context ctx, DataGridView table)
        {
            this.ctx = ctx;
            this.table = table;
            this.table.CellClick += new DataGridViewCellEventHandler(this.OpenFolder);
        }
        private void OpenFolder(object sender, EventArgs e) { this.ctx.files.OpenExplorer(this.GetFolderPath());}
        public string GetFolderPath()
        {
            if (this.table.SelectedCells.Count > 0)
            {
                int rowIndex = this.table.SelectedCells[0].RowIndex;
                DataGridViewRow selectedRow = this.table.Rows[rowIndex];
                string path = Convert.ToString(selectedRow.Cells["folderColumn"].Value);
                return path;
            }
            return string.Empty;
        }
        public bool Exists(string value)
        {
            if (value != string.Empty)
            {
                foreach (KeyValuePair<int, ResponseLinkTObject> values in this.progressDB)
                {
                    if (values.Value.Folder == value)
                    {
                        return true;
                    }
                }
            }
            return false;
        }
        public bool Add(int key, ResponseLinkTObject value)
        {
            if (this.progressDB != null && value != null && value.Folder != string.Empty)
            {
                if (!this.Exists(value.Folder))
                {
                    this.progressDB.Add(key, value);    
                    if (this.table.InvokeRequired)
                    {
                        this.table.Invoke(new MethodInvoker(delegate {
                            this.table.Rows.Add(new object[] { key, value.Folder });
                        }));
                    }
                    else
                    {
                        this.table.Rows.Add(new object[] { key, value.Folder });
                    }
                    return true;
                }
            }
            return false;
        }
        public void CleanUp()
        {
            if (this.table.InvokeRequired)
            {
                this.table.Invoke(new MethodInvoker(delegate
                {
                    this.table.Rows.Clear();
                }));
            }else
            {
                this.table.Rows.Clear();
            }
        }

        public int Total { get { return this.progressDB.Count; } }
    }
}
