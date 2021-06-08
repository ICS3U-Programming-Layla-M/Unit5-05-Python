#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: June 7, 2021
# This program gets the user's name and address information and displays it
# in Canadian post format

def address_format(name, street_num, street_name_type, city, province,
                   postal_code, apt_num=None):
    # this function takes address information from the user and capitalizes
    # every letter while formatting it in Canadian post format with a default
    # value of None for the apt_num
    formatted_address = ""
    formatted_address = formatted_address + name.upper() + "\n"

    if apt_num is not None:
        formatted_address = formatted_address + apt_num.upper() + "-"

    formatted_address = formatted_address + street_num.upper() + " " + \
        street_name_type.upper() + "\n" + city.upper() + " " +\
        province.upper() + " " + postal_code.upper()

    return formatted_address


def main():
    # greet and get the user's address information
    print("This program formats an address to a Canadian mailing address.")
    user_name = input("Enter your full name: ")
    user_apt = input("Do you live in an apartment? (y/n): ")

    if (user_apt == 'y'):
        # check if the user has an apartment
        user_apt_num = input("Enter your apartment number: ")

    user_street_num = input("Enter your street number: ")
    user_street_name_type = input("Enter your street name AND type\
 (Main St., Sunset Blvd., etc.): ")
    user_city = input("Enter your city: ")
    user_province = input("Enter your province as an abbreviation\
 (ON, QC, etc.): ")
    user_postal_code = input("Enter your postal code: ")

    if (user_apt == 'y'):
        # call function if the user has an apartment number
        mailing_address = address_format(user_name, user_street_num,
                                         user_street_name_type, user_city,
                                         user_province, user_postal_code,
                                         user_apt_num)
    else:
        # call function if the user does not have an apartment number
        mailing_address = address_format(user_name, user_street_num,
                                         user_street_name_type, user_city,
                                         user_province, user_postal_code)

    print()
    # display the formatted mailing address
    print("Your Canadian mailing address is: ")
    print(mailing_address)


if __name__ == "__main__":
    main()
