// Problem 1-11 A man has 47 cents in change coming.
// Assuming that the cash register contains an adequately large supply of 1, 5, 10 and 25 cent coins, with how many different combinations of coins can the clerk give the man his change?

function coinCombinations(cents) {
  let count = 0
  for (let i = 0; i <= cents; i += 25) {
    for (let j = 0; j <= cents; j += 10) {
      for (let k = 0; k <= cents; k += 5) {
        for (let m = 0; m <= cents; m += 1) {
          if (i + j + k + m === cents) {
            count += 1
          }
        }
      }
    }
  }
  return count
}

console.log(coinCombinations(47)) // 39
