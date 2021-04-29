using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace Real_estate_Picker_GUI.DAO
{
    public class LocalSettingsTObject
    {
        public string title { get; set; }
        public string version { get; set; }
        public string assets { get; set; }
        public string textsPath { get; set; }
        public string localIp { get; set; }
        public int localPort { get; set; }
        public int maxConnectionLimit { get; set; }


    }
}
