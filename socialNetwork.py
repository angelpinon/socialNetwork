##social network##

class User:
    def __init__(self, firstName, lastName, userName, bio, userId):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.bio = bio
        self.userId = userId
        self.friends = []
        self.posts = []


    def addFriends(self, userName):
        self.friends.append(userName)
        
##    def unFriend(self, ):

    def viewFeed(self, friends):
        self.posts.append(userName)
        
if __name__ == "__main__":
    firstName = "Angel"
    lastName = "Pinon"
    userName = "intergalactor_"
    bio = "yo whats up dogs, this is ya boii angel"
    userId = "42069"
##    viewFeed(Angel.friends)

    Angel = User(firstName, lastName, userName, bio, userId)
    ham = User("Ham", "Burgler", "THE_hamburgler", "hide your burgers before they get whats coming to them >:( ", "12345")
    doe = User("Doe", "Doppler", "$$$DoeDoppler$$$", "youngest flexer of all time", "09876")

    Angel.addFriends("THE_hamburgler")
    Angel.addFriends("$$$DoeDoppler$$$")

    ham.posts.append("this is a post")
    doe.posts.append("hellllloooo")
   
    print(Angel.firstName)
    print(ham.firstName, ham.lastName)
    print(doe.firstName, doe.lastName)
    
    print(Angel.friends)
    print(Angel.posts)
##    print(ham.posts)
##    print(doe.posts)

    for f in Angel.friends:
        print(f.posts)
    
    
    

    
