# noinspection PyGlobalUndefined
# The definition basically means facebook startup

# Here are features I want to add in future :
#    Do it so the bot checks the times on expedition etc. once everytime and then it waits for it not like it looks for
#    it every 3 seconds
#    arena bot
#    circus turma
#    health checker
#    collect daily login bonus
#    automatical food buyer
#    automatical health adder
#    U can select which page to have the food on
#    automatical gold saver
#    automatical stats  improver
#    automatical underground
#    Sell items from inventory to shop
#    Sell all items from shipments
#    Move items from shipments to inventory and u can choose which inventory page to
#    Create a feature so the bot exactly knows in which part of the game you are
#
#    Possible to restart dungeon after losing x matches
#    Possible to do provinciarum arena and provinciarum turma
#    automatical event checker + automatical going to events
#    automatical repair of items
#    option to turn off features like arena circus turma  health checker
#    option to melt some things automatically or to melt things from some inventory pages.
#    automatic selleer from shipments
#    quest checker
#    Add feature that enables the user to tell the bot what exact expedition to go on from the locations
#    gui
#    Show gold status health status and experience status in gui
#    Function that enables you to run the bot without the bot window open
#    Program it so the user can play whenever he wants and the bot will still do the things he has to do
#    Show times of the auction in gui
#    Turma and Arena attack list
#    Checker for the worst enemies in both arena provinciarum and circus turma provinciarum and picking
#    by percentage winrate against them
#    option to donate all your gold to your guild every x minutes
#    Add to gui if there are updates availible
#    Botting multiple accounts at the same time
#    add compatiblity for other other servers then czech
#    Randomized waiting time to avoid detection
#    Scheduler to havee breaks sometime and dont run 24/7
#    Reports from the bot
#    Save gold from auction
#    Save gold from guild
#    Create a site for the gladiatus bot
#    Do compatibility for both chromedrivers and operadrivers


def fb_start_up():
    global error
    expedition_opponent = 4
    # If dungeon difficulty is advanced it will go to the advanced dungeon , if its beginner it will go to the beginner
    # dungeon
    dungeon_difficulty = "advanced"
    error = True
    import time
    from selenium import webdriver
    from selenium.common.exceptions import ElementClickInterceptedException
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.chrome import service
    from Gladiatus_project_v2.Encrypting_lib import write_key_1, write_key_2, write_key_3, load_key_1, \
        load_key_2, load_key_3, encrypt, decrypt

    # Expedition function
    def expedition():
        # the expedtion
        # This part of code serves for the expedition tab to even open so we could locate the opponents later on
        time.sleep(10)
        expedition_loc = driver.find_element_by_xpath("//div[@id='cooldown_bar_expedition']//a["
                                                      "@class='cooldown_bar_link']")
        time.sleep(2)
        expedition_loc.click()
        time.sleep(2)

        class ExpeditionOpponents:
            expedition_1 = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[5]/div[1]/div[2]/div["
                                                        "2]/div[2]/div[1]/div[2]/button[1]")
            expedition_2 = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[5]/div[1]/div[2]/div["
                                                        "2]/div[2]/div[2]/div[2]/button[1]")
            expedition_3 = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[5]/div[1]/div[2]/div["
                                                        "2]/div[2]/div[3]/div[2]/button[1]")
            expedition_4 = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[5]/div[1]/div[2]/div["
                                                        "2]/div[2]/div[4]/div[2]/button[1]")

        time.sleep(3)

        # Here we choose what opponent to against by a variable, what later on I want to try to change this
        # variable by using gui
        if expedition_opponent == 1:
            ExpeditionOpponents.expedition_1.click()
        elif expedition_opponent == 2:
            ExpeditionOpponents.expedition_2.click()
        elif expedition_opponent == 3:
            ExpeditionOpponents.expedition_3.click()
        elif expedition_opponent == 4:
            ExpeditionOpponents.expedition_4.click()

    # Here with this class we basically define all the opponents you can get once u go on an expedition
    # Here we basically check if we can go on an expedition, if cooldown bar is true it means we have to wait for

    def expedition_sched():
        time.sleep(3)
        wait_expedition = driver.find_element_by_xpath("//div[@id='cooldown_bar_text_expedition']")
        wait_time_expedition = wait_expedition.get_attribute('innerHTML')
        if wait_time_expedition == "Jít na výpravu":
            expedition()
        else:
            time_to_wait = (wait_time_expedition.strip())
            time_to_wait = str(time_to_wait)
            trash, minutes, seconds, = time_to_wait.split(':')
            minutes = str(minutes)
            if "0" in minutes:
                minutes = str(minutes)
                minutes.strip("0")
            minutes = (int(minutes) * 60)
            seconds = int(seconds)
            time_wait_expedition = minutes + seconds
            time.sleep(time_wait_expedition)
            expedition()

    # Expedition function
    # Expedition function
    # Expedition function
    # Expedition function
    # Expedition function
    # Expedition function
    # Expedition function
    # Expedition function
    def dungeon_sched():
        time.sleep(5)
        wait_dungeon = driver.find_element_by_xpath("//div[@id='cooldown_bar_text_dungeon']")
        wait_time_dungeon = wait_dungeon.get_attribute('innerHTML')
        if wait_time_dungeon == "Jít do bludiště":
            dungeon()
        else:
            time_to_wait = (wait_time_dungeon.strip())
            time_to_wait = str(time_to_wait)
            trash, minutes, seconds, = time_to_wait.split(':')
            minutes = str(minutes)
            if "0" in minutes:
                minutes = str(minutes)
                minutes.strip("0")
            minutes = (int(minutes) * 60)
            seconds = int(seconds)
            time_wait_dungeon = minutes + seconds
            print(str(time_wait_dungeon) + "till next dungeon.")
            dungeon()

    def dungeon():
        # Here cooldown_bar_d means cooldown bar dungeon

        # This part of code serves for the expedition tab to even open so we could locate the opponents later on
        time.sleep(10)
        dungeon_loc = driver.find_element_by_xpath("//div[@id='cooldown_bar_dungeon']//a["
                                                   "@class='cooldown_bar_link']")
        time.sleep(2)
        dungeon_loc.click()
        time.sleep(2)
        try:
            beginner = driver.find_element_by_xpath("//input[@value='Normální']")
            advanced = driver.find_element_by_xpath("//input[@value='Pokročilý']")
            if dungeon_difficulty == "advanced":
                advanced.click()
            elif dungeon_difficulty == "beginner":
                beginner.click()
        except NoSuchElementException:
            ""
        dungeon_opponent = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div['
                                                        '2]/div[1]/img[6]')
        time.sleep(5)
        dungeon_opponent.click()

        # Here we choose what opponent to against by a variable, what later on I want to try to change this
        # variable by using gui

        # Dungeon function
        # Dungeon function
        # Dungeon function
        # Dungeon function
        # Dungeon function
        # Dungeon function

    # For now I am going to store all keys in one directory but with time i want to try reading the keys from server
    # and I wanna store the passwords encrypted on server
    # Decrypting 1
    with open('key_1.txt', 'r+') as key_11:
        for lines_1 in key_11:
            lines_1 = str(lines_1)
    # Decrypting 1 seems ok
    decrypt('Hesla.txt', key=lines_1)

    # Decrypting 2
    with open('key_2.txt', 'r+') as key_22:
        for lines_2 in key_22:
            lines_2 = str(lines_2)
        # Decrypting 2 seems ok aswell
    decrypt('Hesla.txt', key=lines_2)

    # Decrypting 3
    with open('key_3.txt', 'r+') as key_33:
        for lines_3 in key_33:
            lines_3 = str(lines_3)
        # Decrypting 3 seems ok aswell
    decrypt('Hesla.txt', key=lines_3)

    # Writing key 1
    write_key_1()

    # Writing key 2
    write_key_2()

    # Writing key 3
    write_key_3()

    # The block of writing keys is ok aswell

    # In this block of code we basically read the password and name from txt file, In future I want to encrypt this
    password_email = open('Hesla.txt', "r")
    email = password_email.readline()
    email = email.strip("\n")
    password = password_email.readline()
    password_email.close()

    # Encrypting 1
    key_3 = load_key_3()

    file = "Hesla.txt"
    # encrypt it
    encrypt(file, key_3)

    # Encrypting 2
    key_2 = load_key_2()

    file = "Hesla.txt"
    # encrypt it
    encrypt(file, key_2)

    # Encrypting 3
    key_1 = load_key_1()

    file = "Hesla.txt"
    # encrypt it
    encrypt(file, key_1)

    # Here we basically start opera
    # Later on I will want to get to know where do they have the driver without knowing the exact location before.
    # and probably know their username
    webdriver_service = service.Service('C:\\Users\\vojta\\OneDrive\\Dokumenty\\chromedriver.exe')
    webdriver_service.start()
    driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.CHROME)
    driver.get('https://s36-cz.gladiatus.gameforge.com/game/index.php')
    driver.minimize_window()
    # With this part of code we handle the error when it does not have enough time so it does not find the element
    time.sleep(2)
    # Here you tell the driver to click the facebook login icon
    # and u tell him beforehand what is the main window
    facebook_login = driver.find_element_by_class_name("facebook-login-button-icon")
    time.sleep(2)
    # Here you switch from the main window to the popup window
    parent_window = driver.current_window_handle
    facebook_login.click()
    handles = driver.window_handles
    time.sleep(2)
    handles.remove(parent_window)
    driver.switch_to.window(handles.pop())
    time.sleep(1)

    # Here you are typing your email to facebook and handling time error at the same time
    email_colon = driver.find_element_by_name('email')
    email_colon.send_keys(email)
    time.sleep(1)

    # The same but with password here
    password_colon = driver.find_element_by_name('pass')
    password_colon.send_keys(password)
    time.sleep(1)
    facebook_cookie_accept = driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div['
                                                          '1]/div[3]/button[2]')
    facebook_cookie_accept.click()
    # Here you click the login button after you've put in your password and email
    login_button = driver.find_element_by_name('login')
    login_button.click()
    driver.switch_to.window(parent_window)
    time.sleep(5)
    # Here u click that you wanna play the game and it redirects u to page with your accs
    gladiatus_play_button = driver.find_element_by_link_text('HRÁT')
    # Hre u click the button start playing of the last account you played on
    time.sleep(5)
    gladiatus_play_button.click()
    time.sleep(5)
    # window_before = driver.window_handles[0] (If i want to use this part of code I would have to have problem, when
    # I want to reuse the first window after I switched to the second)
    first_acc_bttn = driver.find_element_by_xpath("//div[@class='rt-tr-group open']//span[normalize-space()='Hrát']")
    first_acc_bttn.click()
    window_after = driver.window_handles[1]
    time.sleep(2)
    driver.close()
    driver.switch_to.window(window_after)
    # Here I am trying to handle the error when it stops on loading screen
    try:
        time.sleep(2)
        driver.find_element_by_class_name('sk-spinner center-spinner ball-grid-pulse')
    except NoSuchElementException:
        error = True
    if error is False:
        driver.quit()
        fb_start_up()
    # Later on I want to optimalize the timings for the program so they are just right and I will do it with :
    # https://selenium-python.readthedocs.io/waits.html
    time.sleep(2)

    # THIS IS WHERE  STARTUP PROGRAM ENDS
    # THIS IS WHERE  STARTUP PROGRAM ENDS
    # THIS IS WHERE  STARTUP PROGRAM ENDS
    # THIS IS WHERE  STARTUP PROGRAM ENDS
    # THIS IS WHERE  STARTUP PROGRAM ENDS
    # THIS IS WHERE  STARTUP PROGRAM ENDS
    # THIS IS WHERE  STARTUP PROGRAM ENDS

    # These are the lines of code i use for endless going on expedition and dungeon in loop

    # With time I will want to reprogram it so the user can choose exactly what expedition to go on
    while True:
        try:
            dungeon_sched()
        except ElementClickInterceptedException:
            driver.find_element_by_id('linkLoginBonus').click()


fb_start_up()

# These lines should part of the code in the end when I want to handle the errors
#     try:
#     except NoSuchElementException:
#         driver.quit()
#         start_up()
