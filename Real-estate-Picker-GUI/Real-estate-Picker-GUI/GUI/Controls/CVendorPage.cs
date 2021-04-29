using Real_estate_Picker_GUI.Core.Config;
using Real_estate_Picker_GUI.Core.Handlers;
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
        private HListBox hListBox;
        private HStrings hStrings;
        public CVendorPage(Context ctx)
        {
            this.ctx = ctx;
            InitializeComponent();

            this.hListBox = new HListBox(this.linksListBox);
            this.hStrings = new HStrings();
            this.lblAddLink.Text = this.ctx.Texts.getText(2);
            this.btnAdd.Text = this.ctx.Texts.getText(3);
            this.btnImport.Text = this.ctx.Texts.getText(4);
            this.btnStart.Text = this.ctx.Texts.getText(6);
            this.btnStop.Text = this.ctx.Texts.getText(7);

            this.openFileDialog.InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
            this.openFileDialog.Filter = this.ctx.constants.LinksImportingFileDialogFilter;
            this.openFileDialog.DefaultExt = "txt";
            this.openFileDialog.CheckFileExists = true;
            this.openFileDialog.CheckPathExists = true;
            this.openFileDialog.Multiselect = false;
            this.openFileDialog.ReadOnlyChecked = true;
            this.openFileDialog.ShowReadOnly = true;
            this.hookControls();
        }

        public Button Start
        {
            get { return this.btnStart; }
        }

        public Button Stop
        {
            get { return this.btnStop; }
        }

        public ListBox ClientsListbox
        {
            get { return this.clientsListbox; }
        }
        public List<string> Links ()
        {
            string content = this.ctx.files.ReadFile(this.openFileDialog.FileName);
            return this.hStrings.splitOnNewLines(content);
        }
        

        private void hookControls()
        {
            this.btnAdd.Click += new EventHandler(this.onAdding);
            this.btnImport.Click += new EventHandler(this.onImporting);
        }

        private void onAdding(object sender, EventArgs e)
        {
           if(this.linkTxt.Text != string.Empty)
            {
                this.addLink(this.linkTxt.Text);
            }
        }

        private void onImporting(object sender, EventArgs e)
        {
            if (this.openFileDialog.ShowDialog() == DialogResult.OK)
            {
                this.hListBox.clear();
                string content = this.ctx.files.ReadFile(this.openFileDialog.FileName);

                foreach(string line in this.hStrings.splitOnNewLines(content))
                {
                    this.addLink(line);
                }
            }

        }

        private void addLink(string link)
        {
            this.hListBox.add(link);
        }
    }
}
