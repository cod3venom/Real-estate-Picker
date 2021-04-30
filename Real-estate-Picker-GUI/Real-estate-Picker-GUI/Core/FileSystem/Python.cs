
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
        private Process process;
        private string executor = "python3 ";
        private string file = @"main.py";

        public Python(Context ctx)
        {
            this.ctx = ctx;
            this.Initialize();
        }

        private void Initialize()
        {
            this.process = new Process();
            this.process.StartInfo = new ProcessStartInfo()
            {
                RedirectStandardOutput = true,
                RedirectStandardInput = true,
                UseShellExecute = false,
                CreateNoWindow = false,
                
            };
        }

        public void Start()
        {
            this.process.StartInfo.FileName = this.executor;
            this.process.StartInfo.Arguments = string.Format("{0} {1} {2}", this.file, this.ctx.Settings.localIp,this.ctx.Settings.localPort);
            this.process.StartInfo.WorkingDirectory = @"C:\Users\venom\Desktop\Real-estate-Picker\";
            this.process.Start();
            this.Report();
        }


        public void Report()
        {
            string output = this.process.StandardOutput.ReadToEnd();
            this.process.WaitForExit();

            Console.WriteLine(output);
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
