package KarateChop

import (
	"testing"
)

func TestValueNotInArrayIsMinus1(t *testing.T) {
	result := binarySearch(8, []int{1, 3, 5, 7})
	expected := -1

	if expected != result {
		t.Errorf("Item not at index %v but %v", expected, result)
	}
}

func TestValueAtIndex0(t *testing.T) {
	result := binarySearch(1, []int{1, 3, 5, 7})
	expected := 0

	if expected != result {
		t.Errorf("Item not at index %v but %v", expected, result)
	}
}

func TestValueAtIndex1(t *testing.T) {
	result := binarySearch(3, []int{1, 3, 5, 7})
	expected := 1

	if expected != result {
		t.Errorf("Item not at index %v but %v", expected, result)
	}
}

func TestValueAtIndex2(t *testing.T) {
	result := binarySearch(5, []int{1, 3, 5, 7})
	expected := 2

	if expected != result {
		t.Errorf("Item not at index %v but %v", expected, result)
	}
}

func TestValueAtIndex3(t *testing.T) {
	result := binarySearch(7, []int{1, 3, 5, 7})
	expected := 3

	if expected != result {
		t.Errorf("Item not at index %v but %v", expected, result)
	}
}
