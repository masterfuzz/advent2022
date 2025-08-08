package day02

import "testing"

func TestPart1(t *testing.T) {
    ans := part1(parse("../inputs/02_small"))

    if ans != 2 {
        t.Fatal("answer should be 2")
    }

}

func TestPart2(t *testing.T) {
    ans := part2(parse("../inputs/02_small"))

    if ans != 4 {
        t.Fatalf("answer %v should be 4", ans)
    }

}

func TestSafe2(t *testing.T) {
    s2s := func(safe bool) string {
        if safe {
            return "SAFE"
        }
        return "UNSAFE"
    }
    
    tt := []struct{
        in []int
        safe bool
    }{
        {
            []int{7,6,4,2,1},
            true,
        },
        {
            []int{1, 2, 7, 8, 9},
            false,
        },
    }

    for _, test := range tt {
        if safe2(test.in) != test.safe {
            t.Fatalf("%v should be %v", test.in, s2s(test.safe))
        }
    }

}
