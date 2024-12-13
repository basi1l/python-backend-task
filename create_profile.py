from app import db
from models import Profile, User

# Fetch the user (make sure the user exists, e.g., user with email "test@example.com")
user = User.query.filter_by(email="test@example.com").first()

if user:
    profile = Profile(name="Sample Profile", user_id=user.id)  # Create a profile for the user
    db.session.add(profile)
    db.session.commit()
    print("Profile created!")
else:
    print("User not found!")
