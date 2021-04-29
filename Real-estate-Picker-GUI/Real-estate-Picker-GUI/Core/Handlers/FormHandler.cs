using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Real_estate_Picker_GUI.Core.Handlers
{
    public class FormHandler
    {
        public FormInvoker invoker;
        public FormHandler()
        {
            this.invoker = new FormInvoker();
        }
        public void ShowWindow(Form form)
        {
            if (form.InvokeRequired)
            {
                this.invoker._invokeShowWindow(form);
            }
            else
            {
                form.Show();
            }
        }
        public void ShowDialog(Form form)
        {
            if (form.InvokeRequired)
            {
                this.invoker._invokeShowDialog(form);
            }
            else
            {
                form.ShowDialog();
            }
        }
        public void HideWindow(Form form)
        {
            if (form.InvokeRequired)
            {
                this.invoker._invokeHideWindow(form);
            }
            else
            {
                form.Hide();
            }
        }

        public void CloseWindow(Form form)
        {
            if (form.InvokeRequired)
            {
                this.invoker._invokeCloseWindow(form);
            }
            else
            {
                form.Close();
            }
        }
    }
}
