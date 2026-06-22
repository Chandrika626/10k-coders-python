n = 16
value=(bool(n))
if(n&(n-1==0)):
    print(n>0)
elif(n&(n-1)==0):
    print(n>0)
else:
    print(n>0 and (n&(n-1))==0)
    
n = 27
print (n > 0 and 1162261467 % n==0)

# Loops – Notes

# Observe 
# A loop is used to execute a block of code repeatedly.
# Loops help reduce code duplication.
# Python provides two main loops:
# for loop – repeats for a fixed number of times.
# while loop – repeats until a condition becomes False.

# Analyze 
# for Loop
# Used when the number of iterations is known.
# Iterates through a sequence such as a list, string, or range.
# while Loop
# Used when the number of iterations is not known.
# Executes as long as the condition is True.
# Loop Components
# Initialization – starting value.
# Condition – checks whether the loop continues.
# Update – changes the value after each iteration.
# Loop Control Statements
# break – exits the loop immediately.
# continue – skips the current iteration.
# pass – does nothing; used as a placeholder.

# Explore 
# Applications of Loops
# Printing patterns.
# Calculating sums and averages.
# Searching and sorting data.
# Traversing lists, tuples, and strings.
# Generating multiplication tables.
# Data analysis and automation tasks.
# Advantages
# Reduces repetitive code.
# Improves efficiency and readability.
# Saves development time.
# Key Points
# Avoid infinite loops.
# Ensure loop conditions are updated correctly.
# Use nested loops when a loop is required inside another loop.

# Summary
# Loops repeat a set of instructions.
# for loop is used for fixed iterations.
# while loop is used for condition-based iterations.
# break, continue, and pass control loop execution.
# Loops are essential for automation, data processing, and problem-solving.