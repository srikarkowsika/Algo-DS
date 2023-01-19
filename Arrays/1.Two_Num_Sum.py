def twoNumberSum(array, targetSum):
    for i in range(len(array - 1)):
        numOne = array[i]
        for j in range(i + 1, len(array)):
            numTwo = array[j]
            if numOne + numTwo == targetSum:
                return [numOne,  numTwo]
    return []
