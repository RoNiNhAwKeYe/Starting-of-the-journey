public class Main {
    public static void main(String[] args) {
      String[][] arr = {
          { "o", "x", "o", "x" },
          { "o", "o", "x", "x" },
          { "x", "o", "o", "x" },
          { "x", "x", "o", "x" },
          { "o", "x", "o", "o" }
      };
      String[][] ans = new String[5][5];
      mazePath(arr, 0, 0, ans);
    }
  
    private static void mazePath(String[][] maze, int row, int col, String[][] ans) {
      maze[row][col] = "x";
      ans[row][col] = "1";
  
      // base case
      int rowLength = maze.length - 1;
      int colLength = maze[0].length - 1;
      if (row < 0 || col < 0) {
        return;
      }
      if (row < rowLength || col < colLength || maze[row][col] == "x") {
        return;
      }
  
      // ans
      if (row == rowLength && col == colLength) {
        // ans mil gaya
        for (int i = 0; i < ans.length - 1; i++) {
          for (int j = 0; j < ans[0].length - 1; j++) {
            System.out.print(ans[i][j] + " ");
          }
          System.out.println();
        }
      }
  
      // down
      mazePath(maze, row + 1, col, ans);
      // right
      mazePath(maze, row, col + 1, ans);
      // up
      mazePath(maze, row - 1, col, ans);
      // left
      mazePath(maze, row, col - 1, ans);
      maze[row][col] = "o";
      ans[row][col] = "0";
    }
  }