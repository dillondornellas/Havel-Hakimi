#[2019-05-20] Challenge #378 [Easy] The Havel-Hakimi algorithm for graph realization
#It was a dark and stormy night. Detective Havel and Detective Hakimi arrived at the scene of the crime.
#Other than the detectives, there were 10 people present. They asked the first person, "out of the 9 other people here, how many had you already met before tonight?"
#The person answered "5". They asked the same question of the second person, who answered "3". And so on. The 10 answers they got from the 10 people were:

#Completed by Dillon D'Ornellas

def hh(input):
    while True:
        # Sort the sequence Descending
        input.sort(reverse=True)
        while True:
            # Check if True when removing '0' elements
            if not input:
                return True
            # Check for when only one element remains, cant index from -1
            # If one element remains and not = 0 then return False
            i = len(input)
            if i == 1:
                if input[0] == 0:
                    input.pop()
                else:
                    return False
            # Remove '0' element from end of list
            else:
                if input[-1] == 0:
                    input.pop()
                else:
                    break
        # Remove first element from list and store it
        n = input.pop(0)
        # Check if n is larger than remaining elements
        if n > len(input):
            return False
        # Subtract one from first n elements
        for x in range(n):
            input[x] -= 1

print(hh([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]))
print(hh([4, 2, 0, 1, 5, 0]))
print(hh([3, 1, 2, 3, 1, 0]))
print(hh([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]))
print(hh([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]))
print(hh([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]))
print(hh([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]))
print(hh([2, 2, 0]))
print(hh([3, 2, 1]))
print(hh([1, 1]))
print(hh([1]))
print(hh([]))