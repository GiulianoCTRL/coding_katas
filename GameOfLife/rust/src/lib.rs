pub struct GameOfLife {
    board: Vec<Vec<usize>>,
}

impl GameOfLife {
    pub fn new(size: usize) -> Self {
        let board: Vec<Vec<usize>> = vec![vec![0; size]; size];
        GameOfLife { board }
    }
}

impl GameOfLife {
    fn should_cell_live(&self, y: usize, x: usize) -> bool {
        let neighbour_count = self.get_neighbour_count(y, x);
        if self.board[y][x] == 1 {
            if neighbour_count == 2 || neighbour_count == 3 {
                return true;
            }
            return false;
        }
        if neighbour_count == 3 {
            return true;
        }
        false
    }
}

impl GameOfLife {
    fn get_neighbour_count(&self, y: usize, x: usize) -> usize {
        let mut count: usize = 0;

        if self.is_neighbour_west_alive(y, x) {
            count += 1;
        }
        if self.is_neighbour_north_alive(y, x) {
            count += 1;
        }
        if self.is_neighbour_east_alive(y, x) {
            count += 1;
        }
        if self.is_neighbour_south_alive(y, x) {
            count += 1;
        }
        if self.is_neighbour_northwest_alive(y, x) {
            count += 1;
        }
        if self.is_neighbour_northeast_alive(y, x) {
            count += 1;
        }
        if self.is_neighbour_southeast_alive(y, x) {
            count += 1;
        }
        if self.is_neighbour_southwest_alive(y, x) {
            count += 1;
        }

        count
    }

    fn is_neighbour_west_alive(&self, y: usize, x: usize) -> bool {
        let neighbour_x = self.get_checked_index_lower_bound(x);
        self.board[y][neighbour_x] == 1
    }

    fn is_neighbour_north_alive(&self, y: usize, x: usize) -> bool {
        let neighbour_y = self.get_checked_index_lower_bound(y);
        self.board[neighbour_y][x] == 1
    }

    fn is_neighbour_east_alive(&self, y: usize, x: usize) -> bool {
        let neighbour_x = self.get_checked_index_upper_bound(x);
        self.board[y][neighbour_x] == 1
    }

    fn is_neighbour_south_alive(&self, y: usize, x: usize) -> bool {
        let neighbour_y = self.get_checked_index_upper_bound(y);
        self.board[neighbour_y][x] == 1
    }

    fn is_neighbour_northwest_alive(&self, y: usize, x: usize) -> bool {
        let neighbour_x = self.get_checked_index_lower_bound(x);
        let neighbour_y = self.get_checked_index_lower_bound(y);
        self.board[neighbour_y][neighbour_x] == 1
    }

    fn is_neighbour_northeast_alive(&self, y: usize, x: usize) -> bool {
        let neighbour_x = self.get_checked_index_upper_bound(x);
        let neighbour_y = self.get_checked_index_lower_bound(y);
        self.board[neighbour_y][neighbour_x] == 1
    }

    fn is_neighbour_southeast_alive(&self, y: usize, x: usize) -> bool {
        let neighbour_x = self.get_checked_index_upper_bound(x);
        let neighbour_y = self.get_checked_index_upper_bound(y);
        self.board[neighbour_y][neighbour_x] == 1
    }

    fn is_neighbour_southwest_alive(&self, y: usize, x: usize) -> bool {
        let neighbour_x = self.get_checked_index_lower_bound(x);
        let neighbour_y = self.get_checked_index_upper_bound(y);
        self.board[neighbour_y][neighbour_x] == 1
    }

    fn get_checked_index_lower_bound(&self, index: usize) -> usize {
        if index != 0 {
            return index - 1;
        }
        self.board.len() - 1
    }

    fn get_checked_index_upper_bound(&self, index: usize) -> usize {
        if index != self.board.len() - 1 {
            return index + 1;
        }
        0
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn board_game_dimensions_correct() {
        let game = GameOfLife::new(5usize);
        assert_eq!(game.board.len(), 5);
        assert_eq!(game.board[0].len(), 5);
    }

    #[test]
    fn lower_bound_index_checked_correctly() {
        let game = GameOfLife::new(5usize);
        assert_eq!(game.get_checked_index_lower_bound(0), 4);
    }

    #[test]
    fn lower_upper_index_checked_correctly() {
        let game = GameOfLife::new(5usize);
        assert_eq!(game.get_checked_index_upper_bound(4), 0);
    }

    #[test]
    fn neighbour_is_west() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][1] = 1;
        assert_eq!(game.is_neighbour_west_alive(2, 2), true);
    }

    #[test]
    fn neighbour_is_north() {
        let mut game = GameOfLife::new(5usize);
        game.board[1][2] = 1;
        assert_eq!(game.is_neighbour_north_alive(2, 2), true);
    }

    #[test]
    fn neighbour_is_east() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][3] = 1;
        assert_eq!(game.is_neighbour_east_alive(2, 2), true);
    }

    #[test]
    fn neighbour_is_south() {
        let mut game = GameOfLife::new(5usize);
        game.board[3][2] = 1;
        assert_eq!(game.is_neighbour_south_alive(2, 2), true);
    }

    #[test]
    fn neighbour_is_northwest() {
        let mut game = GameOfLife::new(5usize);
        game.board[1][1] = 1;
        assert_eq!(game.is_neighbour_northwest_alive(2, 2), true);
    }

    #[test]
    fn neighbour_is_northeast() {
        let mut game = GameOfLife::new(5usize);
        game.board[1][3] = 1;
        assert_eq!(game.is_neighbour_northeast_alive(2, 2), true);
    }

    #[test]
    fn neighbour_is_southeast() {
        let mut game = GameOfLife::new(5usize);
        game.board[3][3] = 1;
        assert_eq!(game.is_neighbour_southeast_alive(2, 2), true);
    }

    #[test]
    fn neighbour_is_southwest() {
        let mut game = GameOfLife::new(5usize);
        game.board[3][1] = 1;
        assert_eq!(game.is_neighbour_southwest_alive(2, 2), true);
    }

    #[test]
    fn neighbour_is_west_boundary() {
        let mut game = GameOfLife::new(5usize);
        game.board[0][4] = 1;
        assert_eq!(game.is_neighbour_west_alive(0, 0), true);
    }

    #[test]
    fn neighbour_is_north_boundary() {
        let mut game = GameOfLife::new(5usize);
        game.board[4][0] = 1;
        assert_eq!(game.is_neighbour_north_alive(0, 0), true);
    }

    #[test]
    fn neighbour_is_east_boundary() {
        let mut game = GameOfLife::new(5usize);
        game.board[4][0] = 1;
        assert_eq!(game.is_neighbour_east_alive(4, 4), true);
    }

    #[test]
    fn neighbour_is_south_boundary() {
        let mut game = GameOfLife::new(5usize);
        game.board[0][4] = 1;
        assert_eq!(game.is_neighbour_south_alive(4, 4), true);
    }

    #[test]
    fn neighbour_is_northwest_boundary() {
        let mut game = GameOfLife::new(5usize);
        game.board[4][4] = 1;
        assert_eq!(game.is_neighbour_northwest_alive(0, 0), true);
    }

    #[test]
    fn neighbour_is_northeast_boundary() {
        let mut game = GameOfLife::new(5usize);
        game.board[4][0] = 1;
        assert_eq!(game.is_neighbour_northeast_alive(0, 4), true);
    }

    #[test]
    fn neighbour_is_southeast_boundary() {
        let mut game = GameOfLife::new(5usize);
        game.board[0][0] = 1;
        assert_eq!(game.is_neighbour_southeast_alive(4, 4), true);
    }

    #[test]
    fn neighbour_is_southwest_boundary() {
        let mut game = GameOfLife::new(5usize);
        game.board[0][4] = 1;
        assert_eq!(game.is_neighbour_southwest_alive(4, 0), true);
    }

    #[test]
    fn zero_neighbours_counted_correctly() {
        let mut game = GameOfLife::new(5usize);
        assert_eq!(game.get_neighbour_count(2, 2), 0);
    }

    #[test]
    fn one_neighbour_counted_correctly() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][1] = 1;
        assert_eq!(game.get_neighbour_count(2, 2), 1);
    }

    #[test]
    fn two_neighbours_counted_correctly() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][1] = 1;
        game.board[2][3] = 1;
        assert_eq!(game.get_neighbour_count(2, 2), 2);
    }

    #[test]
    fn three_neighbours_counted_correctly() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][1] = 1;
        game.board[2][3] = 1;
        game.board[1][1] = 1;
        assert_eq!(game.get_neighbour_count(2, 2), 3);
    }

    #[test]
    fn four_neighbours_counted_correctly() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][1] = 1;
        game.board[2][3] = 1;
        game.board[1][1] = 1;
        game.board[1][2] = 1;
        assert_eq!(game.get_neighbour_count(2, 2), 4);
    }

    #[test]
    fn five_neighbours_counted_correctly() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][1] = 1;
        game.board[2][3] = 1;
        game.board[1][1] = 1;
        game.board[1][2] = 1;
        game.board[1][3] = 1;
        assert_eq!(game.get_neighbour_count(2, 2), 5);
    }

    #[test]
    fn six_neighbours_counted_correctly() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][1] = 1;
        game.board[2][3] = 1;
        game.board[1][1] = 1;
        game.board[1][2] = 1;
        game.board[1][3] = 1;
        game.board[3][1] = 1;
        assert_eq!(game.get_neighbour_count(2, 2), 6);
    }

    #[test]
    fn seven_neighbours_counted_correctly() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][1] = 1;
        game.board[2][3] = 1;
        game.board[1][1] = 1;
        game.board[1][2] = 1;
        game.board[1][3] = 1;
        game.board[3][1] = 1;
        game.board[3][2] = 1;
        assert_eq!(game.get_neighbour_count(2, 2), 7);
    }

    #[test]
    fn eight_neighbours_counted_correctly() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][1] = 1;
        game.board[2][3] = 1;
        game.board[1][1] = 1;
        game.board[1][2] = 1;
        game.board[1][3] = 1;
        game.board[3][1] = 1;
        game.board[3][2] = 1;
        game.board[3][3] = 1;
        assert_eq!(game.get_neighbour_count(2, 2), 8);
    }

    #[test]
    fn alive_cell_lives_with_two_neighbours() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][1] = 1;
        game.board[2][3] = 1;
        game.board[2][2] = 1;
        assert_eq!(game.should_cell_live(2, 2), true);
    }

    #[test]
    fn alive_cell_lives_with_three_neighbours() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][1] = 1;
        game.board[2][3] = 1;
        game.board[1][1] = 1;
        game.board[2][2] = 1;
        assert_eq!(game.should_cell_live(2, 2), true);
    }

    #[test]
    fn alive_cell_dies_with_four_neighbours() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][1] = 1;
        game.board[2][3] = 1;
        game.board[1][1] = 1;
        game.board[1][2] = 1;
        game.board[2][2] = 1;
        assert_eq!(game.should_cell_live(2, 2), false);
    }

    #[test]
    fn alive_cell_dies_with_one_neighbour() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][1] = 1;
        game.board[2][2] = 1;
        assert_eq!(game.should_cell_live(2, 2), false);
    }

    #[test]
    fn dead_cell_with_two_neighbours_stays_dead() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][1] = 1;
        game.board[2][3] = 1;
        assert_eq!(game.should_cell_live(2, 2), false);
    }

    #[test]
    fn dead_cell_with_three_neighbours_becomes_alive() {
        let mut game = GameOfLife::new(5usize);
        game.board[2][1] = 1;
        game.board[2][3] = 1;
        game.board[1][1] = 1;
        assert_eq!(game.should_cell_live(2, 2), true);
    }
}
