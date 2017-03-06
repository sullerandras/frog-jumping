# Frog Jumping

Solver for the "Frog Jumping" problem introduced by Gordon Hamilton in a
comment to this video: [https://www.youtube.com/watch?v=X3HDnrehyDM](https://www.youtube.com/watch?v=X3HDnrehyDM)

The rules of Frog Jumping briefly:

- there are lily-pads and each lily-pad has zero or one frog sitting on them
- the frogs want to have a party, which means they want to gather all
  together on a single lily-pad
- N frogs can jump N lily-pads (so a single frog can jump to the neighbor
  lily-pad only, two frogs can only jump over a lili-pad, and so on)
- frogs can only jump to a lily-pad if there's at least one frog there,
  cannot jump to empty lily-pads (so each jump increases the number of empty
  lily-pads by exactly one)

The initial state can be represented by a binary number: 0 means an empty
lily-pad, 1 means a lily-pad with a single frog. Based on the above rules,
the initially empty lily-pads will always be empty. Gordon Hamilton
called these initially empty lily-pads "waterlogged", but i think it's
unnecessary to introduce a new name, since there's nothing special
about empty lilypads.

A given state is "solvable" if there's a possible jumping sequence so
that at the end all frogs are on a single lily-pad (which means party time).

Example:

- "101" is unsolvable, because none of the frogs can jump over the empty
  lily-pad, that would require 2 frogs.
- "1011" is solvable: 1011 => 1020 => 3000

Hamilton Gordon's problem:
For an initial state of lily-pads, can you always add a finite number of
lily-pads so that it becomes solvable?

For example 1000 can be solved by adding 4 lilypads: 10001111

Do every binary number has a solution? If not - what is the lowest
binary number that is unsolvable by appending finite number of lily-pads?

My theory is that every binary number is solvable and this program
gives a solution (leaving out the unimportant parts).
How it works:

- We append a "group" of lily-pads after the inital state, one group for
  each 1's in the inital state
- All of these appended groups are distinct, the frogs in them never have to
  jump over the group boundaries
- In each group most of the frogs have to gather to a single designated
  lily-pad and all the remaining frogs must gather to the next lily-pad (or
  in other words the "neighbor" lily-pad). This gathering is left out from
  the output for brevity, but it should be trivial to do it even manually
- The first group is the starting point: jump in to rescue the first frog,
  then jump back to the same group (to the neighbor lily-pad)
- All the other groups are handled similarly: the group of frogs jumps to
  the next group, then jumps back to rescue the next frog then jumps
  back to the group (to the neighbor lily-pad as well)
