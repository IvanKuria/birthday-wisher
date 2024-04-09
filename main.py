import pandas
import datetime as dt
import random
import smtplib

# 2. Check if today matches a birthday in the birthdays.csv
csvFile = pandas.read_csv("birthdays.csv")
birthday_name = csvFile.name.to_list()
birthday_month = csvFile.month.to_list()
birthday_day = csvFile.day.to_list()

# Finds the current month and day
now = dt.datetime.now()
month = now.month
day = now.day

index = None

for b_day_month in birthday_month:
    if b_day_month == month:
        index = birthday_month.index(b_day_month)
if index is not None and birthday_day[index] == day:
    random_integer = random.randint(0, 2)
    letter_list = [
        "letter_1.txt",
        "letter_2.txt",
        "letter_3.txt"
    ]

    # Replaces the [NAME] in files with the name of the person
    file_path = f'letter_templates/{letter_list[random_integer]}'
    with open(file_path, 'r') as file:
        file_contents = file.read()
        updated_contents = file_contents.replace('[NAME]', birthday_name[index])

    with open(file_path, 'w') as file:
        file.write(updated_contents)

    # 4. Send the letter generated in step 3 to that person's email address.
    ''' 
    Sets up the email
    '''
    my_email = "h68355132@gmail.com"
    password = "ejclrwnjttqmljge"
    f = open(file_path, 'r')
    with smtplib.SMTP("smtp.gmail.com") as connection:  # works like a file
        connection.starttls()  # helps secure the connection
        connection.login(user=my_email, password=password)  # this logins in to the email account
        connection.sendmail(
            from_addr=my_email,
            to_addrs="harpercolins@yahoo.com",
            msg=f"Subject:Happy Birthday!\n\n{f.read()}"
        )

    file.close()

    # Returns the files to their original state with [NAME]
    with open(file_path, 'r') as file:
        file_contents = file.read()
        updated_contents = file_contents.replace(birthday_name[index], '[NAME]')

    with open(file_path, 'w') as file:
        file.write(updated_contents)

else:
    print(f'{month}-{day} is not a birthday in the csv')