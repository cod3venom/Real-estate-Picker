using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Real_estate_Picker_GUI.Core.Handlers
{
    class HListBox
    {
        private ListBox listbox;
        public HListBox(ListBox listbox)
        {
            this.listbox = listbox;
        }


        public bool exists(string value)
        {
            for(int index = this.listbox.Items.Count - 1; index >= 0; --index)
            {
                if (value == this.listbox.Items[index].ToString())
                {
                    return true;
                }
            }
            return false;
        }

        public void addOnThread(string value, bool allowDuplicate = false)
        {
            if(this.listbox.InvokeRequired)
            {
                this.listbox.Invoke(new MethodInvoker(delegate
                {
                    this.add(value, allowDuplicate);
                }));
            }
        }

        public void add(string value, bool allowDuplicate = false)
        {
            if (allowDuplicate)
            {
                this.listbox.Items.Add(value);
                return;
            }
            if (!this.exists(value))
            {
                this.listbox.Items.Add(value);
                return;
            }
        }

        public void delete(string value)
        {
            for (int index = this.listbox.Items.Count - 1; index >= 0; --index)
            {
                if (value == this.listbox.Items[index].ToString())
                {
                    if(this.listbox.InvokeRequired)
                    {
                        this.listbox.Invoke(new MethodInvoker(delegate
                        {
                            this.listbox.Items.RemoveAt(index);
                        }));
                    }
                    else
                    {
                        this.listbox.Items.RemoveAt(index);
                    }
                }
            }
        }
        public void clear()
        {
            if (this.listbox.InvokeRequired)
            {
                this.listbox.Invoke(new MethodInvoker(delegate
                {
                    this.listbox.Items.Clear();
                }));
            }
            else
            {
                this.listbox.Items.Clear();
            }
        }
    }
}
