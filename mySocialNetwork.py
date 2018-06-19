##social network##

class User:
    def __init__(self,userName):
        self.userName = userName
        self.firstName = ""
        self.lastName = ""
        self.bio = ""
        self.userId = ""
        self.friends = []
        self.posts = []

    def addFriend(self, obj):
        self.friends.append(obj)

    def viewFeed(self):
        for friend in self.friends:
            print(friend.posts)

    def addPost(self, post):
        self.posts.append(post)

    def viewFriends(self):
        for friend in self.friends:
            print(friend.userName)

    def unFriend(self, obj):
        for friend in self.friends:
            if friend.userName == obj.userName:
                self.friends.remove(obj)
        
if __name__ == "__main__":
    
    Angel = User("user_name")
    ham = User("THE_hamburgler")
    doe = User("$$$DoeDoppler$$$") 

    Angel.addFriend(ham)
    Angel.addFriend(doe)

    ham.addPost("this is a post")
    doe.addPost("hellllloooo")

    Angel.viewFriends()
    Angel.viewFeed()
    
    
    
    
    
