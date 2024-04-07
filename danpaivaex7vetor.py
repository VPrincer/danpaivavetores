import java.util.Scanner;

public class OperacoesVetor {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] numeros = new int[5];


        System.out.println("Digite 5 números inteiros:");


        int soma = 0;
        int multiplicacao = 1;
        for (int i = 0; i < 5; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            numeros[i] = scanner.nextInt();
            soma += numeros[i];
            multiplicacao *= numeros[i];
        }
      
        scanner.close();

        System.out.println("\nNúmeros inseridos:");
        for (int i = 0; i < 5; i++) {
            System.out.print(numeros[i] + " ");
        }
       
        System.out.println("\n\nSoma dos números: " + soma);
        System.out.println("Multiplicação dos números: " + multiplicacao);
    }
}