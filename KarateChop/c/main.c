#include <assert.h>
#include <stdbool.h>

int binarySearch(int num, int* array, int array_size);
void testBinarySearchHasExpectedResult(int num, int expected);


int main() {
    testBinarySearchHasExpectedResult(8, -1);
    testBinarySearchHasExpectedResult(1, 0);
    testBinarySearchHasExpectedResult(3, 1);
    testBinarySearchHasExpectedResult(5, 2);
    testBinarySearchHasExpectedResult(7, 3);
}


int binarySearch(int num, int* array, int array_size) {
    if (array_size == 0) {
        return -1;
    }

    if (array_size == 1) {
        if (array[0] == num) {
            return 0;
        }
        return -1;
    }

    int firstIndex = 0;
    int lastIndex = array_size - 1;
    int cursor = lastIndex / 2;
    int midElement = array[cursor];

    while (true) {
        if (firstIndex > lastIndex) {
            return -1;
        }

        if (midElement == num) {
            return cursor;
        } else if (midElement > num) {
            lastIndex = cursor -1;
        } else {
            firstIndex = cursor + 1;
        }

        cursor = (firstIndex + lastIndex) / 2;
        midElement = array[cursor];
    } 


}

void testBinarySearchHasExpectedResult(int num, int expected) {
    int array[4] = {1, 3, 5, 7};
    int array_size = 4;

    int result = binarySearch(num, array, array_size);
    assert(result == expected);

}
