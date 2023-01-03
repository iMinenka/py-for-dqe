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
            news = dict(type='news', news_text=news_content, city=news_city)
            process_post(news)

        elif int(user_input) == 2:
            ad_content = input("Please enter ad text: ")
            ad_expiration = input("Enter ad expiration date yyyy-mm-dd: ")
            ad = dict(type='ads', ads_text=ad_content, expiration=ad_expiration)
            process_post(ad)

        elif int(user_input) == 3:
            forecast_city = input("Please enter city: ")
            forecast_day = input("Enter a date (yyyy-mm-dd): ")
            weather = dict(type='weather', city=forecast_city, day=forecast_day)
            process_post(weather)

        elif int(user_input) == 4:
            input_file_path = input('Please provide file location (default is "records.txt"): ')
            try:
                file_import = ImportFromFile(input_file_path)
                file_content = file_import.file_reader()
                parsed_posts = file_import.process_records_from_file(file_content)
                for post in parsed_posts:
                    process_post(post)
            except:
                print("Error occurred while importing records from file. Terminating..")

        elif int(user_input) == 5:
            input_file_path = input('JSON file (default is "records.json"): ')
            try:
                json_import = ImportFromJson(input_file_path)
                json_content = json_import.read_file()
                parsed_posts = json_import.process_records_from_json(json_content)
                for post in parsed_posts:
                    process_post(post)
            except:
                print("Error occurred while importing records from file. Terminating..")

        else:
            print(f'Invalid option provided - {user_input}')
    except Exception as exc:
        print(f'Error occurred: {exc}')


if __name__ == '__main__':
    main()
