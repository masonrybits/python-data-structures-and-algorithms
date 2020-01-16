Input: [8,4,23,42,16,15]

Pivot = 8
After iteration & swapping: [4,8,23,42,16,15]

Pivot = 23
After iteration: [4,8,15,16,23,42]

Quick sort first sets its pivot to 8, after an iteration to check if 8 is greater than the rest of the values, after swaping pivot(8) with 4, pivot is now at its sorted position. Now working on partition [23,42,16,15], and sets a new pivot to 23, after an iteration to check if 23 is greater than the rest of the values, which are true for 16 and 15, hence swap 16 with 42, and then 15 with 42, lastly after swaping pivot(23) with 15, we have arrived at a sorted list.
