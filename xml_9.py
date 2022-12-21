"""
Home task
Expand previous Homework 5/6/7/8 with additional class, which allow to provide records by XML file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed
"""

import xml.etree.ElementTree as ET
# from classes_5 import *
# from files_6 import *
# from csv_parsing_7 import *
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
            for post in posts.iter('post'):
                post_type = post.find('type').text
                if post_type.lower() == 'news':
                    news_text = normalize_text(post.find('text').text)
                    news_city = normalize_text(post.find('city').text)
                    news_obj = News(news_text, news_city)
                    news_obj.combine_tail_news()
                    news_obj.publish()
                elif post_type.lower() == 'ads':
                    ads_text = normalize_text(post.find('text').text)
                    ads_expiration = post.find('expiration').text
                    ads_obj = Ads(ads_text, ads_expiration)
                    ads_obj.combine_tail_ads()
                    ads_obj.publish()
            # os.remove(self.file_path)
            print("File records added into 'feed.txt' file.")
        except Exception as exp:
            print('Error to process records from file - ' + str(exp))

def main():
    user_input = input("Select 1 - news, 2 - ad, 3 - weather, 4 - import file, 5 - import json, 6 - import xml: ")
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

        elif int(user_input) == 6:
            input_file_path = input('XML file (default is "records.xml"): ')
            try:
                xml_object = XmlImport(input_file_path)
                parsed_xml = xml_object.read_file()
                xml_object.process_xml(parsed_xml)
            except:
                print("Error occured while importing records from file. Terminating..")
        else:
            print('Please, enter 1 (news), 2 (ad), 3 (weather), 4 (import from file), 5 (json import) or 6 (xml import)')
    except Exception as exc:
        print(f'Error occured: {exc}')

if __name__ == '__main__':
    main()
