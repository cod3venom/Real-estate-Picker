
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
            this.lblAddLink = new System.Windows.Forms.Label();
            this.bunifuMetroTextbox1 = new Bunifu.Framework.UI.BunifuMetroTextbox();
            this.btnImport = new System.Windows.Forms.Button();
            this.btnAdd = new System.Windows.Forms.Button();
            this.importedContainer = new System.Windows.Forms.Panel();
            this.linksListBox = new System.Windows.Forms.ListBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.linkOptionsContainer.SuspendLayout();
            this.importedContainer.SuspendLayout();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // linkOptionsContainer
            // 
            this.linkOptionsContainer.BackColor = System.Drawing.Color.White;
            this.linkOptionsContainer.Controls.Add(this.btnImport);
            this.linkOptionsContainer.Controls.Add(this.lblAddLink);
            this.linkOptionsContainer.Controls.Add(this.btnAdd);
            this.linkOptionsContainer.Controls.Add(this.bunifuMetroTextbox1);
            this.linkOptionsContainer.Dock = System.Windows.Forms.DockStyle.Fill;
            this.linkOptionsContainer.Location = new System.Drawing.Point(0, 0);
            this.linkOptionsContainer.Name = "linkOptionsContainer";
            this.linkOptionsContainer.Size = new System.Drawing.Size(775, 88);
            this.linkOptionsContainer.TabIndex = 0;
            // 
            // lblAddLink
            // 
            this.lblAddLink.AutoSize = true;
            this.lblAddLink.Font = new System.Drawing.Font("HelveticaNeueCyr", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblAddLink.Location = new System.Drawing.Point(34, 14);
            this.lblAddLink.Name = "lblAddLink";
            this.lblAddLink.Size = new System.Drawing.Size(39, 14);
            this.lblAddLink.TabIndex = 1;
            this.lblAddLink.Text = "label1";
            // 
            // bunifuMetroTextbox1
            // 
            this.bunifuMetroTextbox1.BorderColorFocused = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(210)))), ((int)(((byte)(149)))));
            this.bunifuMetroTextbox1.BorderColorIdle = System.Drawing.Color.FromArgb(((int)(((byte)(239)))), ((int)(((byte)(243)))), ((int)(((byte)(246)))));
            this.bunifuMetroTextbox1.BorderColorMouseHover = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(210)))), ((int)(((byte)(149)))));
            this.bunifuMetroTextbox1.BorderThickness = 2;
            this.bunifuMetroTextbox1.Cursor = System.Windows.Forms.Cursors.IBeam;
            this.bunifuMetroTextbox1.Font = new System.Drawing.Font("Century Gothic", 9.75F);
            this.bunifuMetroTextbox1.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.bunifuMetroTextbox1.isPassword = false;
            this.bunifuMetroTextbox1.Location = new System.Drawing.Point(37, 31);
            this.bunifuMetroTextbox1.Margin = new System.Windows.Forms.Padding(4);
            this.bunifuMetroTextbox1.Name = "bunifuMetroTextbox1";
            this.bunifuMetroTextbox1.Size = new System.Drawing.Size(498, 36);
            this.bunifuMetroTextbox1.TabIndex = 4;
            this.bunifuMetroTextbox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Left;
            // 
            // btnImport
            // 
            this.btnImport.AutoSize = true;
            this.btnImport.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnImport.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(122)))), ((int)(((byte)(204)))));
            this.btnImport.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnImport.Font = new System.Drawing.Font("HelveticaNeueCyr", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.btnImport.Location = new System.Drawing.Point(627, 31);
            this.btnImport.Name = "btnImport";
            this.btnImport.Size = new System.Drawing.Size(79, 36);
            this.btnImport.TabIndex = 6;
            this.btnImport.Text = "btnImport";
            this.btnImport.UseVisualStyleBackColor = true;
            // 
            // btnAdd
            // 
            this.btnAdd.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnAdd.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(210)))), ((int)(((byte)(149)))));
            this.btnAdd.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnAdd.Font = new System.Drawing.Font("HelveticaNeueCyr", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.btnAdd.Location = new System.Drawing.Point(542, 31);
            this.btnAdd.Name = "btnAdd";
            this.btnAdd.Size = new System.Drawing.Size(79, 36);
            this.btnAdd.TabIndex = 5;
            this.btnAdd.Text = "btnAdd";
            this.btnAdd.UseVisualStyleBackColor = true;
            // 
            // importedContainer
            // 
            this.importedContainer.Controls.Add(this.linksListBox);
            this.importedContainer.Location = new System.Drawing.Point(13, 162);
            this.importedContainer.Name = "importedContainer";
            this.importedContainer.Size = new System.Drawing.Size(725, 471);
            this.importedContainer.TabIndex = 1;
            // 
            // linksListBox
            // 
            this.linksListBox.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.linksListBox.Dock = System.Windows.Forms.DockStyle.Fill;
            this.linksListBox.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
            this.linksListBox.Font = new System.Drawing.Font("HelveticaNeueCyr", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.linksListBox.FormattingEnabled = true;
            this.linksListBox.Location = new System.Drawing.Point(0, 0);
            this.linksListBox.Name = "linksListBox";
            this.linksListBox.Size = new System.Drawing.Size(725, 471);
            this.linksListBox.TabIndex = 0;
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.linkOptionsContainer);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Top;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(775, 88);
            this.panel1.TabIndex = 2;
            // 
            // CVendorPage
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.importedContainer);
            this.Name = "CVendorPage";
            this.Size = new System.Drawing.Size(775, 652);
            this.linkOptionsContainer.ResumeLayout(false);
            this.linkOptionsContainer.PerformLayout();
            this.importedContainer.ResumeLayout(false);
            this.panel1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel linkOptionsContainer;
        private Bunifu.Framework.UI.BunifuMetroTextbox bunifuMetroTextbox1;
        private System.Windows.Forms.Label lblAddLink;
        private System.Windows.Forms.Button btnImport;
        private System.Windows.Forms.Button btnAdd;
        private System.Windows.Forms.Panel importedContainer;
        private System.Windows.Forms.ListBox linksListBox;
        private System.Windows.Forms.Panel panel1;
    }
}
