"""
Home task
Expand previous Homework 5/6/7/8 with additional class, which allow to provide records by XML file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed
"""

import xml.etree.ElementTree as ET
from json_8 import *
from string_object_3 import normalize_text


class XmlImport:
    def __init__(self, file_path):
        self.file_path = file_path if file_path else 'records.xml'

    def read_file(self):
        try:
            tree = ET.parse(self.file_path)
            root = tree.getroot()
            return root
        except FileNotFoundError:
            print("File not found.")

    def process_xml(self, posts):
        try:
            parsed_posts = list()
            for post in posts.iter('post'):
                post_type = post.find('type').text
                if post_type.lower() == 'news':
                    news_text = normalize_text(post.find('text').text)
                    news_city = normalize_text(post.find('city').text)
                    parsed_posts.append(dict(type='news', news_text=news_text, city=news_city))
                elif post_type.lower() == 'ads':
                    ads_text = normalize_text(post.find('text').text)
                    ads_expiration = post.find('expiration').text
                    parsed_posts.append(dict(type='ads', ads_text=ads_text, expiration=ads_expiration))

                elif post_type.lower() == 'weather':
                    weather_city = normalize_text(post.find('city').text)
                    weather_day = post.find('day').text
                    parsed_posts.append(dict(type='weather', city=weather_city, day=weather_day))
                else:
                    print('Unknown post type.')
            # os.remove(self.file_path)
            print(f'Records from "{self.file_path}" have been processed.')
            return parsed_posts
        except Exception as exp:
            print('Error to process records from file - ' + str(exp))


def main(option):
    try:
        if int(option) == 1:
            news_content = input("Please enter news text: ")
            news_city = input("Enter news city: ")
            news = dict(type='news', news_text=news_content, city=news_city)
            process_post(news)

        elif int(option) == 2:
            ad_content = input("Please enter ad text: ")
            ad_expiration = input("Enter ad expiration date yyyy-mm-dd: ")
            ad = dict(type='ads', ads_text=ad_content, expiration=ad_expiration)
            process_post(ad)

        elif int(option) == 3:
            forecast_city = input("Please enter city: ")
            forecast_day = input("Enter a date (yyyy-mm-dd): ")
            weather = dict(type='weather', city=forecast_city, day=forecast_day)
            process_post(weather)

        elif int(option) == 4:
            input_file_path = input('Please provide file location (default is "records.txt"): ')
            try:
                file_import = ImportFromFile(input_file_path)
                file_content = file_import.file_reader()
                parsed_posts = file_import.process_records_from_file(file_content)
                for post in parsed_posts:
                    process_post(post)
            except:
                print("Error occurred while importing records from file. Terminating..")

        elif int(option) == 5:
            input_file_path = input('JSON file (default is "records.json"): ')
            try:
                json_import = ImportFromJson(input_file_path)
                json_content = json_import.read_file()
                parsed_posts = json_import.process_records_from_json(json_content)
                for post in parsed_posts:
                    process_post(post)
            except:
                print("Error occurred while importing records from file. Terminating..")

        elif int(option) == 6:
            input_file_path = input('XML file (default is "records.xml"): ')
            try:
                xml_object = XmlImport(input_file_path)
                file_content = xml_object.read_file()
                parsed_posts = xml_object.process_xml(file_content)
                for post in parsed_posts:
                    process_post(post)
            except Exception:
                print("Error occurred while importing records from file. Terminating..")
        else:
            print(f'Invalid option provided - {user_input}')
    except Exception as exc:
        print(f'Error occurred: {exc}')


if __name__ == '__main__':
    user_input = input("Select 1 - news, 2 - ad, 3 - weather, 4 - import file, 5 - import json, 6 - import xml: ")
    main(user_input)
