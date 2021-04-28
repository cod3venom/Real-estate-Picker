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

namespace Real_estate_Picker_GUI.Core.Config
{
    public class Context
    {
        public Constants constants = new Constants();
        public Files files;
        private LocalSettingsTObject settings;
        private TextBundle texts;

        public Context()
        {
            this.files = new Files();
            this.settings = JsonConvert.DeserializeObject<LocalSettingsTObject>(files.ReadFile(this.constants.SettingsPath));
            this.texts = new TextBundle(this);
        }
        public LocalSettingsTObject Settings
        {
            get { return this.settings; }
        }

        public TextBundle Texts
        {
            get { return this.texts; }
        }
 

    }
}
