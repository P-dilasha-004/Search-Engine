from wiki import article_titles, ask_search, ask_advanced_search


def search_one(keyword):
    keyword = str(keyword)
    keyword = keyword.lower().strip()
    if len(keyword) == 0:
        return []
    article_title_list = article_titles()
    article_title_with_keyword = []
    for article in article_title_list:
        if keyword in article.lower():
            article_title_with_keyword.append(article)
    return article_title_with_keyword
     

def title_length(max_length, titles):
    try:
        if max_length <= 0:
            return []
        titles_within_limit = []
        for title in titles:
            if len(title) <= int(max_length):
                titles_within_limit.append(title)
        return titles_within_limit
    except TypeError:
        return "Not a valid length"


def article_count(count, titles):
    if count <= 0:
        return []
    if count > len(titles):
        return titles
    return titles[:count]
    

def random_article(index, titles):
    try:
        index = int(index)
        if index < 0 or index >= len(titles):
            return ''
        return titles[index]
    except TypeError:
        return 'Not a valid index'
    except ValueError:
        return 'Not a valid index'
      

def favorite_article(favorite, titles):
    favorite = favorite.strip()
    
    titles = list(map(lambda title: title.lower(), titles))
    
    if favorite.lower() in titles:
        return True
    else:
        return False

def multiple_keywords(keyword, titles):
    if len(search_one(keyword)) == 0:
        return titles

    if titles == search_one(keyword):
        return titles

    article_titles_with_new_keyword = set(search_one(keyword))
    return list(article_titles_with_new_keyword.union(set(titles)))
    

def display_result():
  
    articles = search_one(ask_search())
    
    advanced, value = ask_advanced_search()

    if advanced == 1:
        articles = title_length(value, articles)
    if advanced == 2:
        articles = article_count(value, articles)
    elif advanced == 3:
        articles = random_article(value, articles)
    elif advanced == 4:
        has_favorite = favorite_article(value, articles)
    elif advanced == 5:
        articles = multiple_keywords(value, articles)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

    if advanced == 4:
        print("Your favorite article is" + ("" if has_favorite else " not") + " in the returned articles!")

if __name__ == "__main__":
    display_result()


        
