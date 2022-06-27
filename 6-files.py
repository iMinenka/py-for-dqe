"""
Expand previous Homework 5 with additional class, which allow to provide records by text file:
1. Define your input format (one or many records)
2. Default folder or user provided file path
3. Remove file if it was successfully processed
4. Apply case normalization functionality form Homework 3/4
"""
from datetime import datetime, date
from random import choice
import os


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

    def publish_news(self, title, text, city):
        self.post_type = title
        self.text = text
        self.city = city

        with open("feed.txt", "a") as file:
            file.write(self.post_title(self.post_type))
            file.write(self.post_body(self.text))
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


class Files(News):
    def __init__(self, file_path):
        Post.__init__(self)
        self.file_path = file_path

    def reader(self, file):
        self.file = file
        with open(file, "r") as f:
            data_obj = f.readlines()
        return data_obj

    def cleaner(self, raw_data):
        data = []
        for d in raw_data:
            if d.strip("\n"):
                data.append(d.strip("\n"))
        return data

    def parser(self, data):
        for i in range(len(data)):
            if data[i] == "News":
                news_title = data[i]
                news_text = data[i + 1]
                city = data[i + 2]
                News.publish_news(self, news_title, news_text, city)
            elif data[i] == "Private Ad":
                ad_title = data[i]
                ad_text = data[i + 1]
                exp_date = data[i + 2]
            else:
                continue

        # os.remove(self.file_path)


while True:
    dataType = input("Select 1 - news, 2 - ad, 3 - weather, 4 - file upload: ")
    if dataType.isalpha() or int(dataType) not in [1, 2, 3, 4]:
        print(f"Incorrect value {dataType}. Please enter 1, 2, 3 or 4.")
    else:
        break

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

else:  # int(dataType) == 4:
    default_file = "data.txt"
    default_path = os.getcwd()
    file_upload = input(f"Enter full path with file OR only file name (default location {default_path}): ")
    file_upload = os.path.normpath(file_upload)
    if len(file_upload.split(os.sep)) > 1:
        f = Files(file_upload)
    else:
        # f = Files(default_path, file_upload)
        default_path = os.path.join(default_path, file_upload)
        f = Files(default_path)
        r = f.reader(default_path)
        c = f.cleaner(r)
        p = f.parser(c)
