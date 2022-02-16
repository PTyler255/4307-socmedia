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
    db.addPost("aplpaca", "birds are cool")
    db.addPost("aplpaca", "cats are cool")
    db.addPost("aplpaca", "dogs are cool")
    db.addPost("aplpaca", "dinosaurs are cool")
    db.addPost("aplpaca", "bats are cool")
    db.addPost("aplpaca", "bugs are cool")
    db.addPost("Bethesda", "it just works")
    db.addPost("The Soldier", '"If fighting were to result in victory then you must fight" ~Sun Tzu')
    db.addPost("Shogun", "First name Sho last name Gun")
    db.addPost("Shogun", "Why didn't anyone warn me that becoming a robotics engineer would require math")
    db.addPost("The Soldier", "Godspeed, you magnificent bastard.")
    db.addPost("hank1", "Propane and propane accessories")
    db.addPost("samwich", "My name is samwich")
    db.addPost("Bethesda", "Buy Skyrim again")

def makeComment(db):
    db.comment("Shogun", 2, "yeah")
    db.comment("hank1", 2, "I prefer dogs")
    db.comment("hank1", 1, "yeah")
    db.comment("Shogun", 7, "It does not")
    db.comment("aplpaca", 10, "Loser")
    db.comment("aplpaca", 13, "that's a good name")

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

def main():
    db = SocialDB()
    populateUsers(db)
    populateFollow(db)
    makePost(db)
    makeComment(db)
    likePost(db)
    print(db.getFeed("Shogun", 20))

if __name__ == "__main__":
    main()
