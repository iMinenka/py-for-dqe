"""
Expand previous Homework 5 with additional class, which allow to provide records by text file:
1. Define your input format (one or many records)
2. Default folder or user provided file path
3. Remove file if it was successfully processed
4. Apply case normalization functionality form Homework 3/4
"""
from classes_5 import *
import os.path
import string_object_3


class ImportFromFile:
    def __init__(self, file_path):
        self.file_path = 'records.txt' if file_path is None else "records.txt"

    def file_reader(self):
        try:
            with open(self.file_path, "r") as file:
                lines_in_file = file.readlines()
            print("File found and records have been read.")
            return lines_in_file
        except FileNotFoundError:
            print("File not found.")

    def normalize_records(self, records_list):
        normalized_records_list = list()
        for record in records_list:
            normalized_record = list()
            fields = record.split(',', 2)
            for field in fields:
                field_normalized = string_object_3.normalize_text(field)
                normalized_record.append(field_normalized)
            normalized_records_list.append(','.join(normalized_record))
        print("Records from file are normalized.")
        return normalized_records_list

    def process_records_from_file(self, lines):
        try:
            for line in lines:
                parsed_line = line.strip().split(',', 2)
                if parsed_line[0] == 'News':
                    news_obj = News(parsed_line[2], parsed_line[1])
                    news_obj.publish()
                elif parsed_line[0] == 'Ads':
                    ads_obj = Ads(parsed_line[2], parsed_line[1])
                    ads_obj.publish()
                else:
                    print(f"Unknown record type - {line}")
            # os.remove(self.file_path)
            print("File records added into 'feed.txt' file.")
        except Exception as exp:
            print('Error to process records from file.' + str(exp))


def main():
    input_post_type = input("Select 1 - news, 2 - ad, 3 - weather, 4 - import from file: ")
    if input_post_type.isalpha() or int(input_post_type) not in [1, 2, 3, 4]:
        print(f"Incorrect value {input_post_type}. Please enter 1, 2, 3 or 4.")

    elif int(input_post_type) == 1:
        input_news_text = input("Please enter news text: ")
        input_news_city = input("Enter news city: ")
        create_news_post = News(input_news_text, input_news_city)
        create_news_post.publish()

    elif int(input_post_type) == 2:
        input_ad_text = input("Please enter ad text: ")
        input_ad_expiration = input("Enter ad expiration date yyyy-mm-dd: ")
        create_ads_post = Ads(input_ad_text, input_ad_expiration)
        create_ads_post.publish()

    elif int(input_post_type) == 3:
        input_weather_city = input("Please enter city: ")
        input_weather_day = input("Enter a date (yyyy-mm-dd): ")
        create_weather_post = Weather(input_weather_city, input_weather_day)
        create_weather_post.publish()

    elif int(input_post_type) == 4:
        input_file_path = input('Please provide file location (default is file "records.txt" in a program folder): ')
        try:
            records = ImportFromFile(input_file_path)
            raw_records_from_file = records.file_reader()
            # print("raw_records_from_file: ", raw_records_from_file)
            normalized_records_from_file = records.normalize_records(raw_records_from_file)
            # print("normalized_records_from_file: ", normalized_records_from_file)
            records.process_records_from_file(normalized_records_from_file)
        except:
            print("Error occured. Terminating..")
    else:
        print("Please provide a valid option for a new post.")


if __name__ == '__main__':
    main()
