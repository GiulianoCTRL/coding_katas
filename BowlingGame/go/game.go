package main

type game struct {
	rolls []int
}

func (g *game) roll(pins int) {
	g.rolls = append(g.rolls, pins)
}

func (g *game) score() int {
	score := 0
	index := 0
	for frame := 0; frame < 10; frame++ {
		if g.isStrike(index) {
			score += 10 + g.rolls[index+1] + g.rolls[index+2]
			index += 1
		} else if g.isSpare(index) {
			score += 10 + g.rolls[index+2]
			index += 2
		} else {
			score += g.rolls[index] + g.rolls[index+1]
			index += 2
		}
	}
	return score
}

func (g *game) isStrike(index int) bool {
	return g.rolls[index] == 10
}

func (g *game) isSpare(index int) bool {
	return g.rolls[index]+g.rolls[index+1] == 10
}
