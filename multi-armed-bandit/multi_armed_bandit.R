# Two armed bandit with the epsilon-greedy algorithm

# q1 and q2 are the expected rewards for arm 1 and 2 respectively
# q1 and q2 are determined by an average of previous rewards
# i.e. q1 = 1/k(r1 + r2 + ... + rk)
# where k is the number of previous actions, ri is the reward at action i
# this can be rearranged to calculate qk+1 expected reward:
# qk+1 = qk + (1/(k+1))*(rk+1 - qk)

# 0<=epsilon<=1 is the probability our agent chooses an arm randomly
# 1-epsilon is the probability that we choose the arm with the maximum expected reward
# i.e. argmax(q1, q2, ..., qk)

# Problem definition
# w1 and w2 are the real win rates for arm 1 and 2 respectively
w1 <- 0.2
w2 <- 0.7

# Lets say that a win results in reward of 1 and a loss results in nothing
WINAMOUNT <- 1
LOSSAMOUNT <- 0

EPSILON <- 0.1

# A function to simulate pulling an arm of the bandit
pullArm <- function(armWinRate, winAmount, lossAmount) {
  # generate random number between 0 and 1
  x1 <- runif(1, 0.0, 1.0)
  if (x1 <= armWinRate) {
    return(winAmount)
  } else {
    return(lossAmount)
  }
}

#A function to calculate the new expected reward of an arm
newExpectedReward <- function(currentExpectedReward, newReward, k) {
  return(currentExpectedReward + (1/(k+1)) * (newReward - currentExpectedReward))
}

# Algorithm definition
epsilonGreedyTwoArms <- function(epsilon, numberOfIterations) {
  # k1 and k2 are the number of pulls for each arm respectively
  k1 <- k2 <- 0
  # q1 and q2 are the current expected rewards for each arm respectively
  q1 <- q2 <- 0
  while (k1 + k2 <= numberOfIterations) {
    # define a variable that holds the index of the arm to be pulled
    armToBePulled = 0
    # generate random number between 0 and 1
    x1 <- runif(1, 0.0, 1.0)
    if (x1 > epsilon & q1 != q2) {
      # pull the arm based on the greatest expect reward currently
      if (q1 > q2) {
        armToBePulled = 1
      } else {
        armToBePulled = 2
      }
    } else {
      x1 <- runif(1, 0.0, 1.0)
      if (x1 > 0.5) {
        armToBePulled = 1
      } else {
        armToBePulled = 2
      }
    }
    if (armToBePulled == 1) {
      reward <- pullArm(w1, WINAMOUNT, LOSSAMOUNT)
      q1 <- newExpectedReward(q1, reward, k1)
      k1 = k1 + 1
    } else {
      reward <- pullArm(w2, WINAMOUNT, LOSSAMOUNT)
      q2 <- newExpectedReward(q2, reward, k2)
      k2 = k2 + 1
    }
  }
  
  if (q1 > q2) {
    cat("Arm 1 has a higher expected reward with ", q1)
  } else {
    cat("Arm 2 has a higher expected reward with ", q2)
  }
}