from manage_db import SocialDB

def populateUsers(db):
    db.addperson("Hank Hill", "hank1")
    db.addperson("Sam Doe", "samwich")
    db.addperson("Sho Gun", "Shogun")
    db.addperson("Jane Doe", "The Soldier")
    db.addperson("Todd Howard", "Bethesda")
    db.addperson("Anna", "aplpaca")

def populateFollow(db):
    db.following("hank1", "aplpaca")
    db.following("samwich", "aplpaca")
    db.following("Shogun", "aplpaca")
    db.following("The Soldier", "aplpaca")
    db.following("Bethesda", "aplpaca")
    db.following("Shogun", "Bethesda")
    db.following("The Soldier", "Bethesda")
    db.following("The Soldier", "Shogun")
    db.following("hank1", "samwich")

def makePost(db):
    db.addPost("aplpaca", "birds are cool") #1
    db.addPost("aplpaca", "cats are cool") #2
    db.addPost("aplpaca", "dogs are cool") #3
    db.addPost("aplpaca", "dinosaurs are cool") #4
    db.addPost("aplpaca", "bats are cool") #5
    db.addPost("aplpaca", "bugs are cool") #6
    db.addPost("Bethesda", "it just works") #7
    db.addPost("The Soldier", '"If fighting were to result in victory then you must fight" ~Sun Tzu') #8
    db.addPost("Shogun", "First name Sho last name Gun") #9
    db.addPost("Shogun", "Why didn't anyone warn me that becoming a robotics engineer would require math") #10
    db.addPost("The Soldier", "Godspeed, you magnificent bastard.") #11
    db.addPost("hank1", "Propane and propane accessories") #12
    db.addPost("samwich", "My name is samwich") #13
    db.addPost("Bethesda", "Buy Skyrim again") #14

def makeComment(db):
    db.comment("hank1", 2, "I prefer dogs") #1
    db.comment("Shogun", 2, "yeah") #2
    db.comment("hank1", 1, "yeah") #3
    db.comment("Shogun", 7, "It does not") #4
    db.comment("aplpaca", 10, "Loser") #5
    db.comment("aplpaca", 13, "that's a good name") #6

def likePost(db):
    db.like("Shogun", 2)
    db.like("Shogun", 1)
    db.like("Shogun", 3)
    db.like("Shogun", 4)
    db.like("Shogun", 5)
    db.like("Shogun", 6)
    db.like("The Soldier", 7)
    db.like("The Soldier", 12)
    db.like("aplpaca", 9)
    db.like("aplpaca", 10)

def makeReply(db):
    db.reply("aplpaca", 2, 1, "make your own post") #7
    db.reply("hank1", 2, 7, "Fine") #8
    db.reply("Bethesda", 7, 4, "Trust me") #9
    db.reply("samwich", 13, 6, "Thanks :)") #10
    db.reply("Shogun", 10, 5, ":(") #11

def getComment(db):
    comments = db.getComments(2)
    for comment in comments:
       print("."*comment["level"], comment["username"]) 
       print("."*comment["level"], comment["content"])

def main():
    db = SocialDB()
    populateUsers(db)
    populateFollow(db)
    makePost(db)
    makeComment(db)
    likePost(db)
    makeReply(db)
    print(db.getFeed("Shogun", 20))
    getComment(db)

if __name__ == "__main__":
    main()
