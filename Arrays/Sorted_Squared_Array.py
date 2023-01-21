def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]

    for idx in range(len(array)):
        nonSquaredNum = array[idx]
        sortedSquares[idx] = nonSquaredNum * nonSquaredNum

    sortedSquares.sort()
    return sortedSquares