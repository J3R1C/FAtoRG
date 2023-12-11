# Regular Grammar is 4Tuple
# v = set of variables or non-terminal symbols
# t = set of terminal symbols
# s = starting symbol
# p = production rules for terminals and non-terminals
# ∈ = final state / epsilon

def main():
    while True:
        v = []
        t = []
        transitionsRLG = {}
        transitionsLLG = {}
        final_states = set() 

        #setters and getters
        num_states = int(input("Enter number of states(variables): "))
        for i in range(1, num_states + 1):
            state_name = input(f"Enter state {i}: ")
            v.append(state_name)

        num_strings = int(input("Enter number of strings(terminals): "))
        for i in range(1, num_strings + 1):
            string = input(f"Enter string {i}: ")
            t.append(string)

        for state in v:
            num_paths = int(input(f"Enter number of paths for {state}: "))
            for i in range(num_paths):
                path = input(f"Enter terminal  for variable {state}: ")
                to_state = input("going to variable: ")
                pRLG = f"{state}--->{path}{to_state}"
                pLLG = f"{state}--->{to_state}{path}"
                transitionsRLG[pRLG] = to_state
                transitionsLLG[pLLG] = to_state

        s = input("Enter initial state: ")
        final_state = input("Enter final state (use ',' to separate multiple final states): ")
        final_states.update(final_state.split(','))

        #output construction
        print("\nStates(V):", ', '.join(v))
        print("Strings(T):", ', '.join(t))

        print("\nGrammar(P):\n")
        print("RLG:")
        for pRLG, to_state in transitionsRLG.items():
            print(f"{pRLG}")

        for state in final_states:
            print(f"{state}--->∈")     
        
        print("\nLLG:")

        for pLLG, to_state in transitionsLLG.items():
            print(f"{pLLG}")

        for state in final_states:
            print(f"{state}--->∈")    

        print("\nInitial State(S):", s)
        print("Final State:", ', '.join(final_states))

        choice = input("Try again? (Y/N): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()






