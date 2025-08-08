package day02

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func Run() {
    data := parse("inputs/02_big")
    fmt.Println(part1(data))
    fmt.Println(part2(data))
}

type Level = int
type Report = []Level

func parse(fname string) []Report {
    b, err := os.ReadFile(fname)
    if err != nil {
        panic(err)
    }
    s := string(b)

    lines := strings.Split(s, "\n")

    reports := make([]Report, len(lines)-1)

    for x, line := range lines {
        if strings.TrimSpace(line) == "" {
            break
        }

        sp := strings.Fields(line)
        levels := make([]Level, len(sp))

        for y, slevel := range sp {
            level, err := strconv.Atoi(slevel)
            if err != nil {
                panic(err)
            }
            levels[y] = level
        }

        reports[x] = levels

    }

    return reports
}

func i2s(inc bool) string {
    if inc {
        return "INCREASING"
    }
    return "DECREASING"
}

func safe(levels []Level) bool {
    increasing := levels[0] < levels[len(levels)-1]

    previous := levels[0]
    for _, level := range levels[1:] {
        if level == previous {
            fmt.Printf("%v == %v\n", previous, level)
            return false
        }
        if increasing != (previous < level) {
            fmt.Printf("%v, %v are %v but should be %v\n", previous, level, i2s(previous < level), i2s(increasing))
            return false
        }
        if math.Abs(float64(level - previous)) > 3 {
            fmt.Printf("|%v - %v| > 3\n", previous, level)
            return false
        }
        previous = level
    }
    return true
}

func safe2(levels []Level) bool {
    increasing := levels[0] < levels[len(levels)-1]
    tolerate := 0

    previous := levels[0]
    for _, level := range levels[1:] {
        if level == previous {
            fmt.Printf("%v == %v\n", previous, level)
            tolerate++
            if tolerate > 1 {
                return false
            }
            continue
        }
        if increasing != (previous < level) {
            fmt.Printf("%v, %v are %v but should be %v\n", previous, level, i2s(previous < level), i2s(increasing))
            tolerate++
            if tolerate > 1 {
                return false
            }
            continue
        }
        if math.Abs(float64(level - previous)) > 3 {
            fmt.Printf("|%v - %v| > 3\n", previous, level)
            tolerate++
            if tolerate > 1 {
                return false
            }
            continue
        }
        previous = level
    }
    return true
}

func part1(reports []Report) int {
    count := 0
    for _, report := range reports {
        if safe(report) {
            fmt.Printf("%v is SAFE\n", report)
            count++
            continue
        }
        fmt.Printf("%v is NOT SAFE\n", report)
    }
    return count
}

func part2(reports []Report) int {
    count := 0
    for _, report := range reports {
        if safe2(report) {
            fmt.Printf("%v is SAFE\n", report)
            count++
            continue
        }
        fmt.Printf("%v is NOT SAFE\n", report)
    }
    return count
}
