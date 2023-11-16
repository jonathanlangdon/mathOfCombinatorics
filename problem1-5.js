// The largest of r consecutive integers is k. What is the smallest?

function smallestFromLargest(kLargest, rIntegers) {
  return kLargest - rIntegers + 1
}

console.log(smallestFromLargest(307, 2)) // 306
console.log(smallestFromLargest(307, 123)) // 185
