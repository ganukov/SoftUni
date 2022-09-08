import webbrowser as wb


def web_automation():
    chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
    URLS = ("stackoverflow.com", "github.com", "google.com", "gmail.com")

    for url in URLS:
        print("Opening: " + url)
        wb.get(chrome_path).open(url)


web_automation()
