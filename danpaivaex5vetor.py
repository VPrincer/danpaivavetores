import java.util.Scanner;

public class SeparadorParesImpares {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Array para os 20 números inteiros
        int[] numeros = new int[20];
        // Array para os números pares
        int[] pares = new int[20];
        // Array para os números ímpares
        int[] impares = new int[20];

  
        System.out.println("Digite 20 números inteiros:");

        // Loopzinho
        for (int i = 0; i < 20; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            numeros[i] = scanner.nextInt();
        }

        
        scanner.close();

        // Separarando números pares e ímpares
        int contadorPares = 0;
        int contadorImpares = 0;
        for (int i = 0; i < 20; i++) {
            if (numeros[i] % 2 == 0) {
                pares[contadorPares] = numeros[i];
                contadorPares++;
            } else {
                impares[contadorImpares] = numeros[i];
                contadorImpares++;
            }
        }

        // Imprimir nossos três vetores
        System.out.println("\nNúmeros inseridos:");
        for (int i = 0; i < 20; i++) {
            System.out.print(numeros[i] + " ");
        }

        System.out.println("\n\nNúmeros pares:");
        for (int i = 0; i < contadorPares; i++) {
            System.out.print(pares[i] + " ");
        }

        System.out.println("\n\nNúmeros ímpares:");
        for (int i = 0; i < contadorImpares; i++) {
            System.out.print(impares[i] + " ");
        }
    }
}