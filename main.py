import requests
import json



def save_webpage_content_to_json(url, output_file):
    # Send a GET request to the URL
    response = requests.get(url)
    
    if response.status_code == 200:  # If the request is successful
        # Get the content from the response
        webpage_content = response.text
        
        # Create a dictionary to store the webpage content
        data = {
            "url": url,
            "content": webpage_content
        }
        
        # Write the content to a JSON file
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"Webpage content saved to {output_file} successfully.")
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")


if __name__ == "__main__":
    # Example usage:
    userSearch = input("Please enter something you want to find, doesn't need to be an ottoman but it can be.\n")
    webpage_url = "https://bellingham.craigslist.org/search/sss?query=%#search=1~gallery~0~0" % (userSearch)  # Replace this with the URL of the webpage you want to fetch
    output_filename = "webpage_content.json"  # Replace this with your desired output file name
    
    save_webpage_content_to_json(webpage_url, output_filename)

# Open the JSON file
with open('webpage_content.json', 'r', encoding='utf-8') as json_file:
    # Read each line of the JSON file
    for line in json_file:
        # Parse the line as JSON and print it
        print(line)


