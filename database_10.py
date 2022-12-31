"""Home task
Expand previous Homework 5/6/7/8/9 with additional class, which allow to save records into database:
1.Different types of records require different data tables
2.New record creates new row in data table
3.Implement “no duplicate” check.
"""
import pyodbc
from xml_9 import *
from json_8 import *


class DBConnection:
    def __init__(self, db_name):
        with pyodbc.connect(f"Driver=SQLite3 ODBC Driver;Database={db_name}") as self._dbcon:
            self._cursor = self._dbcon.cursor()
            for sql in [sql_create_news, sql_create_ads, sql_create_weather]:
                try:
                    self._cursor.execute(sql)
                    self._cursor.commit()
                except pyodbc.Error as exc:
                    print('Error to create table:', exc)
                    self._cursor.rollback()
    def create_table(self, table_name, *args):
        try:
            self._cursor.execute(f'CREATE TABLE {table_name} {args}')
            self._cursor.commit()
        except pyodbc.Error as exc:
            print('Error to create table:', exc)
            self._cursor.rollback()
    def select_from_table(self, table_name):
        self._cursor.execute(f'SELECT * FROM {table_name}')
        result = self._cursor.fetchall()
        return result

    def insert_into_table(self, table_name, *args):
        data_in_table = list(tuple(i) for i in self.select_from_table(table_name))
        self._cursor.execute(f'INSERT INTO {table_name} VALUES {args}')
        if args not in data_in_table:
            print(f'New record added to {table_name}')
            self._cursor.commit()
        else:
            print(f'Duplicate record in table {table_name}')
            self._cursor.rollback()


    def drop_table(self, table_name):
        self._cursor.execute(f'DROP TABLE {table_name}')
        try:
            self._cursor.commit()
        except Exception as exc:
            self._cursor.rollback()
            print(f'Table {table_name} cannot be dropped.', exc)


def main():
    user_input = input("Select 1 - news, 2 - ad, 3 - weather, 4 - import file, 5 - import json, 6 - import xml: ")
    try:
        if int(user_input) == 1:
            news_content = input("Please enter news text: ")
            news_city = input("Enter news city: ")
            news = News(news_content, news_city)
            news.publish()
            db = DBConnection(DB_NAME)
            db.insert_into_table('news', news.post_content, news.location, news.publish_date())

        elif int(user_input) == 2:
            ad_content = input("Please enter ad text: ")
            ad_expiration = input("Enter ad expiration date yyyy-mm-dd: ")
            ad = Ads(ad_content, ad_expiration)
            ad.publish()
            db = DBConnection(DB_NAME)
            db.insert_into_table('ads', ad.post_content, ad.expiration, ad.calculate_left_days())

        elif int(user_input) == 3:
            forecast_city = input("Please enter city: ")
            forecast_day = input("Enter a date (yyyy-mm-dd): ")
            weather = Weather(forecast_city, forecast_day)
            weather.publish()
            db = DBConnection(DB_NAME)
            db.insert_into_table('weather', weather.post_content, weather.city, weather.day)

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

        elif int(user_input) == 6:
            input_file_path = input('XML file (default is "records.xml"): ')
            try:
                xml_object = XmlImport(input_file_path)
                file_content = xml_object.read_file()
                parsed_posts = xml_object.process_xml(file_content)
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

            except Exception:
                print("Error occurred while importing records from file. Terminating..")
        else:
            print('Please, enter 1 (news), 2 (ad), 3 (weather), 4 (import from file), 5 (json import) or 6 (xml import)')
    except Exception as exc:
        print(f'Error occurred: {exc}')


if __name__ == '__main__':
    DB_NAME = 'sqlite.db'
    sql_create_news = 'CREATE TABLE news (news_text text, city text, publish_date text)'
    sql_create_ads = 'CREATE TABLE ads (ad_text text, expiration_date text, days_left text)'
    sql_create_weather = 'CREATE TABLE weather (forecast text, city text, date text)'
    main()
