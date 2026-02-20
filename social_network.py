"""
social_network.py

Implements a simple social network graph using an adjacency list.
People are nodes; friendships are undirected edges.
"""


class Person:
    '''
    A class representing a person in a social network.

    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).

    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''

    def __init__(self, name: str):
        self.name = name
        self.friends = []  # list[Person]

    def add_friend(self, friend: "Person") -> None:
        """Add friend if not already present (and not self)."""
        if friend is self:
            return
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network (graph using an adjacency list).

    Attributes:
        people (dict): A dictionary mapping names to Person objects.

    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''

    def __init__(self):
        self.people = {}  # dict[str, Person]

    def add_person(self, name: str) -> None:
        """Create and store a new Person, unless they already exist."""
        if name in self.people:
            print(f"Person not added. {name} already exists!")
            return
        self.people[name] = Person(name)

    def add_friendship(self, person1_name: str, person2_name: str) -> None:
        """
        Establish a bidirectional friendship by adding each person to the other's friends list.
        If either person doesn't exist, print a helpful message.
        """
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return
        if person1_name == person2_name:
            print("Friendship not created. A person cannot be friends with themselves!")
            return

        p1 = self.people[person1_name]
        p2 = self.people[person2_name]

        p1.add_friend(p2)
        p2.add_friend(p1)

    def print_network(self) -> None:
        """Print each person and their friends' names."""
        for name, person in self.people.items():
            friend_names = [f.name for f in person.friends]
            friend_names.sort()
            friends_str = ", ".join(friend_names) if friend_names else "(no friends yet)"
            print(f"{person.name} is friends with: {friends_str}")


# Test your code here
if __name__ == "__main__":
    network = SocialNetwork()

    # Add people (at least 6)
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    # Duplicate person edge case
    network.add_person("Alex")

    # Create friendships (at least 8)
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    # Missing person edge case
    network.add_friendship("Jordan", "Johnny")

    # Duplicate friendship edge case
    network.add_friendship("Alex", "Jordan")

    # Self-friendship edge case
    network.add_friendship("Alex", "Alex")

    print("\n--- Network ---")
    network.print_network()


"""
DESIGN MEMO (200–300 words)

A graph is the right structure for representing a social network because the system is fundamentally
about relationships between people. Each user can be connected to many other users, and those
connections naturally map to edges between nodes. Friendships are also bidirectional (if Alex is friends
with Jordan, Jordan is friends with Alex), which is directly modeled by an undirected graph.

A plain list would not work as well because it does not capture connections efficiently. You could store
friend pairs in a list, but then checking whether someone is already connected, finding all of a
person’s friends, or preventing duplicates would require scanning large portions of the list. A tree is
also a poor fit because trees impose a hierarchy and a single-parent structure. Social networks are not
hierarchical—people belong to overlapping groups, and there is no single root user or strict “branch”
relationship.

Using an adjacency list is a practical choice because most real networks are relatively sparse: each
person is friends with a small fraction of the entire user base. With an adjacency list, we only store
friendships that exist. Adding a person is O(1) average using a dictionary lookup, and adding a
friendship is efficient because we quickly locate each Person by name and then update each friends list.
A key trade-off is that checking whether a friend is already in a list can take O(degree) time, but this
keeps memory usage lower and the code simpler. Printing the network visits each person and their edges,
which is O(V + E), matching the natural cost of displaying the entire graph.
"""
