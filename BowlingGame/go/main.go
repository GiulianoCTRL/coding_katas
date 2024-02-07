package main

import "fmt"

func main() {
	g := game{rolls: []int{}}
	g.roll(4)
	fmt.Printf("%+v", g)
}
