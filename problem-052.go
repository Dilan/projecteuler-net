// It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
// but in a different order.
//
// Find the smallest positive integer, X such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

package main

import (
    "fmt"
    "strconv"
    "strings"
    "sort"
)

func SortString(w string) string {
    s := strings.Split(w, "")
    sort.Strings(s)
    return strings.Join(s, "")
}

func IsContainSameDigits(x, y int) bool {
    xStr := strconv.Itoa(x)
    yStr := strconv.Itoa(y)
    return len(xStr) == len(yStr) && SortString(xStr) == SortString(yStr)
}

func main() {
    for counter := 1; ; counter++ {
        flag := true
        for i := 6; i > 1; i-- {
            if IsContainSameDigits(counter, counter * i) == false {
                flag = false
                break
            }
        }
        if flag == true {
            fmt.Println("Answer is:", counter)
            break
        }
    }
}
