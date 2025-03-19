from selenium.webdriver.common.by import By

class FeedPageLocators:
    all_time_text = [By.XPATH, ".//p[text()='Выполнено за все время:']"]
    all_time_count = [By.XPATH, "//div[@class='undefined mb-15']/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"]
    today_text = [By.XPATH, ".//p[text()='Выполнено за сегодня:']"]
    today_count = [By.XPATH, ".//div[last()]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"]
    search_order = [By.XPATH, ".//p[@class='text text_type_digits-default']"]
    icon_constructor = [By.XPATH, ".//p[text()='Конструктор']"]
    in_process_counter = [By.XPATH,".//li[(@class='text text_type_digits-default mb-2')]/parent::ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']"]
    first_order = [By.XPATH, ".//li[@class='OrderHistory_listItem__2x95r mb-6']/a[@class='OrderHistory_link__1iNby']"]
    composition = [By.XPATH, ".//p[text()='Cостав']"]
    personal_account = [By.XPATH, ".//p[text()='Личный Кабинет']"]