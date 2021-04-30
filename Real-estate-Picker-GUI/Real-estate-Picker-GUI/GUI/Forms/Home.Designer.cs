
namespace Real_estate_Picker_GUI.GUI.Forms
{
    partial class Home
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.topbar = new System.Windows.Forms.Panel();
            this.cTopbar = new Real_estate_Picker_GUI.GUI.Controls.CTopbar();
            this.mainContainer = new System.Windows.Forms.Panel();
            this.panel1 = new System.Windows.Forms.Panel();
            this.clientsListbox = new System.Windows.Forms.ListBox();
            this.cHorizontalSeparator1 = new Real_estate_Picker_GUI.GUI.Controls.CHorizontalSeparator();
            this.cVerticalSeparator2 = new Real_estate_Picker_GUI.GUI.Controls.CVerticalSeparator();
            this.cVerticalSeparator1 = new Real_estate_Picker_GUI.GUI.Controls.CVerticalSeparator();
            this.panel2 = new System.Windows.Forms.Panel();
            this.richText = new System.Windows.Forms.RichTextBox();
            this.panel3 = new System.Windows.Forms.Panel();
            this.button1 = new System.Windows.Forms.Button();
            this.topbar.SuspendLayout();
            this.mainContainer.SuspendLayout();
            this.panel1.SuspendLayout();
            this.panel2.SuspendLayout();
            this.panel3.SuspendLayout();
            this.SuspendLayout();
            // 
            // topbar
            // 
            this.topbar.Controls.Add(this.cTopbar);
            this.topbar.Dock = System.Windows.Forms.DockStyle.Top;
            this.topbar.Location = new System.Drawing.Point(0, 0);
            this.topbar.Name = "topbar";
            this.topbar.Size = new System.Drawing.Size(1158, 47);
            this.topbar.TabIndex = 0;
            // 
            // cTopbar
            // 
            this.cTopbar.Dock = System.Windows.Forms.DockStyle.Fill;
            this.cTopbar.Location = new System.Drawing.Point(0, 0);
            this.cTopbar.Name = "cTopbar";
            this.cTopbar.Size = new System.Drawing.Size(1158, 47);
            this.cTopbar.TabIndex = 0;
            this.cTopbar.Title = "Title";
            // 
            // mainContainer
            // 
            this.mainContainer.Controls.Add(this.panel1);
            this.mainContainer.Dock = System.Windows.Forms.DockStyle.Fill;
            this.mainContainer.Location = new System.Drawing.Point(0, 47);
            this.mainContainer.Name = "mainContainer";
            this.mainContainer.Size = new System.Drawing.Size(1158, 640);
            this.mainContainer.TabIndex = 1;
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.White;
            this.panel1.Controls.Add(this.clientsListbox);
            this.panel1.Controls.Add(this.cHorizontalSeparator1);
            this.panel1.Controls.Add(this.cVerticalSeparator2);
            this.panel1.Controls.Add(this.cVerticalSeparator1);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Right;
            this.panel1.Location = new System.Drawing.Point(912, 0);
            this.panel1.Margin = new System.Windows.Forms.Padding(20);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(246, 640);
            this.panel1.TabIndex = 0;
            // 
            // clientsListbox
            // 
            this.clientsListbox.BackColor = System.Drawing.Color.White;
            this.clientsListbox.Dock = System.Windows.Forms.DockStyle.Fill;
            this.clientsListbox.FormattingEnabled = true;
            this.clientsListbox.Location = new System.Drawing.Point(16, 0);
            this.clientsListbox.Name = "clientsListbox";
            this.clientsListbox.Size = new System.Drawing.Size(211, 621);
            this.clientsListbox.TabIndex = 2;
            // 
            // cHorizontalSeparator1
            // 
            this.cHorizontalSeparator1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(245)))), ((int)(((byte)(247)))), ((int)(((byte)(247)))));
            this.cHorizontalSeparator1.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.cHorizontalSeparator1.Location = new System.Drawing.Point(16, 621);
            this.cHorizontalSeparator1.Name = "cHorizontalSeparator1";
            this.cHorizontalSeparator1.Size = new System.Drawing.Size(211, 19);
            this.cHorizontalSeparator1.TabIndex = 1;
            // 
            // cVerticalSeparator2
            // 
            this.cVerticalSeparator2.BackColor = System.Drawing.Color.White;
            this.cVerticalSeparator2.Dock = System.Windows.Forms.DockStyle.Left;
            this.cVerticalSeparator2.Location = new System.Drawing.Point(0, 0);
            this.cVerticalSeparator2.Name = "cVerticalSeparator2";
            this.cVerticalSeparator2.Size = new System.Drawing.Size(16, 640);
            this.cVerticalSeparator2.TabIndex = 1;
            // 
            // cVerticalSeparator1
            // 
            this.cVerticalSeparator1.BackColor = System.Drawing.Color.White;
            this.cVerticalSeparator1.Dock = System.Windows.Forms.DockStyle.Right;
            this.cVerticalSeparator1.Location = new System.Drawing.Point(227, 0);
            this.cVerticalSeparator1.Name = "cVerticalSeparator1";
            this.cVerticalSeparator1.Size = new System.Drawing.Size(19, 640);
            this.cVerticalSeparator1.TabIndex = 3;
            // 
            // panel2
            // 
            this.panel2.Controls.Add(this.panel3);
            this.panel2.Controls.Add(this.richText);
            this.panel2.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.panel2.Location = new System.Drawing.Point(0, 687);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(1158, 177);
            this.panel2.TabIndex = 2;
            // 
            // richText
            // 
            this.richText.BackColor = System.Drawing.Color.Black;
            this.richText.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.richText.Dock = System.Windows.Forms.DockStyle.Fill;
            this.richText.Font = new System.Drawing.Font("HelveticaNeueCyr", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.richText.ForeColor = System.Drawing.Color.Green;
            this.richText.Location = new System.Drawing.Point(0, 0);
            this.richText.Name = "richText";
            this.richText.Size = new System.Drawing.Size(1158, 177);
            this.richText.TabIndex = 0;
            this.richText.Text = "";
            // 
            // panel3
            // 
            this.panel3.Controls.Add(this.button1);
            this.panel3.Dock = System.Windows.Forms.DockStyle.Top;
            this.panel3.Location = new System.Drawing.Point(0, 0);
            this.panel3.Name = "panel3";
            this.panel3.Size = new System.Drawing.Size(1158, 34);
            this.panel3.TabIndex = 1;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(1124, 8);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(31, 23);
            this.button1.TabIndex = 0;
            this.button1.Text = "-";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // Home
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1158, 864);
            this.Controls.Add(this.mainContainer);
            this.Controls.Add(this.panel2);
            this.Controls.Add(this.topbar);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "Home";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Home";
            this.topbar.ResumeLayout(false);
            this.mainContainer.ResumeLayout(false);
            this.panel1.ResumeLayout(false);
            this.panel2.ResumeLayout(false);
            this.panel3.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion
        private System.Windows.Forms.Panel topbar;
        private System.Windows.Forms.Panel mainContainer;
        public Controls.CTopbar cTopbar;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.ListBox clientsListbox;
        private Controls.CVerticalSeparator cVerticalSeparator1;
        private Controls.CHorizontalSeparator cHorizontalSeparator1;
        private Controls.CVerticalSeparator cVerticalSeparator2;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Panel panel3;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.RichTextBox richText;
    }
}