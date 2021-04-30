
using Real_estate_Picker_GUI.Core.Config;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Real_estate_Picker_GUI.Core.FileSystem
{
    public class Python
    {
        private Context ctx;
        private _Process process;
        private string executor = "python3.exe";
        private string file = @"main.py";

        public Python(Context ctx)
        {
            this.ctx = ctx;
            this.process = new _Process();
        }

        
        public void Start()
        {
            this.process.SetFileName(executor);
            this.process.SetArgument(string.Format("{0} {1} {2}", this.file, this.ctx.Settings.localIp,this.ctx.Settings.localPort));
            this.process.SetwWrkDir(@"C:\Users\venom\Desktop\Real-estate-Picker\");
            this.process.Start();
      
        }

 

        public void Stop()
        {
            Process[] chromeDriverProcesses = Process.GetProcessesByName("chromedriver");

            foreach (var chromeDriverProcess in chromeDriverProcesses)
            {
                chromeDriverProcess.Kill();
            }
        }

        

    }
}
