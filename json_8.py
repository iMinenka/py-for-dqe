"""
Expand previous Homework 5/6/7 with additional class, which allow to provide records by JSON file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed
"""
from classes_5 import *
from files_6 import *
import os.path
import string_object_3
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

    def normalize_records(self, records_dict):
        for post in records_dict['posts']:
            for k, v in post.items():
                post[k] = string_object_3.normalize_text(v)
        return records_dict

    def process_records_from_file(self, json_posts):
        try:
            for post in json_posts['posts']:
                if post['type'] == 'News':
                    news_obj = News(post['text'], post['city'])
                    news_obj.publish()
                elif post['type'] == 'Ads':
                    ads_obj = Ads(post['text'], post['expiration'])
                    ads_obj.publish()
                else:
                    print(f"Unknown post type - {post['type']}. Skipping..")
            # os.remove(self.file_path)
            print("File records added into 'feed.txt' file.")
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
            input_file_path = input('Import file (default is "records.txt"): ')
            try:
                records = ImportFromFile(input_file_path)
                raw_records_from_file = records.file_reader()
                normalized_records_from_file = records.normalize_records(raw_records_from_file)
                records.process_records_from_file(normalized_records_from_file)
            except:
                print("Error occured while importing records from file. Terminating..")

        elif int(user_input) == 5:
            input_file_path = input('JSON file (default is "records.json"): ')
            try:
                records = ImportFromJson(input_file_path)
                raw_records_from_file = records.read_file()
                normalized_records_from_file = records.normalize_records(raw_records_from_file)
                records.process_records_from_file(normalized_records_from_file)
            except:
                print("Error occured while importing records from file. Terminating..")

        else:
            print('Please, enter 1 (news), 2 (ad), 3 (weather), 4 (import from file) or 5 (json import.')
    except Exception as exc:
        print(f'Error occured: {exc}')

if __name__ == '__main__':
    main()