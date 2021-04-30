
namespace Real_estate_Picker_GUI.GUI.Controls
{
    partial class CVendorPage
    {
        /// <summary> 
        /// Wymagana zmienna projektanta.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary> 
        /// Wyczyść wszystkie używane zasoby.
        /// </summary>
        /// <param name="disposing">prawda, jeżeli zarządzane zasoby powinny zostać zlikwidowane; Fałsz w przeciwnym wypadku.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Kod wygenerowany przez Projektanta składników

        /// <summary> 
        /// Metoda wymagana do obsługi projektanta — nie należy modyfikować 
        /// jej zawartości w edytorze kodu.
        /// </summary>
        private void InitializeComponent()
        {
            this.linkOptionsContainer = new System.Windows.Forms.Panel();
            this.btnImport = new System.Windows.Forms.Button();
            this.lblAddLink = new System.Windows.Forms.Label();
            this.btnAdd = new System.Windows.Forms.Button();
            this.linkTxt = new Bunifu.Framework.UI.BunifuMetroTextbox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.openFileDialog = new System.Windows.Forms.OpenFileDialog();
            this.mainPanel = new System.Windows.Forms.Panel();
            this.linksListBox = new System.Windows.Forms.ListBox();
            this.emptyPanel = new System.Windows.Forms.Panel();
            this.panel2 = new System.Windows.Forms.Panel();
            this.pageFooter = new System.Windows.Forms.Panel();
            this.btnStop = new System.Windows.Forms.Button();
            this.btnStart = new System.Windows.Forms.Button();
            this.lblPageName = new System.Windows.Forms.Label();
            this.panel3 = new System.Windows.Forms.Panel();
            this.lblPage = new System.Windows.Forms.Label();
            this.cHorizontalSeparator1 = new Real_estate_Picker_GUI.GUI.Controls.CHorizontalSeparator();
            this.linkOptionsContainer.SuspendLayout();
            this.panel1.SuspendLayout();
            this.mainPanel.SuspendLayout();
            this.pageFooter.SuspendLayout();
            this.panel3.SuspendLayout();
            this.SuspendLayout();
            // 
            // linkOptionsContainer
            // 
            this.linkOptionsContainer.BackColor = System.Drawing.Color.White;
            this.linkOptionsContainer.Controls.Add(this.cHorizontalSeparator1);
            this.linkOptionsContainer.Controls.Add(this.btnImport);
            this.linkOptionsContainer.Controls.Add(this.lblAddLink);
            this.linkOptionsContainer.Controls.Add(this.btnAdd);
            this.linkOptionsContainer.Controls.Add(this.linkTxt);
            this.linkOptionsContainer.Dock = System.Windows.Forms.DockStyle.Fill;
            this.linkOptionsContainer.Location = new System.Drawing.Point(0, 0);
            this.linkOptionsContainer.Name = "linkOptionsContainer";
            this.linkOptionsContainer.Padding = new System.Windows.Forms.Padding(5);
            this.linkOptionsContainer.Size = new System.Drawing.Size(697, 104);
            this.linkOptionsContainer.TabIndex = 0;
            // 
            // btnImport
            // 
            this.btnImport.AutoSize = true;
            this.btnImport.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnImport.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(122)))), ((int)(((byte)(204)))));
            this.btnImport.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnImport.Font = new System.Drawing.Font("HelveticaNeueCyr", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.btnImport.Location = new System.Drawing.Point(568, 31);
            this.btnImport.Name = "btnImport";
            this.btnImport.Size = new System.Drawing.Size(79, 36);
            this.btnImport.TabIndex = 6;
            this.btnImport.Text = "btnImport";
            this.btnImport.UseVisualStyleBackColor = true;
            // 
            // lblAddLink
            // 
            this.lblAddLink.AutoSize = true;
            this.lblAddLink.Font = new System.Drawing.Font("HelveticaNeueCyr", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblAddLink.Location = new System.Drawing.Point(25, 13);
            this.lblAddLink.Name = "lblAddLink";
            this.lblAddLink.Size = new System.Drawing.Size(39, 14);
            this.lblAddLink.TabIndex = 1;
            this.lblAddLink.Text = "label1";
            // 
            // btnAdd
            // 
            this.btnAdd.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnAdd.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(210)))), ((int)(((byte)(149)))));
            this.btnAdd.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnAdd.Font = new System.Drawing.Font("HelveticaNeueCyr", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.btnAdd.Location = new System.Drawing.Point(483, 31);
            this.btnAdd.Name = "btnAdd";
            this.btnAdd.Size = new System.Drawing.Size(79, 36);
            this.btnAdd.TabIndex = 5;
            this.btnAdd.Text = "btnAdd";
            this.btnAdd.UseVisualStyleBackColor = true;
            // 
            // linkTxt
            // 
            this.linkTxt.BorderColorFocused = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(210)))), ((int)(((byte)(149)))));
            this.linkTxt.BorderColorIdle = System.Drawing.Color.FromArgb(((int)(((byte)(239)))), ((int)(((byte)(243)))), ((int)(((byte)(246)))));
            this.linkTxt.BorderColorMouseHover = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(210)))), ((int)(((byte)(149)))));
            this.linkTxt.BorderThickness = 2;
            this.linkTxt.Cursor = System.Windows.Forms.Cursors.IBeam;
            this.linkTxt.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.linkTxt.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.linkTxt.isPassword = false;
            this.linkTxt.Location = new System.Drawing.Point(28, 31);
            this.linkTxt.Margin = new System.Windows.Forms.Padding(4);
            this.linkTxt.Name = "linkTxt";
            this.linkTxt.Size = new System.Drawing.Size(448, 36);
            this.linkTxt.TabIndex = 4;
            this.linkTxt.TextAlign = System.Windows.Forms.HorizontalAlignment.Left;
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.linkOptionsContainer);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Top;
            this.panel1.Location = new System.Drawing.Point(0, 52);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(697, 104);
            this.panel1.TabIndex = 2;
            // 
            // mainPanel
            // 
            this.mainPanel.BackColor = System.Drawing.Color.White;
            this.mainPanel.Controls.Add(this.linksListBox);
            this.mainPanel.Controls.Add(this.emptyPanel);
            this.mainPanel.Controls.Add(this.panel2);
            this.mainPanel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.mainPanel.Location = new System.Drawing.Point(0, 156);
            this.mainPanel.Name = "mainPanel";
            this.mainPanel.Padding = new System.Windows.Forms.Padding(5);
            this.mainPanel.Size = new System.Drawing.Size(697, 482);
            this.mainPanel.TabIndex = 4;
            // 
            // linksListBox
            // 
            this.linksListBox.BackColor = System.Drawing.Color.White;
            this.linksListBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.linksListBox.Cursor = System.Windows.Forms.Cursors.Hand;
            this.linksListBox.Dock = System.Windows.Forms.DockStyle.Fill;
            this.linksListBox.Font = new System.Drawing.Font("HelveticaNeueCyr", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.linksListBox.ItemHeight = 12;
            this.linksListBox.Location = new System.Drawing.Point(33, 5);
            this.linksListBox.Margin = new System.Windows.Forms.Padding(10);
            this.linksListBox.Name = "linksListBox";
            this.linksListBox.ScrollAlwaysVisible = true;
            this.linksListBox.Size = new System.Drawing.Size(631, 472);
            this.linksListBox.TabIndex = 0;
            // 
            // emptyPanel
            // 
            this.emptyPanel.Dock = System.Windows.Forms.DockStyle.Left;
            this.emptyPanel.Location = new System.Drawing.Point(5, 5);
            this.emptyPanel.Name = "emptyPanel";
            this.emptyPanel.Size = new System.Drawing.Size(28, 472);
            this.emptyPanel.TabIndex = 2;
            // 
            // panel2
            // 
            this.panel2.Dock = System.Windows.Forms.DockStyle.Right;
            this.panel2.Location = new System.Drawing.Point(664, 5);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(28, 472);
            this.panel2.TabIndex = 3;
            // 
            // pageFooter
            // 
            this.pageFooter.Controls.Add(this.btnStop);
            this.pageFooter.Controls.Add(this.btnStart);
            this.pageFooter.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.pageFooter.Location = new System.Drawing.Point(0, 638);
            this.pageFooter.Name = "pageFooter";
            this.pageFooter.Size = new System.Drawing.Size(697, 103);
            this.pageFooter.TabIndex = 5;
            // 
            // btnStop
            // 
            this.btnStop.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(246)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
            this.btnStop.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnStop.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(246)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
            this.btnStop.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnStop.Font = new System.Drawing.Font("Helvetica Neue", 8.999999F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.btnStop.ForeColor = System.Drawing.Color.White;
            this.btnStop.Location = new System.Drawing.Point(483, 21);
            this.btnStop.Name = "btnStop";
            this.btnStop.Size = new System.Drawing.Size(79, 24);
            this.btnStop.TabIndex = 7;
            this.btnStop.Text = "btnStop";
            this.btnStop.UseVisualStyleBackColor = false;
            // 
            // btnStart
            // 
            this.btnStart.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(210)))), ((int)(((byte)(149)))));
            this.btnStart.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnStart.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(210)))), ((int)(((byte)(149)))));
            this.btnStart.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnStart.Font = new System.Drawing.Font("Helvetica Neue", 8.999999F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.btnStart.ForeColor = System.Drawing.Color.White;
            this.btnStart.Location = new System.Drawing.Point(568, 21);
            this.btnStart.Name = "btnStart";
            this.btnStart.Size = new System.Drawing.Size(79, 24);
            this.btnStart.TabIndex = 6;
            this.btnStart.Text = "btnStart";
            this.btnStart.UseVisualStyleBackColor = false;
            // 
            // lblPageName
            // 
            this.lblPageName.AutoSize = true;
            this.lblPageName.Font = new System.Drawing.Font("HelveticaNeueCyr", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblPageName.Location = new System.Drawing.Point(83, 13);
            this.lblPageName.Name = "lblPageName";
            this.lblPageName.Size = new System.Drawing.Size(64, 14);
            this.lblPageName.TabIndex = 8;
            this.lblPageName.Text = "pageName";
            // 
            // panel3
            // 
            this.panel3.BackColor = System.Drawing.Color.White;
            this.panel3.Controls.Add(this.lblPage);
            this.panel3.Controls.Add(this.lblPageName);
            this.panel3.Dock = System.Windows.Forms.DockStyle.Top;
            this.panel3.Location = new System.Drawing.Point(0, 0);
            this.panel3.Name = "panel3";
            this.panel3.Size = new System.Drawing.Size(697, 52);
            this.panel3.TabIndex = 6;
            // 
            // lblPage
            // 
            this.lblPage.AutoSize = true;
            this.lblPage.Font = new System.Drawing.Font("HelveticaNeueCyr", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblPage.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.lblPage.Location = new System.Drawing.Point(21, 13);
            this.lblPage.Name = "lblPage";
            this.lblPage.Size = new System.Drawing.Size(33, 14);
            this.lblPage.TabIndex = 9;
            this.lblPage.Text = "page";
            // 
            // cHorizontalSeparator1
            // 
            this.cHorizontalSeparator1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(245)))), ((int)(((byte)(247)))), ((int)(((byte)(247)))));
            this.cHorizontalSeparator1.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.cHorizontalSeparator1.Location = new System.Drawing.Point(5, 96);
            this.cHorizontalSeparator1.Name = "cHorizontalSeparator1";
            this.cHorizontalSeparator1.Size = new System.Drawing.Size(687, 3);
            this.cHorizontalSeparator1.TabIndex = 7;
            // 
            // CVendorPage
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.mainPanel);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.panel3);
            this.Controls.Add(this.pageFooter);
            this.Name = "CVendorPage";
            this.Size = new System.Drawing.Size(697, 741);
            this.linkOptionsContainer.ResumeLayout(false);
            this.linkOptionsContainer.PerformLayout();
            this.panel1.ResumeLayout(false);
            this.mainPanel.ResumeLayout(false);
            this.pageFooter.ResumeLayout(false);
            this.panel3.ResumeLayout(false);
            this.panel3.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel linkOptionsContainer;
        private Bunifu.Framework.UI.BunifuMetroTextbox linkTxt;
        private System.Windows.Forms.Label lblAddLink;
        private System.Windows.Forms.Button btnImport;
        private System.Windows.Forms.Button btnAdd;
        private System.Windows.Forms.Panel panel1;
        private CHorizontalSeparator cHorizontalSeparator1;
        private System.Windows.Forms.OpenFileDialog openFileDialog;
        private System.Windows.Forms.Panel mainPanel;
        private System.Windows.Forms.ListBox linksListBox;
        private System.Windows.Forms.Panel pageFooter;
        private System.Windows.Forms.Button btnStop;
        private System.Windows.Forms.Button btnStart;
        private System.Windows.Forms.Panel emptyPanel;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Label lblPageName;
        private System.Windows.Forms.Panel panel3;
        private System.Windows.Forms.Label lblPage;
    }
}
