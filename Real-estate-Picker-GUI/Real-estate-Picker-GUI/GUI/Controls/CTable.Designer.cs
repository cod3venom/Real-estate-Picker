
namespace Real_estate_Picker_GUI.GUI.Controls
{
    partial class CTable
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
            this.table = new System.Windows.Forms.DataGridView();
            this.idColumn = new System.Windows.Forms.DataGridViewLinkColumn();
            this.folderColumn = new System.Windows.Forms.DataGridViewLinkColumn();
            this.footerContainer = new System.Windows.Forms.Panel();
            this.totalRecordsTitleLabel = new System.Windows.Forms.Label();
            this.totalRecordsAmountLabel = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.table)).BeginInit();
            this.footerContainer.SuspendLayout();
            this.SuspendLayout();
            // 
            // table
            // 
            this.table.AllowUserToAddRows = false;
            this.table.AllowUserToDeleteRows = false;
            this.table.BackgroundColor = System.Drawing.Color.White;
            this.table.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.table.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.idColumn,
            this.folderColumn});
            this.table.Dock = System.Windows.Forms.DockStyle.Fill;
            this.table.GridColor = System.Drawing.Color.White;
            this.table.Location = new System.Drawing.Point(0, 0);
            this.table.Name = "table";
            this.table.ReadOnly = true;
            this.table.Size = new System.Drawing.Size(618, 420);
            this.table.TabIndex = 0;
            // 
            // idColumn
            // 
            this.idColumn.ActiveLinkColor = System.Drawing.Color.Black;
            this.idColumn.HeaderText = "ID";
            this.idColumn.Name = "idColumn";
            this.idColumn.ReadOnly = true;
            this.idColumn.VisitedLinkColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(18)))), ((int)(((byte)(25)))));
            this.idColumn.Width = 60;
            // 
            // folderColumn
            // 
            this.folderColumn.ActiveLinkColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(18)))), ((int)(((byte)(25)))));
            this.folderColumn.HeaderText = "Folder";
            this.folderColumn.LinkBehavior = System.Windows.Forms.LinkBehavior.NeverUnderline;
            this.folderColumn.LinkColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(18)))), ((int)(((byte)(25)))));
            this.folderColumn.Name = "folderColumn";
            this.folderColumn.ReadOnly = true;
            this.folderColumn.VisitedLinkColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(18)))), ((int)(((byte)(25)))));
            this.folderColumn.Width = 500;
            // 
            // footerContainer
            // 
            this.footerContainer.Controls.Add(this.totalRecordsAmountLabel);
            this.footerContainer.Controls.Add(this.totalRecordsTitleLabel);
            this.footerContainer.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.footerContainer.Location = new System.Drawing.Point(0, 420);
            this.footerContainer.Name = "footerContainer";
            this.footerContainer.Size = new System.Drawing.Size(618, 32);
            this.footerContainer.TabIndex = 1;
            // 
            // totalRecordsTitleLabel
            // 
            this.totalRecordsTitleLabel.AutoSize = true;
            this.totalRecordsTitleLabel.Font = new System.Drawing.Font("Helvetica Neue", 8.999999F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.totalRecordsTitleLabel.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(210)))), ((int)(((byte)(149)))));
            this.totalRecordsTitleLabel.Location = new System.Drawing.Point(5, 7);
            this.totalRecordsTitleLabel.Name = "totalRecordsTitleLabel";
            this.totalRecordsTitleLabel.Size = new System.Drawing.Size(86, 15);
            this.totalRecordsTitleLabel.TabIndex = 0;
            this.totalRecordsTitleLabel.Text = "Ilość rekordów: ";
            // 
            // totalRecordsAmountLabel
            // 
            this.totalRecordsAmountLabel.AutoSize = true;
            this.totalRecordsAmountLabel.Font = new System.Drawing.Font("Helvetica Neue", 8.999999F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.totalRecordsAmountLabel.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(210)))), ((int)(((byte)(149)))));
            this.totalRecordsAmountLabel.Location = new System.Drawing.Point(88, 7);
            this.totalRecordsAmountLabel.Name = "totalRecordsAmountLabel";
            this.totalRecordsAmountLabel.Size = new System.Drawing.Size(0, 15);
            this.totalRecordsAmountLabel.TabIndex = 1;
            // 
            // CTable
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.table);
            this.Controls.Add(this.footerContainer);
            this.Name = "CTable";
            this.Size = new System.Drawing.Size(618, 452);
            ((System.ComponentModel.ISupportInitialize)(this.table)).EndInit();
            this.footerContainer.ResumeLayout(false);
            this.footerContainer.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataGridView table;
        private System.Windows.Forms.DataGridViewLinkColumn idColumn;
        private System.Windows.Forms.DataGridViewLinkColumn folderColumn;
        private System.Windows.Forms.Panel footerContainer;
        private System.Windows.Forms.Label totalRecordsTitleLabel;
        private System.Windows.Forms.Label totalRecordsAmountLabel;
    }
}
