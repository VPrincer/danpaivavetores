import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int tamanho = 5;
      int [] vetor = new int[tamanho];

    System.out.println("Digite os 5 numeros inteiros: ");
    for (int i = 0; i < tamanho; i++) {
      System.out.println("Número " + (i + 1) + ": ");
      vetor[i] = scanner.nextInt();
    }
    System.out.println("os Números digitados são: ");
    for(int i = 0; i < tamanho; i++){
      System.out.println("Número " + (i + 1) + ": " + vetor[i]);
    }
    scanner.close();
  }
}