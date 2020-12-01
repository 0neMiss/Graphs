from room import Room
from player import Player
from world import World
from collections import deque

import random
from ast import literal_eval

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.traversal_path =[]

    def add_room(self, room_id, adjacent_rooms):
        """
        Add a vertex to the graph.
        """

        if room_id not in self.vertices:
            self.vertices[room_id] =  {}
            for room in adjacent_rooms:
                self.vertices[room_id].update({room: '?'})




    #fills the graph with empty values for me to iterate through
    def fill_graph(self):

        for room in room_graph:
            self.add_room(room, room_graph[room][1])

        #walks until it cant find any undescovered rooms to walk to.
    def random_walk(self):

        undescovered_room_in_range = True
        while undescovered_room_in_range == True:
            #check the exits of the current room
            exits = player.current_room.get_exits()
            #choose one at random
            direction = random.choice(exits)
            #once its been chosen remove it from the list in case its not a ?
            exits.remove(direction)
            room = self.vertices[player.current_room.id]

            #if the direction is a ?
            if room[direction] == '?':
                #append the direction to the path
                self.traversal_path.append(direction)
                #set the old_id so we can reference for setting two directions at once
                old_id = player.current_room.id
                #move the player so we can get the nexts rooms id

                player.travel(direction)

                #set the room id to the value of the direction of the current room
                room[direction] = player.current_room.id
                #adding both directions to and from at the same time
                if direction == 'n':
                    self.vertices[player.current_room.id]['s'] = old_id

                if direction == 's':
                    self.vertices[player.current_room.id]['n'] = old_id

                if direction == 'e':
                    self.vertices[player.current_room.id]['w'] = old_id

                if direction == 'w':
                    self.vertices[player.current_room.id]['e'] = old_id
            if len(exits) < 1:
                
                undescovered_room_in_range = self.find_unexplored(player.current_room.id)
        answer = self.traversal_path
        return answer

    def move_to_unexplored(self, room_array):

        for room in room_array:

            currRoom = player.current_room.id

            for key, value in self.vertices[currRoom].items():
                if room == value:
                    self.traversal_path.append(key)
                    player.travel(key)
        return self.traversal_path



    def find_unexplored(self, starting_room):
        """
        return a list containing the directions to the next closest unexplored room
        passing the starting room it would traverse through self.vertices to find the closest room with ? as the value to the direction provided
        starting_room would need to be the id of the room we are in.
        return false fi no more ? exist in the graph
        this function should NOT move the player but return a list of directions to add to the path and then also traverse theplayer filling in the directions as we go.
        """

        #for key, value in my_dict.items():
        #   if my_color in value:
        #       solutions.append(key)

        #setting up
        visited = set()
        queue = deque()
        queue.append([starting_room])
        #while the queue has an element
        while len(queue) > 0:
            #set the current path
            currPath = queue.popleft()

            #set the current node to the last thing appended to the path
            currRoom = currPath[-1]


            adjacent_rooms = self.vertices[currRoom].values()

            #if the node is the destination return
            if '?' in adjacent_rooms:
                self.traversal_path = self.move_to_unexplored(currPath)
                return True

            else:
            #if the node has not been visited
                if currRoom not in visited:
                    #add to set
                    visited.add(currRoom)
                    #check adjacent rooms
                    for room in self.vertices[currRoom].values():
                        # add each neighbor as the next node in the path to the queue so the queue should look like This
                        #queue = [[1,2],[1,2,3],[1,2,3,4]]
                        #evaluate which path provides us with the destination.
                        newPath = list(currPath)
                        newPath.append(room)
                        queue.append(newPath)
        print('its hitting right HERE')
        return False




# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

def fill_traversal():
    graph = Graph()
    graph.fill_graph()
    graph.random_walk()
    return graph.traversal_path

traversal_path = fill_traversal()




#traversal_path = fill_traversal()


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    print(move)
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
