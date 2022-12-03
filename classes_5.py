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
    def __init__(self, post_type, post_content):
        self.post_type = post_type
        self.post_content = post_content
        self.post_tail = None

    def publish(self):
        with open('feed.txt', 'a') as file:
            file.write(self.post_type)
            file.write(self.post_content + '\n')
            if self.post_tail:
                file.write(self.post_tail + '\n')


class News(Post):
    def __init__(self, text, location):
        self.post_type = 'News'
        Post.__init__(self, self.post_type, text)
        # self.post_tail = None
        self.location = location

    def publish_date(self):
        pub_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        return pub_date

    def combine_tail_city_date(self):
        self.post_tail = self.location + ', ' + self.publish_date() + '\n\n'
        # self.post_content = self.post_content + self.post_tail



# class Ads(Post):
#     def __init__(self, text, expiration):
#         Post.__init__(self, body_text=text)
#         self.expiration = expiration
#         self.title = "Private Ad"
#
#     def day_left(self):
#         return self.day_left_calc().days
#
#     def day_left_calc(self):
#         today = date.today()
#         user_date = datetime.strptime(self.expiration, "%Y-%m-%d").date()
#         return user_date - today
#
#     def publish(self):
#         with open("feed.txt", "a") as file:
#             file.write(self.post_title(self.title))
#             file.write(self.post_body(self.body_text))
#             file.write(f"Actual until: {self.expiration}" + ", ")
#             file.write(f"{self.day_left()} days left")
#
#
# class Weather(Post):
#     def __init__(self, place, time):
#         Post.__init__(self)
#         self.place = place
#         self.time = time
#         self.title = "Weather Forecast"
#
#     def get_sky_forecast(self):
#         forecast = ["clear", "cloudy", "partially cloudy"]
#         return choice(forecast)
#
#     def get_temperature_forecast(self):
#         temperature_scale = range(-30, 40)
#         return choice(temperature_scale)
#
#     def publish(self):
#         with open("feed.txt", "a") as file:
#             file.write(self.post_title(self.title))
#             file.write(f"On {self.time} the sky in {self.place} will be most probably {self.get_sky_forecast()}.")
#             file.write(f"\nThe temperature will be around {self.get_temperature_forecast()} degrees.")
#

# def main():
#     dataType = input("Select 1 - news, 2 - ad, 3 - weather: ")
#     if dataType.isalpha() or int(dataType) not in [1, 2, 3]:
#         print(f"Incorrect value {dataType}. Please enter 1, 2 or 3.")
#
#     if int(dataType) == 1:
#         news = input("Please enter news text: ")
#         city = input("Enter news city: ")
#         n = News(news, city)
#         n.publish()

    # elif int(dataType) == 2:
    #     ad = input("Please enter ad text: ")
    #     expiration = input("Enter ad expiration date yyyy-mm-dd: ")
    #     a = Ads(ad, expiration)
    #     a.publish()
    #
    # elif int(dataType) == 3:
    #     city = input("Please enter city: ")
    #     day = input("Enter a date (yyyy-mm-dd): ")
    #     w = Weather(city, day)
    #     w.publish()

    # else:
    #     print("Please enter 1 (for news) or 2 (for private ad)")


if __name__ == '__main__':
    # main()
    my_news = News('Hello! I am a sensation!', 'New-York')
    my_news.combine_tail_city_date()
    print(my_news.__dict__)
    # print(my_news.post_body)
    print(my_news.__class__.__dict__)
    # my_news.publish()