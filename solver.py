# Solver for the "Frog Jumping" problem introduced by Gordon Hamilton in a
# comment to this video: https://www.youtube.com/watch?v=X3HDnrehyDM
# The rules of Frog Jumping briefly:
# - there are lily-pads and each lily-pad has zero or one frog sitting on them
# - the frogs want to have a party, which means they want to gather all
#   together on a single lily-pad
# - N frogs can jump N lily-pads (so a single frog can jump to the neighbor
#   lily-pad only, two frogs can only jump over a lili-pad, and so on)
# - frogs can only jump to a lily-pad if there's at least one frog there,
#   cannot jump to empty lily-pads (so each jump increases the number of empty
#   lily-pads by exactly one)
#
# The initial state can be represented by a binary number: 0 means an empty
# lily-pad, 1 means a lily-pad with a single frog. Based on the above rules,
# the initially empty lily-pads will always be empty. Gordon Hamilton
# called these initially empty lily-pads "waterlogged", but i think it's
# unnecessary to introduce a new name, since there's nothing special
# about empty lilypads.
#
# A given state is "solvable" if there's a possible jumping sequence so
# that at the end all frogs are on a single lily-pad (which means party time).
#
# Example:
# - "101" is unsolvable, because none of the frogs can jump over the empty
#   lily-pad, that would require 2 frogs.
# - "1011" is solvable: 1011 => 1020 => 3000
#
# Hamilton Gordon's problem:
# For an initial state of lily-pads, can you always add a finite number of
# lily-pads so that it becomes solvable?
# For example 1000 can be solved by adding 4 lilypads: 10001111
# Do every binary number has a solution? If not - what is the lowest
# binary number that is unsolvable by appending finite number of lily-pads?
#
# My theory is that every binary number is solvable and this program
# gives a solution (leaving out the unimportant parts).
# How it works:
# - We append a "group" of lily-pads after the inital state, one group for
#   each 1's in the inital state
# - All of these appended groups are distinct, the frogs in them never have to
#   jump over the group boundaries
# - In each group most of the frogs have to gather to a single designated
#   lily-pad and all the remaining frogs must gather to the next lily-pad (or
#   in other words the "neighbor" lily-pad). This gathering is left out from
#   the output for brevity, but it should be trivial to do it even manually
# - The first group is the starting point: jump in to rescue the first frog,
#   then jump back to the same group (to the neighbor lily-pad)
# - All the other groups are handled similarly: the group of frogs jumps to
#   the next group, then jumps back to rescue the next frog then jumps
#   back to the group (to the neighbor lily-pad as well)
#
# (c) Andras Suller <suller.andras@gmail.com>, 5/March/2017

binary_string = '101010'

def solve(binary_string):
  length = len(binary_string)
  current_position = None
  arr = [ord(ch) - ord('0') for ch in binary_string]

  for i in xrange(len(arr)):
    ch = arr[i]
    if ch == 1:
      print('i: %s' % (i,))
      if current_position == None:
        distance_to_jump = length - i
        group_size = distance_to_jump + 1
        print('need %s frogs on position %s' % (distance_to_jump, length))
        print('need 1 frog on position %s' % (length + 1))
        print('need %s empty lily-pads' % (group_size - 2))
        current_position = length
        length += group_size

        arr.append(distance_to_jump)
        arr.append(1)
        for x in xrange(0, group_size - 2):
          arr.append(0)
        print('%s, current_position: %s' % (arr, current_position))
        frogs = arr[current_position]
        new_position = current_position - frogs
        print('%s frogs on position %s jump left to position %s' % (frogs, current_position, new_position))
        arr[new_position] += frogs
        arr[current_position] = 0
        current_position = new_position

        print('%s, current_position: %s' % (arr, current_position))
        frogs = arr[current_position]
        new_position = current_position + frogs
        print('%s frogs on position %s jump right to position %s' % (frogs, current_position, new_position))
        arr[new_position] += frogs
        arr[current_position] = 0
        current_position = new_position

        print('%s, current_position: %s' % (arr, current_position))

      else:
        frogs = arr[current_position]
        extra_distance = current_position - i
        extra_frogs = 1
        group_size = extra_distance + extra_frogs
        # make sure there's at least 3 lily-pads after `current_position + frogs`
        if length + group_size - (current_position + frogs + 1) < 3:
          extra_frogs += 3 - (length + group_size - (current_position + frogs + 1))
          group_size = extra_distance + extra_frogs
        # if there are 2 empty lily-pads after the extra_frogs and we need exactly 2 extra_frogs,
        # than that's impossible to achieve, so need to add an additional extra lily-pad
        if (extra_frogs == 2) and (length + group_size - (current_position + frogs + 1) == 3):
          extra_frogs += 1
          group_size = extra_distance + extra_frogs
        print('need %s frogs on position %s' % (extra_distance, current_position + frogs))
        print('need %s frogs on position %s' % (extra_frogs, current_position + frogs + 1))
        print('need %s empty lily-pads' % (group_size - 2))
        for x in xrange(0, group_size):
          arr.append(0)
        arr[current_position + frogs] = extra_distance
        arr[current_position + frogs + 1] = extra_frogs
        length += group_size

        print('%s, current_position: %s' % (arr, current_position))
        new_position = current_position + frogs
        print('%s frogs on position %s jump right to position %s' % (frogs, current_position, new_position))
        arr[new_position] += frogs
        arr[current_position] = 0
        current_position = new_position

        print('%s, current_position: %s' % (arr, current_position))
        frogs = arr[current_position]
        new_position = current_position - frogs
        print('%s frogs on position %s jump left to position %s' % (frogs, current_position, new_position))
        arr[new_position] += frogs
        arr[current_position] = 0
        current_position = new_position

        print('%s, current_position: %s' % (arr, current_position))
        frogs = arr[current_position]
        new_position = current_position + frogs
        print('%s frogs on position %s jump right to position %s' % (frogs, current_position, new_position))
        arr[new_position] += frogs
        arr[current_position] = 0
        current_position = new_position

        print('%s, current_position: %s' % (arr, current_position))

solve(binary_string)
