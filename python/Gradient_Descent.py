
def gradient_decent():
    i = 0
    intercept = 0
    slope = derivitive(intercept)
    for i in range (1000):
        step_size = slope*0.001
        print("the step size is:",step_size)
        intercept = intercept - step_size
        print("new intercept is:", intercept)
        slope = derivitive_intercept(intercept)
    return

def derivitive_intercept(intercept):
    result = (-2*(1.4-(intercept + 0.64*0.5))
              -2*(1.9-(intercept + 0.64*2.3))
              -2*(3.2-(intercept + 0.64*2.9))
              )
    return result
    
gradient_decent()