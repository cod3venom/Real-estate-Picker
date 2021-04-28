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
    public partial class CMarkup : UserControl
    {
        public CMarkup()
        {
            InitializeComponent();
        }
        
        
        public FlowLayoutPanel Sidebar
        {
            get { return this.sidebar; }
        }
        
        public Panel Page
        {
            get { return this.pagesContainer; }
        }


        public void showPage(CVendorPage page)
        {
            foreach(Control ctrl in this.pagesContainer.Controls)
            {
                this.pagesContainer.Controls.Remove(ctrl);
            }
            this.pagesContainer.Controls.Add(page);


        }
 
 
    }
}
