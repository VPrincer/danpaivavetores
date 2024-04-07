import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
  Scanner scanner = new Scanner(System.in);

    double[] notas = new double[4];

  System.out.println("Digite as 4 notas: ");

    for(int i = 0; i < 4; i++) {
      System.out.println("Nota " + (i + 1) + ": ");
      notas[i] = scanner.nextDouble();
    }
    scanner.close();

    double soma = 0;
    for(double nota : notas) {
      soma += nota;
    }
    double media = soma / notas.length;

    System.out.println("Notas inseridas: ");
    for(int i = 0; i < 4; i++) {
      System.out.println("Nota " + (i + 1) + ": " + notas[i]);
    }
    System.out.println("Média: " + media);
  }
}