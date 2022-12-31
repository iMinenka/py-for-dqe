"""
Expand previous Homework 5/6/7 with additional class, which allow to provide records by JSON file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed
"""
from files_6 import *
import os.path
from string_object_3 import normalize_text
import json


class ImportFromJson:
    def __init__(self, file_path):
        self.file_path = file_path if file_path else 'records.json'

    def read_file(self):
        try:
            with open(self.file_path, "r") as file:
                json_content = json.load(file)
            return json_content
        except FileNotFoundError:
            print("File not found.")

    def process_records_from_json(self, json_posts):
        try:
            processed_records = list()
            for post in json_posts['posts']:
                print(post)
                if post['type'].lower() == 'news':
                    news_text = normalize_text(post['text'])
                    news_city = normalize_text(post['city'])
                    processed_records.append(dict(type='news', news_text=news_text, city=news_city))
                elif post['type'].lower() == 'ads':
                    ads_text = normalize_text(post['text'])
                    processed_records.append(dict(type='ads', ads_text=ads_text, expiration=post['expiration']))
                elif post['type'].lower() == 'weather':
                    weather_city = normalize_text(post['city'])
                    processed_records.append(dict(type='weather', city=weather_city, day=post['day']))
                else:
                    print(f"Unknown post type - {post['type']}. Skipping..")
            print("File records added into 'feed.txt' file.")
            return processed_records
            # os.remove(self.file_path)
        except Exception as exp:
            print('Error to process records from file - ' + str(exp))


def main():
    user_input = input("Select 1 - news, 2 - ad, 3 - weather, 4 - import from file, 5 - import from json: ")
    try:
        if int(user_input) == 1:
            news_content = input("Please enter news text: ")
            news_city = input("Enter news city: ")
            my_news = News(news_content, news_city)
            my_news.publish()

        elif int(user_input) == 2:
            ad_content = input("Please enter ad text: ")
            ad_expiration = input("Enter ad expiration date yyyy-mm-dd: ")
            my_ad = Ads(ad_content, ad_expiration)
            my_ad.publish()

        elif int(user_input) == 3:
            forecast_city = input("Please enter city: ")
            forecast_day = input("Enter a date (yyyy-mm-dd): ")
            weather = Weather(forecast_city, forecast_day)
            weather.publish()

        elif int(user_input) == 4:
            input_file_path = input('Please provide file location (default is "records.txt" in a program folder): ')
            try:
                file_import = ImportFromFile(input_file_path)
                file_content = file_import.file_reader()
                parsed_content = file_import.process_records_from_file(file_content)
                for post in parsed_content:
                    if post['type'] == 'news':
                        news = News(post['news_text'], post['city'])
                        news.publish()
                    elif post['type'] == 'ads':
                        ad = Ads(post['ads_text'], post['expiration'])
                        ad.publish()
                    elif post['type'] == 'weather':
                        weather = Weather(post['city'], post['day'])
                        weather.publish()
            except:
                print("Error occurred while importing records from file. Terminating..")

        elif int(user_input) == 5:
            input_file_path = input('JSON file (default is "records.json"): ')
            try:
                json_import = ImportFromJson(input_file_path)
                json_content = json_import.read_file()
                parsed_posts = json_import.process_records_from_json(json_content)
                for post in parsed_posts:
                    if post['type'] == 'news':
                        news = News(post['news_text'], post['city'])
                        news.publish()
                    elif post['type'] == 'ads':
                        ad = Ads(post['ads_text'], post['expiration'])
                        ad.publish()
                    elif post['type'] == 'weather':
                        weather = Weather(post['city'], post['day'])
                        weather.publish()
                    else:
                        print(f'Unknown post type - {post["type"]}')
            except:
                print("Error occurred while importing records from file. Terminating..")

        else:
            print('Please, enter 1 (news), 2 (ad), 3 (weather), 4 (import from file) or 5 (json import.')
    except Exception as exc:
        print(f'Error occurred: {exc}')


if __name__ == '__main__':
    main()
