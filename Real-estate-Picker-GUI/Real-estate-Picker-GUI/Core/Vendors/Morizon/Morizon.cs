using Real_estate_Picker_GUI.Core.Config;
using Real_estate_Picker_GUI.GUI.Controls;
using Real_estate_Picker_GUI.GUI.Forms;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

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
        }


        public void show()
        {
            this.parent.cmarkup.showPage(this.page);
        }
        
        public void hide()
        {

        }

        public void start()
        {

        }

    }
}
