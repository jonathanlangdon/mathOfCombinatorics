// How many integers are there in the sequence n, n + 1, n + 2, • • • n + h ?

function numberOfIntegers(nStart, hEnd) {
  return hEnd - nStart + 1
}

console.log(numberOfIntegers(4, 8)) // 5
