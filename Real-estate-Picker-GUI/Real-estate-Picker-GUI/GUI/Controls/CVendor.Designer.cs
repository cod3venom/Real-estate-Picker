
namespace Real_estate_Picker_GUI.GUI.Controls
{
    partial class CVendor
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(CVendor));
            this.keyLabel = new System.Windows.Forms.Label();
            this.menuBtn = new Bunifu.Framework.UI.BunifuFlatButton();
            this.SuspendLayout();
            // 
            // keyLabel
            // 
            this.keyLabel.AutoSize = true;
            this.keyLabel.Location = new System.Drawing.Point(162, 25);
            this.keyLabel.Name = "keyLabel";
            this.keyLabel.Size = new System.Drawing.Size(35, 13);
            this.keyLabel.TabIndex = 1;
            this.keyLabel.Text = "label1";
            // 
            // menuBtn
            // 
            this.menuBtn.Activecolor = System.Drawing.Color.Transparent;
            this.menuBtn.BackColor = System.Drawing.Color.Transparent;
            this.menuBtn.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.menuBtn.BorderRadius = 0;
            this.menuBtn.ButtonText = "bunifuFlatButton1";
            this.menuBtn.Cursor = System.Windows.Forms.Cursors.Hand;
            this.menuBtn.DisabledColor = System.Drawing.Color.Gray;
            this.menuBtn.Iconcolor = System.Drawing.Color.Transparent;
            this.menuBtn.Iconimage = ((System.Drawing.Image)(resources.GetObject("menuBtn.Iconimage")));
            this.menuBtn.Iconimage_right = null;
            this.menuBtn.Iconimage_right_Selected = null;
            this.menuBtn.Iconimage_Selected = null;
            this.menuBtn.IconMarginLeft = 0;
            this.menuBtn.IconMarginRight = 0;
            this.menuBtn.IconRightVisible = true;
            this.menuBtn.IconRightZoom = 0D;
            this.menuBtn.IconVisible = true;
            this.menuBtn.IconZoom = 30D;
            this.menuBtn.IsTab = false;
            this.menuBtn.Location = new System.Drawing.Point(0, 0);
            this.menuBtn.Name = "menuBtn";
            this.menuBtn.Normalcolor = System.Drawing.Color.Transparent;
            this.menuBtn.OnHovercolor = System.Drawing.Color.Transparent;
            this.menuBtn.OnHoverTextColor = System.Drawing.Color.Black;
            this.menuBtn.Padding = new System.Windows.Forms.Padding(5);
            this.menuBtn.selected = false;
            this.menuBtn.Size = new System.Drawing.Size(211, 43);
            this.menuBtn.TabIndex = 0;
            this.menuBtn.Text = "bunifuFlatButton1";
            this.menuBtn.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.menuBtn.Textcolor = System.Drawing.Color.FromArgb(((int)(((byte)(5)))), ((int)(((byte)(5)))), ((int)(((byte)(5)))));
            this.menuBtn.TextFont = new System.Drawing.Font("HelveticaNeueCyr", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            // 
            // CVendor
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(245)))), ((int)(((byte)(247)))), ((int)(((byte)(247)))));
            this.Controls.Add(this.menuBtn);
            this.Controls.Add(this.keyLabel);
            this.Cursor = System.Windows.Forms.Cursors.Hand;
            this.Name = "CVendor";
            this.Size = new System.Drawing.Size(211, 43);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Label keyLabel;
        private Bunifu.Framework.UI.BunifuFlatButton menuBtn;
    }
}
