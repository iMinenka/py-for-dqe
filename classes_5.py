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
import csv_parsing_7


class Post:
    def __init__(self, post_type=None, post_content=None):
        self.post_type = post_type
        self.post_content = post_content
        self.post_tail = None

    def publish(self):
        with open('feed.txt', 'a') as file:
            file.write(self.post_type + '\n')
            file.write(self.post_content + '\n')
            if self.post_tail:
                file.write(self.post_tail + '\n\n')
        csv_parsing_7.main()

class News(Post):
    def __init__(self, text, location):
        self.post_type = 'News'
        Post.__init__(self, self.post_type, text)
        self.location = location

    def publish_date(self):
        pub_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        return pub_date

    def combine_tail_news(self):
        self.post_tail = self.location + ', ' + self.publish_date()
        # self.post_content = self.post_content + self.post_tail



class Ads(Post):
    def __init__(self, text, expiration):
        self.post_type = "Private Ad"
        Post.__init__(self, self.post_type, text)
        self.expiration = expiration

    def calculate_left_days(self):
        today = date.today()
        user_date = datetime.strptime(self.expiration, "%Y-%m-%d").date()
        left_days = (user_date - today).days
        return str(left_days)

    def combine_tail_ads(self):
        self.post_tail = f'Actual until: {self.expiration}, {self.calculate_left_days()} days left'


class Weather(Post):
    def __init__(self, city, day):
        self.post_type = 'Weather Forecast'
        Post.__init__(self, self.post_type)
        self.city = city
        self.day = day

    def guess_sky(self):
        forecast_options = ["clear", "cloudy", "partially cloudy"]
        forecast = choice(forecast_options)
        return forecast

    def guess_temperature(self):
        temperature_scale = range(-30, 40)
        temperature = choice(temperature_scale)
        return str(temperature)

    def combine_forecast(self):
        self.post_content = f'On {self.day} the sky in {self.city} will be most probably {self.guess_sky()}.' \
                            f'\nThe temperature will be around {self.guess_temperature()} degrees.'

    def combine_tail_forecast(self):
        self.post_tail = f'Forecast probability is {choice(range(1, 100))} %.'


def main():
    user_input = input("Select 1 - news, 2 - ad, 3 - weather: ")
    try:
        if int(user_input) == 1:
            news_content = input("Please enter news text: ")
            news_city = input("Enter news city: ")
            my_news = News(news_content, news_city)
            my_news.combine_tail_news()
            my_news.publish()

        elif int(user_input) == 2:
            ad_content = input("Please enter ad text: ")
            ad_expiration = input("Enter ad expiration date yyyy-mm-dd: ")
            my_ad = Ads(ad_content, ad_expiration)
            my_ad.combine_tail_ads()
            my_ad.publish()

        elif int(user_input) == 3:
            forecast_city = input("Please enter city: ")
            forecast_day = input("Enter a date (yyyy-mm-dd): ")
            weather = Weather(forecast_city, forecast_day)
            weather.combine_forecast()
            weather.combine_tail_forecast()
            weather.publish()

        else:
            print('Please, enter 1 (news), 2 (ad) or 3 (weather).')

    except Exception as exc:
        print(f'Error occured: {exc}')


if __name__ == '__main__':
    main()
