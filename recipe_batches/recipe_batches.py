#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  num_of_ri = len(recipe)
  num_of_i = len(ingredients)
  totals = []
  if num_of_ri > num_of_i:
    return 0
  else:
    for item in recipe:
      totals.append(ingredients[item] // recipe[item])

    def selection_sort( arr ):
    # loop through n-1 elements
      for i in range(0, len(arr) - 1):
          cur_index = i
          smallest_index = cur_index
          # TO-DO: find next smallest element
          # (hint, can do in 3 loc) 
          for j in range(cur_index, len(arr)):
              if arr[j] < arr[smallest_index]:
                  smallest_index = j
          # TO-DO: swap
          temp = arr[smallest_index]
          arr[smallest_index] = arr[cur_index]
          arr[cur_index] = temp

      return arr[0]

    return selection_sort(totals)



print (recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 5,},
  { 'milk': 138, 'butter': 50, 'flour': 51 }
))


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))