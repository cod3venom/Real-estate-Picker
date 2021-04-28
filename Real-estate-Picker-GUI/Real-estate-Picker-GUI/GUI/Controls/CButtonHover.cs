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
    public partial class CButtonHover : UserControl
    {
        public CButtonHover()
        {
            InitializeComponent();

            this.btn.MouseHover += new EventHandler(this.onHover);
            this.btn.MouseLeave += new EventHandler(this.onLeave);
        }

        private void onLeave(object sender, EventArgs e)
        {
            this.btn.FlatAppearance.BorderSize = 0;
        }

        private void onHover(object sender, EventArgs e)
        {
            this.btn.FlatAppearance.BorderColor = Color.FromArgb(74, 210, 149);
            this.btn.BackColor = Color.White;
            this.btn.FlatAppearance.BorderSize = 1;
        }



        public Button Button
        {
            get { return this.btn; }
        }

        public string Text
        {
            set{ this.btn.Text = value.ToString(); }
            get { return this.btn.Text; }
        }
    }
}
