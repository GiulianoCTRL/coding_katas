package main

import (
	"testing"
)

func rollMany(g *game, times int, pins int) {
	for i := 0; i < times; i++ {
		g.roll(pins)
	}
}

func TestPinsCorrectlyAddedToRolls(t *testing.T) {
	g := game{rolls: []int{}}

	g.roll(4)
	if g.rolls[0] != 4 {
		t.Errorf("%v does not equal 4.", g.rolls[0])
	}
}

func TestAll0GameHas0Score(t *testing.T) {
	g := game{rolls: []int{}}

	rollMany(&g, 20, 0)
	score := g.score()
	if score != 0 {
		t.Errorf("Game score: %v is not 0. Rolls: %v", score, g.rolls)
	}
}

func TestAllStrikeGameHas300Score(t *testing.T) {
	g := game{rolls: []int{}}

	rollMany(&g, 12, 10)
	score := g.score()
	if score != 300 {
		t.Errorf("Game score: %v is not 300. Rolls: %v", score, g.rolls)
	}
}

func TestAllOnesGameHas20Score(t *testing.T) {
	g := game{rolls: []int{}}

	rollMany(&g, 20, 1)
	score := g.score()
	if score != 20 {
		t.Errorf("Game score: %v is not 20. Rolls: %v", score, g.rolls)
	}
}

func TestOneSpareAnd5Has20Score(t *testing.T) {
	g := game{rolls: []int{}}
	g.roll(5)
	g.roll(5)
	g.roll(5)

	rollMany(&g, 17, 0)
	score := g.score()
	if score != 20 {
		t.Errorf("Game score: %v is not 20. Rolls: %v", score, g.rolls)
	}
}
