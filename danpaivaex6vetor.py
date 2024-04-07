import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        double[] medias = new double[10];

     
        for (int i = 0; i < 10; i++) {
            System.out.println("Aluno " + (i + 1));
            double somaNotas = 0;

     
            for (int j = 0; j < 4; j++) {
                System.out.print("Digite a nota " + (j + 1) + ": ");
                double nota = scanner.nextDouble();
                somaNotas += nota;
            }

           
            double media = somaNotas / 4;
            medias[i] = media;
        }

        
        scanner.close();

       
        int contadorAlunosAprovados = 0;
        for (double media : medias) {
            if (media >= 7.0) {
                contadorAlunosAprovados++;
            }
        }

    
        System.out.println("\nNúmero de alunos com média maior ou igual a 7.0: " + contadorAlunosAprovados);
    }
}