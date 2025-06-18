using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BubbleSort
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] lista = { 5, 3, 8, 4, 2, 6, 7, 34, 53, 213, 43, 654 };
            
            int n = lista.Length;

            for (int i = 0; i < lista.Length; i++){
                bool troca = false;
                for (int j = 0; j < (lista.Length - 1); j++){
                    if (lista[j] > lista[j + 1]){
                        int temp = lista[j];
                        lista[j] = lista[j + 1];
                        lista[j + 1] = temp;
                        troca = true;
                    }
                }

                if (!troca) break;
            }

            for (int a = 0; a < (lista.Length); a++)
               Console.WriteLine(lista[a]);
        }

        static void listaOrdenada(int[] lista, int size){
            int i;
            for (i = 0; i < size; i++){
                Console.Write(lista[i] + " ");
            }
        }
    }
}
