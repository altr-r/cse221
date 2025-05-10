times = int(input())

for i in range(times):
    st = input()

    operation = st.split(" ")[1::]

    if operation[1] == "+":
        print(float(operation[0]) + float(operation[2]))
    elif operation[1] == "-":
        print(float(operation[0]) - float(operation[2]))
    elif operation[1] == "/":
        print(float(operation[0]) / float(operation[2]))
    elif operation[1] == "*":
        print(float(operation[0]) * float(operation[2]))