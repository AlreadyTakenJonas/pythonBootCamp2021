#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def square_sum(array: list, weights: (list, float) = 1, normalise: bool = False) -> float:
    """
    This function computes the square sum of an array. You can pass a second array with the same length as the first array. The second array will be used as weights.

    Parameters
    ----------
    array : list of float
        An array of numbers.
    weights : list of float or float, optional
        An array of numbers or a single number. Will be used to compute the weighted sum of the parameter array. If the parameters weights is shorter than the array parameter, the elements of weights will be repeated until the lengths match. If the parameter weights is to long, weights without matching element in the array parameter will be ignored. If weights is a single number, it will be converted into a list. The default is 1.
    normalise : bool, optional
        If true the array of weights will be normalised with the sum of the weights. The default is False.
    
    Returns
    -------
    square_sum : float
        The weighted square sum of the the passed array..

    """
    
    # Check the type of the weights
    if not isinstance(weights, list):
        # Convert the parameter weights into an array of the length len(array)
        weights = [ weights for number in array ]
    
    # Check the length of the array
    # If the array is longer than the weights array make them the same length
    elif len(weights) < len(array):
        # Create a list of indices
        # There will be one index for every element in the parameter array
        # repeated_indices contains repeating indices of the parameter weights
        repeated_indices = [ index % len(weights) for index, number in enumerate(array) ]
        # Use repeated_indices to elongate the weights list
        weights = [ weights[index] for index in repeated_indices ]
    
    # Normalise the weights
    if normalise:
        weights = [ weight / sum(weights) for weight in weights ]
    
    # Calculate the weighted square sum
    square_sum = sum([ weight * number**2 for weight, number in zip(weights, array) ])
    
    # Return the result
    return square_sum