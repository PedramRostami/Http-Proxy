import CategoryApp
import WebsitesApp
import HttpProxy
import StatusApp
import threading

if __name__ == '__main__' :
    default_user_data = [['sport', [['amirmaleki.com', 12], ['aaa.com', 23]], 35],
                         ['work', [['senario.net', 223], ['ooo.ir', 200]], 423]]

    # StatusApp.StatusApp(default_user_data)
    data = []
    category_app = CategoryApp.CategoryApp()
    for i in range(len(category_app.category_items_list)):
        temp_app = WebsitesApp.WebsitesApp(category_app.category_items_list[i])
        temp_list = []
        for j in range(len(temp_app.websites_list)):
            temp_list.append([temp_app.websites_list[j], 0])
        data.append([category_app.category_items_list[i], temp_list, 0])

    print(data)
    print(data[0][1][0][1])
    http_proxy = HttpProxy.HttpProxy('127.0.0.1', 12345, data)
    d = threading.Thread(target=http_proxy.run)
    d.start()
    print('http proxy is running ...')
    print('press \'1\' and then \'Enter\' to see usage')
    print('if you want to refresh, quit status window and press \'1\' and \'Enter\' again')
    while True:
        s = int(input())
        if s == 1:
            StatusApp.StatusApp(http_proxy.user_data)