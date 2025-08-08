package main

import (
    "flag"
    "github.com/masterfuzz/advent2022/2024/day02"
)

var days = map[int]func(){
    2: day02.Run,
}

func main() {
    day := flag.Int("day", 0, "day")
    flag.Parse()

    if *day == 0 {
        panic("must specify a day")
    }

    run, ok := days[*day]

    if !ok {
        panic("not a day")
    }
    run()
}
