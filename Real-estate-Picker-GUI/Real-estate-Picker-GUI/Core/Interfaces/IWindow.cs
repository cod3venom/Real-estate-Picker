using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Real_estate_Picker_GUI.Core.Interfaces
{
    interface IWindow
    {
        void initializeGUI();
        void hookControls();
        void close(object sender, EventArgs e);
        void minimize(object sender, EventArgs e);

    }
}
