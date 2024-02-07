pub struct Game {
    rolls: Vec<usize>,
}

impl Game {
    pub fn new() -> Self {
        let rolls: Vec<usize> = Vec::new();
        Game { rolls }
    }

    pub fn roll(&mut self, pins: usize) {
        self.rolls.push(pins);
    }

    pub fn roll_many(&mut self, pins: usize, rolls: usize) {
        for _ in 0..rolls {
            self.roll(pins);
        }
    }

    pub fn score(&self) -> usize {
        let mut score: usize = 0;
        let mut index: usize = 0;

        for _frame in 0..10 {
            if self.is_strike(index) {
                score += 10 + self.rolls[index + 1] + self.rolls[index + 2];
                index += 1;
            } else if self.is_spare(index) {
                score += 10 + self.rolls[index + 2];
                index += 2;
            } else {
                score += self.rolls[index] + self.rolls[index + 1];
                index += 2;
            }
        }
        score
    }

    fn is_strike(&self, index: usize) -> bool {
        self.rolls[index] == 10
    }

    fn is_spare(&self, index: usize) -> bool {
        self.rolls[index] + self.rolls[index + 1] == 10
    }
}

impl Default for Game {
    fn default() -> Self {
        Game::new()
    }
}

pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_pins_appended_to_rolls() {
        let mut game = Game::new();
        game.roll(5);
        assert_eq!(game.rolls.last().unwrap(), &5usize);
    }

    #[test]
    fn test_all_zeros_is_0_score() {
        let mut game = Game::new();
        game.roll_many(0, 20);
        assert_eq!(0, game.score())
    }

    #[test]
    fn test_all_strikes_is_300_score() {
        let mut game = Game::new();
        game.roll_many(10, 12);
        assert_eq!(300, game.score())
    }

    #[test]
    fn test_all_ones_is_20_score() {
        let mut game = Game::new();
        game.roll_many(1, 20);
        assert_eq!(20, game.score())
    }

    #[test]
    fn test_role_one_spare_and_5_scores_20() {
        let mut game = Game::new();
        game.roll_many(5, 3);
        game.roll_many(0, 17);
        assert_eq!(20, game.score())
    }
}
