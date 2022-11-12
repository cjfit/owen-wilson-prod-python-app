# CLI program that reads from provided CSV file, combines
# its information with data from the API, and
# outputs a new CSV file

import csv
import sys
import os.path
import urllib
import requests
from requests.exceptions import HTTPError

def load_csv(filepath):
    """
    Opens input file and writes output to a list
    :param filepath: string
    :return: return_list: list
    """

    with open(filepath, mode='r', encoding="utf-8") as csv_file:
        return_list = []
        csv_reader = csv.reader(csv_file, delimiter=',')

        for i, row in enumerate(csv_reader):
            # if header
            if i == 0:
                if row != ['Movie Name', 'Release Year', 'Rating', 'id']:
                    raise ValueError("Mismatching headers, exiting.")
            if len(row) != 4:
                raise ValueError("Mismatching row length, exiting.")
            return_list.append(row)
        return return_list



def get_account(movie_name):
    """
    Makes a GET request to the endpoint
    Retrieve a random "wow" by the name of the movie it appears in.
    :param movie_name: string
    :return: JSON-serialized response object
    """
    try:
        movie_name_parsed = urllib.parse.quote(movie_name)
        endpoint = f'https://owen-wilson-wow-api.onrender.com/wows/random?movie={movie_name_parsed}'
        response = requests.get(f'{endpoint}', timeout=10)
        response.raise_for_status()
        return response.json()
    except HTTPError as http_err:
        raise HTTPError("HTTP Error Occurred:", http_err) from http_err
    except TimeoutError as timeout_err:
        raise TimeoutError("Timeout Occurred:", timeout_err) from timeout_err
    except Exception as err:
        raise Exception("Another exception occurred:", err) from err


def merge_data(csv_list):
    """
    Takes input_data list of CSV file data and extends API request data into input_data
    :param input_data: list
    :return: input_data: list
    """
    for i, record in enumerate(csv_list):
        if i == 0:
            # skip header row
            continue
        res = get_account(record[0])[0]
        csv_list[i].extend([str(res['total_wows_in_movie']), res['full_line']])

    # Add new headers
    csv_list[0].extend(["Total Wows", "Full Line"])

    return csv_list

def write_csv(path, data_to_write):
    """
    Writes output to a csv file
    :param path: string, header: list
    :return: None
    """
    with open(path, mode='w', encoding='UTF-8') as output_file:
        output_writer = csv.writer(output_file, delimiter=',',
                                   quotechar='"',
                                   quoting=csv.QUOTE_MINIMAL)
        output_writer.writerows(data_to_write)


if __name__ == '__main__':

    try:
        INPUT_PATH = sys.argv[1]
    except IndexError:
        print("Missing input path parameter.")
        raise

    try:
        OUTPUT_PATH = sys.argv[2]
    except IndexError:
        print("Missing output path parameter.")
        raise

    if not os.path.exists(INPUT_PATH):
        print("Input path does not exist.")
        raise FileNotFoundError

    # Build a list from the CSV file
    input_data = load_csv(INPUT_PATH)

    # Merge information from API
    write_data = merge_data(input_data)

    # Write to output file
    write_csv(OUTPUT_PATH, write_data)
