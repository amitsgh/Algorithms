import java.util.*;

public class modifiedBinarySort {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.printf("Enter the Array length: ");
    byte listLength = scanner.nextByte();

    System.out.println("Enter the elements value: ");
    int[] list = new int[listLength];
    for (byte i = 0; i < listLength; i++) {
      list[i] = scanner.nextInt();
    }

    sorting(list);
    System.out.println("Sorted Elements are: " + Arrays.toString(list));
    scanner.close();
    return;
  }

  public static void sorting(int[] list){
    int n = list.length;
    boolean swapped;
    for (int i = 0; i < n; i++) {

      swapped = false;
      for (int j = 0; j < n - 1; j++) {
        if (list[j] > list[j + 1]) {
          int temp = list[j];
          list[j] = list[j + 1];
          list[j + 1] = temp;
          swapped = true;
        }
      }
      if (!swapped){
        break;
      }
    }
  }
}
