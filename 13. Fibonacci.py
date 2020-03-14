#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def input_text(prompt):
    return int(input(prompt))

def calc_fib(num):
    current_fib = 0
    final_fib = 0
    for i in range(1,num+1):
        if num==1:
            final_fib==1
        else:
            final_fib=current_fib+i
            current_fib=final_fib
            print(final_fib, end=" ")
    print ("\n",num,"th fibanocci Number is ", final_fib)

calc_fib(input_text("Please Input the number of fib sequence you are going to find :"))