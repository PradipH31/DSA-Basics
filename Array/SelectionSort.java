import java.util.Arrays;
import java.util.logging.Logger;

public class SelectionSort {
    static Logger logger = Logger.getLogger("");

    class Sort {
        public static void selectionSort(int[] array) {
            int n = array.length;
            int i, j, min_index, temp;
            for (i = 0; i < n; i++) {
                min_index = i;
                for (j = i + 1; j < n; j++) {
                    if(array[j] < array[min_index]){
                        min_index = j;
                    }
                }
                temp = array[min_index];
                array[min_index] = array[i];
                array[i] = temp;
            }
        }
    }

    public static void main(String[] args) {
        int[] unsorted = new int[] { 9, 1, 5, 43, 32, 22, 19, 90, 55, 66, 45, 88 };
        Sort.selectionSort(unsorted);
        logger.info(Arrays.toString(unsorted));
    }
}
