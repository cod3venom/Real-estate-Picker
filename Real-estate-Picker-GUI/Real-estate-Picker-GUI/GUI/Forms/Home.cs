using Real_estate_Picker_GUI.Core.Config;
using Real_estate_Picker_GUI.Core.Interfaces;
using Real_estate_Picker_GUI.Core.Vendors;
using Real_estate_Picker_GUI.Core.Vendors.Morizon;
using Real_estate_Picker_GUI.GUI.Controls;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Real_estate_Picker_GUI.GUI.Forms
{
    public partial class Home : Form, IWindow
    {
        private Context ctx;
        public CMarkup cmarkup;

        private Morizon morizon;

        protected override CreateParams CreateParams
        {
            get
            {
                const int CS_DROPSHADOW = 0x20000;
                CreateParams cp = base.CreateParams;
                cp.ClassStyle |= CS_DROPSHADOW;
                return cp;
            }
        }

        public Home(Context ctx)
        {
            InitializeComponent();
            this.ctx = ctx;
            this.ctx.Nethandler = new Core.Net.NetHandler(this, this.ctx);
            this.morizon = new Morizon(this, this.ctx);
            this.initializeGUI();
            this.morizon.Show();
        }

        public void initializeGUI()
        {
            this.cTopbar.Title = this.ctx.Settings.title;
            this.cmarkup = new CMarkup();
            this.cmarkup.Dock = DockStyle.Fill;
            this.mainContainer.Controls.Add(this.cmarkup);

            this.hookControls();

            CVendor cvendor;
            foreach (KeyValuePair<string, string> vendor in this.ctx.constants.Vendors)
            {
                cvendor = new CVendor();
                cvendor.title = vendor.Key;
                cvendor.icon = vendor.Value;
                cvendor.btn.Click += new EventHandler(this.selectVendor);
                this.cmarkup.Sidebar.Controls.Add(cvendor);
            }
        }
        
        public void hookControls(){
            this.cTopbar.Close.Click += new EventHandler(this.close);
            this.cTopbar.Minimize.Click += new EventHandler(this.minimize);
            this.cTopbar.Run.Click += new EventHandler(this.initializeServer);
        }

        private void selectVendor(object sender, EventArgs e)
        {
            string key = (sender as Bunifu.Framework.UI.BunifuFlatButton).Text;
            switch (key)
            {
                case Vendors.Morizon:
                    this.morizon.Show();
                    break;

                case Vendors.Otodom:
                    break;

                case Vendors.Gratka:
                    break;

                case Vendors.Gumtree:
                    break;

                case Vendors.Domy:
                    break;

                case Vendors.Olx:
                    break;

                case Vendors.DomiPortal:
                    break;
                default:
                    this.morizon.Show();
                    break;
            }
        }
        
        public void initializeServer(object sender, EventArgs e) 
        {
            if (!this.ctx.Nethandler.IsActive())
            {
                this.ctx.Nethandler.Start();
                this.cTopbar.ActionIcon = Properties.Resources.stop;
            }
            else
            {
                this.ctx.Nethandler.Stop();
                this.cTopbar.ActionIcon = Properties.Resources.start;
            }
        }


        public void close(object sender, EventArgs e)  {Application.Exit(); }

        public void minimize(object sender, EventArgs e) { this.WindowState = FormWindowState.Minimized; }
    }
}
