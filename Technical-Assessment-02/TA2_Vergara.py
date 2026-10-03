import random

# TASK 1: SET UP THE ENVIRONMENT
class TwoRoomEnvironment:
    """Represents the 2-room environment (Rooms A and B)."""
    def __init__(self, state_a="Clean", state_b="Clean"):
        # Initializing two rooms using a Python dictionary
        self.rooms = {
            'A': state_a.capitalize(),
            'B': state_b.capitalize()
        }

    def is_dirty(self, room: str) -> bool:
        """Function to check if a specified room is dirty."""
        return self.rooms.get(room) == "Dirty"

    def clean_room(self, room: str):
        """Function to clean a specified room."""
        self.rooms[room] = "Clean"

# TASK 2: IMPLEMENT THE RULE-BASED AGENT
class RuleBasedVacuumAgent:
    """Represents the rule-based reflex agent."""
    def __init__(self, initial_location='A'):
        self.current_location = initial_location.upper()

    def move(self):
        """Switches the agent's location between Room A and Room B."""
        self.current_location = 'B' if self.current_location == 'A' else 'A'

    def perceive_and_act(self, env: TwoRoomEnvironment) -> str:
        """Perceives environment state and acts according to predefined rules."""
        curr = self.current_location
        
        # Rule 1: If current room is dirty, clean it.
        if env.is_dirty(curr):
            env.clean_room(curr)
            return f"Cleaned Room {curr}"
            
        # Rule 2: If current room is clean, move to the other room.
        else:
            self.move()
            return f"Moved to Room {self.current_location}"

# TASK 3: RUN THE SIMULATION (2 ROOMS) WITH RETRY OPTION
def run_task3_simulation():
    while True:
        print("\nTASKS 1, 2, & 3: 2-ROOM AGENT SIMULATION")
        
        # Task 1: User inputs for environment setup
        state_a = input("Enter initial state for Room A (Clean/Dirty): ").strip().capitalize()
        state_b = input("Enter initial state for Room B (Clean/Dirty): ").strip().capitalize()
        start_loc = input("Enter agent starting room (A/B): ").strip().upper()
        if start_loc not in ['A', 'B']:
            start_loc = 'A'

        env = TwoRoomEnvironment(state_a=state_a, state_b=state_b)
        agent = RuleBasedVacuumAgent(initial_location=start_loc)

        try:
            steps = int(input("Enter number of simulation steps to run: "))
        except ValueError:
            print("Invalid input! Defaulting to 4 steps.")
            steps = 4

        print("\n" + "-" * 65)
        print(f"INITIAL STATE: {env.rooms} | AGENT START: Room {agent.current_location}")
        print("-" * 65)

        # Task 3: Simulation loop
        for step in range(1, steps + 1):
            loc_before = agent.current_location
            action = agent.perceive_and_act(env)
            
            print(f"\nStep {step}:")
            print(f"  Agent Location Before Action : Room {loc_before}")
            print(f"  Action Taken                 : {action}")
            print(f"  Current Environment State    : {env.rooms}")

        print("Simulation Complete.")

        # Retry prompt
        retry = input("\nDo you want to retry this 2-Room simulation? (y/n): ").strip().lower()
        if retry != 'y':
            print("Returning to main menu...\n")
            break

# OPTIONAL (BONUS TASK): 3 ROOMS WITH TEXT-GRID VISUALIZATION & RETRY
class ThreeRoomEnvironment:
    """Environment for Rooms A, B, and C."""
    def __init__(self, a, b, c):
        self.rooms = {'A': a.capitalize(), 'B': b.capitalize(), 'C': c.capitalize()}

    def is_dirty(self, room):
        return self.rooms.get(room) == "Dirty"

    def clean(self, room):
        self.rooms[room] = "Clean"

    def get_dirty_rooms(self):
        return [r for r, s in self.rooms.items() if s == "Dirty"]


class BonusAgent:
    """Agent that navigates 3 rooms and targets dirty rooms randomly."""
    def __init__(self, start='A'):
        self.location = start.upper()

    def perceive_and_act(self, env: ThreeRoomEnvironment):
        curr = self.location
        if env.is_dirty(curr):
            env.clean(curr)
            return f"Cleaned Room {curr}"

        dirty_rooms = [r for r in env.get_dirty_rooms() if r != curr]
        if dirty_rooms:
            self.location = random.choice(dirty_rooms)
            return f"Moved to Dirty Room {self.location}"
        else:
            other_rooms = [r for r in ['A', 'B', 'C'] if r != curr]
            self.location = random.choice(other_rooms)
            return f"Patrolled to Clean Room {self.location}"


def render_grid(env_rooms, agent_loc):
    """Evenly spaced 1x3 grid box with aligned boundary borders."""
    row_strings = []
    for r in ['A', 'B', 'C']:
        status = env_rooms[r]
        agent_str = "[*AGENT*]" if agent_loc == r else ""
        content = f"Room {r}: {status} {agent_str}".strip()
        row_strings.append(f"| {content:<24} ")
    
    border = "+--------------------------" * 3 + "+"
    print(border)
    print("".join(row_strings) + "|")
    print(border)


def run_bonus_simulation():
    while True:
        print("\nBONUS TASK: 3-ROOM GRID SIMULATION")
        
        state_a = input("Enter state for Room A (Clean/Dirty): ").strip().capitalize()
        state_b = input("Enter state for Room B (Clean/Dirty): ").strip().capitalize()
        state_c = input("Enter state for Room C (Clean/Dirty): ").strip().capitalize()
        start_loc = input("Enter starting room (A/B/C): ").strip().upper()
        if start_loc not in ['A', 'B', 'C']:
            start_loc = 'A'

        try:
            steps = int(input("Enter number of simulation steps: "))
        except ValueError:
            print("Invalid input! Defaulting to 4 steps.")
            steps = 4

        b_env = ThreeRoomEnvironment(state_a, state_b, state_c)
        b_agent = BonusAgent(start_loc)

        print("\nInitial Grid:")
        render_grid(b_env.rooms, b_agent.location)

        for s in range(1, steps + 1):
            act = b_agent.perceive_and_act(b_env)
            print(f"\nStep {s}: {act}")
            render_grid(b_env.rooms, b_agent.location)

        print("\n" + "=" * 65)
        print("Bonus Simulation Complete.")
        print("=" * 65)

        # Retry prompt
        retry = input("\nDo you want to retry this 3-Room simulation? (y/n): ").strip().lower()
        if retry != 'y':
            print("Returning to main menu...\n")
            break

# MAIN EXECUTION MENU
if __name__ == "__main__":
    while True:
        print("\nCS0065 TECHNICAL ASSESSMENT 2")
        print("1. Run Tasks 1, 2 & 3 (2-Room Simulation)")
        print("2. Run Bonus Task (3-Room Text-Grid Simulation)")
        print("3. Exit")
        
        choice = input("\nSelect an option (1/2/3): ").strip()
        
        if choice == '1':
            run_task3_simulation()
        elif choice == '2':
            run_bonus_simulation()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")