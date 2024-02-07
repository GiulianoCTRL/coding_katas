use std::cmp::Ordering;

pub fn binary_search(num: usize, array: &[usize]) -> Option<usize> {
    let size = array.len();

    if size == 0 {
        return None;
    }

    if size == 1 {
        if array[0] == num {
            return Some(0);
        }
        return None;
    }

    let mut first_index = 0usize;
    let mut last_index = size - 1;
    let mut cursor = last_index / 2;
    let mut mid_element = array[cursor];

    loop {
        if first_index > last_index {
            return None;
        }

        match mid_element.cmp(&num) {
            Ordering::Equal => return Some(cursor),
            Ordering::Greater => {
                last_index = cursor - 1;
            },
            Ordering::Less => {
                first_index = cursor + 1;
            }
        }

        cursor = (first_index + last_index) / 2;
        mid_element = array[cursor];
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_0_length_array_returns_none() {
        let input: [usize; 4] = [1, 3, 5, 7];
        let result = binary_search(8, &input);
        let expected = None;

        assert_eq!(expected, result);
    }

    #[test]
    fn test_value_at_index_0() {
        let input: [usize; 4] = [1, 3, 5, 7];
        let result = binary_search(1, &input);
        let expected = Some(0usize);

        assert_eq!(expected, result);
    }

    #[test]
    fn test_value_at_index_1() {
        let input: [usize; 4] = [1, 3, 5, 7];
        let result = binary_search(3, &input);
        let expected = Some(1usize);

        assert_eq!(expected, result);
    }

    #[test]
    fn test_value_at_index_2() {
        let input: [usize; 4] = [1, 3, 5, 7];
        let result = binary_search(5, &input);
        let expected = Some(2usize);

        assert_eq!(expected, result);
    }

    #[test]
    fn test_value_at_index_3() {
        let input: [usize; 4] = [1, 3, 5, 7];
        let result = binary_search(7, &input);
        let expected = Some(3usize);

        assert_eq!(expected, result);
    }

    #[test]
    fn test_value_at_index_13() {
        let input: [usize; 15] = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29];
        let result = binary_search(27, &input);
        let expected = Some(13usize);

        assert_eq!(expected, result);
    }
}
