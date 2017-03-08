/*
A number chain is created by continuously adding the square of the digits in 
a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
*/

package main

import "fmt"
import "strconv"

func toInt(str string) int {
    i, _ := strconv.Atoi(str)
    return i
}

func square(val int) int {
    return val * val
}

func get_next(n int) int {
    str := strconv.Itoa(n)
    next := 0
    for _, r := range str {
        s := string(r)
        next += square(toInt(s))
    }
    return next
}

func updateSeen(flag bool, chain []int, seen map[int]bool) {
    for _, x:= range chain {
        seen[x] = flag
    }
}

func isChainArriveAt89(num int, seen map[int]bool, chain []int) bool {
    if flag, ok := seen[num]; ok { // is number was scanned already?
        updateSeen(flag, chain, seen)
        return flag != true
    }

    next := get_next(num)

    switch next {
    case 1:
        updateSeen(true, chain, seen)
        return false
    case 89:
        updateSeen(false, chain, seen)
        return true
    default:
        chain = append(chain, next)
        return isChainArriveAt89(next, seen, chain)
    }
}

func main() {
    seen := make(map[int]bool)
    counter := 0
	for i := (10000000); i > 0; i-- {
	    chain := []int{i}
    	if isChainArriveAt89(i, seen, chain) {
            counter += 1
        }
    }
    fmt.Println("Answer is:", counter)
}
