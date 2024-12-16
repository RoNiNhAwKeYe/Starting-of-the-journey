import java.util.ArrayList;
import java.util.List;

public class Main {
  static boolean val = false;

  public static void display(String[][] ans) {

    for (int i = 0; i < ans.length; i++) {
      for (int j = 0; j < ans[0].length; j++) {
        System.out.print(ans[i][j] + " ");
      }
      System.out.println();
    }
  }

  public static void mazePath(String[][] maze, int row, int col, String[][] ans, List<String[][]> result) {
    int rows = maze.length;
    int cols = maze[0].length;

    if (row < 0 || col < 0 || row >= rows || col >= cols || maze[row][col] == "x") {
      return;
    }

    if (row == rows - 1 && col == cols - 1) {
      // Copy the current ans to result
      String[][] path = new String[rows][cols];
      for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
          path[i][j] = ans[i][j];
        }
      }
      val = true;
      result.add(path);
      display(path);
      return;
    }

    maze[row][col] = "x";
    ans[row][col] = "1";

    mazePath(maze, row + 1, col, ans, result);
    mazePath(maze, row, col + 1, ans, result);
    mazePath(maze, row - 1, col, ans, result);
    mazePath(maze, row, col - 1, ans, result);

    maze[row][col] = "o";
    ans[row][col] = "0";
  }

  public static void main(String[] args) {
    String[][] maze = {
        { "o", "x", "o", "x" },
        { "o", "o", "x", "x" },
        { "x", "o", "o", "x" },
        { "x", "x", "o", "x" },
        { "o", "x", "o", "o" }
    };
    String[][] ans = new String[maze.length][maze[0].length];
    List<String[][]> result = new ArrayList<String[][]>();
    mazePath(maze, 0, 0, ans, result);
    if (!val) {
      System.out.println("No path found");
    }
  }
}