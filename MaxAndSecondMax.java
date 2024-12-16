import java.util.Scanner;
import java.util.Arrays;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int len = sc.nextInt();
    int[] arr = new int[len];
    for (int i = 0; i < len; i++) {
      arr[i] = sc.nextInt();
    }
    int max = Integer.MIN_VALUE;
    for (int i = 0; i < len; i++) {
      if (arr[i] > max) {
        max = arr[i];
      }
    }
    Arrays.sort(arr);
    System.out.println("The Maximum Number is: " + max);
    System.out.println("Second Max Number is" + arr[arr.length - 2]);
  }
}