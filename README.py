import math
import random

# Fun math facts
math_facts = [
    "Did you know? The number π (pi) never ends and never repeats.",
    "The golden ratio (1.618...) appears in nature, art, and architecture.",
    "Zero is the only number that can't be represented in Roman numerals.",
    "A 'googol' is 10^100, much larger than the number of atoms in the universe!",
    "The number 2 and 5 are the only primes that end with 2 or 5."
]

# History storage
history = []

def calculator():
    print("🧮 Welcome to the Special Calculator 🧮")
    print("Type 'exit' to quit, 'history' to view past calculations.\n")

    while True:
        expr = input("Enter your calculation: ")

        if expr.lower() == "exit":
            print("Goodbye! 👋")
            break
        elif expr.lower() == "history":
            print("\n📜 Calculation History:")
            if not history:
                print("No calculations yet.")
            else:
                for h in history:
                    print(h)
            print()
            continue

        try:
            # Evaluate safely
            result = eval(expr, {"__builtins__": None}, 
                          {"sqrt": math.sqrt, "pow": pow, "abs": abs, "round": round, "pi": math.pi, "e": math.e})
            
            history.append(f"{expr} = {result}")
            print(f"✅ Result: {result}")

            # Random math fact
            print(f"💡 Fun Fact: {random.choice(math_facts)}\n")

        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    calculator()
