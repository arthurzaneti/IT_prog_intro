def levenshtein_distance(s1, s2):
  m = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
  for i in range(len(s2) + 1):
    m[0][i] = i
  for j in range(len(s1) + 1):
    m[j][0] = j

  for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
      if s1[i - 1] == s2[j - 1]:
        diag_cost = 0
      else:
        diag_cost = 1
      m[i][j] = min(m[i-1][j] + 1, m[i][j-1] + 1, m[i-1][j-1] + diag_cost)
  return(m[len(s1)][len(s2)])