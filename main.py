if __name__ == "__main__":
  # Using the symmetric_difference() method to find the symmetric difference of sets

  """
  new_set = set1.symmetric_difference(set2, set3,...)
  """

  s1 = {"Python", "Java", "C++"}
  s2 = {"C#", "Java", "C++"}
  s = s1.symmetric_difference(s2)

  print(s1)
  print(s2)
  print(s)

  # Using the symmetric difference operator(^) to find the symmetric difference of sets

  """
  new_set = set1 ^ set2 ^...
  """

  s1 = {"Python", "Java", "C++"}
  s2 = {"C#", "Java", "C++"}
  s = s1 ^ s2

  print(s1)
  print(s2)
  print(s)

  # The symmetric_difference() method vs symmetric difference operator (^)

  scores = {7, 8, 9}
  ratings = [8, 9, 10]
  new_set = scores.symmetric_difference(ratings)

  print(scores)
  print(ratings)
  print(new_set)

  scores = {7, 8, 9}
  ratings = [8, 9, 10]
  # new_set = scores ^ ratings
  # TypeError
