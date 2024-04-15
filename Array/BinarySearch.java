import java.util.logging.Logger;

public class BinarySearch {

    static Logger logger = Logger.getLogger("");

    class Search {
        public static int binSearch(int[] hayStack, int needle) {
            int l = 0;
            int r = hayStack.length - 1;
            int m;
            while (l <= r) {
                m = (l + r) / 2;
                if (hayStack[m] == needle) {
                    return m;
                } else if (needle > hayStack[m]) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
            return -1;
        }
    }

    public static void main(String[] args) {
        logger.info(Boolean.toString(Search.binSearch(new int[] { 20, 25, 26, 33, 45, 56, 59 }, 7) == -1));
        logger.info(Boolean.toString(Search.binSearch(new int[] { 20, 25, 26, 33, 45, 56, 59 }, 20) == 0));
        logger.info(Boolean.toString(Search.binSearch(new int[] { 20, 25, 26, 33, 45, 56, 59 }, 59) == 6));
        logger.info(Boolean.toString(Search.binSearch(new int[] { 20, 25, 26, 33, 45, 56, 59 }, 45) == 4));
        logger.info(Boolean.toString(Search.binSearch(new int[] { 20, 25, 26, 33, 45, 56, 59 }, 100) == -1));
    }
}