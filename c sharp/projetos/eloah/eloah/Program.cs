namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            int n =int.Parse(Console.ReadLine());
            float n1 = float.Parse(Console.ReadLine());
            float n2 = float.Parse(Console.ReadLine());
            float n3 = float.Parse(Console.ReadLine());
            float me = float.Parse(Console.ReadLine());
            float ma = 0;
            string maa = "";
            ma = (n1 + n2 * 2 + n3 * 3 + me) / 7;
            if (ma >= 90)
                maa = "A Aprovado";
            if (ma<90 && ma>=75)
                maa = "B Aprovado";
            if (ma<75 && ma>=60)
                maa = "C aprovado";
            if (ma < 60 && ma >= 40)
                maa = "D Reprovado";
            if (ma<40)
                maa = "E Reprovado";
            Console.WriteLine(n);
            Console.WriteLine(n1);
            Console.WriteLine(n2);
            Console.WriteLine(n3);
            Console.WriteLine(me);
            Console.WriteLine(ma);
            Console.WriteLine(maa);

        }  
    }
}