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
    public partial class CTable : UserControl
    {
        private int index = 0;
        public CTable()
        {
            InitializeComponent();
            this.initialize_GUI();
        }
        public DataGridView Table
        {
            get { return this.table; }
        }

        private void initialize_GUI()
        {
            this.Dock = DockStyle.Fill;
            this.Table.EnableHeadersVisualStyles = false;
            this.Table.RowHeadersVisible = false;
            this.Table.AllowUserToResizeColumns = false;
            this.Table.MultiSelect = false;
            this.Table.AllowUserToResizeRows = false;
            this.Table.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
            this.Table.ColumnHeadersDefaultCellStyle.SelectionBackColor = this.Table.ColumnHeadersDefaultCellStyle.BackColor;
            this.Table.BackgroundColor = Color.White;
            this.Table.RowHeadersVisible = false;
        }

 
        
    }
}
