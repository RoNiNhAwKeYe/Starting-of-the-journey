import java.util.Stack;
class StackExample {
  public static void main(String[] args){
    int nums[] = {11,12,13,20,5};
    int[] result = findGreaterNumbers(nums, 15); 
  }
    public static int[] findGreaterNumbers(int[] nums, int target) {
        Stack<Integer> stack = new Stack<Integer>();
        int[] result = new int[nums.length];
        for (int i = nums.length - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= target) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                result[i] = stack.peek();
            } else {
                result[i] = -1;
            }
            stack.push(nums[i]);
        }
        return result;
    }
}