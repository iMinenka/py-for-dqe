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
        return normalized_records_list

    def process_records_from_file(self, lines):
        try:
            for line in lines:
                parsed_line = line.strip().split(',', 2)
                if parsed_line[0] == 'News':
                    news_obj = News(parsed_line[2], parsed_line[1])
                    news_obj.combine_tail_news()
                    news_obj.publish()
                elif parsed_line[0] == 'Ads':
                    ads_obj = Ads(parsed_line[2], parsed_line[1])
                    ads_obj.combine_tail_ads()
                    ads_obj.publish()
                else:
                    print(f"Unknown record type - {line}")
            # os.remove(self.file_path)
            print("File records added into 'feed.txt' file.")
        except Exception as exp:
            print('Error to process records from file.' + str(exp))


def main():
    user_input = input("Select 1 - news, 2 - ad, 3 - weather, 4 - import from file: ")
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
            # print(my_ad.__dict__)
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
            input_file_path = input('Please provide file location (default is "records.txt" in a program folder): ')
            try:
                records = ImportFromFile(input_file_path)
                raw_records_from_file = records.file_reader()
                normalized_records_from_file = records.normalize_records(raw_records_from_file)
                records.process_records_from_file(normalized_records_from_file)
            except:
                print("Error occured while importing records from file. Terminating..")
        else:
            print('Please, enter 1 (news), 2 (ad), 3 (weather) or 4 (import from file).')
    except Exception as exc:
        print(f'Error occured: {exc}')

if __name__ == '__main__':
    main()
