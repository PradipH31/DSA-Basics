import java.util.Arrays;
import java.util.logging.Logger;

public class QuickSort {
    static Logger logger = Logger.getLogger("");

    class Sort {
        public static void sort(int[] array) {
            quickSort(array, 0, array.length - 1);
        }

        public static void quickSort(int[] array, int l, int r) {
            if (l < r) {
                int pivot = part(array, l, r);
                quickSort(array, l, pivot - 1);
                quickSort(array, pivot + 1, r);
            }
        }

        public static int part(int[] array, int l, int r) {
            int pivot = array[r];
            int i = l - 1;
            int temp, j;
            for (j = l; j < r; j++) {
                if (array[j] < pivot) {
                    i++;
                    temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;
                }
            }
            temp = array[i + 1];
            array[i + 1] = array[r];
            array[r] = temp;
            return i + 1;
        }
    }

    public static void main(String[] args) {
        int[] unsorted = new int[] { 9, 1, 5, 43, 32, 22, 19, 90, 55, 66, 45, 88 };
        Sort.sort(unsorted);
        logger.info(Arrays.toString(unsorted));
    }
}
