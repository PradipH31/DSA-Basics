import java.util.Arrays;
import java.util.logging.Logger;

public class BubbleSort {
    static Logger logger = Logger.getLogger("");

    class Sort {
        public static void bubbleSort(int[] array) {
            int n = array.length;
            int i, j, temp;
            boolean swapped;
            for (i = 0; i < n; i++) {
                swapped = false;
                for (j = 0; j < n - 1 - i; j++) {
                    if (array[j] > array[j + 1]) {
                        temp = array[j];
                        array[j] = array[j + 1];
                        array[j + 1] = temp;
                        swapped = true;
                    }
                }
                if(swapped == false){
                    break;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] unsorted = new int[] { 9, 1, 5, 43, 32, 22, 19, 90, 55, 66, 45, 88 };
        Sort.bubbleSort(unsorted);
        logger.info(Arrays.toString(unsorted));
    }
}
