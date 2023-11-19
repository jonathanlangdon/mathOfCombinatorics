// Problem 1.9 How many integers between 1 and 2000... using a loop
// (a) are multiples of 11;
// (b) are multiples of 11 but not multiples of 3;
// (c) are multiples of 6 but not multiples of 4?

function multiplesWithWithout(withMultiple, without = 0) {
  const maxNum = 2000
  let count = 0
  for (let i = 1; i <= 2000; i++) {
    if (without === 0) {
      if (i % withMultiple === 0) {
        count += 1
      }
    } else {
      if (i % withMultiple === 0 && i % without !== 0) {
        count += 1
      }
    }
  }
  return count
}

console.log(multiplesWithWithout(11)) // 181
console.log(multiplesWithWithout(11, 3)) // 121
console.log(multiplesWithWithout(6, 4)) // 167
