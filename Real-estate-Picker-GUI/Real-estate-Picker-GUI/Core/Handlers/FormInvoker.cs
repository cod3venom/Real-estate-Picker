using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Real_estate_Picker_GUI.Core.Handlers
{
    public class FormInvoker
    {
        public bool _invokeShowWindow(Form form)
        {
            if (form.InvokeRequired)
            {
                form.Invoke(new MethodInvoker(delegate {
                    form.Show();
                }));
                return true;
            }
            return false;
        }

        public bool _invokeShowDialog(Form form)
        {
            if (form.InvokeRequired)
            {
                form.Invoke(new MethodInvoker(delegate {
                    form.ShowDialog();
                }));
                return true;
            }
            return false;
        }
        public bool _invokeHideWindow(Form form)
        {
            if (form.InvokeRequired)
            {
                form.Invoke(new MethodInvoker(delegate {
                    form.Hide();
                }));
                return true;
            }
            return false;
        }
        public bool _invokeCloseWindow(Form form)
        {
            if (form.InvokeRequired)
            {
                form.Invoke(new MethodInvoker(delegate {
                    form.Close();
                }));
                return true;
            }
            return false;
        }
    }
}
