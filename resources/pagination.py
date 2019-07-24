from flask import Flask, jsonify, request
from flask_restful import Resource
import pymongo
import ast


connection = pymongo.MongoClient('localhost', 27017)

database = connection['myPropertyDB']

collection = database['property_01']

data_list = []


class Pagination(Resource):
    def get(self):

        # count all data
        count = collection.count()
        # count page no
        if count / 48 == int(count/48):
            all_page = count / 48

        else:
            all_page = int(count / 48)+1

        # input feed_ratio and page no from url
        feed_ratio = request.args['feed_ratio']
        feed_ratio = ast.literal_eval(feed_ratio)
        # check feed ratio number
        if len(feed_ratio) != 3:
            return {'status': 'Feed content is not equal 3'}, 400
        else:
            pass

        page_no = int(request.args['page'])

        # collect data for every feed
        all_feed_11_data = collection.find({'feed': 11})
        all_feed_12_data = collection.find({'feed': 12})
        all_feed_16_data = collection.find({'feed': 16})

        # Count
        count_feed_11_data = collection.find({'feed': 11}).count()
        count_feed_12_data = collection.find({'feed': 12}).count()
        count_feed_16_data = collection.find({'feed': 16}).count()

        # feed ratio value
        feed_11_ratio = 16
        feed_12_ratio = 16
        feed_16_ratio = 16

        # declare list variable
        data_11_list = []
        data_12_list = []
        data_16_list = []

        d_11 = (page_no + 1) * feed_11_ratio
        d_12 = (page_no + 1) * feed_12_ratio
        d_16 = (page_no + 1) * feed_16_ratio

        if (page_no >= 0) and (page_no <= all_page-1):

            for data in all_feed_11_data:
                data_11_list.append(str(data))
                # if feed 11 data not enough
                if count_feed_11_data < (page_no+1)*feed_11_ratio:
                    diff_11 =  ((page_no + 1) * feed_11_ratio)- count_feed_11_data
                    diff_12 = count_feed_16_data - ((page_no + 1) * feed_16_ratio)
                    diff_16 = count_feed_16_data - ((page_no + 1) * feed_16_ratio)
                    if diff_12 > diff_16:
                        d_12 = ((page_no + 1) * feed_12_ratio)+diff_11
                    else:

                        d_16 = ((page_no + 1) * feed_16_ratio) + diff_11

            for data in all_feed_12_data:
                data_12_list.append(str(data))
                # if feed 12 data not enough
                if count_feed_12_data < (page_no + 1) * feed_12_ratio:
                    diff_11 = count_feed_11_data - ((page_no + 1) * feed_11_ratio)
                    diff_12 = ((page_no + 1) * feed_12_ratio)- count_feed_12_data
                    diff_16 = count_feed_16_data - ((page_no + 1) * feed_16_ratio)
                    if diff_11 > diff_16:
                        d_11 = ((page_no + 1) * feed_11_ratio) + diff_12
                    else:

                        d_16 = ((page_no + 1) * feed_16_ratio) + diff_12

            for data in all_feed_16_data:
                data_16_list.append(str(data))
                # if feed 16 data not enough
                if count_feed_16_data < (page_no + 1) * feed_16_ratio:
                    diff_11 = count_feed_11_data - ((page_no + 1) * feed_11_ratio)
                    diff_12 = count_feed_16_data - ((page_no + 1) * feed_16_ratio)
                    diff_16 = count_feed_16_data - ((page_no + 1) * feed_16_ratio)
                    if diff_12 > diff_11:
                        d_12 = ((page_no + 1) * feed_12_ratio) + diff_16
                    else:

                        d_11 = ((page_no + 1) * feed_11_ratio) + diff_16

            return {'All data =': count, 'Total Page': all_page, 'Current_page': page_no,
                    'Feed_11_data': data_11_list[page_no*feed_11_ratio: d_11],
                    'Feed_12_data': data_12_list[page_no*feed_12_ratio: d_12],
                    'Feed_16_data': data_16_list[page_no*feed_16_ratio: d_16]}, 200

        else:
            return {'Result': " Find data = " + str(count) + " And  Page number should be between 0  to "
                              + str(all_page - 1)}

