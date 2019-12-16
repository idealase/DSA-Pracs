from time import localtime


class ListNode:
    def __init__(self, in_value):
        self.value = in_value
        self.next = None

    def get_value(self):
        """this will get the value"""
        return self.value

    def set_value(self, in_value):
        self.value = in_value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        empty = (self.head is None)
        return empty

    def insert_first(self, new_value):
        new_node = ListNode(new_value)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def insert_last(self, new_value):
        new_node = ListNode(new_value)
        if self.is_empty():
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.get_next():
                curr_node = curr_node.get_next()
            curr_node.set_next(new_node)

    def peek_first(self):
        if self.is_empty():
            raise ValueError
        else:
            node_value = self.head.get_value()
            return node_value

    def peek_last(self):
        if self.is_empty():
            raise ValueError
        else:
            curr_node = self.head
            while curr_node.get_next():
                curr_node = curr_node.get_next()
            node_value = curr_node.get_value()
            return node_value

    def remove_first(self):
        if self.is_empty():
            raise ValueError
        else:
            node_value = self.head.get_value()
            self.head = self.head.get_next()
            return node_value

    def remove_last(self):
        if self.is_empty():
            raise ValueError
        elif not self.head.get_next():
            node_value = self.head.get_value()
            self.head = None
        else:
            prev_node = None
            curr_node = self.head
            while curr_node.get_next():
                prev_node = curr_node
                curr_node = curr_node.get_next()
            prev_node.set_next(None)
            node_value = curr_node.get_value()
        return node_value

    def __iter__(self):
        self._curr = self.head
        return self

    def __next__(self):
        curval = None
        if not self._curr:
            raise StopIteration
        else:
            curval = self._curr.value
            self._curr = self._curr.next
        return curval

    def display(self):
        if not self.is_empty():
            iter_ob = iter(self)
            value = next(iter_ob)
            for value in iter_ob:
                print(value, end="\n")
            print("-- End of List --")
        else:
            print("None")

    def get_count(self):
        return self._get_count_rec(self.head)

    def _get_count_rec(self, node):
        if not node:
            return 0
        else:
            return 1 + self._get_count_rec(node.get_next())


class SocNet:
    def __init__(self):
        self.humanoids = LinkedList()
        self.connections = LinkedList()

    def add_human(self, name):
        # init DSAGraphVertex object
        new_human = Humanoid(name)
        # add to humanoids linked list
        self.humanoids.insert_last(new_human)

    def has_humanoid(self, name):
        has_h = False
        humanoids_iter = iter(self.humanoids)
        hum = next(humanoids_iter)
        for hum in humanoids_iter:
            if hum.name == name:
                has_h = True
        return has_h

    def add_relationship(self, name1, name2):
        """
        --- IMPORTANT METHOD ---
        :param name1: Name of the INFLUENCER
        :param name2: Name of the FOLLOWER
        :return:
        """
        # first checks that these people are present in the network
        if self.has_humanoid(name1) and self.has_humanoid(name2):
            influencer = self.get_human(name1)
            follower = self.get_human(name2)
            influencer.followers.insert_last(follower)
            influencer.links.insert_last(follower)      # LEGACY remove later
            follower.following.insert_last(influencer)
            follower.links.insert_last(influencer)      # LEGACY remove later
            new_conx = SocConx(influencer.name, follower.name)
            self.connections.insert_last(new_conx)
        else:
            print("Can't find human")

    def get_humanoid_count(self):
        return self.humanoids.get_count()

    def get_connection_count(self):
        return self.connections.get_count()

    def get_human(self, name):
        humanoids_iter = iter(self.humanoids)
        hum = next(humanoids_iter)
        for hum in humanoids_iter:
            if hum.name == name:
                return hum

    def get_adjacent(self, name):
        h = self.get_human(name)
        h.get_adjacent()

    def show_adjacent(self, name):
        h = self.get_human(name)
        hlinks = h.get_adjacent()
        hlinks.display()

    def show_followers(self, name):
        h = self.get_human(name)
        hfollowers = h.get_followers()
        hfollowers.display()

    def show_following(self, name):
        h = self.get_human(name)
        hfollowing = h.get_following()
        hfollowing.display()

    def is_adjacent(self, name1, name2):
        is_adj = False
        h1 = self.get_human(name1)
        h1links = h1.get_adjacent()
        for link in h1links:
            if link.name == name2:
                is_adj = True
        return is_adj

    def display_as_list(self):
        vertices_iter = iter(self.humanoids)
        val = next(vertices_iter)
        print("SocNet Members:")
        for val in vertices_iter:
            print(val, end="\n")

    def display_as_matrix(self):
        pass

    def statistics(self):
        print("\n --- Network Statistics --- \n")
        print("Total Members: " + str(self.get_humanoid_count()))
        print("Total Connections: " + str(self.get_connection_count()))
        humanoids_iter = iter(self.humanoids)
        hum = next(humanoids_iter)
        for hum in humanoids_iter:
            print("\nName: " + hum.get_name())
            print("Followers: " + str(hum.get_followers_count()))
            print("Following: " + str(hum.get_following_count()))


    def infection_report(self):
        """
        Generates an output of all humans in the network and their
        infection status. Sorted by Infected or Healthy
        :return:
        """
        print("\n -- Infection Status Report -- \n")
        humanoids_iter = iter(self.humanoids)
        val = next(humanoids_iter)
        print("Infected Scum:")
        for val in humanoids_iter:
            if val.is_infected():
                print("\t" + val.get_name())
        print("\nHealthy Pre-scum:")
        for val in humanoids_iter:
            if not val.is_infected():
                print("\t" + val.get_name())
        print("\n -- Infection Status Current as of -- ")
        time_now = localtime()
        print("\tDate: " + str(time_now[2]) + "-" + str(time_now[1]) + "-" +
              str(time_now[0]))
        print("\tTime: " + str(time_now[3]) + ":" + str(time_now[4]) + ":" +
              str(time_now[5]))

    def post(self, poster, negativity):
        if self.has_humanoid(poster):       # check poster exists
            inf = self.get_human(poster)    # return poster as the influencer
            if inf.is_infected():
                neg_mod = 0.2 * inf.get_follower_count()
            else:
                neg_mod = 0.01 * inf.get_follower_count()
            transmitted_neg = negativity * neg_mod

            followers_iter = iter(inf.get_followers())
            next_follower = next(followers_iter)
            for next_follower in followers_iter:
                # universal negativity response
                next_follower.add_negativity(transmitted_neg)
                # unique local negativity response
                unique_neg = negativity * \
                             (1 / next_follower.get_following_count())
                next_follower.add_negativity(unique_neg)

                next_follower.infection_check()
        else:
            print("Can't find poster " + poster)



class Humanoid:
    def __init__(self, name, negativity=0.1):
        self.name = name
        self.negativity = negativity      # baseline starting negativity
        self.followers = LinkedList()
        self.following = LinkedList()
        self.links = LinkedList()
        self.infected = False
        self.visited = False        # TODO: remove????

    def get_name(self):
        return self.name

    def get_negativity(self):        # TODO: REMOVE POSSIBLY
        return self.negativity

    def add_negativity(self, neg_addition):
        self.negativity += neg_addition

    def get_adjacent(self):     # TODO: LEGACY ... REMOVE POSSIBLY
        return self.links

    def get_followers(self):
        return self.followers

    def get_followers_count(self):
        return self.followers.get_count()

    def get_following(self):
        return self.following

    def get_following_count(self):
        return self.following.get_count()

    def add_edge(self, vertex):     # TODO: LEGACY ... REMOVE POSSIBLY
        self.links.insert_first(vertex)

    def infect(self):
        self.infected = True

    def infection_check(self):
        if self.get_negativity() > 0.8:
            self.infect()

    def is_infected(self):
        return self.infected

    def get_friend_count(self):     # TODO: LEGACY ... REMOVE POSSIBLY
        return self.links.get_count()

    def get_follower_count(self):
        return self.followers.get_count()

    def get_following_count(self):
        return self.following.get_count()

    def set_visited(self):
        pass

    def clear_visited(self):
        pass

    def get_visited(self):
        pass

    def __str__(self):
        return "Name: {0}\t\t\t Negativity: {1}\t\t Infected: {2}"\
            .format(self.name, round(self.negativity, 2), self.infected)


class SocConx:  # GraphEdge
    def __init__(self, follower, influencer, interest=0.5):
        self.label = str(follower) + " follows " + str(influencer)
        self.follower = follower
        self.influencer = influencer
        self.interest = interest

    def get_label(self):
        return self.label

    def get_value(self):
        return self.interest

    def get_from(self):
        return self.influencer

    def get_to(self):
        return self.follower

    def update_interst(self, modifier):
        self.interest = self.interest * modifier

    def __str__(self):
        return "{0} is following {1}, " \
               "with an interest level of {2}"\
            .format(self.follower, self.influencer, self.interest)
