import java.util.Arrays;
import java.util.logging.Logger;

public class BubbleSort {
    static Logger logger = Logger.getLogger("");

    class Sort {
        public static void bubbleSort(int[] haystack) {
            int n = haystack.length;
            boolean swapped;
            int temp;
            for (int i = 0; i < n; i++) {
                swapped = false;
                for (int j = 0; j < n - i - 1; j++) {
                    if (haystack[j] > haystack[j + 1]) {
                        temp = haystack[j];
                        haystack[j] = haystack[j + 1];
                        haystack[j + 1] = temp;
                        swapped = true;
                    }
                }
                if (swapped = false) {
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
