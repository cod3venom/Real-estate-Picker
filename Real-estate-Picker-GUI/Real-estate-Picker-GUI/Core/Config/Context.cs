using Real_estate_Picker_GUI.DAO;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Real_estate_Picker_GUI.Core.FileSystem;
using System.Windows.Forms;
using Real_estate_Picker_GUI.GUI.Controls;
using Real_estate_Picker_GUI.Core.Texts;
 using System.Threading;
using Real_estate_Picker_GUI.Core.Handlers;
using Real_estate_Picker_GUI.Core.Net;
using System.Net.Sockets;

namespace Real_estate_Picker_GUI.Core.Config
{
    public class Context
    {
        private FormHandler formHandler = new FormHandler();
        public Constants constants = new Constants();
        public Files files;
        private LocalSettingsTObject settings;
        private TextBundle texts;
        private NetHandler nethandler;
        

        public Context()
        {
            this.files = new Files();
            this.settings = JsonConvert.DeserializeObject<LocalSettingsTObject>(files.ReadFile(this.constants.SettingsPath));
            this.texts = new TextBundle(this);
            
        }

        public FormHandler Formhandler
        {
            get { return this.formHandler; }
        }

        public LocalSettingsTObject Settings
        {
            get { return this.settings; }
        }

        public TextBundle Texts
        {
            get { return this.texts; }
        }

        public NetHandler Nethandler
        {
            set { this.nethandler = value; }
            get { return this.nethandler; }
        }
 

    }
}
