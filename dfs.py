class State:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __hash__(self):
        return hash((self.x,self.y))
def is_valid_state(state,jug1_capacity,jug2_capacity):
    return 0 <= state.x <= jug1_capacity and 0 <= state.y <= jug2_capacity
def depth_first_search(jug1_capacity, jug2_capacity, target):
    visited_states=set()
    stack=[State(0,0)]
    while stack:
        current_state=stack.pop()
        if current_state.x == target or current_state.y == target:
            print("Solution found!",(current_state.x,current_state.y))
            return 
        visited_states.add(current_state)
        next_states=[
            State(min(current_state.x+current_state.y,jug1_capacity),max(0,current_state.y-(jug1_capacity-current_state.x))),
            State(max(0,current_state.x-(jug2_capacity-current_state.y)),min(current_state.y+current_state.x,jug2_capacity)),
            State(jug1_capacity,current_state.y),
            State(current_state.x,jug2_capacity),
            State(0,current_state.y),
            State(current_state.x,0)
        ]
        for next_state in next_states:
            if is_valid_state(next_state,jug1_capacity,jug2_capacity) and next_state not in visited_states:
                stack.append(next_state)
    print("Solution not found!")
if __name__=="__main__":
    jug1_capacity=int(input("Enter capacity of jug1:"))
    jug2_capacity=int(input("Enter capacity of jug2:"))
    target=int(input("Enter target amount of water"))
    print("\nDepth first search solution:")
    depth_first_search(jug1_capacity, jug2_capacity, target)
