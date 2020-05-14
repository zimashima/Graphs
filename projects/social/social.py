import random

class User:
    def __init__(self, name):
        self.name = name

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add user

        #create friendship
        for i in range(0, num_users):
            self.add_user(f"User {i +1 }")
        
        possible_friendships = []

        #avoid duplication
        for user_id in self.users:
            for friend_id in range(user_id+1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))

        # Create friendships
        #generate friendship combinations
        #avoid dupes by making sure first number is smaller than the second
        #shuffle all possible friendships
        random.shuffle(possible_friendships)

        #create for first X pairs x is total
        #friendship a -> b and b<- n
        for i in range(num_users * avg_friendships //2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        
        while q.size() > 0:
            path = q.dequeue()
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path
                visited.add(path[-1])
                for next_vert in self.friendships[path[-1]]:
                    new_path = path[:]
                    new_path.append(next_vert)
                    q.enqueue(new_path)


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        
        visited = {}
        fof = []
        visited[user_id] = [user_id]
        for friend in self.friendships[user_id]:
            visited[friend] = self.bfs(user_id, friend)
            fof.append(friend)
        while len(fof) != 0:
            for friends in self.friendships[fof[0]]:
                if friends not in fof:
                    if friends not in visited:
                        fof.append(friends)
                if friends not in visited:
                    visited[friends] = self.bfs(user_id, friends)
                    if friends not in fof:
                        fof.append(friends)
                if len(fof) > 0:
                    fof.pop(0)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
