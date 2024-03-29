import math
import numpy as np

import softmax as sr # sr = softmax regression
#-------------------------------------------------------------------------
'''
    two-layer fully connected neural network.
    implement a classification method using fully-connected neural network (FC) with two layers.
    The main goal of this problem is to extend the softmax regression method in the previous problem to having multiple layers (instead of one layer in softmax regression).
    In the first layer, the sigmoid activation function will be used to convert the linear logits into a non-linear activation.
    In the second layer, we will use softmax as the activation function (the same as softmax regression in the previous problem).
    We will use multi-class cross entropy as the loss function and stochastic gradient descent to train the model parameters.
    You could test the correctness of your code by typing `nosetests test3.py` in the terminal.

    Notations:
            ---------- input data ----------------------
            p: the number of input features, an integer scalar.
            c: the number of classes in the classification task, an integer scalar.
            x: the feature vector of a data instance, a float numpy vector of shape p by 1.
            y: the label of a training instance, an integer scalar value. The values can be 0,1,2, ..., or (c-1).

            ---------- model parameters ----------------------
            h: the number of outputs in the 1st layer (or the number of neuron in the first layer).
                ---------- 1st layer ----------------------
            W1: the weight matrix of the 1st layer, a float numpy matrix of shape (h by p).
            b1: the bias values of the 1st layer, a float numpy vector of shape h by 1.
                ---------- 2nd layer ----------------------
            W2: the weight matrix of the 2nd layer, a float numpy matrix of shape (h by c). Here c is the number of classes.
            b2: the bias values of the 2nd layer, a float numpy vector of shape c by 1.

            ---------- values ----------------------
                ---------- 1st layer ----------------------
            z1: the linear logits of the 1st layer, a float numpy vector of shape h by 1.
            a1: the sigmoid activations in the 1st layer, a float numpy vector of shape h by 1.
                The i-th element represents the sigmoid of the i-th logit z1[i].
                ---------- 2nd layer ----------------------
            z2: the linear logits, a float numpy vector of shape c by 1.
            a2: the softmax activations in the 2nd layer, a float numpy vector of shape c by 1.
            L: the multi-class cross entropy loss, a float scalar.

            ---------- partial gradients ----------------------
                ---------- 2nd layer ----------------------
            dL_da2: the partial gradients of the loss function L w.r.t. the activations a2, a float numpy vector of shape c by 1.
                    The i-th element dL_da2[i] represents the partial gradient of the loss function L w.r.t. the i-th activation a2[i]:  d_L / d_a2[i].
            da2_dz2: the partial gradient of the activations a2 w.r.t. the logits z2, a float numpy matrix of shape (c by c).
                   The (i,j)-th element represents the partial gradient ( d_a2[i]  / d_z2[j] )
            dz2_dW2: the partial gradient of logits z2 w.r.t. the weight matrix W2, a numpy float matrix of shape (c by h).
                   The (i,j)-th element represents the partial gradient of the i-th logit (z2[i]) w.r.t. the weight W2[i,j]:   d_z2[i] / d_W2[i,j]
            dz2_db2: the partial gradient of the logits z2 w.r.t. the biases b2, a float vector of shape c by 1.
                   Each element represents the partial gradient of the i-th logit z2[i] w.r.t. the i-th bias b2[i]:  d_z2[i] / d_b2[i]
            dz2_da1: the partial gradient of the logits z2 w.r.t. the inputs a1, a float numpy matrix of shape (c, h).
                   The i-th element represents the partial gradient ( d_z2[i]  / d_a1[i] ).
                ---------- 1st layer ----------------------
            da1_dz1: the partial gradient of the activations a1 w.r.t. the logits z1, a float numpy vector of shape h by 1.
                   The i-th element of da1_dz1 represents the partial gradient ( d_a1[i]  / d_z1[i] )
            dz1_dW1: the partial gradient of logits z1 w.r.t. the weight matrix W1, a numpy float matrix of shape (h by p).
                   The (i,j)-th element represents the partial gradient of the i-th logit (z1[i]) w.r.t. the weight W1[i,j]:   d_z1[i] / d_W1[i,j]
            dz1_db1: the partial gradient of the logits z1 w.r.t. the biases b1, a float vector of shape h by 1.
                   Each element represents the partial gradient of the i-th logit z1[i] w.r.t. the i-th bias b1[i]:  d_z1[i] / d_b1[i]

            ---------- partial gradients of parameters ------------------
                ---------- 2nd layer ----------------------
            dL_dW2: the partial gradients of the loss function L w.r.t. the weights W1, a float numpy matrix of shape (h by p).
                    The i,j-th element represents the partial gradient of the loss function L w.r.t. the i,j-th weight W1[i,j]:  d_L / d_W1[i,j].
            dL_db2: the partial gradients of the loss function L w.r.t. the biases b1, a float numpy vector of shape c by 1.
                    The i-th element represents the partial gradient of the loss function L w.r.t. the i-th bias b1[i]:  d_L / d_b1[i].
                ---------- 1st layer ----------------------
            dL_dW1: the partial gradients of the loss function L w.r.t. the weights W1, a float numpy matrix of shape (h by p).
                    The i,j-th element represents the partial gradient of the loss function L w.r.t. the i,j-th weight W1[i,j]:  d_L / d_W1[i,j].
            dL_db1: the partial gradients of the loss function L w.r.t. the biases b1, a float numpy vector of shape h by 1.
                    The i-th element represents the partial gradient of the loss function L w.r.t. the i-th bias b2[i]:  d_L / d_b2[i].

            ---------- training ----------------------
            alpha: the step-size parameter of gradient ascent, a float scalar.
            n_epoch: the number of passes to go through the training set, an integer scalar.
'''

#-----------------------------------------------------------------
# Forward Pass
#-----------------------------------------------------------------

#-----------------------------------------------------------------
def compute_z1(x,W1,b1):
    '''
        Compute the linear logit values of a data instance in the first layer. z1 =  W1 x + b1
        Input:
            x: the feature vector of a data instance, a float numpy vector of shape p by 1. Here p is the number of features/dimensions.
            W1: the weight matrix of the first layer, a float numpy matrix of shape (h by p). Here h is the number of outputs in the first layer.
            b1: the bias values of the first layer, a float numpy vector of shape h by 1.
        Output:
            z1: the linear logits, a float numpy vector of shape h by 1.
        
    '''
    #########################################
  
    z1 = W1 * x + b1
    #########################################
    return z1


#-----------------------------------------------------------------
def compute_a1(z1):
    '''
        Compute the sigmoid activations a1 from the linear logits z1 in the first layer.
        Input:
            z1: linear logits in the first layer, a float numpy vector of shape h by 1.
                Here h is the number of outputs in the 1st fully connected layer.
        Output:
            a1: the non-linear activations in the first layer, a float numpy vector of shape h by 1.
               The i-th element represents the sigmoid of the i-th logit z1[i].
        Note: this function is different from the sigmoid function in problem 1.
              In problem 1, the input z to the sigmoid function is a scalar, but here the input z is a vector.
    '''
    #########################################

    try:
        a1 = 1/(1 + np.exp(-1*z1))
    # except OverflowError:
    except FloatingPointError:
        if np.max(z1) > 100:
            a1 = np.ones(z1.shape)
        if np.min(z1) < -100:
            a1 = np.zeros(z1.shape)
    #########################################
    return a1

#-----------------------------------------------------------------
def compute_z2(a1,W2,b2):
    '''
        Compute the linear logit values of a data instance in the first layer. z1 =  W1 x + b1
        Input:
            a1: the non-linear activations in the first layer, a float numpy vector of shape h by 1.
            W2: the weight matrix of the 2nd layer, a float numpy matrix of shape (h by c). Here c is the number of classes.
            b2: the bias values of the 2nd layer, a float numpy vector of shape c by 1.
        Output:
            z2: the linear logits of the 2nd layer, a float numpy vector of shape c by 1.
    '''
    #########################################


    z2 = W2 * a1 + b2

    #########################################
    return z2



#-----------------------------------------------------------------
def compute_a2(z2):
    '''
        Compute the softmax activations a2 from the linear logits z2 in the second layer.
        Input:
            z2: linear logits in the second layer, a float numpy vector of shape c by 1.
                Here c is the number of classes.
        Output:
            a2: the non-linear activations in the 2nd layer, a float numpy vector of shape c by 1.
    '''
    #########################################

    try:
        e_z = np.exp(z2)
        e_sum = np.sum(e_z)
        a2 = e_z / e_sum
    except FloatingPointError:
        if (z2 == z2[0]).all():
            a2 = np.ones((z2.shape))
            a2 = a2 / z2.shape[0]
        else:
            a2 = np.zeros((z2.shape))
            a2[np.argmax(z2)] = 1.

    #########################################
    return a2


#-----------------------------------------------------------------
def forward(x, W1, b1, W2, b2):
    '''
       Forward pass: given an instance in the training data, compute the logits z, activations a in each layer.
        Input:
            x: the feature vector of a data instance, a float numpy vector of shape p by 1.
               Here p is the number of input features/dimensions.
            W1: the weight matrix in the 1st layer.
            b1: the biases in the 1st layer.
            W2: the weight matrix in the 2nd layer.
            b2: the biases in the 2nd layer.
        Output:
            z1: the linear logits in the 1st layer.
            a1: the non-linear activations in the 1st layer.
            z2: the linear logits in the 2nd layer.
            a2: the non-linear activations in the 2nd layer.
    '''
    #########################################
    # first layer
    z1 = compute_z1(x,W1,b1)
    a1 = compute_a1(z1)

    # second layer
    z2 = compute_z2(a1, W2, b2)
    a2 = compute_a2(z2)

    #########################################
    return z1, a1, z2, a2


#-----------------------------------------------------------------
# Compute Local Gradients
#-----------------------------------------------------------------

#-----------------------------------------------------------------
def compute_dL_da2(a2, y):
    '''
        Compute local gradient of the multi-class cross-entropy loss function L w.r.t. the activations a2 in the 2nd layer.
        Input:
            a2: the activations in the 2nd layer, a float numpy vector of shape c by 1. Here c is the number of classes.
            y: the label of a training instance, an integer scalar value. The values can be 0,1,2, ..., or (c-1).
        Output:
            dL_da2: the local gradients of the loss function L w.r.t. the activations a2, a float numpy vector of shape c by 1.
                    The i-th element dL_da2[i] represents the partial gradient of the loss function L w.r.t. the i-th activation a2[i]:  d_L / d_a2[i].
    '''
    #########################################
    dL_da2 = np.asmatrix(np.zeros(a2.shape))

    if a2[y] == 0.0 :
        dL_da2[y] = -1e6
        return dL_da2

    dL_da2[y] = -1/ a2[y]
    #########################################
    return dL_da2

#-----------------------------------------------------------------
def compute_da2_dz2(a2):
    '''
        Compute local gradient of the softmax activations a2 w.r.t. the logits z2 in the 2nd layer.
        Input:
            a2: the activation values of softmax function, a numpy float vector of shape c by 1. Here c is the number of classes.
        Output:
            da2_dz2: the local gradient of the activations a2 w.r.t. the logits z2, a float numpy matrix of shape (c by c).
                   The (i,j)-th element represents the partial gradient ( d_a2[i]  / d_z2[j] )
    '''
    #########################################
    mat1 = -1 * a2* a2.T
    mat2 = a2 * (1- a2).T

    m = a2.shape[0]
    da2_dz2 = np.mat(np.zeros((m,m)))
    for i in range(m):
        for j in range(m):
            if (i == j):
                da2_dz2[i, i] = mat2[i,i]
            else:
                da2_dz2[i,j ] = mat1[i,j]

    #########################################
    return da2_dz2


#-----------------------------------------------------------------
def compute_dz2_dW2(a1,c):
    '''
        Compute local gradient of the logits function z2 w.r.t. the weights W2.
        Input:
            a1: the activations of sigmoid function, a numpy float vector of shape h by 1.
        Output:
            dz2_dW2: the partial gradient of logits z2 w.r.t. the weight matrix W2, a numpy float matrix of shape (c by h).
                   The (i,j)-th element represents the partial gradient of the i-th logit (z2[i]) w.r.t. the weight W2[i,j]:   d_z2[i] / d_W2[i,j]
    '''
    #########################################
    result_list = a1.T.tolist() * c
    dz2_dW2 = np.mat(result_list)
    #########################################
    return dz2_dW2


#-----------------------------------------------------------------
def compute_dz2_db2(c):
    '''
        Compute local gradient of the logits function z2 w.r.t. the biases b2.
        Input:
            c: the number of classes, an integer.
        Output:
            dz2_db2: the partial gradient of the logits z2 w.r.t. the biases b2, a float vector of shape c by 1.
                   Each element represents the partial gradient of the i-th logit z2[i] w.r.t. the i-th bias b2[i]:  d_z2[i] / d_b2[i]
    '''
    #########################################
    dz2_db2 = np.mat(np.array([1] * c))
    dz2_db2 = dz2_db2.T
    #########################################
    return dz2_db2


#-----------------------------------------------------------------
def compute_dz2_da1(W2):
    '''
        Compute local gradient of the logits z2 w.r.t. the activations a1.
        Input:
            W2: the weights in the 2nd layer, a numpy float matrix of shape (c, h).
        Output:
            dz2_da1: the local gradient of the logits z2 w.r.t. the inputs a1, a float numpy matrix of shape (c, h).
                   The i-th element represents the partial gradient ( d_z2[i]  / d_a1[i] ).
    '''
    #########################################

    dz2_da1 = W2

    #########################################
    return dz2_da1


#-----------------------------------------------------------------
def compute_da1_dz1(a1):
    '''
        Compute local gradient of the sigmoid activations a1 w.r.t. the logits z1 in the first layer.
        Input:
            a1: the activations of sigmoid function, a numpy float vector of shape h by 1.
            a1: the non-linear activations in the 1st layer.
        Output:
            da1_dz1: the local gradient of the activations a1 w.r.t. the logits z1, a float numpy vector of shape h by 1.
                   The i-th element of da1_dz1 represents the partial gradient ( d_a1[i]  / d_z1[i] )
    '''
    #########################################
    da1_dz1 = np.multiply(a1 , (1-a1))


    #########################################
    return da1_dz1


#-----------------------------------------------------------------
def compute_dz1_dW1(x,h):
    '''
        Compute local gradient of the logits function z1 w.r.t. the weights W1 in the 1st layer.
        Input:
            x: the feature vector of a data instance, a float numpy vector of shape p by 1. Here p is the number of features/dimensions.
            h: the number of output activations in the first layer, an integer.
        Output:
            dz1_dW1: the partial gradient of logits z1 w.r.t. the weight matrix W1, a numpy float matrix of shape (h by p).
                   The (i,j)-th element represents the partial gradient of the i-th logit (z1[i]) w.r.t. the weight W1[i,j]:   d_z1[i] / d_W1[i,j]
    '''
    #########################################
    result_list = x.T.tolist() * h
    dz1_dW1 = np.mat(result_list)
    #########################################
    return dz1_dW1


#-----------------------------------------------------------------
def compute_dz1_db1(h):
    '''
        Compute local gradient of the logits function z2 w.r.t. the biases b2.
        Input:
            h: the number of output activations in the first layer, an integer.
        Output:
            dz1_db1: the partial gradient of the logits z1 w.r.t. the biases b1, a float vector of shape h by 1.
                   Each element represents the partial gradient of the i-th logit z1[i] w.r.t. the i-th bias b1[i]:  d_z1[i] / d_b1[i]
    '''
    #########################################

    dz1_db1 = np.mat(np.array([1] * h))
    dz1_db1 = dz1_db1.T

    #########################################
    return dz1_db1

#-----------------------------------------------------------------
def backward(x,y,a1,a2,W2):
    '''
       Back Propagation: given an instance in the training data, compute the local gradients of the logits z, activations a, weights W and biases b in the two layers.
        Input:
            x: the feature vector of a training instance, a float numpy vector of shape p by 1. Here p is the number of features/dimensions.
            y: the label of a training instance, an integer scalar value. The values can be 0,1,2, ..., or (c-1).
            a1: the activations of a training instance in the 1st layer, a float numpy vector of shape h by 1.
            a2: the activations of a training instance in the 2nd layer, a float numpy vector of shape c by 1.
        Output:
            dL_da2: the local gradients of the loss function w.r.t. the activations in the 2nd layer, a float numpy vector of shape c by 1.
            da2_dz2: the local gradient of the activation a2 w.r.t. the logits z2, a float numpy matrix of shape (c by c).
            dz2_dW2: the partial gradient of logits z2 w.r.t. the weight matrix W2, a numpy float matrix of shape (c by h).
            dz2_db2: the partial gradient of the logits z2 w.r.t. the biases b2, a float vector of shape c by 1.
            dz2_da1: the partial gradient of the logits z2 w.r.t. the activations a1.
            da1_dz1: the partial gradient of the activations a1 w.r.t. the logits z1.
            dz1_dW1: the partial gradient of the logits z1 w.r.t. the weights W1.
            dz1_db1: the partial gradient of the weights z1 w.r.t. the weights b1.
    '''
    #########################################
    c = a2.shape[0]
    h = a1.shape[0]

    # 2nd layer

    dL_da2 = compute_dL_da2(a2, y)
    da2_dz2 = compute_da2_dz2(a2)
    dz2_dW2 = compute_dz2_dW2(a1,c)
    dz2_db2  = compute_dz2_db2(c)



    # 1st layer

    dz2_da1 = compute_dz2_da1(W2)
    da1_dz1 = compute_da1_dz1(a1)
    dz1_dW1 = compute_dz1_dW1(x,h)
    dz1_db1 = compute_dz1_db1(h)



    #########################################
    return dL_da2, da2_dz2, dz2_dW2, dz2_db2, dz2_da1, da1_dz1, dz1_dW1, dz1_db1

#-----------------------------------------------------------------
# Back Propagation
#-----------------------------------------------------------------

#-----------------------------------------------------------------
def compute_dL_da1(dL_dz2,dz2_da1):
    '''
        Compute local gradient of the loss function L w.r.t. the activations a1 using chain rule.
        Input:
            dL_dz2: the gradient of the loss function L w.r.t. the logits z2
            dz2_da1: the gradient of the logits z2 L w.r.t. the activations a1
        Output:
            dL_da1: the partial gradient of the loss function w.r.t. the activations a1, a numpy float vector of shape h by 1.
                   Each element represents the partial gradient of the loss function L w.r.t. the i-th activation a1[i]:  d_L / d_a1[i]
    '''
    #########################################

    dL_da1 = dL_dz2.T * dz2_da1
    dL_da1 = dL_da1.T
    #########################################
    return dL_da1


#-----------------------------------------------------------------
def compute_dL_dz1(dL_da1,da1_dz1):
    '''
        Compute local gradient of the loss function L w.r.t. the logits z1 using chain rule.
        Input:
            dL_da1: the gradient of the loss function L w.r.t. the activations a1
            da1_dz1: the gradient of the activations z1 L w.r.t. the logits z1
        Output:
            dL_dz1: the partial gradient of the loss function w.r.t. the logits z1, a numpy float vector of shape h by 1.
                   Each element represents the partial gradient of the loss function L w.r.t. the i-th logit z1[i]:  d_L / d_z1[i]
    '''
    #########################################
    dL_dz1 = np.multiply(dL_da1 , da1_dz1)
    # dL_dz1 = dL_dz1.T

    #########################################
    return dL_dz1

#-----------------------------------------------------------------
def compute_gradients(dL_da2, da2_dz2, dz2_dW2, dz2_db2, dz2_da1, da1_dz1, dz1_dW1, dz1_db1):
    '''
       Given the local gradients, compute the gradient of the loss function L w.r.t. model parameters: the weights W1, W2 and biases b1 and b2.
        Input: see details in the above functions.
        Output:
            dL_dW2: the gradient of the loss function L w.r.t. the weight matrix W2
            dL_db2: the gradient of the loss function L w.r.t. the biases b2
            dL_dW1: the gradient of the loss function L w.r.t. the weight matrix W1
            dL_db1: the gradient of the loss function L w.r.t. the biases b1
    '''

    #########################################

    # the 2nd layer
    dL_dz2 = sr.compute_dL_dz(dL_da2, da2_dz2)
    dL_dW2 = sr.compute_dL_dW(dL_dz2, dz2_dW2)

    dL_db2 = sr.compute_dL_db(dL_dz2, dz2_db2)

    # the 1st layer
    dL_da1 = compute_dL_da1(dL_dz2,dz2_da1)
    dL_dz1 = compute_dL_dz1(dL_da1,da1_dz1)
    dL_dW1 = sr.compute_dL_dW(dL_dz1, dz1_dW1)
    dL_db1 = sr.compute_dL_db(dL_dz1, dz1_db1)


    #########################################

    return dL_dW2, dL_db2, dL_dW1, dL_db1


#--------------------------
# train
def train(X, Y,h=3,  alpha=0.01, n_epoch=100):
    '''
       Given a training dataset, train the FC model by iteratively updating the weights W and biases b using the gradients computed over each data instance.
        Input:
            X: the feature matrix of training instances, a float numpy matrix of shape (n by p). Here n is the number of data instance in the training set, p is the number of features/dimensions.
            Y: the labels of training instance, a numpy integer vector of shape n by 1. The values can be 0 or 1.
            h: the number of neurons in the first layer
            alpha: the step-size parameter of gradient ascent, a float scalar.
            n_epoch: the number of passes to go through the training set, an integer scalar.
        Output:
            W1: the weight matrix in the 1st layer trained on the training set
            b1: the bias in the 1st layer trained on the training set
            W2: the weight matrix in the 2nd layer trained on the training set
            b2: the bias in the 2nd layer trained on the training set
    '''
    # number of features
    p = X.shape[1]
    # number of classes
    c = max(Y) + 1

    # initialize W and b as 0
    W1 = np.asmatrix(np.zeros((h,p)))
    b1 = np.asmatrix(np.zeros((h,1)))
    W2 = np.asmatrix(np.zeros((c,h)))
    b2= np.asmatrix(np.zeros((c,1)))

    h = b1.shape[0]

    for _ in range(n_epoch):
        # go through each training instance
        for x,y in zip(X,Y):
            x = x.T
            #########################################
            # Forward pass
            z1, a1, z2, a2 =  forward(x, W1, b1, W2, b2)

            # compute local gradients
            dL_da2 = compute_dL_da2(a2, y)
            da2_dz2 = compute_da2_dz2(a2)
            dz2_dW2 = compute_dz2_dW2(a1,c)
            dz2_db2 = compute_dz2_db2(c)
            dz2_da1 = compute_dz2_da1(W2)
            da1_dz1 = compute_da1_dz1(a1)
            dz1_dW1 = compute_dz1_dW1(x,h)
            dz1_db1 = compute_dz1_db1(h)
            dL_dW2, dL_db2, dL_dW1, dL_db1 = compute_gradients(dL_da2, da2_dz2, dz2_dW2, dz2_db2, dz2_da1, da1_dz1, dz1_dW1, dz1_db1)

            # Back Propagation
            dL_da2, da2_dz2, dz2_dW2, dz2_db2, dz2_da1, da1_dz1, dz1_dW1, dz1_db1 = backward(x,y,a1,a2,W2)

            # update the paramters using gradient descent

            W1 = sr.update_W(W1, dL_dW1, alpha)
            b1 = sr.update_b(b1, dL_db1, alpha)

            W2 = sr.update_W(W2, dL_dW2, alpha)
            b2 = sr.update_b(b2, dL_db2, alpha)
            #########################################
    return W1, b1, W2, b2

#--------------------------
def predict(Xtest, W1,b1,W2,b2):
    '''
       Predict the labels of the instances in a test dataset using fully connected network.
        Input:
            Xtest: the feature matrix of testing instances, a float numpy matrix of shape (n_test by p). Here n_test is the number of data instance in the test set, p is the number of features/dimensions.
        Output:
            Y: the predicted labels of test data, an integer numpy list of length ntest. Each element can be 0, 1, ..., or (c-1)
            P: the predicted probabilities of test data to be in different classes, a float numpy matrix of shape (ntest,c). Each (i,j) element is between 0 and 1, indicating the probability of the i-th instance having the j-th class label.
    '''
    n = Xtest.shape[0]
    c = W2.shape[0]
    Y = np.zeros(n) # initialize as all zeros
    P = np.asmatrix(np.zeros((n,c)))
    for i, x in enumerate(Xtest):
        x = x.T # convert to column vector
        #########################################
        z1 = compute_z1(x,W1,b1)
        a1 = compute_a1(z1)

        z2 = compute_z2(a1,W2,b2)
        a2 = compute_a2(z2)
        Y[i] = np.argmax(a2)
        P[i, :] = a2.T

        #########################################
    return Y, P



#-----------------------------------------------------------------
# gradient checking
#-----------------------------------------------------------------

#--------------------------
def check_da1_dz1(z1,delta= 1e-7):
    '''
        Compute local gradient of the sigmoid activations a using gradient check.
        Input:
            z1: the input logits values of activation function, a float vector of shape p by 1.
            delta: a small number for gradient check, a float scalar.
        Output:
            da1_dz1: the approximated local gradient of the activations a1 w.r.t. the logits z1, a float numpy vector of shape p by 1.
                   The i-th element of da1_dz1 represents the partial gradient ( d_a1[i]  / d_z1[i] )
    '''
    p = z1.shape[0]
    da1_dz1 = np.asmatrix(np.zeros((p,1)) )
    for i in range(p):
        d = np.asmatrix(np.zeros((p,1)))
        d[i] = delta
        da1_dz1[i] = (compute_a1(z1+d)[i] - compute_a1(z1)[i]) / delta
    return da1_dz1

#--------------------------
def check_dL_dW2(x,y, W1,b1,W2,b2, delta= 1e-7):
    '''
        Compute gradient of the weights W1 a using gradient check.
        Input:
            delta: a small number for gradient check, a float scalar.
        Output:
            dL_dW1: the approximated gradient of the loss L w.r.t. the weights W1
    '''
    c,h = W2.shape
    dL_dW2 = np.asmatrix(np.zeros((c,h)))
    for i in range(c):
        for j in range(h):
            d = np.asmatrix(np.zeros((c,h)) )
            d[i,j] = delta
            z1, a1, z2, a2 = forward(x, W1, b1, W2+d, b2)
            L = sr.compute_L(a2,y)
            z1, a1, z2, a2 = forward(x, W1, b1, W2, b2)
            dL_dW2[i,j] = (L - sr.compute_L(a2,y)) / delta
    return dL_dW2

#--------------------------
def check_dL_dW1(x,y, W1,b1,W2,b2, delta= 1e-7):
    '''
        Compute gradient of the weights W1 a using gradient check.
        Input:
            delta: a small number for gradient check, a float scalar.
        Output:
            dL_dW1: the approximated gradient of the loss L w.r.t. the weights W1
    '''
    h,p = W1.shape
    dL_dW1 = np.asmatrix(np.zeros((h,p)) )
    for i in range(h):
        for j in range(p):
            d = np.asmatrix(np.zeros((h,p)) )
            d[i,j] = delta
            z1, a1, z2, a2 = forward(x, W1+d, b1, W2, b2)
            L = sr.compute_L(a2,y)
            z1, a1, z2, a2 = forward(x, W1, b1, W2, b2)
            dL_dW1[i,j] = (L - sr.compute_L(a2,y)) / delta
    return dL_dW1
