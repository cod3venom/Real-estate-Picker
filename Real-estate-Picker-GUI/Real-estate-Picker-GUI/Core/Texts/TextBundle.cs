using Real_estate_Picker_GUI.Core.Config;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Real_estate_Picker_GUI.Core.Texts
{
    public class TextBundle
    {
        private Context ctx;
        private string currentlanguage;
        private Dictionary<int, string> textsPack = new Dictionary<int, string>();
        
        public TextBundle(Context ctx)
        {
            this.ctx = ctx;
            this.currentlanguage = CultureInfo.InstalledUICulture.Name;
            this.ctx.Settings.textsPath = string.Format("{0}{1}{2}.lang", Environment.CurrentDirectory, this.ctx.Settings.textsPath, this.currentlanguage);

            if (this.ctx.files.fexists(this.ctx.Settings.textsPath))
            {
                this.loadTexts();
            }

        }


        private void loadTexts()
        {
            string content = this.ctx.files.ReadFile(this.ctx.Settings.textsPath);
            
            if (content.Contains('\n'))
            {
                string[] lines = content.Split('\n');
                foreach(string line in lines)
                {
                    if (line.Contains('#'))
                    {
                        string[] splitOnHashtag = line.Split('#');

                        if(splitOnHashtag.Length == 2)
                        {
                            int txtNum = Int32.Parse(splitOnHashtag[0]);
                            string txt = splitOnHashtag[1].ToString();

                            this.textsPack.Add(txtNum, txt);
                        }
                    }
                }

            }
        }

        public string getText(int num)
        {
            if (num > 0)
            {
                foreach (KeyValuePair<int, string> pack in this.textsPack)
                {
                    if (pack.Key == num)
                    {
                        return pack.Value;
                    }
                }
            }
            return string.Empty;
        }
    }   
}
