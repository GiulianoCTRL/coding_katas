package KarateChop

func binarySearch(num int, array []int) int {
	size := len(array)

	if size == 0 {
		return -1
	}

	if size == 1 {
		if array[0] == num {
			return 0
		}
		return -1
	}

	firstIndex := 0
	lastIndex := size - 1
	cursor := lastIndex / 2
	midElement := array[cursor]

	for {
		if firstIndex > lastIndex {
			return -1
		}

		if midElement == num {
			return cursor
		} else if midElement > num {
			lastIndex = cursor - 1
		} else {
			firstIndex = cursor + 1
		}

		cursor = (firstIndex + lastIndex) / 2
		midElement = array[cursor]
	}

}
