import webbrowser

# Dicthinary to store my favourite websites
my_websites = {"Youtube" : "https://www.youtube.com/", 
               "Whatsapp" : "https://web.whatsapp.com/",
               "Hacking Cpp": "https://hackingcpp.com/",
               "Chat GPT" : "https://chat.openai.com/",
               "Coursera" : "https://www.coursera.org/",
               "Udemy" : "https://www.udemy.com/"}

# function take the name of website and open it in default webbrowser
def open_web(name):
    if name in my_websites:
        url = my_websites[name]
        webbrowser.get("firefox").open(url)
    else:
        print(f"{name} is not in your list of websites.")

print("Welcome to favorite website program.")

while(True):
    print("\nYour favourite websites are : ")
    for web_name in my_websites.keys():
        print(web_name)

    website_name = input("\nEnter the name of website you want from this list (or 'q' to exist) : ")

    if website_name.lower() == "q":
        break
    else:
        open_web(website_name)