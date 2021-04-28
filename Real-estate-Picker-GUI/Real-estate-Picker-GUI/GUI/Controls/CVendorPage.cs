using Real_estate_Picker_GUI.Core.Config;
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
    public partial class CVendorPage : UserControl
    {
        private Context ctx;
        public CVendorPage(Context ctx)
        {
            this.ctx = ctx;
            InitializeComponent();

            this.lblAddLink.Text = this.ctx.Texts.getText(2);
            this.btnAdd.Text = this.ctx.Texts.getText(3);
            this.btnImport.Text = this.ctx.Texts.getText(4);
        }
    }
}
