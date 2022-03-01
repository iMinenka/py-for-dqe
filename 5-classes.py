"""
Create a tool, which will do user generated news feed:
- User select what data type he wants to add
- Provide record type required data
- Record is published on text file in special format

You need to implement:
- News – text and city as input. Date is calculated during publishing.
- Private ad – text and expiration date as input. Day left is calculated during publishing.
Your unique one with unique publish rules.

Each new record should be added to the end of file. Commit file in git for review.
"""
from datetime import datetime, date
from random import choice


class Post:
    def __init__(self, body_text="post", post_type="post"):
        self.body_text = body_text
        self.post_type = post_type

    def post_title(self, post_type):
        return "\n\n" + post_type + 10 * "-" + "\n"

    def post_body(self, text):
        return text + "\n"

    def publish(self):
        with open("feed.txt", "a") as file:
            file.write("\n\nPost" + 5 * "-" + "\n")
            file.write(self.body_text)


class News(Post):
    def __init__(self, text, location):
        Post.__init__(self, body_text=text)
        self.location = location
        self.post_type = "News"

    def publish_date(self):
        pub_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        return pub_date

    def publish(self):
        with open("feed.txt", "a") as file:
            file.write(self.post_title(self.post_type))
            file.write(self.post_body(self.body_text))
            file.write(self.location + ", ")
            file.write(self.publish_date())


class Ads(Post):
    def __init__(self, text, expiration):
        Post.__init__(self, body_text=text)
        self.expiration = expiration
        self.title = "Private Ad"

    def day_left(self):
        return self.day_left_calc().days

    def day_left_calc(self):
        today = date.today()
        user_date = datetime.strptime(self.expiration, "%Y-%m-%d").date()
        return user_date - today

    def publish(self):
        with open("feed.txt", "a") as file:
            file.write(self.post_title(self.title))
            file.write(self.post_body(self.body_text))
            file.write(f"Actual until: {self.expiration}" + ", ")
            file.write(f"{self.day_left()} days left")

class Weather(Post):
    def __init__(self, city, day):
        Post.__init__(self)
        self.city = city
        self.day = day
        self.title = "Weather Forecast"

    def sky(self):
        forecast = ["clear", "cloudy", "partially cloudy"]
        return choice(forecast)

    def temperature(self):
        temperature_scale = range(-30, 40)
        return choice(temperature_scale)


    def publish(self):
        with open("feed.txt", "a") as file:
            file.write(self.post_title(self.title))
            file.write(f"On {self.day} the sky in {self.city} will be most probably {self.sky()}.")
            file.write(f"\nThe temperature will be around {self.temperature()} degrees.")


dataType = input("Select 1 - news, 2 - ad, 3 - weather: ")
if dataType.isalpha() or int(dataType) not in [1, 2, 3]:
    print(f"Incorrect value {dataType}. Please enter 1, 2 or 3.")

if int(dataType) == 1:
    news = input("Please enter news text: ")
    city = input("Enter news city: ")
    n = News(news, city)
    n.publish()

elif int(dataType) == 2:
    ad = input("Please enter ad text: ")
    expiration = input("Enter ad expiration date yyyy-mm-dd: ")
    a = Ads(ad, expiration)
    a.publish()

elif int(dataType) == 3:
    city = input("Please enter city: ")
    day = input("Enter a date (yyyy-mm-dd): ")
    w = Weather(city, day)
    w.publish()

else:
    print("Please enter 1 (for news) or 2 (for private ad)")
