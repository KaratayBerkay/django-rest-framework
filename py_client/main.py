from shared_functions import ApiTest


if __name__ == "__main__":
    # ApiTest.prefix = '/products/'
    # print(ApiTest.get_url())
    # # print(ApiTest.params)
    # # print(ApiTest.json_add)
    # get_response = ApiTest.post()
    # print('json', get_response.json)
    # print('status', get_response.status)

    ApiTest.prefix = '/products/2/update'
    ApiTest.json_add = {"price": "12.18"}
    ApiTest.put()
