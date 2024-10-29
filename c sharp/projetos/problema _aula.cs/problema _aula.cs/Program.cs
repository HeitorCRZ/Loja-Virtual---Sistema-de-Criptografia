/* *******************************************************************
* Colégio Técnico Antônio Teixeira Fernandes (Univap)
* Curso Técnico em Informática - Data de Entrega:26/03/2024
* Autores do Projeto: Heitor Rodrigues Cruz
*                     	Thiago Cesar Carvalho
* Turma: 2ºH
* Proposta: Fazer um algoritmo que simule uma pesquisa envolvendo um grupo de pessoas. 
: 
* 
* problema _aula.cs

* ************************************************************/

using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            string continuar, nome, maiornome = "", menornome = "";
            int contador = 1, idade = 0, grau = 0, superior500 = 0, mais25 = 0, menos25 = 0;
            int grau1 = 0, grau2 = 0, grau3 = 0, maiorgrau = 0, menorgrau = 0, maioridade = 0, menoridade = 0, diferenca = 0;
            float salarioemdolar = 0, mediaidade2 = 0, salario = 0, dolar = 0, maiorsalario = 0, menorsalario = 0;
            double soma = 0, acrescimo = 0;

            do
            {
                Console.WriteLine("Digite o nome da " + contador + "º pessoa:");
                nome = Console.ReadLine();

                Console.WriteLine("Digite o valor do salario(dolar) da " + contador + "º pessoa:");
                salarioemdolar = float.Parse(Console.ReadLine());
                while (salarioemdolar < 0)
                {
                    Console.WriteLine("Resposta invalida!!!! Digite um salario valido:");
                    salarioemdolar = float.Parse(Console.ReadLine());
                }

                Console.WriteLine("Digite a idade da " + contador + "º pessoa:");
                idade = int.Parse(Console.ReadLine());
                while (idade < 0)
                {
                    Console.WriteLine("Resposta invalida!!!! Digite uma idade valida:");
                    idade = int.Parse(Console.ReadLine());
                }

                Console.WriteLine("Digite o valor da cotação do dolar:", contador);
                dolar = float.Parse(Console.ReadLine());
                if (dolar > 0)
                    salario = salarioemdolar * dolar;
                else
                    salario = salarioemdolar;

                Console.WriteLine("Digite grau de instrução da " + contador + "º pessoa:(1-Primário)(2-Segundo grau)(3-Superior)");
                grau = int.Parse(Console.ReadLine());
                while (grau < 1 || grau > 3)
                {
                    Console.WriteLine("Resposta invalida!!!! Digite um grau valido:");
                    grau = int.Parse(Console.ReadLine());
                }
                Console.WriteLine("---------------------------------------------------------------------------------------------------");

                switch (idade)
                {
                    case > 25:
                        mais25++;
                        break;
                    case < 25:
                        menos25++;
                        break;
                }

                switch (grau)
                {
                    case 1:
                        grau1++;
                        break;

                    case 2:
                        grau2++;
                        mediaidade2 += idade;
                        break;

                    case 3:
                        grau3++;
                        if (salario > 500)
                            superior500++;
                        break;

                }

                if (contador == 1)
                {
                    maiorsalario = salario;
                    maiorgrau = grau;
                    maioridade = idade;
                    maiornome = nome;
                    menorsalario = salario;
                    menorgrau = grau;
                    menoridade = idade;
                    menornome = nome;
                }
                if (maiorsalario < salario)
                {
                    maiorgrau = grau;
                    maioridade = idade;
                    maiornome = nome;
                    maiorsalario = salario;
                }
                if (menorsalario > salario)
                {
                    menorsalario = salario;
                    menorgrau = grau;
                    menoridade = idade;
                    menornome = nome;
                }

                Console.WriteLine("Gostaria de adicionar mais uma pessoa?(S/N)");
                continuar = Console.ReadLine();
                while (continuar != "S" && continuar != "N")
                {
                    Console.WriteLine("Resposta invalida!!!!:(S/N)");
                    continuar = Console.ReadLine();
                }
                contador += 1;
                soma += salario;
                Console.WriteLine("---------------------------------------------------------------------------------------------------");
            } while (continuar == "S");


            Console.WriteLine("Pessoa que tem curso superior e ganham mais que 500R$:" + superior500);
            Console.WriteLine();

            diferenca = mais25 - menos25;
            if (diferenca < 0)
                diferenca = diferenca * (-1);
            Console.WriteLine("A diferença entre a quantidade de pessoas com mais de 25 anos menos de 25 anos:" + diferenca);
            Console.WriteLine();
            if (grau2 > 0)
            {
                mediaidade2 = mediaidade2 / grau2;
                string media = mediaidade2.ToString("0.00");
                Console.WriteLine("A idade média das pessoas que possuem 2o grau:" + media);
                Console.WriteLine();
            }
            else
            {
                Console.WriteLine("A idade média das pessoas que possuem 2o grau: Não possuem pessoas com 2o grau");
                Console.WriteLine();
            }


            Console.WriteLine("A porcentagem de pessoas que possuem 1o grau:" + grau1 * 100 / (contador - 1) + "%");
            Console.WriteLine();
            Console.WriteLine("A porcentagem de pessoas que possuem 3o grau:" + grau3 * 100 / (contador - 1) + "%");
            Console.WriteLine("---------------------------------------------------------------------------------------------------");

            Console.WriteLine("PESSOA COM MAIOR SALARIO");
            string maior = maiorsalario.ToString("0.00");
            Console.WriteLine("SALARIO:" + maior + "R$");
            Console.WriteLine("GRAU:" + maiorgrau);
            Console.WriteLine("IDADE:" + maioridade);
            Console.WriteLine("NOME:" + maiornome);
            Console.WriteLine("---------------------------------------------------------------------------------------------------");

            Console.WriteLine("PESSOA COM MENOR SALARIO");
            string menor = menorsalario.ToString("0.00");
            Console.WriteLine("SALARIO:" + menor + "R$");
            Console.WriteLine("GRAU:" + menorgrau);
            Console.WriteLine("IDADE:" + menoridade);
            Console.WriteLine("NOME:" + menornome);
            Console.WriteLine("---------------------------------------------------------------------------------------------------");

            acrescimo = soma;
            string somatorio = soma.ToString("0.00");
            Console.WriteLine("somatorio dos salarios sem acrescimos:" + somatorio + "R$");

            switch (soma)
            {
                case > 50000:
                    soma = soma + (soma * 0.2 );
                    soma = soma + (soma * 0.1);
                    soma = soma + (soma * 0.05);
                    soma = soma + (soma * 0.03);
                    break;

                case > 45000:
                    soma = soma + (soma * 0.2);
                    soma = soma + (soma * 0.1);
                    soma = soma + (soma * 0.05);
                    break;

                case > 35000:
                    soma = soma + (soma * 0.2);
                    soma = soma + (soma * 0.1); 
                    break;

                case > 20000:
                    soma = soma + (soma * 0.2);
                    break;
            }


            somatorio = soma.ToString("0.00");
            if (soma == acrescimo)
            {
                Console.WriteLine("somatorio dos salarios com acrescimos: Não tem acrescimo");
                Console.WriteLine("---------------------------------------------------------------------------------------------------");
            }
            else
            {
                Console.WriteLine("somatorio dos salarios com acrescimos:" + somatorio + "R$");
                Console.WriteLine("---------------------------------------------------------------------------------------------------");
            }


            Console.Write("FIM DO PROGRAMA");
            Console.Read();
        }
    }
}
