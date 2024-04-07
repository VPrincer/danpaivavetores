import java.util.Scanner;

public class Main{
  public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);

    int tamanho = 10;
    double[] vetor = new double[tamanho];

    System.out.println("Digite os numeros inteiros: ");
    for(int i = 0; i < tamanho; i++) {
      System.out.println("Numero " + (i + 1) + ": ");
      vetor[i] = scanner.nextDouble();
    }
    System.out.println("Os numeros digitados na ordem inversa são: ");
    for(int i = tamanho - 1; i >= 0; i--) {
    System.out.println("Numero " + (i + 1) + ": " + vetor[i]);
    }
  }
}