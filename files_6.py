"""
Expand previous Homework 5 with additional class, which allow to provide records by text file:
1. Define your input format (one or many records)
2. Default folder or user provided file path
3. Remove file if it was successfully processed
4. Apply case normalization functionality form Homework 3/4
"""
from classes_5 import *
import os.path
from string_object_3 import normalize_text


class ImportFromFile:
    def __init__(self, file_path):
        self.file_path = file_path if file_path else "records.txt"

    def file_reader(self):
        try:
            with open(self.file_path, "r") as file:
                lines_in_file = file.readlines()
            return lines_in_file
        except FileNotFoundError:
            print("File not found.")

    def process_records_from_file(self, lines):
        """ Load posts from file, split each post by comma. Parse post type and
        add post as a dictionary to list.

        :param list lines: posts from file
        :return: list of dictionaries
        """
        try:
            parsed_posts = list()
            for line in lines:
                split_line = line.strip().split(',', 2)
                if split_line[0].lower() == 'news':
                    news_text = normalize_text(split_line[2])
                    news_city = normalize_text(split_line[1])
                    parsed_posts.append(dict(type='news', news_text=news_text, city=news_city))
                elif split_line[0].lower() == 'ads':
                    ads_text = normalize_text(split_line[2])
                    parsed_posts.append(dict(type='ads', ads_text=ads_text, expiration=split_line[1]))
                elif split_line[0].lower() == 'weather':
                    weather_city = normalize_text(split_line[2])
                    parsed_posts.append(dict(type='weather', city=weather_city, day=split_line[1]))
                else:
                    print(f"Unknown post type - {line}")
            print("File records processed from file.")
            # os.remove(self.file_path)
            return parsed_posts
        except Exception as exp:
            print('Error to process records from file.' + str(exp))


def process_post(post):
    """ Decide about post type and publish it to the feed file.

    :param posts: dictionary containing post
    :type posts: dict
    """
    if post['type'] == 'news':
        news = News(post['news_text'], post['city'])
        news.publish()
    elif post['type'] == 'ads':
        ad = Ads(post['ads_text'], post['expiration'])
        ad.publish()
    elif post['type'] == 'weather':
        weather = Weather(post['city'], post['day'])
        weather.publish()

def main():
    user_input = input("Select 1 - news, 2 - ad, 3 - weather, 4 - import from file: ")
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
        else:
            print(f'Invalid option provided - {user_input}')
    except Exception as exc:
        print(f'Error occurred: {exc}')


if __name__ == '__main__':
    main()
