##social network##
import sys
import optparse

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

    def viewMyProfile(self):
        print(self.userName)
        print("")
        print("friends:")
        self.viewFriends()
        print("")
        print("my posts:")
        print(self.posts)
        
        
if __name__ == "__main__":
    
    Angel = User("intergalactor_")
    ham = User("THE_hamburgler")
    doe = User("$$$DoeDoppler$$$") 

    Angel.addFriend(ham)
    Angel.addFriend(doe)

    ham.addPost("this is library")
    doe.addPost("hellllloooo")
    Angel.addPost("this isss myyyyy post")
    Angel.addPost("this is another post. awesome")

    parser = optparse.OptionParser()
parser.add_option('-n', '--name', dest='name', help='Your Name')

(options, args) = parser.parse_args()

if options.name is None:
    options.name = input('profile? Or, newsfeed?:')

if options.name == ("profile"):
    sayOption = Angel.viewMyProfile()
elif options.name == ("newsfeed"):
    sayOption = Angel.viewFeed()
##elif options.name == ("see friends"):
##    sayOption = Angel.viewFeed()
    
    
