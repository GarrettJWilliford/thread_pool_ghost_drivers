from selenium import webdriver
import random
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import time
import datetime
import pickle


path = input('PATH_TO_GHOSTDRIVER>> ')

def request_me(driver, website, commands):
    bot_name = list(commands.keys())[0]
    print('[' + datetime.datetime.now().strftime("%H:%M:%S") + ']: ' + bot_name + ' REQUSTING ' + website)
    driver.get(website)
    for c in commands[bot_name]:
        try:
            print('[' + datetime.datetime.now().strftime("%H:%M:%S") + ']: ' + bot_name + ' PREFORMING ' + c)
            exec(c)
        except:
            print(bot_name + ' FAILED ' + c)
            
    print('[' + datetime.datetime.now().strftime("%H:%M:%S") + ']: ' + bot_name + ' TASK_COMPLETE')


def driver_bots(website = '!!!<>!!!', commands = [], bot_amount = 10, hits = 1, saftey = True):
    bots = {}
    if website == '!!!<>!!!':
        print('<<!NO_WEBSITE_LISTED!>>')
        return
    for i in range(bot_amount):
        bots.update({'bot_' + str(i) : webdriver.PhantomJS(path)})
        print('[' + datetime.datetime.now().strftime("%H:%M:%S") + ']: ' + 'bot_' + str(i) + ' CREATED')    
    is_first = True
    web_pool = [website for w in range(bot_amount)]
    if saftey:
        while True:
            commit = input('>>!EXECUTE?[Y/N]!>> ')
            if commit == 'Y':
                break
            if commit == 'N':
                print('<<!BOTNET_ABORTED!>>')
                for b in bots:
                    bots[b].quit()
                    print(b + ' TERMINATIED')
                    return
    print('<<!EXECUTING!>>')
    for h in range(hits):
        with ThreadPoolExecutor(max_workers = 50) as pool:
            pool.map(request_me, [bots[b] for b in bots], web_pool, [{b : commands} for b in bots])
    print('PROCESS COMPLETE')
    for b in bots:
        bots[b].quit()
        print('[' + datetime.datetime.now().strftime("%H:%M:%S") + ']: '+ b + ' TERMINATED')

