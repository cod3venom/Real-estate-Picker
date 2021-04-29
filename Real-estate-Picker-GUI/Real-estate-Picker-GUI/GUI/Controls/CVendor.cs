using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Threading;
using Real_estate_Picker_GUI.Core.Config;

namespace Real_estate_Picker_GUI.GUI.Controls
{
    public partial class CVendor : UserControl
    {

        public CVendor()
        {
            InitializeComponent();
        }
        
        public string Key
        {
            set { this.keyLabel.Text = value.ToString(); }
            get { return this.keyLabel.Text; }
        }
        public string icon 
        {
            set { this.menuBtn.Iconimage = Image.FromFile(value.ToString()); }
        }

        public string title 
        {
            set { this.menuBtn.Text = value.ToString(); }
            get { return this.menuBtn.Text; }
        }
        public Bunifu.Framework.UI.BunifuFlatButton btn
        {
            get { return this.menuBtn; }
        }


    }
}
