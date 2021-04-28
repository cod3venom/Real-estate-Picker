using Real_estate_Picker_GUI.Core.Config;
using Real_estate_Picker_GUI.Core.Interfaces;
using Real_estate_Picker_GUI.Core.Vendors.Morizon;
using Real_estate_Picker_GUI.GUI.Controls;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
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
            this.ctx = ctx;

            InitializeComponent();
            this.initializeGUI();

            this.morizon = new Morizon(this, this.ctx);
        }

        public void initializeGUI()
        {
            this.cTopbar1.Title = this.ctx.Settings.title;
            this.cmarkup = new CMarkup();
            this.cmarkup.Dock = DockStyle.Fill;
            this.mainContainer.Controls.Add(this.cmarkup);

            this.createSidebar();
            this.hookControls();
        }

        private void createSidebar()
        {
            CVendor cvendor;

            int counter = -1;
            foreach(KeyValuePair<string,string> vendor in this.ctx.constants.Vendors)
            {
                counter += 1;
                cvendor = new CVendor();
                cvendor.title = vendor.Key;
                cvendor.icon = vendor.Value;
                cvendor.btn.Click += new EventHandler(this.selectVendor);
                this.cmarkup.Sidebar.Controls.Add(cvendor);
            }
        }
        public void hookControls()
        {
            this.cTopbar1.Close.Click += new EventHandler(this.close);
            this.cTopbar1.Minimize.Click += new EventHandler(this.minimize);
        }



        public void close(object sender, EventArgs e)
        {
            Application.Exit();
        }

        public void minimize(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
        }
    }
}
