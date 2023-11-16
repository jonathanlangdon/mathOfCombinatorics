// How many integers x satisfy the inequalities 12 < sqrt(x) < 15, that is sqrt(x) exceeds 12, but sqrt(x) is less than 15?

function sqrtIntegersRange(startNum, endNum) {
  const startSquare = startNum ** 2
  const endSquare = endNum ** 2
  return endSquare - startSquare - 1
}

console.log(sqrtIntegersRange(1, 2)) // 2 (2 and 3)
console.log(sqrtIntegersRange(1, 3)) // 7 (2,3,4,5,6,7,8)
console.log(sqrtIntegersRange(12, 15)) // 80 (145 to 224)
