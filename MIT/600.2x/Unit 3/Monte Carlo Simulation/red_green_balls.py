import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    same_color = 0
    for i in range(numTrials):
        bucket = ['green', 'green', 'green', 'red', 'red', 'red']
        for draw in range(1, 4):
            ball = random.choice(bucket)
            bucket.remove(ball)
        if bucket.count('green') in (0, 3):
            same_color += 1
    return same_color/numTrials


print(noReplacementSimulation(20))
