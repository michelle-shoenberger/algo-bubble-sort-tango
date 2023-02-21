exports.bubbleSort = function (sequence) {
  let previous_swaps = 0;
  let iter = 0;
  let sorted = false;
  let swaps = 0
  while (sorted == false) {
    for (let i=0; i<sequence.length; i++) {
      if (i<sequence.length-1 && sequence[i+1] < sequence[i]) {
        let elem = sequence[i];
        sequence[i] = sequence[i+1];
        sequence[i+1] = elem;
        swaps += 1;
      }
    }
    if (swaps == previous_swaps) {
      sorted = true;
    }
    previous_swaps = swaps;
    iter += 1
  }
  return sequence
}