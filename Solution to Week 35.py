def majority_vote(list_elements):

    """STEP 1 - Stating condition 1 ------> If length of given list is greater than 0."""
    if len(list_elements) > 0:
        """STEP 1a - Obtain the most frequent element and then collate it in a list, based on the number of time it  
        occurs."""
        maj_of_elements = [i for i in list_elements if (list_elements.count(i) > len(list_elements) / 2)]
        """STEP 1b - Obtain the unique form of the most frequent element from the initially created list."""
        if len(maj_of_elements) > 0:
            unique_count = maj_of_elements[0]
            print(f'"{unique_count}"')
            """STEP 1c - If no element is strictly greater than N/2, return "None"."""
        else:
            print("None")
        """STEP 2 - Stating condition 1 ------> If length of given list is not greater than 0, return "None"."""
    else:
        print ("None")


majority_vote(["A", "A", "B"])

majority_vote(["A", "A", "A", "B", "C", "A"])

majority_vote(["A", "B", "B", "A", "C", "C"])

majority_vote([])

majority_vote(["F", "F", "B", "F", "F", "C"])
