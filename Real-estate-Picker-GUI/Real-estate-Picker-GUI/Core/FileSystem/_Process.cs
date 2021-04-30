using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Real_estate_Picker_GUI.Core.FileSystem
{
    class _Process
    {
        private Process process;
        private string output;

        public _Process()
        {
            this.process = new Process();
        }

        public void SetFileName(string fileName) { this.process.StartInfo.FileName = fileName; }
        private string GetFileName() { return this.process.StartInfo.FileName; }
        public void SetArgument(string argument) { this.process.StartInfo.Arguments =  argument; }
        private string GetArgument() { return this.process.StartInfo.Arguments; }

        public void SetShell(bool flag) { this.process.StartInfo.UseShellExecute = flag; }
        private bool GetShell() { return this.process.StartInfo.UseShellExecute; }

        public void SetRedirectOutp(bool flag) { this.process.StartInfo.RedirectStandardOutput = flag; }
        private bool GetRedirectOutp() { return this.process.StartInfo.RedirectStandardOutput; }

        public void SetRedirectErr(bool flag) { this.process.StartInfo.RedirectStandardError = flag; }
        private bool GetRedirectErr() { return this.process.StartInfo.RedirectStandardError; }

        public void SetRedirectInp(bool flag) { this.process.StartInfo.RedirectStandardInput = flag; }
        private bool GetRedirectInp() { return this.process.StartInfo.RedirectStandardInput; }

        public void SetwWrkDir(string dir) { this.process.StartInfo.WorkingDirectory = dir; }
        private string GetWorkDir() { return this.process.StartInfo.WorkingDirectory; }

        public Process Process {  get { return this.process; } }
        public string Output { get { return this.output; } }
        
        public void Start()
        {
            if (this.process != null)
            {
                if (this.process.StartInfo.RedirectStandardInput && this.process.StartInfo.RedirectStandardOutput)
                {
                    this.process.OutputDataReceived += (sender, args) => OnOutputReceiving(args.Data);
                    this.process.ErrorDataReceived += (sender, args) => OnOutputReceiving(args.Data);
                    process.BeginErrorReadLine();
                    process.BeginOutputReadLine();
                }

                this.process.Start();
                process.WaitForExit();
            }
        }

        private void OnOutputReceiving(string data)
        {
            if (this.output != data)
            {
                this.output = data;
                Console.WriteLine(this.Output);
            }
        }
    }
}
