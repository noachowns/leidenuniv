# Your classes and functions here
class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.moves = set()  # set to store the moves as strings and are unique

    def __repr__(self):
        return f"{self.name} (level: {self.level} | moves: {self.moves})"  # Output for Pokemon

class Trainer:
    def __init__(self, name, pokemons):  # Creates trainer with name and the list of Pokemons they own
        self.name = name
        self.pokemons = pokemons

    def __repr__(self):
        return f"{self.name} pokemons: {self.pokemons}"  # Output for Trainer

def add_pokemon(pokemon_mapping, name, pokemon_id, level):  # Adds a new pokemon to the pokemon_mapping dictionary as keys
    if pokemon_id in pokemon_mapping:
        print(f"Error: Pokemon ID {pokemon_id} already exists!")
    else:
        pokemon_mapping[pokemon_id] = Pokemon(name, level)  # If it does not exist, we add the pokemon name and level in pokemon_id
    return pokemon_mapping  # Returns the (possibly update) dictionary if new pokemon

def add_move(pokemon_mapping, all_moves, pokemon_id, move):
    if pokemon_id not in pokemon_mapping:  # Checks whether the pokemon ID exists in the dictionary. If pokemon not added yet it returns True and the error message
        print(f"Error: Pokemon ID {pokemon_id} not found!")
    else:
        pokemon_mapping[pokemon_id].moves.add(move)  # Adds move to the Pokemons personal set
        all_moves.add(move)  # Adds move to the global set of all moves
    return all_moves  # Function returns the updates set of moves

def add_trainer(trainer_mapping, name, trainer_id, pokemon_mapping, pokemon_ids):
    if trainer_id in trainer_mapping:
        print(f"Error: Pokemon ID {trainer_id} already exists!")  # Checks whether trainer ID already exists in the dictionary
    else:  # Runs only if the trainer ID is new
        # Make sure all pokemon IDs exist before adding the trainer
        for pid in pokemon_ids:
            if pid not in pokemon_mapping:
                print(f"Pokemon ID {pid} not found!")  # Make sure every pokemon ID actually exists. Loops through each pid in pokemon_ids
                return trainer_mapping  # Stop early if missing

        trainer_pokemons = []  # Empty lists that holds all Pokemon objects owned by trainer
        for pid in pokemon_ids:  # Loops through list of pokemon_ids again
            trainer_pokemons.append(pokemon_mapping[pid])  # Adds that object to the trainer's pokemon list

        # Create trainer using pokemon objects from mapping
        trainer_mapping[trainer_id] = Trainer(name, [pokemon_mapping[pid] for pid in pokemon_ids])

    return trainer_mapping


def strongest_pokemon(pokemon_mapping):  # Finds the pokemon with the highest level from the mapping
    if not pokemon_mapping:
        return None

    # Start wth no pokemons, then find the on with the max level
    max_pokemon = None
    for pokemon in pokemon_mapping.values():
        if max_pokemon is None or pokemon.level > max_pokemon.level:
            max_pokemon = pokemon


    return max_pokemon

# Your scripts is in here (make sure it only runs if you run the specific file)
if __name__ == "__main__":
    print("=== Pokemon Training Program ===")


    # Main data structures
    pokemon_mapping = {}  # Dictionary: ID Pokemon object
    trainer_mapping = {}  # Dictionary: ID Trainer object
    all_moves = set()  # This will store all unique moves, best to use sets

    # Adding pokemons
    add_pokemon(pokemon_mapping, "Pikachu", 1, 20)
    add_pokemon(pokemon_mapping, "Bulbasaur", 2, 12)
    add_pokemon(pokemon_mapping, "Charmander", 3, 7)
    add_pokemon(pokemon_mapping, "Squirtle", 4, 5)

    # Add moves to each pokemon
    add_move(pokemon_mapping, all_moves, 1, "Thunder Shock")
    add_move(pokemon_mapping, all_moves, 1, "Quick Attack")
    add_move(pokemon_mapping, all_moves, 2, "Vine Whip")
    add_move(pokemon_mapping, all_moves, 2, "Tackle")
    add_move(pokemon_mapping, all_moves, 3, "Flamethrower")
    add_move(pokemon_mapping, all_moves, 4, "Water Gun")

    # Add trainers and their Pokemons
    add_trainer(trainer_mapping, "Chris", 1, pokemon_mapping,[1,3])
    add_trainer(trainer_mapping, "Brock", 2, pokemon_mapping,[2,4])

    # Print all Pokemons
    print("All Pokemons:")
    for pid in pokemon_mapping:
        pokemon = pokemon_mapping[pid]
        print(pid, ": ", pokemon)
    print()

    # Print all Trainers
    print("All Trainers:")
    for tid in trainer_mapping:
        trainer = trainer_mapping[tid]
        print(tid, ":", trainer)
    print()

    # Print all unique moves
    print("All Moves:")
    print(all_moves)
    print()

    # Print strongest Pokemon
    print("Strongest Pokemon:")
    strongest = strongest_pokemon(pokemon_mapping)
    print(strongest)
    print()