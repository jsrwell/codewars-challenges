//::::DESCRIPTION:::://

/* 
3 kyu
Sudoku Solver (JavaScript)

Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.
The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.
For Sudoku rules, see the Wikipedia article.

var puzzle = [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]];

sudoku(puzzle);
/* Should return
[[5,3,4,6,7,8,9,1,2],
[6,7,2,1,9,5,3,4,8],
[1,9,8,3,4,2,5,6,7],
[8,5,9,7,6,1,4,2,3],
[4,2,6,8,5,3,7,9,1],
[7,1,3,9,2,4,8,5,6],
[9,6,1,5,3,7,2,8,4],
[2,8,7,4,1,9,6,3,5],
[3,4,5,2,8,6,1,7,9]] 
*/

  //::::OBSERVATION OF SOLUTION:::://

  /*
  In this challenge I use a resursive strategy to get the solution of this Kata, calling the solve, that it selfs call a function that checks if the number is valid with the rules of the game and make a recursive call until it complete solved.
  */

//::::SOLUTION:::://

function sudoku(grid) {
    // ::RECURSIVE SOLVE by jsrwell::
    
    // NUMBER VALIDATION FUNCTION
    function isValid(row, col, num) {
      
      // Verify if the number aready is in the row
      for (let i = 0; i < 9; i++)
        if (grid[row][i] === num)
          return false
      
      // Verify if the number aready is in the column
      for (let i = 0; i < 9; i++)
        if (grid[i][col] === num)
          return false
      
      // Verify if the number aready is in the bloq 3x3
      const blockRow = Math.floor(row / 3) * 3
      const blockCol = Math.floor(col / 3) * 3
      for (let i = 0; i < 3; i++)
        for (let j = 0; j < 3; j++)
          if (grid[blockRow + i][blockCol + j] === num)
            return false
      
      // Return true if the number is not used
      return true
    }
  
    // RECURSIVE FUNCTION
    function solve() {
      
      // Initiate the loop searching for zeros
      for (let row = 0; row < 9; row++) {
        for (let col = 0; col < 9; col++) {
          if (grid[row][col] === 0) {
            
            // Initiate the number full check on zero
            for (let num = 1; num <= 9; num++) {
              
              // Verify if the number is free and use him if is true
              if (isValid(row, col, num)) {
                grid[row][col] = num
                
                // Check if solve is true by a recursive call to continue the next numbers
                // Case false return zero and return to the last call
                if (solve())
                  return true
                else
                  grid[row][col] = 0
              }
            }
            
            // Case a zero is found the solve is false
            return false
          }
        }
      }
      
      // Case not found zeros on solve return true
      return true
    }
  
    // FINAL CHECK OF SOLUTION
    if (solve())
      return grid
    else
      return false
  }