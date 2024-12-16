public class Main{
    public static void main(String[] args){
        int[] arr={11,12,13,20,5};
        int[] result=new int[arr.length];
        for(int i=0 ; i<arr.length ; i++){
            for(int j=i+1 ; j<arr.length-1 ; j++){
                if(arr[i]>arr[j]){
                    arr[j]=-1;
                }
                else if(arr[i]<arr[j]){
                  result[i]=arr[j];
                }
            }
        }
        for(int i=0 ; i<arr.length ; i++){
            System.out.println(result[i]);
        }
    }
}