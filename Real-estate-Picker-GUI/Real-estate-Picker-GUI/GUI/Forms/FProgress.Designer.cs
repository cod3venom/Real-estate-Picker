
namespace Real_estate_Picker_GUI.GUI.Forms
{
    partial class FProgress
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
            this.mainContainer = new System.Windows.Forms.Panel();
            this.topContainer = new System.Windows.Forms.Panel();
            this.cTable1 = new Real_estate_Picker_GUI.GUI.Controls.CTable();
            this.cTopbar = new Real_estate_Picker_GUI.GUI.Controls.CTopbar();
            this.mainContainer.SuspendLayout();
            this.topContainer.SuspendLayout();
            this.SuspendLayout();
            // 
            // mainContainer
            // 
            this.mainContainer.Controls.Add(this.cTable1);
            this.mainContainer.Dock = System.Windows.Forms.DockStyle.Fill;
            this.mainContainer.Location = new System.Drawing.Point(0, 44);
            this.mainContainer.Name = "mainContainer";
            this.mainContainer.Size = new System.Drawing.Size(457, 406);
            this.mainContainer.TabIndex = 0;
            // 
            // topContainer
            // 
            this.topContainer.Controls.Add(this.cTopbar);
            this.topContainer.Dock = System.Windows.Forms.DockStyle.Top;
            this.topContainer.Location = new System.Drawing.Point(0, 0);
            this.topContainer.Name = "topContainer";
            this.topContainer.Size = new System.Drawing.Size(457, 44);
            this.topContainer.TabIndex = 1;
            // 
            // cTable1
            // 
            this.cTable1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.cTable1.Location = new System.Drawing.Point(0, 0);
            this.cTable1.Name = "cTable1";
            this.cTable1.Size = new System.Drawing.Size(457, 406);
            this.cTable1.TabIndex = 0;
            // 
            // cTopbar
            // 
            this.cTopbar.Dock = System.Windows.Forms.DockStyle.Fill;
            this.cTopbar.Location = new System.Drawing.Point(0, 0);
            this.cTopbar.Name = "cTopbar";
            this.cTopbar.Size = new System.Drawing.Size(457, 44);
            this.cTopbar.TabIndex = 0;
            this.cTopbar.Title = "topBarTitle";
            // 
            // FProgress
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(457, 450);
            this.Controls.Add(this.mainContainer);
            this.Controls.Add(this.topContainer);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "FProgress";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "FProgress";
            this.mainContainer.ResumeLayout(false);
            this.topContainer.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel mainContainer;
        private System.Windows.Forms.Panel topContainer;
        private Controls.CTopbar cTopbar;
        private Controls.CTable cTable1;
    }
}