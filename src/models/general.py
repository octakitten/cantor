import torch
import numpy as np

class general():

    # dimensions of the neural space
    width = 0
    height = 0
    depth = 0
    
    # how many control neurons there are
    num_controls = 0
    # array of those controls
    controls = []
    # array of those controls' positive and negative firing thresholds
    thresholds_pos = []
    thresholds_neg = []
    
    # neuron layer
    layer0 = 0
    
    # threshold layers
    layer1 = 0
    layer2 = 0
    
    # emotion layers
    emotion1 = 0
    emotion2 = 0
    emotion3 = 0
    emotion4 = 0
    
    # personality layers
    personality1 = 0
    personality2 = 0
    personality3 = 0
    personality4 = 0
    personality5 = 0
    personality6 = 0
    personality7 = 0
    personality8 = 0
    
    # range of propensity to fire for personality layers
    pos_propensity = 0
    neg_propensity = 0

    def __init__(self):
        return
    
    def save(self, path):
        np.save(path, self.controls)
        np.save(path, self.thresholds_pos)
        np.save(path, self.thresholds_neg)
        torch.save(self.layer0, path)
        torch.save(self.layer1, path)
        torch.save(self.layer2, path)
        torch.save(self.emotion1, path)
        torch.save(self.emotion2, path)
        torch.save(self.emotion3, path)
        torch.save(self.emotion4, path)
        torch.save(self.personality1, path)
        torch.save(self.personality2, path)
        torch.save(self.personality3, path)
        torch.save(self.personality4, path)
        torch.save(self.personality5, path)
        torch.save(self.personality6, path)
        torch.save(self.personality7, path)
        torch.save(self.personality8, path)
        return
    
    '''
    Copy a model's parameters to a new model.
    
    Parameters:
    model (general): the model to copy
    
    Returns:
    none
    '''
    def copy(self, model):
        self.width = model.width
        self.height = model.height
        self.depth = model.depth
        self.num_controls = model.num_controls
        self.controls = model.controls
        self.thresholds_pos = model.thresholds_pos
        self.thresholds_neg = model.thresholds_neg
        self.layer0 = model.layer0
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.emotion1 = model.emotion1
        self.emotion2 = model.emotion2
        self.emotion3 = model.emotion3
        self.emotion4 = model.emotion4
        self.personality1 = model.personality1
        self.personality2 = model.personality2
        self.personality3 = model.personality3
        self.personality4 = model.personality4
        self.personality5 = model.personality5
        self.personality6 = model.personality6
        self.personality7 = model.personality7
        self.personality8 = model.personality8
        self.pos_propensity = model.pos_propensity
        self.neg_propensity = model.neg_propensity
        return
    
    '''
    Create a new model with the given dimensions and number of controls.
    
    Parameters: 
    w (int): width of input images in pixels
    h (int): height of input images in pixels
    d (int): depth of the neural space
    num_controls (int): number of controls
    
    Returns:
    none
    
    This function creates a new, randomly initialized model with the dimensions and number of controls given.
    Importantly, this model will only be able to accept images of the specified width and height.
    The depth of the model determines its complexity. With more depth, the runtime and memory usage
    also increase dramatically. The number of controls determines what outputs the model can have. If you want it to 
    perform a certain task that requires, for instance, controlling 4 seperate keyboard keypresses, 
    then you would want a model with 4 controls.
    '''
    def create(self, w, h, d, num_controls):
        self.width = w
        self.height = h
        self.depth = d
        self.num_controls = num_controls
        self.__new_controls()
        self.__new_thresholds()
        self.__new_propensity()
        self.__new_personality()
        return
    
    def __new_thresholds(self):
        self.thresholds_pos = []
        self.thresholds_neg = []
        threshhold_max = np.random.uniform(low=1, high=255)
        for i in range(0, self.num_controls):
            self.thresholds_pos.append(np.random.uniform(low=1, high=threshhold_max))
            self.thresholds_neg.append(-np.random.uniform(low=1, high=threshhold_max))
        return
    
    def __new_controls(self):
        self.controls = []
        for i in range(0, self.num_controls):
            self.controls.append((np.random.randint(low=1, high=self.width), np.random.randint(low=1, high=self.height), np.random.randint(low=1, high=self.depth)))
        return
    
    def __new_personality(self):
        
        # neuron layer
        self.layer0 = torch.zeros((self.width, self.height, self.depth))
        # threshold layers
        self.layer1 = torch.zeros((self.width, self.height, self.depth))
        self.layer2 = torch.zeros((self.width, self.height, self.depth))
        # emotion layers
        self.emotion1 = torch.zeros((self.width, self.height, self.depth))
        self.emotion2 = torch.zeros((self.width, self.height, self.depth))
        self.emotion3 = torch.zeros((self.width, self.height, self.depth))
        self.emotion4 = torch.zeros((self.width, self.height, self.depth))
        # personality layers
        # positive thresh firing is used
        self.personality1 = torch.zeros((self.width, self.height, self.depth))
        # positive thresh firing is unused
        self.personality2 = torch.zeros((self.width, self.height, self.depth))
        # positive thresh resting is used
        self.personality3 = torch.zeros((self.width, self.height, self.depth))
        # positive thresh resting is unused
        self.personality4 = torch.zeros((self.width, self.height, self.depth))
        # negative thresh firing is used
        self.personality5 = torch.zeros((self.width, self.height, self.depth))
        # negative thresh firing is unused
        self.personality6 = torch.zeros((self.width, self.height, self.depth))
        # negative thresh resting is used
        self.personality7 = torch.zeros((self.width, self.height, self.depth))
        # negative thresh resting is unused
        self.personality8 = torch.zeros((self.width, self.height, self.depth))
        # personality layers
        # positive thresh firing is used
        random_gen = torch.Generator()
        random_gen.seed()
        self.personality1 = torch.multiply(self.pos_propensity, torch.rand(size=(self.width, self.height, self.depth), generator=random_gen, dtype=torch.float32))
        random_gen.seed()
        # positive thresh firing is unused
        self.personality2 = torch.multiply(self.neg_propensity, torch.rand(size=(self.width, self.height, self.depth), generator=random_gen, dtype=torch.float32))
        random_gen.seed()
        # positive thresh resting is used
        self.personality3 = torch.multiply(self.pos_propensity, torch.rand(size=(self.width, self.height, self.depth), generator=random_gen, dtype=torch.float32))
        random_gen.seed()
        # positive thresh resting is unused
        self.personality4 = torch.multiply(self.neg_propensity, torch.rand(size=(self.width, self.height, self.depth), generator=random_gen, dtype=torch.float32))
        random_gen.seed()
        # negative thresh firing is used
        self.personality5 = torch.multiply(self.pos_propensity, torch.rand(size=(self.width, self.height, self.depth), generator=random_gen, dtype=torch.float32))
        random_gen.seed()
        # negative thresh firing is unused
        self.personality6 = torch.multiply(self.neg_propensity, torch.rand(size=(self.width, self.height, self.depth), generator=random_gen, dtype=torch.float32))
        random_gen.seed()
        # negative thresh resting is used
        self.personality7 = torch.multiply(self.pos_propensity, torch.rand(size=(self.width, self.height, self.depth), generator=random_gen, dtype=torch.float32))
        random_gen.seed()
        # negative thresh resting is unused
        self.personality8 = torch.multiply(self.neg_propensity, torch.rand(size=(self.width, self.height, self.depth), generator=random_gen, dtype=torch.float32))
        return
    
    def __new_propensity(self):
        self.pos_propensity = np.random.uniform(low=1, high=255)
        self.neg_propensity = -np.random.uniform(low=1, high=255)
        return
    
    def permute(self, degree):
        model = general()
        model.copy(self)
        model.__new_thresholds()
        model.__new_propensity()
        model.__new_personality()
        for i in range(0, degree):
            self.thresholds_pos = np.add(self.thresholds_pos, model.thresholds_pos)
            self.thresholds_neg = np.add(self.thresholds_neg, model.thresholds_neg)
            self.personality1 = torch.add(self.personality1, model.personality1)
            self.personality2 = torch.add(self.personality2, model.personality2)
            self.personality3 = torch.add(self.personality3, model.personality3)
            self.personality4 = torch.add(self.personality4, model.personality4)
            self.personality5 = torch.add(self.personality5, model.personality5)
            self.personality6 = torch.add(self.personality6, model.personality6)
            self.personality7 = torch.add(self.personality7, model.personality7)
            self.personality8 = torch.add(self.personality8, model.personality8)
        self.thresholds_pos = np.divide(self.thresholds_pos, degree + 1)
        self.thresholds_neg = np.divide(self.thresholds_neg, degree + 1)
        self.personality1 = torch.divide(self.personality1, degree + 1)
        self.personality2 = torch.divide(self.personality2, degree + 1)
        self.personality3 = torch.divide(self.personality3, degree + 1)
        self.personality4 = torch.divide(self.personality4, degree + 1)
        self.personality5 = torch.divide(self.personality5, degree + 1)
        self.personality6 = torch.divide(self.personality6, degree + 1)
        self.personality7 = torch.divide(self.personality7, degree + 1)
        self.personality8 = torch.divide(self.personality8, degree + 1)
        return
    
    def save(self, path):
        torch.save(self, path)
        return

    def update(self, input_image):
        if (torch.is_tensor(input_image) == False):
            return -1
        # add in the input image
        torch.add(self.layer0[:, :, 1],  input_image)

        #check which neurons are firing and which arent, do the stuff
        positive_firing = torch.greater(self.layer0, self.layer1)
        positive_resting = torch.less_equal(self.layer0, self.layer1)
        negative_firing = torch.less(self.layer0, self.layer2)
        negative_resting = torch.greater_equal(self.layer0, self.layer2)

        # keep track of the values of the firing neurons
        pos_fire_amt = torch.multiply(positive_firing, self.layer1)
        neg_fire_amt = torch.multiply(negative_firing, self.layer2)

        # apply the firing values to each of the near neighbors
        self.layer0 = torch.add(self.layer0, torch.roll(pos_fire_amt, 1, 0))
        self.layer0 = torch.add(self.layer0, torch.roll(neg_fire_amt, -1, 0))
        self.layer0 = torch.add(self.layer0, torch.roll(pos_fire_amt, 1, 1))
        self.layer0 = torch.add(self.layer0, torch.roll(neg_fire_amt, -1, 1))
        self.layer0 = torch.add(self.layer0, torch.roll(pos_fire_amt, 1, 2))
        self.layer0 = torch.add(self.layer0, torch.roll(neg_fire_amt, -1, 2))

        # update the threshold layers
        self.layer1 = torch.add(self.layer1, torch.multiply(positive_firing, self.emotion1))
        self.layer1 = torch.add(self.layer1, torch.multiply(positive_resting, self.emotion2))
        self.layer2 = torch.add(self.layer1, torch.multiply(negative_firing, self.emotion3))
        self.layer2 = torch.add(self.layer1, torch.multiply(negative_resting, self.emotion4))

        # figure out which emotions were used and which weren't
        # and then update them
        self.emotion1 = torch.add(torch.multiply(positive_firing, self.personality1), torch.multiply(positive_resting, self.personality3))
        self.emotion2 = torch.add(torch.multiply(positive_resting, self.personality2), torch.multiply(positive_firing, self.personality4))
        self.emotion3 = torch.add(torch.multiply(negative_firing, self.personality5), torch.multiply(negative_resting, self.personality7))
        self.emotion4 = torch.add(torch.multiply(negative_resting, self.personality6), torch.multiply(negative_firing, self.personality8))
        
        # check the predefined output neurons to see if they're ready to fire
        # if they are, then return the action(s) to take
        take_action = []
        
        for i in range(0, self.num_controls):
            if (self.layer0[self.controls[i]].item() > self.thresholds_pos[i]):
                take_action.append(True)
            else:
                if (self.layer0[self.controls[i]].item() < self.thresholds_neg[i]):
                    take_action.append(False)
                else:
                    take_action.append(-1)
        #print(take_action)
        return take_action