use std::env;

use rust::GameOfLife;

fn main() {
    let args: Vec<String> = env::args().collect();
    let size: usize = args[1].parse::<usize>().unwrap();
    let board_str: &str = &args[2];
    let iterations: usize = args[3].parse::<usize>().unwrap();
    let iter_time_ms: u64 = args[4].parse::<u64>().unwrap();
    let mut game = GameOfLife::from_string(size, board_str);
    game.game_loop(iterations, iter_time_ms);
}
