# import sys
# import yadisk
#
# y = yadisk.YaDisk(token="y0_AgAAAABpwoqRAAmkQQAAAADgOBTq6DJ2ymp-TdazGtxVdU6ao_xo54M")

# y = yadisk.YaDisk("1fa64dae38e74ce8b3314875e4cce609", "b8f269efb8ef4da08b41fecedaa94feb")
# url = y.get_code_url()
#
# print("Go to the following url: %s" % url)
# code = input("Enter the confirmation code: ")

# try:
#     response = y.get_token(code)
# except yadisk.exceptions.BadRequestError:
#     print("Bad code")
#     sys.exit(1)
#
# y.token = response.access_token

# if y.check_token():
#     print("Sucessfully received token!")
# else:
#     print("Something went wrong. Not sure how though...")
# if y.check_token():
#     if not y.is_dir("/test-dir1"):
#         y.mkdir("/test-dir1")
#         print('Папка "test-dir1" создана')

import configparser

#
# def get_token_ini():
#     config = configparser.ConfigParser()
#     config.read('config.ini')
#     return config['API']['token']
#
# print(get_token_ini())
