// The smallest of r consecutive integers is n. What is the largest?

function largestFromSmallest(smallest, rIntegers) {
  return smallest + rIntegers - 1
}

console.log(largestFromSmallest(3, 4)) // 6
