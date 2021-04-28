using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Real_estate_Picker_GUI.Core.FileSystem
{
    public class Files
    {
        private bool isFile(string path)
        {
            if (File.Exists(path)) { return true; }
            return false;
        }
        private bool isDir(string path)
        {
            if (Directory.Exists(path)) { return true; };
            return false;
        }
        public string ReadFile(string path)
        {
            string _retCode = String.Empty;
            if (this.isFile(path))
            {
                return File.ReadAllText(path).ToString();
            }
            return _retCode;
        }
        public bool writeFile(string path, string content)
        {
            using (StreamWriter writer = new StreamWriter(path))
            {
                writer.WriteLine(content);
                writer.Close();
                return true;
            }
        }
        public bool AppendToFile(string path, string content)
        {
            if (!string.IsNullOrEmpty(path) && !string.IsNullOrEmpty(content))
            {
                File.AppendAllText(path, content);
                return true;
            }
            return false;
        }
        public bool fexists(string path)
        {
            return File.Exists(path);
        }
    }
}
