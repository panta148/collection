for block in info_div:
        print(block) 
        text=block.find("strong",class_="bg-blue").get_text()
        count=block.find("span",class_="bg-blue").get_text()
    print(text+":"+count)