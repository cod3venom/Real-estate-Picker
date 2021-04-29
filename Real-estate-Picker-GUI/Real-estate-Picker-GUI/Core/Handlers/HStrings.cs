using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Real_estate_Picker_GUI.Core.Handlers
{
    class HStrings
    {
        public List<string> splitOnNewLines(string content)
        {
            List<string> pack = new List<string>();

            if (content.Contains(Environment.NewLine))
            {
                string[] lines = content.Split('\n');
                foreach(string line in lines)
                {
                    pack.Add(line);
                }
            }
            return pack;
        }

        
    }
}
