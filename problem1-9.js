// Problem 1.9 How many integers between 1 and 2000...
// (a) are multiples of 11;
// (b) are multiples of 11 but not multiples of 3;
// (c) are multiples of 6 but not multiples of 4?

function multiplesWithWithout(withMultiple, without = 0) {
  const maxNum = 2000
  const numWith = Math.floor(maxNum / withMultiple)
  let numWithout = without
  if (without !== 0) {
    numWithout = Math.floor(maxNum / lcm(withMultiple, without))
  }
  return numWith - numWithout
}

function gcd(a, b) {
  return b === 0 ? a : gcd(b, a % b)
}

function lcm(a, b) {
  return Math.abs(a * b) / gcd(a, b)
}

console.log(multiplesWithWithout(11)) // 181
console.log(multiplesWithWithout(11, 3)) // 121
console.log(multiplesWithWithout(6, 4)) // 167
