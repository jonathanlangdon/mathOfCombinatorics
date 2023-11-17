// Problem 1-14. The measure in degrees of an angle of a regular polygon is an integer.
// How many sides can such a polygon have?

function possibleSides() {
  let count = 0
  const angleList = []
  const maxDegrees = 360
  for (let i = 1; i <= maxDegrees; i++) {
    if (maxDegrees % i === 0) {
      count += 1
      angleList.push(i)
    }
  }
  console.log(
    `The number of polygons possible with integers as angles is ${count}`
  )
  return count, angleList
}

console.log(possibleSides()) // 24 polygons
