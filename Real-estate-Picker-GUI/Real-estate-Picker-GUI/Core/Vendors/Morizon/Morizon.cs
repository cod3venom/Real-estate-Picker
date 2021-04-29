using Real_estate_Picker_GUI.Core.Config;
using Real_estate_Picker_GUI.GUI.Controls;
using Real_estate_Picker_GUI.GUI.Forms;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
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
            this.page = new CVendorPage(this.ctx);
            this.page.Start.Click += new EventHandler(this.Start);
            this.page.Stop.Click += new EventHandler(this.Stop);
            
            this.ctx.Nethandler.setListbox(this.page.ClientsListbox);

        }


        public void Show()
        {
            this.parent.cmarkup.showPage(this.page);
        }
        
        public void Hide()
        {

        }

        private void Start(object sender, EventArgs e)
        {
            if (!this.ctx.Nethandler.IsActive())
            {
                 MessageBox.Show(this.ctx.Texts.getText(9),this.ctx.Texts.getText(8), MessageBoxButtons.OK, MessageBoxIcon.Stop);
                return;
            }
            if(this.page.ClientsListbox.SelectedIndex == -1)
            {
                MessageBox.Show(this.ctx.Texts.getText(11), this.ctx.Texts.getText(10), MessageBoxButtons.OK, MessageBoxIcon.Information);
                return;
            }
            else
            {
                this.ctx.Nethandler.netMessageHandler.AddMessageHeader(Vendors.Morizon);
                string json = this.ctx.Nethandler.netMessageHandler.AddList("Links", this.page.Links());
                this.ctx.Nethandler.Send(json, this.ctx.Nethandler.clientEndpoint);
                 

            }
            
        }

        private void Stop(object sender, EventArgs e)
        {

        }

    }
}
