/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
	low := 1
	high := n
	myGuess := (high + low) / 2
	for {

		if guess(myGuess) == 0 {
			return myGuess
		} else if guess(myGuess) == -1 {
			high = myGuess
		} else {
			low = myGuess + 1
		}

		myGuess = (high + low) / 2
	} 

	return myGuess
}
