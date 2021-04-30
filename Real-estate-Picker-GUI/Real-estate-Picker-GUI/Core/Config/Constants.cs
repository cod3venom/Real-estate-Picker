using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Real_estate_Picker_GUI.Core.Config
{
    public class Constants
    {
        public  string SettingsPath = Environment.CurrentDirectory + "\\SharpSettings\\Settings\\Settings.jsonc";        
        public Dictionary<string, string> Vendors = new Dictionary<string, string>();
        public string LinksImportingFileDialogFilter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";



        public Constants()
        {
            Vendors.Add("Morizon", Environment.CurrentDirectory+ "\\SharpSettings\\Assets\\vendors\\morizon.png");
            Vendors.Add("Otodom", Environment.CurrentDirectory + "\\SharpSettings\\Assets\\vendors\\otodom.png");
            Vendors.Add("Gratka", Environment.CurrentDirectory + "\\SharpSettings\\Assets\\vendors\\gratka.png");
            Vendors.Add("Gumtree", Environment.CurrentDirectory + "\\SharpSettings\\Assets\\vendors\\gumtree.png");
            Vendors.Add("Domy", Environment.CurrentDirectory + "\\SharpSettings\\Assets\\vendors\\domy.png");
            Vendors.Add("Olx", Environment.CurrentDirectory + "\\SharpSettings\\Assets\\vendors\\olx.png");
            Vendors.Add("DomiPortal", Environment.CurrentDirectory + "\\SharpSettings\\Assets\\vendors\\domiportal.png");
        }
    }
}
