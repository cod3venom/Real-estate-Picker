using Real_estate_Picker_GUI.Core.Config;
using Real_estate_Picker_GUI.GUI.Controls;
using Real_estate_Picker_GUI.GUI.Forms;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Real_estate_Picker_GUI.Core.Vendors.Morizon
{
    class Morizon
    {
        private Home parent;
        private Context ctx;
        private CVendorPage page;

        public Morizon (Home parent, Context ctx)
        {

            this.parent = parent;
            this.ctx = ctx;
            this.ctx.Nethandler.netMessageHandler.AddMessageHeader(Vendors.Morizon);
            this.page = new CVendorPage(this.ctx);
            this.page.PageName = Vendors.Morizon;
            this.page.Start.Click += new EventHandler(this.Start);
            this.page.Stop.Click += new EventHandler(this.Stop);
            this.ctx.Nethandler.setListbox(this.parent.ClientsListbox);

        }


        public void Show()
        {
            this.parent.cmarkup.showPage(this.page);
        }
        
        public void Hide()
        {
            this.page.Visible = false;
        }

        private void Start(object sender, EventArgs e)
        {
             
                if (!this.ctx.Nethandler.IsActive())
                {
                    MessageBox.Show(this.ctx.Texts.getText(9), this.ctx.Texts.getText(8), MessageBoxButtons.OK, MessageBoxIcon.Stop);
                    return;
                }
                if (this.parent.ClientsListbox.SelectedIndex == -1)
                {
                    MessageBox.Show(this.ctx.Texts.getText(11), this.ctx.Texts.getText(10), MessageBoxButtons.OK, MessageBoxIcon.Information);
                    return;
                }
                else
                {
                    string json = this.ctx.Nethandler.netMessageHandler.ListTOJsonMessage("Links", this.page.Links(), true);
                    this.ctx.Nethandler.Send(json, this.ctx.Nethandler.clientEndpoint);
                    this.ShowProgress();
                }
           
            
        }

        private void Stop(object sender, EventArgs e)
        {
            
            this.ctx.Nethandler.netMessageHandler.Add("Action", "Stop");
            string json = this.ctx.Nethandler.netMessageHandler.DictToJsonMessage(true);

        }

        private void ShowProgress()
        {
            FProgress fProgress = new FProgress(this.ctx);
            fProgress.Show();
 
        }

    }
}
