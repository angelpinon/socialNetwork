##social network##
import optparse

print("MySpace 2.0")
print("")

class User:
    def __init__(self,userName):
        self.userName = userName
        self.firstName = ""
        self.lastName = ""
        self.bio = ""
        self.userId = ""
        self.friends = []
        self.posts = []

##class POST:
##    def __init__(self, postContent):
##        self.postContent = postContent
##        self.postId = ""
##        self.commnets = []
    
    def addFriend(self, obj):
        self.friends.append(obj)

    def viewFeed(self):
        for friend in self.friends:
            print("")
            print(friend.userName)
            print(friend.posts)
            print("")

    def addPost(self, post):
        self.posts.append(post)

    def viewFriends(self):
        for friend in self.friends:
            print(friend.userName)

    def unFriend(self, obj):
        for friend in self.friends:
            if friend.userName == obj.userName:
                self.friends.remove(obj)

    def viewMyProfile(self):
        print(self.userName)
        print("")
        print("friends:")
        self.viewFriends()
        print("")
        print("posts:")
        print(self.posts)
        
        
if __name__ == "__main__":
    
    Angel = User("intergalactor_")
    ham = User("THE_hamburgler")
    doe = User("DoeDoppler") 

    Angel.addFriend(ham)
    Angel.addFriend(doe)
    doe.addFriend(Angel)
    doe.addFriend(ham)
    ham.addFriend(Angel)
    ham.addFriend(doe)

    ham.addPost("this is library")
    ham.addPost("ESSSSKEEEETTTIIIIITTTT")

    doe.addPost("hellllloooo")
    doe.addPost("youngest flexa of all time")

    Angel.addPost("this isss myyyyy post")
    Angel.addPost("this is another post. awesome")

parser = optparse.OptionParser()
parser.add_option('-n', '--name', dest='name', help='Your Name')

(options, args) = parser.parse_args()

if options.name is None:
    options.name = input('profile? newsfeed? OR friends?:')

if options.name == ("profile"):
    sayOption = Angel.viewMyProfile()
elif options.name == ("newsfeed"):
    sayOption = Angel.viewFeed()
elif options.name == ("friends"):
    sayOption = Angel.viewFriends()





       


    
