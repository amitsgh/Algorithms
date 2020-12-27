import java.util.*;

public class selectionSort {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.printf("Enter the Array length: ");
    byte listLength = scanner.nextByte();

    System.out.println("Enter the elements value: ");
    int[] list = new int[listLength];
    for(byte i=0; i<listLength; i++){
    list[i] = scanner.nextInt();
    }
    
    sorting(list);
    System.out.println("Sorted Elements are: " + Arrays.toString(list));
    scanner.close();
    return;
  }

  public static void sorting(int[] list){
    int n = list.length;
    int min_idx;
    for(int i=0; i<n-1; i++){
      min_idx = i;
      for(int j=i+1; j<n;j++){
        if (list[min_idx] > list[j]){
          min_idx = j;
        }
      }
      int temp = list[min_idx];
      list[min_idx] = list[i];
      list[i] = temp;
    }
  }
}
