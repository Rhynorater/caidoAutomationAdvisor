import requests
import json

def get_digest_url(input_text):
    """Sends a POST request to the ingest API and returns the digest_url."""
    url = "https://gitingest.com/api/ingest"
    data = {
        "input_text": input_text,
        "token": "",
        "max_file_size": "1851",
        "pattern_type": "include",
        "pattern": "*.md"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.json().get("digest_url")

def download_and_merge(urls):
    """Downloads content from a list of URLs and merges them."""
    merged_content = ""
    for url in urls:
        if url:
            response = requests.get(url)
            response.raise_for_status()
            merged_content += response.text + "\n"
    return merged_content

if __name__ == "__main__":
    input_texts = [
        "caido/doc-developer/tree/main/src/reference",
        "caido/documentation/tree/main/src/reference"
    ]
    
    digest_urls = []
    for text in input_texts:
        try:
            digest_url = get_digest_url(text)
            print(f"Successfully got digest_url for {text}: {digest_url}")
            digest_urls.append(digest_url)
        except requests.exceptions.RequestException as e:
            print(f"Error getting digest_url for {text}: {e}")

    if digest_urls:
        try:
            merged_content = download_and_merge(digest_urls)
            with open("merged_documentation.txt", "w") as f:
                f.write(merged_content)
            print("Successfully downloaded and merged documentation into merged_documentation.md")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading or merging content: {e}")
