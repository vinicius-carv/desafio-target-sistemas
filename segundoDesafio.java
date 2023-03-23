/*
Autor: Vinícius ALves de Carvalho
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
 */
import java.util.*;
public class segundoDesafio {
    public static Boolean fibonacci(int num){
        // Primeiro número da sequencia
        int num1=0;
        int num2=1;
        List<Integer> sequencia = new ArrayList<Integer>();
        // Adicionando primeiro número da sequencia
        sequencia.add(num1);
        while(num1<num){
            num1+=num2;
            sequencia.add(num1);
        }
        boolean resultado = sequencia.contains(num);
        return resultado;
    }
    public static void main(String[] args){
        // Inicializando input do usuario
        Scanner usrInput = new Scanner(System.in);
        System.out.println("Digite o numero que deseja checar se faz ou nao parte da sequencia de Fibonacci: ");
        int input = usrInput.nextInt();
        // Chamando funcao
        if(fibonacci(input)){
            System.out.println("O numero "+input+" faz parte da sequencia de Fibonacci");
        }else{
            System.out.println("O numero "+input+" nao faz parte da sequencia de Fibonacci");
        }
        usrInput.close();
    }
}
