import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
  Scanner scanner = new Scanner(System.in);
  
    char[] caracteres = new char[10];
    
    System.out.println("Digite os 10 caracteres: ");
    for(int i = 0; i < 10; i++) {
      System.out.println("caractere " + (i + 1) + ": ");
      caracteres[i] = scanner.nextLine().charAt(0);
    }
    scanner.close();
    int contadorConsoantes = 0;
    System.out.println("\nConsoantes lidas: ");
    for(int i = 0; i < 10; i++) {
      char c = Character.toLowerCase(caracteres[i]);
      if ((c >= 'a' && c <= 'z') && c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
        contadorConsoantes++;
        System.out.println(caracteres[i]); }
    }
    System.out.println("\nTotal de consoantes lidas: " + contadorConsoantes);
  }
}