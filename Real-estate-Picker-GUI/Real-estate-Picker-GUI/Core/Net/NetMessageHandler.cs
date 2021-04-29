using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Real_estate_Picker_GUI.Core.Net
{
    public class NetMessageHandler : NetJsonBuilder
    {
        private Dictionary<string, string> messageStack = new Dictionary<string, string>();
        private char messageHeaderDelimiter = '>';
        private string messageHeader = string.Empty;
        
        /// <summary>
        /// By default delimiter is '>'.
        /// </summary>
        /// <param name="delimiter"></param>
        public void addDelimiter(char delimiter) { this.messageHeaderDelimiter = delimiter; }
        
        
        /// <summary>
        /// Add header to message to easyli identify what command was received
        /// for example it will looks like this : HEADER > {"key": "value", "key1": "value1"}
        /// on the client side just split received message on '>' then use Switch(case) on
        /// header and once needle header will appears then parse full json.
        /// </summary>
        /// <param name="header"></param>
        public void AddMessageHeader(string header) { this.messageHeader = header; }

        

        /// <summary>
        /// Check if value exists in dictionary
        /// </summary>
        /// <param name="key"></param>
        /// <param name="value"></param>
        /// <returns></returns>
        public bool Exists(string key = "", string value = null)
        {
            foreach (KeyValuePair<string, string> objects in this.messageStack)
            {
                if (objects.Key == key) { return true; }
                if (objects.Value == value){return true; }
            }
            return false;
        }

        /// <summary>
        /// Add or overwrite value in dictionary
        /// </summary>
        /// <param name="key"></param>
        /// <param name="value"></param>
        /// <param name="overWrite"></param>
        public void Add(string key, string value, bool overWrite = false)
        {
            if (key != string.Empty && value != null)
            {
                if(!this.Exists(value))
                {
                    this.messageStack.Add(key, value);
                    return;
                }
                if(overWrite)
                {
                    foreach(KeyValuePair<string,string> objects in this.messageStack)
                    {
                        if(objects.Key == key)
                        {
                            this.messageStack[key] = value;
                            return;
                        }
                    }
                }
            }

        }

        public string DictToJsonMessage(bool add_header = false)
        {
            string jsonCode = this.DictToJsonString(this.messageStack);

            if (add_header)
            {
                jsonCode = string.Format("{0}{1}{2}", this.messageHeader, this.messageHeaderDelimiter.ToString(), jsonCode);
            }
            
            return jsonCode;
        }

        public string ListTOJsonMessage(string key, List<string> list, bool add_header = false)
        {
            string jsonCode = this.AddList(key, list);

            if (add_header)
            {
                jsonCode = string.Format("{0}{1}{2}", this.messageHeader, this.messageHeaderDelimiter.ToString(), jsonCode);
            }

            return jsonCode;
        }


    }
}
