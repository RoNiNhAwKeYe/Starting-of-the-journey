import java.util.Scanner;

public class printing2Darray {
  public static void main(String[] args) {
    int [][] arr2D = new int[2][2];
    int m = arr2D.length;
    int n = arr2D[0].length;
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the elements of the 2D");
    for(int i = 0; i < m; i++){
      for(int j = 0; j < n; j++){
        arr2D[i][j] = sc.nextInt();
      }
    }
    System.out.println("The 2D array is: ");
    for(int i = 0; i < m; i++){
      for(int j = 0; j < n; j++){
        System.out.print(arr2D[i][j] + " ");
      }
      System.out.println();
    }
  }
}