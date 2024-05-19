# -*- coding: utf-8 -*-  # Define the encoding of the script
# usr/bin/env/python  # Specify the interpreter for the script
# Err0r_HB  # Author information
# Cyb3r Drag0nz Team  # Team information

import random  # Import the random module for shuffling lines
import sys  # Import sys module for system-specific parameters and functions
import time  # Import the time module for time-related functions
import os  # Import the os module for operating system functions
import re  # Import the re module for regular expressions
import concurrent.futures  # Import concurrent.futures for parallel execution
import requests  # Import requests library for HTTP requests
import tldextract  # Import tldextract module for extracting domain from URLs
from colorama import init, Fore  # Import colorama for colored text output
from requests.packages.urllib3.exceptions import (
    InsecureRequestWarning,
)  # Import specific exception

init()  # Initialize colorama for colored text output
requests.packages.urllib3.disable_warnings(
    InsecureRequestWarning
)  # Disable insecure request warnings

if os.name == "nt":
    os.system("cls")  # Clear the screen for Windows OS
else:
    os.system("clear")  # Clear the screen for Unix-like OS

# Colors
RED = "\033[31m"  # Define the color red
GREEN = "\033[32m"  # Define the color green
YELLOW = "\033[33m"  # Define the color yellow
BLUE = "\033[34m"  # Define the color blue
CYAN = "\033[36m"  # Define the color cyan
BOLD = "\033[1m"  # Define bold text
MAGENTA = "\033[35m"  # Define the color magenta


def remove_duplicates(input_file, output_file):  # Define a function to remove duplicates from input file and write to output file
    # Function to remove duplicate lines from a text file
    unique_lines = set()  # Create an empty set to store unique lines
    deleted_lines_count = 0  # Initialize the count of deleted lines

    encodings = ["utf-8", "latin-1"]  # Specify possible encodings of the input file

    for encoding in encodings:
        try:  # Attempt to open the input file with different encodings
            with open(input_file, "r", encoding=encoding) as file:
                for line in file:  # Iterate through each line in the file
                    unique_lines.add(line.strip())  # Add stripped lines to the set
        except UnicodeDecodeError:  # Handle UnicodeDecodeError
            continue  # Continue with the next encoding
        else:
            break  # Break the loop if successful decoding

    with open(
        output_file, "w", encoding="utf-8"
    ) as file:  # Open the output file for writing
        for line in unique_lines:  # Iterate through unique lines
            file.write(line + "\n")  # Write each unique line to the output file

    if len(unique_lines) > 0:  # Check if there are unique lines
        # Calculate the count of deleted lines
        deleted_lines_count = sum(
            1 for line in open(input_file, "r", encoding=encoding)
        ) - len(unique_lines)

    return deleted_lines_count, len(
        unique_lines
    )  # Return counts of deleted and unique lines


def randomize_lines(input_file):
    # Function to randomize the order of lines in a text file
    with open(input_file, "r") as f:  # Open the input file for reading
        lines = f.readlines()  # Read all lines from the file

    random.shuffle(lines)  # Shuffle the lines randomly

    with open(
        "randomize.txt", "w"
    ) as f:  # Open a new file for writing the randomized lines
        f.writelines(lines)  # Write the shuffled lines to the new file


def list_lines_lexicographically():
    # Function to list lines in lexicographically ascending order
    file_path = input("Please enter the file path: ")  # Get the file path from the user

    with open(file_path, "r", encoding="utf-8") as file:  # Open the file for reading
        lines = file.readlines()  # Read all lines from the file

    lines.sort()  # Sort the lines in lexicographical order

    with open(
        "lex.txt", "w", encoding="utf-8"
    ) as output_file:  # Open a new file for writing sorted lines
        for line in lines:  # Iterate through sorted lines
            output_file.write(line.strip() + "\n")  # Write each line to the output file

    print(
        Fore.WHITE + "Sorted lines have been saved to lex.txt"
    )  # Print a message indicating successful sorting


def list_lines_lexicographically_descending():
    # Function to list lines in lexicographically descending order
    file_path = input("Please enter the file path: ")  # Get the file path from the user

    with open(file_path, "r", encoding="utf-8") as file:  # Open the file for reading
        lines = file.readlines()  # Read all lines from the file

    lines.sort(reverse=True)  # Sort the lines in descending order

    with open(
        "desc.txt", "w", encoding="utf-8"
    ) as output_file:  # Open a new file for writing sorted lines
        for line in lines:  # Iterate through sorted lines
            output_file.write(line.strip() + "\n")  # Write each line to the output file

    print(
        Fore.WHITE + "Sorted lines in descending order have been saved to desc.txt"
    )  # Print a message indicating successful sorting


def merge_txt_files(folder_path, output_file_path, buffer_size=1024 * 1024):
    # Function to merge multiple .txt files into a single file
    with open(
        output_file_path, "wb"
    ) as output_file:  # Open the output file in binary write mode
        for filename in os.listdir(
            folder_path
        ):  # Iterate through files in the specified folder
            if filename.endswith(".txt"):  # Check if the file is a .txt file
                file_path = os.path.join(
                    folder_path, filename
                )  # Get the full path of the file
                with open(
                    file_path, "rb"
                ) as input_file:  # Open the file in binary read mode
                    while True:  # Loop until the end of the file
                        data = input_file.read(buffer_size)  # Read data from the file
                        if not data:  # Check if no data is read
                            break  # Break the loop
                        output_file.write(data)  # Write the data to the output file

    print(
        Fore.WHITE + "Merging complete. Output file:", output_file_path
    )  # Print a message indicating successful merging


def merge_html_files(folder_path, output_file_path, buffer_size=1024 * 1024):
    # Function to merge multiple .html files into a single file
    with open(
        output_file_path, "w", encoding="utf-8"
    ) as output_file:  # Open the output file for writing
        for filename in os.listdir(
            folder_path
        ):  # Iterate through files in the specified folder
            if filename.endswith(".html"):  # Check if the file is a .html file
                file_path = os.path.join(
                    folder_path, filename
                )  # Get the full path of the file
                with open(
                    file_path, "r", encoding="utf-8"
                ) as input_file:  # Open the file for reading
                    while True:  # Loop until the end of the file
                        data = input_file.read(buffer_size)  # Read data from the file
                        if not data:  # Check if no data is read
                            break  # Break the loop
                        output_file.write(data)  # Write the data to the output file

    print(
        Fore.WHITE + "Merging complete. Output file:", output_file_path
    )  # Print a message indicating successful merging


def filter_urls_from_text_files():
    # Function to filter URLs from text files
    input_file = input(
        "Please enter the path of the input text file: "
    )  # Get the input text file path
    output_file = input(
        "Please enter the path of the output file to save filtered URLs: "
    )  # Get the output file path

    with open(input_file, "r", encoding="utf-8") as f, open(
        output_file, "w", encoding="utf-8"
    ) as out:
        # Open input and output files for reading and writing
        for line in f:  # Iterate through each line in the input file
            if line.strip().startswith("http://") or line.strip().startswith(
                "https://"
            ):
                out.write(
                    line
                )  # Write lines starting with http:// or https:// to the output file

    print(
        Fore.WHITE + "URLs filtered and saved successfully."
    )  # Print a message indicating successful filtering

def check_url(url):
    response = requests.get(url)  # Sending a GET request to the specified URL
    if response.status_code == 200:  # Checking if the response status code is 200 (OK)
        return f"{url} - 200 OK"  # Returning a success message if status code is 200
    else:
        return f"{url} - {response.status_code}"  # Returning the URL along with the status code

# File Checker function to check and remove certain files if they exist
def file_checker():
    if os.path.exists("bad_con.txt"):  # Checking if "bad_con.txt" file exists
        os.remove("bad_con.txt")  # Removing the "bad_con.txt" file if it exists
    if os.path.exists("dead.txt"):  # Checking if "dead.txt" file exists
        os.remove("dead.txt")  # Removing the "dead.txt" file if it exists
    if os.path.exists("live.txt"):  # Checking if "live.txt" file exists
        os.remove("live.txt")  # Removing the "live.txt" file if it exists
    if os.path.exists("ddos_guard.txt"):  # Checking if "ddos_guard.txt" file exists
        os.remove("ddos_guard.txt")  # Removing the "ddos_guard.txt" file if it exists
    if os.path.exists("redirects.txt"):  # Checking if "redirects.txt" file exists
        os.remove("redirects.txt")  # Removing the "redirects.txt" file if it exists

def remove_duplicate_domains(input_file):
    unique_domains = set()  # Initialize a set to store unique domains
    deleted_domains_count = 0  # Initialize count for deleted duplicate domains

    with open(input_file, "r") as file:
        for line in file:
            line = line.strip()
            domain = re.search(
                r"(?<=://)(.*?)(?=/|:|$)", line
            )  # Extract domain from URL
            if domain and domain.group():  # Check if domain is found
                domain_name = domain.group()
                if domain_name not in unique_domains:  # Check if domain is unique
                    unique_domains.add(
                        domain_name
                    )  # Add domain to unique_domains set if not present
                else:
                    deleted_domains_count += (
                        1  # Increment count of deleted duplicate domains
                    )

    with open(input_file, "w") as output:
        for domain in unique_domains:
            output.write(
                f"http://{domain}\n"
            )  # Write unique domains to the output file with http:// prefix

    return deleted_domains_count, len(
        unique_domains
    )  # Return count of deleted domains and total unique domains


def extract_domains(text):
    # Function to extract domains from URLs in a text
    url_regex = r"(https?://\S+)"  # Define the regex pattern for URLs
    urls = re.findall(url_regex, text)  # Find all URLs in the text
    domains = set()  # Create an empty set to store unique domains

    for url in urls:  # Iterate through each URL
        domain = re.findall(
            r"https?://([^\s/]+)", url
        )  # Extract the domain from the URL
        if domain:
            domains.add(domain[0])  # Add the domain to the set

    return domains  # Return the set of extracted domains


def filter_urls_from_text_files(input_file):  # Function to filter URLs from text files
    unique_urls = set()  # Create an empty set to store unique URLs
    sorted_urls = []  # Create an empty list to store sorted URLs

    with open(input_file, "r") as file:  # Open the input file in read mode
        for line in file:  # Iterate through each line in the file
            url = line.strip()  # Remove leading and trailing whitespaces from the line

            # Check if URL status code is 200
            try:
                response = requests.head(
                    url, allow_redirects=True
                )  # Send a HEAD request to the URL
                if (
                    response.status_code == 200
                ):  # Check if the response status code is 200
                    # Check if URLs start with 'http://' or 'https://'
                    if url.startswith("http://") or url.startswith(
                        "https://"
                    ):  # Check URL prefixes
                        domain = url.split("//")[-1].split("/")[
                            0
                        ]  # Extract domain from the URL
                        if (
                            domain,
                            url,
                        ) not in unique_urls:  # Check if domain and URL tuple is unique
                            unique_urls.add(
                                (domain, url)
                            )  # Add unique domain and URL tuple to the set
                            sorted_urls.append(url)  # Append the URL to the sorted list
            except requests.ConnectionError:  # Handle connection errors
                continue  # Continue to the next iteration

    sorted_urls.sort()  # Sort URLs lexicographically in ascending order

    with open(input_file, "w") as file:  # Open the input file in write mode
        for url in sorted_urls:  # Iterate through sorted URLs
            file.write(
                url + "\n"
            )  # Write each URL to the file with a newline character

    print(
        "\nFiltered URLs saved and printed in the same input file."
    )  # Print a message indicating URLs are filtered and saved


def check_cms(input_file):  # Function to check if URLs belong to WordPress sites
    wordpress_urls = []  # List to store WordPress URLs

    try:  # Try block to handle file opening
        with open(input_file, "r") as file:  # Open input file for reading
            urls = file.readlines()  # Read URLs from the file

            for url in urls:  # Iterate over each URL in the file
                url = url.strip()  # Remove leading/trailing whitespaces
                if not url.startswith("http"):  # Check if URL is missing protocol
                    url = "http://" + url  # Add http:// if missing

                try:  # Try block to handle HTTP requests
                    response = requests.get(f"{url}/wp-login.php", timeout=5)  # Send GET request to WordPress login page
                    if response.status_code == 200:  # Check if WordPress login page exists
                        print(f"{url} is a WordPress site.")  # Print message if URL is a WordPress site
                        wordpress_urls.append(url)  # Add WordPress URL to the list
                except requests.exceptions.RequestException as e:  # Handle request exceptions
                    print(f"Error occurred for {url}: {e}")  # Print error message

    except FileNotFoundError:  # Handle file not found error
        print("Input file not found.")  # Print error message

    # Save WordPress URLs to a file
    with open("wp.txt", "w") as wp_file:  # Open file for writing WordPress URLs
        for wp_url in wordpress_urls:  # Iterate over WordPress URLs
            wp_file.write(wp_url + "\n")  # Write WordPress URL to the file

    return len(wordpress_urls)  # Return the count of WordPress URLs found

def trim_http_https(input_file, output_file):
    # Function to trim "http://" or "https://" from URLs in a file
    trimmed_urls = []  # Initialize an empty list to store trimmed URLs

    with open(input_file, "r") as file:  # Open the input file in read mode
        for line in file:  # Iterate through each line in the input file
            if line.startswith("http://"):  # Check if the line starts with "http://"
                trimmed_urls.append(
                    line[len("http://") :].strip()
                )  # Add the trimmed URL to the list
            elif line.startswith(
                "https://"
            ):  # Check if the line starts with "https://"
                trimmed_urls.append(
                    line[len("https://") :].strip()
                )  # Add the trimmed URL to the list
            else:
                trimmed_urls.append(
                    line.strip()
                )  # Add the original line to the list if no trimming needed

    with open(output_file, "w") as file:  # Open the output file in write mode
        for trimmed_url in trimmed_urls:  # Iterate through the trimmed URLs
            file.write(trimmed_url + "\n")  # Write the trimmed URL to the output file
            print(trimmed_url)  # Print the trimmed URL

    return trimmed_urls  # Return the list of trimmed URLs


def trim_to_root(input_file, output_file):
    # Function to trim URLs to the root domain
    trimmed_domains = set()  # Create an empty set to store trimmed domains

    with open(input_file, "r") as file:  # Open the input file for reading
        for url in file:  # Iterate through each URL in the file
            domain = tldextract.extract(
                url.strip()
            ).registered_domain  # Extract the root domain
            trimmed_domains.add(domain)  # Add the trimmed domain to the set

    with open(output_file, "w") as file:  # Open the output file for writing
        for domain in trimmed_domains:  # Iterate through trimmed domains
            file.write(domain + "\n")  # Write each trimmed domain to the file

    return len(trimmed_domains)  # Return the count of unique trimmed domains

def save_domains(domains, filename="domains.txt"):
    # Function to save extracted domains to a file
    with open(filename, "w") as file:  # Open the file for writing
        for domain in domains:  # Iterate through extracted domains
            file.write(domain + "\n")  # Write each domain to the file

def process_urls_in_file(file_name):  # Function to process URLs in a file
    try:  # Start of error handling block
        with open(file_name, "r") as file:  # Open file in read mode
            urls = file.readlines()  # Read all lines in the file and store them in a list

        processed_urls = []  # Initialize an empty list to store processed URLs
        for url in urls:  # Iterate through each URL in the list
            url = url.strip()  # Remove leading and trailing whitespaces
            if not url.startswith("http://") and not url.startswith("https://"):  # Check if URL does not start with http:// or https://
                url = "http://" + url  # Prepend http:// to the URL
            processed_urls.append(url)  # Add the processed URL to the list

        with open(file_name, "w") as file:  # Reopen the file in write mode
            for processed_url in processed_urls:  # Iterate through each processed URL
                file.write(processed_url + "\n")  # Write the processed URL to the file followed by a newline character
                print(processed_url)  # Print the processed URL

    except FileNotFoundError:  # Handle file not found error
        print("File not found. Please make sure the file exists.")  # Print error message

def main_menu():
    # Main menu function for user interaction
    print(
        """\033[1;96m╭━╮╱╭╮╱╱╭╮
┃┃╰╮┃┃╱╭╯╰╮
┃╭╮╰╯┣━┻╮╭╋━━╮╱╭╮╱╭╮
┃┃╰╮┃┃╭╮┃┃┃┃━┫╭╯╰┳╯╰╮
┃┃╱┃┃┃╰╯┃╰┫┃━┫╰╮╭┻╮╭╯
╰╯╱╰━┻━━┻━┻━━╯╱╰╯╱╰╯
 """
    )
    print(
        Fore.WHITE
        + "\033[1;93m[\033[1;92m01\033[1;93m]\033[1;90m --➤ \033[1;97m Remove Duplicate Lines"
    )  # Print menu option
    print(
        Fore.WHITE
        + "\033[1;93m[\033[1;92m02\033[1;93m]\033[1;90m --➤ \033[1;97m Randomize Line Order"
    )  # Print menu option
    print(
        Fore.WHITE
        + "\033[1;93m[\033[1;92m03\033[1;93m]\033[1;90m --➤ \033[1;97m Sort Lines Lexicographically ascending"
    )  # Print menu option
    print(
        Fore.WHITE
        + "\033[1;93m[\033[1;92m04\033[1;93m]\033[1;90m --➤ \033[1;97m Sort Lines Lexicographically descending"
    )  # Print menu option
    print(
        Fore.WHITE
        + "\033[1;93m[\033[1;92m05\033[1;93m]\033[1;90m --➤ \033[1;97m Merge .txt files"
    )  # Print menu option
    print(
        Fore.WHITE
        + "\033[1;93m[\033[1;92m06\033[1;93m]\033[1;90m --➤ \033[1;97m Merge .html Files"
    )  # Print menu option
    print(
        Fore.WHITE
        + "\033[1;93m[\033[1;92m07\033[1;93m]\033[1;90m --➤ \033[1;97m Filter URLs from text files"
    )  # Print menu option
    print(
        Fore.WHITE
        + "\033[1;93m[\033[1;92m08\033[1;93m]\033[1;90m --➤ \033[1;97m Trim URLs to root"
    )  # Print menu option
    print(
        Fore.WHITE
        + "\033[1;93m[\033[1;92m09\033[1;93m]\033[1;90m --➤ \033[1;97m 200 OK Status code Checker"
    )  # Print menu option
    print(
        Fore.WHITE
        + "\033[1;93m[\033[1;92m10\033[1;93m]\033[1;90m --➤ \033[1;97m Add http/https to URLs"
    )  # Print menu option
    print(
        Fore.WHITE
        + "\033[1;93m[\033[1;92m11\033[1;93m]\033[1;90m --➤ \033[1;97m Delete http/https from URLs"
    )  # Print menu option
    print(
        Fore.WHITE
        + "\033[1;93m[\033[1;92m12\033[1;93m]\033[1;90m --➤ \033[1;97m Delete duplicate domains"
    )  # Print menu option
    print(
        Fore.WHITE
        + "\033[1;93m[\033[1;92m13\033[1;93m]\033[1;90m --➤ \033[1;97m Wordpress Checker"
    )  # Print menu option
    print(
        Fore.WHITE
        + "\033[1;93m[\033[1;92m14\033[1;93m]\033[1;90m --➤ \033[1;97m Trim by Keyword"
    )  # Print menu option
    print(
        Fore.WHITE + "\033[1;93m[\033[1;92m00\033[1;93m]\033[1;90m --➤ \033[1;91m Exit"
    )  # Print menu option
    choice = input(
        Fore.WHITE
        + "\n\033[1;96mroot@notepad>_ \033[1;93mEnter your choice (1/2/3/etc...): \033[1;97m"
    )  # Get user choice

    if choice == "1" or choice == "01":
        input_file = input(
            "\n\033[1;93mPlease put your input file .txt:\033[1;92m "
        )  # Get input file from user
        output_file = input(
            "\033[1;93mPlease specify output file .txt:\033[1;92m "
        )  # Get output file from user
        deleted_count, left_count = remove_duplicates(
            input_file, output_file
        )  # Call remove_duplicates function
        print(
            f"\n\033[1;92m{deleted_count} lines were deleted, {left_count} lines left."
        )  # Print deletion stats
        time.sleep(2)  # Pause for 2 seconds
        redirect_or_close()  # Call redirection function
    elif choice == "2" or choice == "02":
        input_file = input(
            "\n\033[1;93mEnter the input file name (.txt):\033[1;92m "
        )  # Get input file for randomization
        if not input_file.endswith(".txt"):  # Check if file is in the correct format
            print(
                "\n\033[1;91mInvalid file format. Please enter a .txt file."
            )  # Print error message
        else:
            randomize_lines(input_file)  # Call randomize_lines function
            print(
                "\n\033[1;92mLines have been randomized successfully and saved as randomize.txt."
            )  # Print success message
            time.sleep(2)  # Pause for 2 seconds
            redirect_or_close()  # Call redirection function
    elif choice == "3" or choice == "03":
        list_lines_lexicographically()  # Call lexicographical sorting function
        time.sleep(2)  # Pause for 2 seconds
        redirect_or_close()  # Call redirection function
    elif choice == "4" or choice == "04":
        list_lines_lexicographically_descending()  # Call descending sorting function
        time.sleep(2)  # Pause for 2 seconds
        redirect_or_close()  # Call redirection function
    elif choice == "5" or choice == "05":
        folder_path = input(
            "\033[1;93mEnter the folder path containing .txt files:\033[1;92m "
        )  # Get folder path for merging
        output_file_path = input(
            "\033[1;93mEnter the output file path (e.g., merged.txt):\033[1;92m "
        )  # Get output file path
        merge_txt_files(
            folder_path, output_file_path
        )  # Call .txt file merging function
        time.sleep(2)  # Pause for 2 seconds
        redirect_or_close()  # Call redirection function
    elif choice == "6" or choice == "06":
        folder_path = input(
            "\033[1;93mEnter the folder path containing .html files:\033[1;92m "
        )  # Get folder path for merging
        output_file_path = input(
            "\033[1;93mEnter the output file path (e.g., merged.html):\033[1;92m "
        )  # Get output file path
        merge_html_files(
            folder_path, output_file_path
        )  # Call .html file merging function
        time.sleep(2)  # Pause for 2 seconds
        redirect_or_close()  # Call redirection function
    elif choice == "7" or choice == "07":
        filter_urls_from_text_files()  # Call URL filtering function
        time.sleep(2)  # Pause for 2 seconds
        redirect_or_close()  # Call redirection function
    # Check if the user input is "8" or "08"
    elif choice == "8" or choice == "08":
        # Request user input for the file containing URLs
        input_file = input(
            "\n\033[1;93mPlease input the file containing URLs:\033[1;92m "
        )
        # Request user input for the output file for trimmed domains
        output_file = input(
            "\033[1;93mSpecify the output file for trimmed domains:\033[1;92m "
        )
        # Call the trim_to_root function with input and output files
        trimmed_count = trim_to_root(
            input_file, output_file
        )  # Call trim_to_root function
        # Print the number of unique domains extracted and saved
        print(f"\n\033[1;92m{trimmed_count} unique domains were extracted and saved.")
        # Pause for 2 seconds
        time.sleep(2)
        # Call the redirection or close function
        redirect_or_close()
        # Check if the user input is "9" or "09"
    elif choice == "9" or choice == "09":  # Check if user chose option 9
	    file_checker()  # Call function to check for necessary files
	    file = ""  # Initialize variable to store selected file
	    path = os.getcwd()  # Get current working directory
	    useragent = "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"  # Define user agent
	
	    # Listing All Files (For Check)
	    print(f"{YELLOW}[*] {BLUE}Listing files in the current directory.")  # Print message in yellow and blue
	    print(f"{CYAN}")  # Print message in cyan color
	    files = [f for f in os.listdir() if os.path.isfile(f)]  # List all files in current directory
	    for f in files:  # Iterate through files
	        print(f"{f}")  # Print each file name
	    print()  # Print empty line
	    file = (  # Prompt user to select a file
	        input(f"{YELLOW}[*] {BLUE}Select a file (default: urls.txt): {CYAN}")  # Input message
	        or "urls.txt"  # Default to 'urls.txt' if no input
	    )
	    print()  # Print empty line
	
	    # Configure URL List
	    print(f"{GREEN}[*] {BLUE}Configuring file...")  # Print message in green and blue
	    print()  # Print empty line
	    with open(file, "r") as f:  # Open selected file for reading
	        urls = f.readlines()  # Read lines from file
	    urls = list(set(urls))  # Remove duplicates from URL list
	    with open("urls.txt", "w") as f:  # Open 'urls.txt' for writing
	        for url in urls:  # Iterate through URLs
	            f.write(url)  # Write URL to file
	    print(f"{GREEN}[i] {BLUE}Done.")  # Print completion message
	    print()  # Print empty line
	    input(f"{YELLOW}[>] {BLUE}Press [ENTER] to continue")  # Prompt user to press Enter
	
	    print(f"{GREEN}[i] {BLUE}Loading Configuration")  # Print loading message
	    print(f"{GREEN}[*] {BLUE}File selected: {YELLOW}{file}\n")  # Print selected file
	    print(f"{GREEN}[*] {BLUE}Useragent selected: {YELLOW}{useragent}\n")  # Print selected user agent
	    print(f"{GREEN}[*] {BLUE}Path: {YELLOW}{path}\n")  # Print current path
	
	    # Start Tester
	    input(f"{GREEN}[i] {BLUE}Press {RED}[ENTER] {BLUE}To Start")  # Prompt user to press Enter
	    print()  # Print empty line
	    print()  # Print empty line
	
	    for url in urls:  # Iterate through URLs
	        url = url.strip()  # Remove whitespace from URL
	        try:  # Start try block
	            response = requests.head(  # Send HEAD request to URL
	                url, timeout=10, headers={"User-Agent": useragent}  # Specify timeout and user agent
	            )
	            code = response.status_code  # Get HTTP status code
	            if code in [301, 302]:  # Check for redirect status codes
	                print(  # Print redirection message
	                    f"{GREEN}[>>] {BLUE}Website {GREEN}Live {BLUE}but redirects: {CYAN}{url}"
	                )
	                with open("redirects.txt", "a") as f:  # Append URL to redirects file
	                    f.write(url + "\n")
	            elif code == 200:  # Check for successful status code
	                print(f"{GREEN}[+] {BLUE}Website {GREEN}Live {BLUE}: {CYAN}{url}")  # Print live website message
	                with open("live.txt", "a") as f:  # Append URL to live file
	                    f.write(url + "\n")
	            elif code == 403:  # Check for forbidden status code
	                if "ddos-guard" in response.text.lower():  # Check for DDoS protection
	                    print(  # Print DDoS protection message
	                        f"{MAGENTA}[-] {BLUE}Live But Detected {MAGENTA}DDoS Guard{BLUE}: {CYAN}{url}"
	                    )
	                    with open("ddos_guard.txt", "a") as f:  # Append URL to DDoS guard file
	                        f.write(url + "\n")
	                else:  # Handle other forbidden cases
	                    print(  # Print forbidden message
	                        f"{YELLOW}[-] {BLUE}Website {YELLOW}Live But Bad Connection{BLUE}: {CYAN}{url}"
	                    )
	                    with open("bad_con.txt", "a") as f:  # Append URL to bad connection file
	                        f.write(url + "\n")
	            elif code == 503:  # Check for service unavailable status code
	                print(  # Print service unavailable message
	                    f"{YELLOW}[-] {BLUE}Website {YELLOW}Live But Bad Connection{BLUE}: {CYAN}{url}"
	                )
	                with open("bad_con.txt", "a") as f:  # Append URL to bad connection file
	                    f.write(url + "\n")
	            else:  # Handle all other cases
	                print(f"{RED}[!] {BLUE}Website {RED}Dead {BLUE}: {CYAN}{url}")  # Print dead website message
	                with open("dead.txt", "a") as f:  # Append URL to dead file
	                    f.write(url + "\n")
	        except Exception as e:  # Catch any exceptions
	            print(f"{RED}[!] {BLUE}Website {RED}Dead {BLUE}: {CYAN}{url}")  # Print dead website message
	            with open("dead.txt", "a") as f:  # Append URL to dead file
	                f.write(url + "\n")
	    print()  # Print empty line
	    input(f"{GREEN}[i] {BLUE}Clear your url file? [Y/N]: {YELLOW}")  # Prompt user to clear URL file
	    print()  # Print empty line
	    # Pause for 2 seconds
	    time.sleep(2)  # Pause for 2 seconds
	    # Call the redirection or close function
	    redirect_or_close()  # Call redirection function
    elif choice == "10":
        file_name = input("Enter the name of the file containing URLs: ")
        process_urls_in_file(file_name)
    elif choice == "11":
        # Request user input for the URLs file
        input_file = input("\n\033[1;93mPlease input your URLs file: \033[1;92m")
        # Request user input for the output file
        output_file = input("\033[1;93mPlease specify the output file: \033[1;92m")
        # Call the trim_http_https function with input and output files
        trimmed_urls = trim_http_https(input_file, output_file)
        # Pause for 2 seconds
        time.sleep(2)
        # Call the redirection or close function
        redirect_or_close()
        # Check if the user input is "12"
    elif choice == "12":
        # Request user input for the input file (.txt)
        input_file = input("\n\033[1;93mPlease provide the input file (.txt): ")
        # Call the remove_duplicate_domains function with the input file
        deleted_count, left_count = remove_duplicate_domains(input_file)
        # Print the number of domains deleted and left
        print(
            f"\n\033[1;92m{deleted_count} domains were deleted, {left_count} domains left."
        )
        # Pause for 2 seconds
        time.sleep(2)
        # Call the redirection or close function
        redirect_or_close()
        # Check if the user input is "14"
    elif choice == "14":
        def delete_text_after_pattern(file_name, pattern):
           # Apri il file in modalità lettura
            with open(file_name, 'r') as file:
                content = file.readlines()

               # Inizializza una lista per salvare i nuovi contenuti
                new_content = []

                # Itera su ogni riga del contenuto
                for line in content:
               # Utilizza la regex per trovare il pattern nella riga
                    match = re.search(pattern, line)
        
            # Se trova il pattern, aggiungi solo la parte precedente al pattern alla nuova lista
                if match:
                    new_content.append(line[:match.start()] + '\n')
                else:
                    # Se il pattern non viene trovato, aggiungi la riga intera alla nuova lista
                    new_content.append(line)

            # Mostra i risultati con un URL per riga
            for line in new_content:
                print(line)

            # Sovrascrivi il file con il nuovo contenuto
            with open(file_name, 'w') as file:
                file.writelines(new_content)

        # Richiedi il nome del file di testo
        file_name = input("List: ")

        # Richiedi il pattern da cercare
        pattern = input("Keywords to trim: ")

        # Chiama la funzione per cancellare il testo dopo il pattern
        delete_text_after_pattern(file_name, pattern)
    elif choice == "13":
        input_file = input("\n\033[1;93mPlease input your file name containing URLs: ")
        check_wordpress_cms(input_file)
        time.sleep(2)
        redirect_or_close()
    elif choice == "0" or choice == "00":
        # Print a thank you message
        print("\nThanks for using this tool")
        # Pause for 1.5 seconds
        time.sleep(1.5)
        # Exit the program
        sys.exit()
        # Clear the terminal screen
        os.system("clear")
        # Call the check_cms function
        check_cms(input_file)  # Call check_cms function
        # Print the message for WordPress URLs saved
        print("\033[1;92mWordPress URLs saved in wp.txt.")
        # Pause for 2 seconds
        time.sleep(2)  # Pause for 2 seconds
        # Call the redirection or close function
        redirect_or_close()  # Call redirection function

    else:
        print(
            "\033[1;91m\nInvalid choice. Please enter a valid option."
        )  # Print error message
        time.sleep(2)  # Pause for 2 seconds
        redirect_or_close()  # Call redirection function


def redirect_or_close():
    # Function to determine whether to redirect to the main menu or close the program
    choice = input(
        "\033[1;97m\nDo you want to redirect to the main menu? (Y/N):\033[1;93m "
    ).upper()  # Get user choice

    if choice == "Y":  # Check if user wants to redirect
        main_menu()  # Redirect to the main menu
    elif choice == "N":  # Check if user wants to close
        print("\033[1;93mClosing...")  # Print closing message
        time.sleep(5)  # Pause for 5 seconds
    else:
        print("\033[1;91mInvalid choice.")  # Print error message
        redirect_or_close()  # Call redirection function


if __name__ == "__main__":
    main_menu()  # Call the main menu function
