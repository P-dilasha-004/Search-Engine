from wiki import article_metadata, ask_search, ask_advanced_search

def search_two(keyword):
    keyword = keyword.strip()
    metadata = article_metadata()
    result_metadata = []
    for article in metadata:
        if len(article) == 0:
            continue
        for relevant_keyword in article[4]:
            if relevant_keyword.lower() == keyword.lower():
                result_metadata.append(article[:4])
    return result_metadata


def article_length(max_length, metadata):
    result_metadata = []
    for article in metadata:
        if len(article) == 0:
            continue
        if article[3] <= max_length:
            result_metadata.append(article[:4])
    return result_metadata
  

def unique_authors(count, metadata):
    if count <= 0 or len(metadata) == 0:
        return []
    authors_set = set()
    result_metadata = []
    for article in metadata:
        if len(article) == 0:
            continue
        author = article[1].lower()
        if not author in authors_set:
            result_metadata.append(article[:4])
            authors_set.add(author)
        if len(result_metadata) == count:
            break
    return result_metadata
  

def most_recent_article(metadata):
    time = 0
    result_metadata = []
    if len(metadata) == 0:
        return result_metadata
    for article in metadata:
        if len(article) == 0:
            continue
        if article[2] > time:
            result_metadata = article[:4]
            time = article[2]
    return result_metadata


def favorite_author(favorite, metadata):
    favorite = favorite.strip()
    for article in metadata:
        if len(article) == 0:
            continue
        if favorite.lower() == article[1].lower():
            return True
    return False
  

def title_and_author(metadata):
    result_metadata = []
    for article in metadata:
        if len(article) == 0:
            continue
        result_metadata.append((article[0], article[1]))
    return result_metadata


def refine_search(keyword, metadata):
    new_metadata = search_two(keyword)
    result_metadata = []
    for article in metadata:
        if article in new_metadata:
            result_metadata.append(article)
    return result_metadata

def display_result():
  
    articles = search_two(ask_search())

    advanced, value = ask_advanced_search()

    if advanced == 6:
        articles = article_length(value, articles)
    if advanced == 7:
        articles = unique_authors(value, articles)
    elif advanced == 8:
        articles = most_recent_article(articles)
    elif advanced == 9:
        has_favorite = favorite_author(value, articles)
    elif advanced == 10:
        articles = title_and_author(articles)
    elif advanced == 11:
        articles = refine_search(value, articles)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

    if advanced == 4:
        print("Your favorite author is" + ("" if has_favorite else " not") + " in the returned articles!")

if __name__ == "__main__":
    display_result()
    