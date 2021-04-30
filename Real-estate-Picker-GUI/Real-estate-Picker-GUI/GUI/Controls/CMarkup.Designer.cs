
namespace Real_estate_Picker_GUI.GUI.Controls
{
    partial class CMarkup
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
            this.background = new System.Windows.Forms.Panel();
            this.pagesContainer = new System.Windows.Forms.Panel();
            this.leftBarContainer = new System.Windows.Forms.Panel();
            this.sidebar = new System.Windows.Forms.FlowLayoutPanel();
            this.background.SuspendLayout();
            this.leftBarContainer.SuspendLayout();
            this.SuspendLayout();
            // 
            // background
            // 
            this.background.BackColor = System.Drawing.Color.White;
            this.background.Controls.Add(this.pagesContainer);
            this.background.Controls.Add(this.leftBarContainer);
            this.background.Dock = System.Windows.Forms.DockStyle.Fill;
            this.background.Location = new System.Drawing.Point(0, 0);
            this.background.Name = "background";
            this.background.Size = new System.Drawing.Size(1197, 788);
            this.background.TabIndex = 0;
            // 
            // pagesContainer
            // 
            this.pagesContainer.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pagesContainer.Location = new System.Drawing.Point(181, 0);
            this.pagesContainer.Name = "pagesContainer";
            this.pagesContainer.Size = new System.Drawing.Size(1016, 788);
            this.pagesContainer.TabIndex = 6;
            // 
            // leftBarContainer
            // 
            this.leftBarContainer.Controls.Add(this.sidebar);
            this.leftBarContainer.Dock = System.Windows.Forms.DockStyle.Left;
            this.leftBarContainer.Location = new System.Drawing.Point(0, 0);
            this.leftBarContainer.Name = "leftBarContainer";
            this.leftBarContainer.Size = new System.Drawing.Size(181, 788);
            this.leftBarContainer.TabIndex = 5;
            // 
            // sidebar
            // 
            this.sidebar.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(239)))), ((int)(((byte)(243)))), ((int)(((byte)(246)))));
            this.sidebar.Dock = System.Windows.Forms.DockStyle.Fill;
            this.sidebar.Location = new System.Drawing.Point(0, 0);
            this.sidebar.Name = "sidebar";
            this.sidebar.Size = new System.Drawing.Size(181, 788);
            this.sidebar.TabIndex = 3;
            // 
            // CMarkup
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.background);
            this.Name = "CMarkup";
            this.Size = new System.Drawing.Size(1197, 788);
            this.background.ResumeLayout(false);
            this.leftBarContainer.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel background;
        private System.Windows.Forms.Panel leftBarContainer;
        private System.Windows.Forms.FlowLayoutPanel sidebar;
        private System.Windows.Forms.Panel pagesContainer;
    }
}
