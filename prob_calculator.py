import random
import copy
class Hat:
    def __init__(self, **args):
        self.contents = []
        for arg in args.items(): # e.g of arg ("yellow":3)
            for i in range(arg[1]): # 3
                self.contents.append(arg[0]) # append yellow --> ["yellow", "yellow", "yellow"]
    def draw(self, draw_balls):
        balls_drawn = []
        if draw_balls > len(self.contents): # number of balls to be drawn is greater than the balls in hat
            balls_drawn = self.contents # return all balls
        else:
            for i in range(draw_balls):
                ind = random.randrange(0,len(self.contents)) # select a random index
                balls_drawn.append(self.contents.pop(ind)) # append to balls drawn array
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    exp = expected_balls
    for j in range(num_experiments):
        hat_inp = hat # reserved copy of hat
        h = copy.deepcopy(hat_inp) # deep copy of hat to work on
        d = h.draw(num_balls_drawn) # draw balls
        drw = {}
        for i in d:
            drw[i] = drw.get(i,0) + 1 # count the number of balls for each color (Histogram)
        hit = 0
        for i in range(len(list(exp.keys()))): # for all elements/colors in expected 
            if(list(exp.keys())[i] in drw): # if the color is drawn --> proceed
                if (exp[list(exp.keys())[i]] <= drw[list(exp.keys())[i]]): # check if the color drawn is atleast equal to or greater than expected
                    hit += 1
            if hit == len(list(exp.keys())): # if above conditions are satisfied for all the expected colors
                M += 1 # increment a success counter

    print(M)
    return M/num_experiments # return probability