using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Real_estate_Picker_GUI.Core.Net
{
    public  class NetJsonBuilder
    {
        public string DictToJsonString(Dictionary<string, string> dict)
        {
            string retCode = "{JSON}";
            string jsonCode = string.Empty;

            int item_counter = 1;
            int total_items = dict.Count;
            foreach (KeyValuePair<string, string> data in dict)
            {
                if (item_counter < total_items)
                {
                    jsonCode += string.Format("\"{0}\": \"{1}\",", data.Key, data.Value);
                }
                else
                {
                    jsonCode += string.Format("\"{0}\": \"{1}\"", data.Key, data.Value);
                }
                item_counter += 1;
            }

            retCode = retCode.Replace("JSON", jsonCode);
            return retCode;
        }

        public string AddList(string key, List<string> values)
        {
            string placeholder = "{" + string.Format(" \"{0}\" : [items]", key) + "}";
            string items = "";
            foreach(string value in values) {
                items +='"' + value + '"' + ',';
            }
            placeholder = placeholder.Replace("items", items).Replace("\n", "");
            return placeholder;
        }

        private string ReplaceLastOccurence(string source, string needle, string replace)
        {
            int lastPoint = source.LastIndexOf(needle);
            if (lastPoint == -1) { return source; }

            return source.Remove(lastPoint, needle.Length).Insert(lastPoint, replace);
        }



    }
}
