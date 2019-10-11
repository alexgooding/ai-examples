# Two armed bandit with the epsilon-greedy algorithm

# q1 and q2 are the expected rewards for arm 1 and 2 respectively
# q1 and q2 are determined by an average of previous rewards
# i.e. q1 = 1/k(r1 + r2 + ... + rk)
# where k is the number of previous actions, ri is the reward at action i

# 0<=epsilon<=1 is the probability our agent chooses an arm randomly
# 1-epsilon is the probability that we choose the arm with the maximum expected reward
# i.e. argmax(q1, q2, ..., qk)

# Problem definition
# w1 and w2 are the real win rates for arm 1 and 2 respectively
w1 <- 0.2
w2 <- 0.7

epsilon <- 0.1

q1 <- 0
q2 <- 0

