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
            this.hookActions();
        }
        public DataGridView Table
        {
            get { return this.table; }
        }
        
        public string TotalTitle
        {
            set { this.totalRecordsTitleLabel.Text = value.ToString(); }
            get { return this.totalRecordsTitleLabel.Text; }
        }

        public void SetTotalAmount (string amount)
        {
            if(this.totalRecordsAmountLabel.InvokeRequired)
            {
                this.totalRecordsAmountLabel.Invoke(new MethodInvoker(delegate
                {
                    this.totalRecordsAmountLabel.Text = amount;
                }));
            }
            else
            {
                this.totalRecordsAmountLabel.Text = amount;
            }
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

        private void hookActions()
        {
            this.table.RowsAdded += new DataGridViewRowsAddedEventHandler(this.OnNewRowAdded);
        }

        private void OnNewRowAdded(object sender, EventArgs e)
        {
            this.totalRecordsAmountLabel.Text = this.table.Rows.Count.ToString();
        }
    }
}
