import webbrowser as wb

s_string = input("Enter search string: ").strip(" ")
wb.open(f"https://google.com/search?q={s_string.replace(' ', '+')}")