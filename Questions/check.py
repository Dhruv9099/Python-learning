# Let's learn about list comprehensions! You are given three integers  and  representing
# the dimensions of a cuboid along with an integer . Print a list of all possible 
# coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . 
# Please use list comprehensions rather than multiple loops, as a learning exercise.


# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# all_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in  range(z+1) if (i+j+k)!=n]
# print(all_list)






# 
"""
    Given the participants' score sheet for your University Sports Day, 
    you are required to find the runner-up score. You are given  scores. 
    Store them in a list and find the score of the runner-up.
Input Format

The first line contains n. 
The second line contains an array  A[] of n  integers each separated by a space.

Constraints
2<= n<= 10
-100<=A[i]<=100

Output Format
Print the runner-up score.
"""

# mehtod 1

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Convert the list to a set to remove duplicates, then back to a list
    unique_scores = list(set(arr))
    
    # Sort the unique scores in descending order
    unique_scores.sort(reverse=True)
    
    # The runner-up score is the second element in the sorted list
    runner_up_score = unique_scores[1]
    
    print(runner_up_score)




# mehtod 2
def find_runner_up_score():
    n = int(input("Enter the number of participants: "))
    scores = list(map(int, input("Enter the scores separated by space: ").split()))
    
    # Removing duplicates by converting to a set, then back to a list
    unique_scores = list(set(scores))
    
    # Sort the list in descending order
    unique_scores.sort(reverse=True)
    
    # Check if there are at least two unique scores
    if len(unique_scores) < 2:
        print("There is no runner-up score.")
    else:
        # The runner-up score is the second element in the sorted list
        runner_up_score = unique_scores[1]
        print("Runner-up score:", runner_up_score)

find_runner_up_score()
