from fake_useragent import UserAgent

if __name__ == '__main__':
    ua = UserAgent()
    # print(ua.ie)
    # print(ua.opera)
    # print(ua.chrome)
    # print(ua.google)
    # print(ua['google chrome'])
    # print(ua.firefox)
    # print(ua.ff)
    # print(ua.safari)
    i = 0;
    while (i < 50):
        print(ua.random)
        i += 1
