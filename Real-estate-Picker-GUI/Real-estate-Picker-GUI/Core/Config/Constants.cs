using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Real_estate_Picker_GUI.Core.Config
{
    public class Constants
    {
        public  string SettingsPath = Environment.CurrentDirectory + "/Settings/Settings.jsonc";        
        public Dictionary<string, string> Vendors = new Dictionary<string, string>();




        public Constants()
        {
            Vendors.Add("Morizon", Environment.CurrentDirectory+ "\\Assets\\vendors\\morizon.png");
            Vendors.Add("Otodom", Environment.CurrentDirectory + "\\Assets\\vendors\\otodom.png");
            Vendors.Add("Gratka", Environment.CurrentDirectory + "\\Assets\\vendors\\gratka.png");
            Vendors.Add("Gumtree", Environment.CurrentDirectory + "\\Assets\\vendors\\gumtree.png");
            Vendors.Add("Domy", Environment.CurrentDirectory + "\\Assets\\vendors\\domy.png");
            Vendors.Add("Olx", Environment.CurrentDirectory + "\\Assets\\vendors\\olx.png");
            Vendors.Add("DomiPortal", Environment.CurrentDirectory + "\\Assets\\vendors\\domiportal.png");
        }
    }
}
