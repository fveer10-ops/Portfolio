import java.util.Scanner;
public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String answer;

        do{
            System.out.print("Please enter first number: ");
            double num1 = scanner.nextDouble();

            System.out.print("Please enter second number: ");
            double num2 = scanner.nextDouble();

            System.out.print("Please enter an operator; + - * or / : ");
            char operator = scanner.next().charAt(0);
            double result;

            switch(operator){
                case '+' -> { result = num1 + num2;
                    System.out.println("Result is: " +  result);
                    break;
                }
                case '-' -> { result = num1 - num2;
                    System.out.println("Result is: " + result);
                    break;
                }

                case '*'-> {
                    result = num1*num2;
                    System.out.println("Result is: " + result);
                    break;
                }
                case '/' -> {
                    result = num1 / num2;
                    System.out.println("Result is: " + result);
                    break;
                }
                default -> System.out.println("Please enter a valid operator");
            }
            System.out.print("Would you like to perform another calculation? Y/N: ");
            answer = scanner.next();
        }
        while(answer.equalsIgnoreCase("Y"));
        scanner.close();
        System.out.println("Goodbye!");

        }
}
