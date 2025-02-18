from wiki import article_metadata, ask_search, ask_advanced_search
import datetime
import time

def keyword_to_titles(metadata):

    keyword_to_articles = {}

    for article in metadata:

        title = article[0]
        keywords = article[4]

        for keyword in keywords: 

            if keyword not in keyword_to_articles:
                keyword_to_articles[keyword] = []

            keyword_to_articles[keyword].append(title)

    return keyword_to_articles
     

def title_to_info(metadata):

    article_titles = {}

    for article_list in metadata: 
    
        if not article_list or len(article_list) < 4 or not article_list[0]: 
            continue 

        article_information = {
            'author': article_list[1], 
            'timestamp': article_list[2], 
            'length': article_list[3]
        }

        article_titles[article_list[0]] = article_information

    return article_titles

def search_three(keyword, keyword_to_titles):

    keyword_titles = keyword_to_titles

    if keyword not in keyword_titles: 
        return []

    return keyword_titles[keyword]
    
    
def article_length(max_length, article_titles, title_to_info):

    article_list = []

    for article in article_titles: 

        if article in title_to_info and title_to_info[article]['length'] <= max_length: 
            article_list.append(article)

    return article_list


def key_by_author(article_titles, title_to_info):

    if not title_to_info or not article_titles: 
        return {}

    author_articles = {}

    for article in article_titles:

        if article not in title_to_info:
            continue 

        author = title_to_info[article]['author']

        if author not in author_articles:
            author_articles[author] = []
        author_articles[author].append(article)

    return author_articles


def filter_to_author(author, article_titles, title_to_info):

    article_titles_list = []

    for article in article_titles: 

        if title_to_info[article]['author'] == author: 
            article_titles_list.append(article)

    return article_titles_list


def filter_out(keyword, article_titles, keyword_to_titles):

   filtered_articles = []

   if keyword not in keyword_to_titles:
        return article_titles

   excluded_articles = keyword_to_titles[keyword]

   for article in article_titles: 
        if article not in excluded_articles: 
            filtered_articles.append(article)

   return filtered_articles


def articles_from_year(year, article_titles, title_to_info):
    first_day_of_year = datetime.date(year, 1, 1)
    last_day_of_year = datetime.date(year+1, 1, 1)
    first_day_unix = int(time.mktime(first_day_of_year.timetuple()))
    last_day_unix = int(time.mktime(last_day_of_year.timetuple()))

    articles_from_year_list = []

    for article_title in article_titles:
        if title_to_info[article_title]['timestamp'] in range(first_day_unix, last_day_unix):
            articles_from_year_list.append(article_title)
   
    return articles_from_year_list


def display_result():
    
    keyword_to_titles_dict = keyword_to_titles(article_metadata())
    title_to_info_dict = title_to_info(article_metadata())
    
    articles = search_three(ask_search(), keyword_to_titles_dict)

    advanced, value = ask_advanced_search()

    if advanced == 12:
        articles = article_length(value, articles, title_to_info_dict)
    if advanced == 13:
        articles = key_by_author(articles, title_to_info_dict)
    elif advanced == 14:
        articles = filter_to_author(value, articles, title_to_info_dict)
    elif advanced == 15:
        articles = filter_out(value, articles, keyword_to_titles_dict)
    elif advanced == 16:
        articles = articles_from_year(value, articles, title_to_info_dict)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

if __name__ == "__main__":
    display_result()