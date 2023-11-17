// How many integers are there in the sequences
// (a) 60, 70, 80, • • ·, 540;
// (b) 15, 18, 21, • • ·, 144;
// (c) 17, 23, 29, 35, •··, 221?

function integersByInterval(startNum, endNum, interval) {
  return endNum / interval - startNum / interval + 1
}

console.log(integersByInterval(60, 540, 10)) // 49
console.log(integersByInterval(15, 144, 3)) // 44
console.log(integersByInterval(17, 221, 6)) // 35
