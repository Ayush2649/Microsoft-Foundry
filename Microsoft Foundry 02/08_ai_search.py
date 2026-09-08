from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient

search_client = SearchClient(
    endpoint="https://cloudxeusdev04.search.windows.net",
    index_name="rag-1788706303333",
    credential=DefaultAzureCredential(),
)

results = search_client.search(
    search_text="refund",
    select=["chunk", "title"],
)

for result in results:
    print(f"Score:  {result['@search.score']:.4f}")
    print(f"Source: {result['title']}")
    print(f"Text:   {result['chunk']}")
    print("---")