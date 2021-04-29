
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
            this.topbar.SuspendLayout();
            this.SuspendLayout();
            // 
            // topbar
            // 
            this.topbar.Controls.Add(this.cTopbar);
            this.topbar.Dock = System.Windows.Forms.DockStyle.Top;
            this.topbar.Location = new System.Drawing.Point(0, 0);
            this.topbar.Name = "topbar";
            this.topbar.Size = new System.Drawing.Size(1115, 47);
            this.topbar.TabIndex = 0;
            // 
            // cTopbar
            // 
            this.cTopbar.Dock = System.Windows.Forms.DockStyle.Fill;
            this.cTopbar.Location = new System.Drawing.Point(0, 0);
            this.cTopbar.Name = "cTopbar";
            this.cTopbar.Size = new System.Drawing.Size(1115, 47);
            this.cTopbar.TabIndex = 0;
            this.cTopbar.Title = "Title";
            // 
            // mainContainer
            // 
            this.mainContainer.Dock = System.Windows.Forms.DockStyle.Fill;
            this.mainContainer.Location = new System.Drawing.Point(0, 47);
            this.mainContainer.Name = "mainContainer";
            this.mainContainer.Size = new System.Drawing.Size(1115, 605);
            this.mainContainer.TabIndex = 1;
            // 
            // Home
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1115, 652);
            this.Controls.Add(this.mainContainer);
            this.Controls.Add(this.topbar);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "Home";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Home";
            this.topbar.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion
        private System.Windows.Forms.Panel topbar;
        private System.Windows.Forms.Panel mainContainer;
        public Controls.CTopbar cTopbar;
    }
}