using Real_estate_Picker_GUI.Core.Config;
using Real_estate_Picker_GUI.GUI.Forms;
using System;
using System.Windows.Forms;

namespace Real_estate_Picker_GUI
{
    static class Program
    {
        /// <summary>
        /// Główny punkt wejścia dla aplikacji.
        /// </summary>
        [STAThread]
        static void Main()
        {


            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Home(new Context()));
        }
    }
}
