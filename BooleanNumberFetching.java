import java.util.Scanner;

public class Main {
  public static boolean search(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] == target) {
        return true;
      }
    }
    return false;
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int len = sc.nextInt();
    int[] arr = new int[len];
    int target = sc.nextInt();
    for (int i = 0; i < len; i++) {
      arr[i] = sc.nextInt();
    }
    System.out.println(search(arr, target));
  }

}
