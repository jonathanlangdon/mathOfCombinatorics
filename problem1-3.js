//The largest of 123 consecutive integers is 307. What is the smallest?

function smallestFromLargest(largest, totalIntegers) {
  return largest - totalIntegers + 1
}

console.log(smallestFromLargest(307, 2)) // 306
console.log(smallestFromLargest(307, 123)) // 185
