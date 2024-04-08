import random

def build_markov_model(input_text, order):
    words = input_text.split()
    model = {}

    for i in range(len(words) - order):
        state = tuple(words[i:i + order])
        next_state = words[i + order]

        if state not in model:
            model[state] = []

        model[state].append(next_state)

    return model

def generate_text(markov_model, order, max_length=30):
    output = []
    initial_state = random.choice(list(markov_model.keys()))
    output.extend(initial_state)

    for i in range(max_length):
        current_state = tuple(output[-order:])
        if current_state not in markov_model:
            break
        next_word = random.choice(markov_model[current_state])
        output.append(next_word)

    return " ".join(output)

# Load and preprocess your input text
input_text = ""
with open("./gecko.txt") as f:
    input_text = f.read().replace("\n", " ")

# Specify the desired order and build the model
order = 2  # Change this value to the desired order
markov_model = build_markov_model(input_text, order)


def print_markov_model(markov_model, max_states=10, max_next_states=10):
    states_printed = 0
    for state, next_states in markov_model.items():
        if states_printed >= max_states:
            break

        state_str = " ".join(state)
        next_states_str = ", ".join(next_states[:max_next_states])
        print(f"State: '{state_str}' -> Next States: [{next_states_str}]")
        states_printed += 1

# Example usage:
# Assuming you have already built a Markov model, you can print it using this function
print_markov_model(markov_model, max_states=5, max_next_states=10)



# Generate the phrase
output_phrase = generate_text(markov_model, order, 50)
print("Gecko GPT: ", output_phrase)

