package main

import (
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
    left, right := parse()

    partOne(left, right)

    partTwo(left, right)
        
}

func parse() ([]int, []int) {
    b, err := os.ReadFile("inputs/01_big")
    if err != nil {
        panic(err)
    }
    s := string(b)


    lines := strings.Split(s, "\n")

    left := make([]int, len(lines))
    right := make([]int, len(lines))

    for idx, line := range lines {
        if strings.TrimSpace(line) == "" {
            break
        }

        sp := strings.Fields(line)

        i, err := strconv.Atoi(sp[0])
        if err != nil {
            panic(err)
        }
        left[idx] = i

        i, err = strconv.Atoi(sp[1])
        if err != nil {
            panic(err)
        }
        right[idx] = i
    }

    sort.Ints(left)
    sort.Ints(right)

    return left, right
}

func partOne(left []int, right []int) {
    sum := 0
    for idx, l := range left {
        sum += int(math.Abs(float64(l - right[idx])))
    }

    fmt.Println(sum)
}

func partTwo(left []int, right []int) {
    counts := make(map[int]int)

    for _, r := range right {
        count, _ := counts[r]
        // if ok {
        counts[r] = count + 1
        // } else {
        //     counts[r] = 1
        // }
    }

    sum := 0
    for _, l := range left {
        count, ok := counts[l]
        if ok {
            sum += count * l
        }
    }

    fmt.Println(sum)
}
