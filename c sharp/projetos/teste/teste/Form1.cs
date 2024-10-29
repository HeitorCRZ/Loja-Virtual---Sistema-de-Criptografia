namespace teste
{
    public partial class Form1 : Form
    {
        int n = 0;
        int d = 0;
        double v = 0;
        double div = 0;
        public Form1()
        {
            InitializeComponent();
        }
        private void label2_Click(object sender, EventArgs e)
        {

        }
        private void label1_Click(object sender, EventArgs e)
        {
 
        }
        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            for (int i = 0; i <= n - 1; i++)
            {
                string linhas = textBox2.Lines[i].ToString();
                v = double.Parse(linhas);
                if (v >= 1 && v <= 1000000)
                {
                    div = v;
                    d = 0;
                    while (div >= 10)
                    {
                        div /= 10;
                        d += 1;
                    }
                    while (d >= 1)
                    {
                        div = 10;
                        for (int x = 1; x <= d - 1; x++)
                            div *= 10;
                        d -= 1;

                    }                    
                    textBox3.AppendText(div + Environment.NewLine);
                }
                else
                    textBox3.AppendText("Entrada invalida" + Environment.NewLine);
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            n = int.Parse(textBox1.Text);
        }
    }
}
