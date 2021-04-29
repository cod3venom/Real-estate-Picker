using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Real_estate_Picker_GUI.GUI.Controls
{
    public partial class CTopbar : UserControl
    {
        
        public CTopbar()
        {
            InitializeComponent();
        }


        public string Title
        {
            set { this.title.Text = value.ToString(); }
            get { return this.title.Text; }
        }


        public Bunifu.Framework.UI.BunifuImageButton Close
        {
            get { return this.closeBtn; }
        }

        public Bunifu.Framework.UI.BunifuImageButton Minimize
        {
            get { return this.minimizeBtn; }
        }

        public Bunifu.Framework.UI.BunifuImageButton Run
        {
            get { return this.btnServer; }
        }
         
        public Image ActionIcon
        {
            set { this.btnServer.Image = value; }
        }
    }
}
