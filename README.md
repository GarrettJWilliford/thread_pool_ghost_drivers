# thread_pool_ghost_drivers
a selenium thread pool


This is a tool for large amounts of webscraping/stress testing. You need to download a phantomjs driver for the program to work,
which can be found here

https://phantomjs.org/download.html

I would recommend not using this on websites with smaller servers.
syntax goes as follows

main.driver_bots(website = 'https://www.bbc.com', \
commands = ["a = driver.find_elements_by_class_name('media__link')", "print(random.choice(a).get_attribute('innerHTML'))"],\
bot_amount = 5, \
hits = 3, \
safety = True)

this script picks a random headline from bbc.com and prints it


safety      = Adds a are you sure message to your script, so it does not execute automaticly
commands[]  = commands you would like to run on each driver
bot_amount  = the amount of phantomjs drivers you would like to run
hits        = amount of times each driver runs the commands, refreshes page every time
