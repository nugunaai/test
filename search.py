import meilisearch

# client = meilisearch.Client('http://localhost:7700', 'UnZt-Twd2nxjfOnflA1PT0mMHcH154hJcpDrQRjADfo')
client = meilisearch.Client('https://ms-aeee07451e97-23818.jpn.meilisearch.io', '0fcfd13faeb2a3bb4f90034069f57536d339e21e')

def stock_search(query):
    return client.index('nasdaq').search(query)
