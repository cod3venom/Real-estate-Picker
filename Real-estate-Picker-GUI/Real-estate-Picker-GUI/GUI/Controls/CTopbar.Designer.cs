
namespace Real_estate_Picker_GUI.GUI.Controls
{
    partial class CTopbar
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
            this.components = new System.ComponentModel.Container();
            this.title = new System.Windows.Forms.Label();
            this.dragTitle = new Bunifu.Framework.UI.BunifuDragControl(this.components);
            this.dragControls = new Bunifu.Framework.UI.BunifuDragControl(this.components);
            this.minimizeBtn = new Bunifu.Framework.UI.BunifuImageButton();
            this.closeBtn = new Bunifu.Framework.UI.BunifuImageButton();
            this.panel3 = new System.Windows.Forms.Panel();
            this.cHorizontalSeparator1 = new Real_estate_Picker_GUI.GUI.Controls.CHorizontalSeparator();
            ((System.ComponentModel.ISupportInitialize)(this.minimizeBtn)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.closeBtn)).BeginInit();
            this.panel3.SuspendLayout();
            this.SuspendLayout();
            // 
            // title
            // 
            this.title.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(210)))), ((int)(((byte)(149)))));
            this.title.Cursor = System.Windows.Forms.Cursors.Hand;
            this.title.Dock = System.Windows.Forms.DockStyle.Fill;
            this.title.Font = new System.Drawing.Font("HelveticaNeueCyr", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.title.ForeColor = System.Drawing.Color.White;
            this.title.Location = new System.Drawing.Point(0, 0);
            this.title.Name = "title";
            this.title.Size = new System.Drawing.Size(798, 44);
            this.title.TabIndex = 0;
            this.title.Text = "topBarTitle";
            this.title.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // dragTitle
            // 
            this.dragTitle.Fixed = true;
            this.dragTitle.Horizontal = true;
            this.dragTitle.TargetControl = this.title;
            this.dragTitle.Vertical = true;
            // 
            // dragControls
            // 
            this.dragControls.Fixed = true;
            this.dragControls.Horizontal = true;
            this.dragControls.TargetControl = null;
            this.dragControls.Vertical = true;
            // 
            // minimizeBtn
            // 
            this.minimizeBtn.Anchor = System.Windows.Forms.AnchorStyles.Right;
            this.minimizeBtn.BackColor = System.Drawing.Color.Transparent;
            this.minimizeBtn.Cursor = System.Windows.Forms.Cursors.Hand;
            this.minimizeBtn.Image = global::Real_estate_Picker_GUI.Properties.Resources.minimizeButton;
            this.minimizeBtn.ImageActive = null;
            this.minimizeBtn.Location = new System.Drawing.Point(726, 16);
            this.minimizeBtn.Name = "minimizeBtn";
            this.minimizeBtn.Size = new System.Drawing.Size(15, 15);
            this.minimizeBtn.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.minimizeBtn.TabIndex = 1;
            this.minimizeBtn.TabStop = false;
            this.minimizeBtn.Zoom = 10;
            // 
            // closeBtn
            // 
            this.closeBtn.Anchor = System.Windows.Forms.AnchorStyles.Right;
            this.closeBtn.BackColor = System.Drawing.Color.Transparent;
            this.closeBtn.Cursor = System.Windows.Forms.Cursors.Hand;
            this.closeBtn.Image = global::Real_estate_Picker_GUI.Properties.Resources.closeButton;
            this.closeBtn.ImageActive = null;
            this.closeBtn.Location = new System.Drawing.Point(764, 16);
            this.closeBtn.Name = "closeBtn";
            this.closeBtn.Size = new System.Drawing.Size(15, 15);
            this.closeBtn.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.closeBtn.TabIndex = 0;
            this.closeBtn.TabStop = false;
            this.closeBtn.Zoom = 10;
            // 
            // panel3
            // 
            this.panel3.Controls.Add(this.minimizeBtn);
            this.panel3.Controls.Add(this.closeBtn);
            this.panel3.Controls.Add(this.cHorizontalSeparator1);
            this.panel3.Controls.Add(this.title);
            this.panel3.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panel3.Location = new System.Drawing.Point(0, 0);
            this.panel3.Name = "panel3";
            this.panel3.Size = new System.Drawing.Size(798, 44);
            this.panel3.TabIndex = 2;
            // 
            // cHorizontalSeparator1
            // 
            this.cHorizontalSeparator1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(245)))), ((int)(((byte)(247)))), ((int)(((byte)(247)))));
            this.cHorizontalSeparator1.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.cHorizontalSeparator1.Location = new System.Drawing.Point(0, 41);
            this.cHorizontalSeparator1.Name = "cHorizontalSeparator1";
            this.cHorizontalSeparator1.Size = new System.Drawing.Size(798, 3);
            this.cHorizontalSeparator1.TabIndex = 0;
            // 
            // CTopbar
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.panel3);
            this.Name = "CTopbar";
            this.Size = new System.Drawing.Size(798, 44);
            ((System.ComponentModel.ISupportInitialize)(this.minimizeBtn)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.closeBtn)).EndInit();
            this.panel3.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion
        private Bunifu.Framework.UI.BunifuImageButton closeBtn;
        private Bunifu.Framework.UI.BunifuImageButton minimizeBtn;
        private System.Windows.Forms.Label title;
        private Bunifu.Framework.UI.BunifuDragControl dragTitle;
        private Bunifu.Framework.UI.BunifuDragControl dragControls;
        private System.Windows.Forms.Panel panel3;
        private CHorizontalSeparator cHorizontalSeparator1;
    }
}
