#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8

import sys
import time
from googlesearch import search

# Define colors for terminal output
class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"

# Display the banner
def display_banner():
    banner = """

    
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░       ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░       ░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓██████▓▒░   
░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░        
 ░▒▓██████▓▒░   ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░  ░▒▓█▓▒░   ░▒▓████████▓▒░ 
                                                                                                                 
                                                                                                                 
                                                            by RAHUL KUMAR
                                                            insta @cyber.ahul
							    mail rahulkahar00001@gmail.com

The script searches for all indexed pages on a specific website (the one provided by the user) on Google.
This can help users find:
- All publicly accessible pages of the specified website.
- Pages that might not be easily found through regular navigation of the site.
- Potential vulnerabilities or sensitive information indexed by Google 
							     """
    
    print(colors.CRED2 + banner + colors.ENDC)

# Logging function
def logger(data, filename):
    """Logs data to a file if filename is provided."""
    if filename:
        with open(filename + ".txt", "a", encoding='utf-8') as file:
            file.write(str(data) + "\n")

# Main function to execute Google dork search
def dorks():
    try:
        display_banner()
        
        # Ask if the user wants to save output
        save_output = input("\n[+] Do You Like To Save The Output In A File? (Y/N) [Default: N]: ").strip().upper() or "N"
        filename = ""
        if save_output == "Y":
            filename = input("[~] Provide a Name for the Output File (without extension): ").strip()
        
        # Prompt for URL and search term
        base_url = input("\n[+] Enter the URL you want to search from (e.g., example.com): ").strip()
        search_term = f"site:{base_url}"

        amount = input("[+] Enter The Number Of Websites To Display (Press Enter for all results): ").strip()
        
        # Use a default value if amount is empty
        if amount == "":
            amount = 100  # Default to 100 results, adjust as needed
        else:
            if not amount.isdigit():
                print("[-] Invalid number. Please enter a valid integer.")
                return

        amount = int(amount)
        results_list = []
        print(f"\nSearching Google for URLs related to '{search_term}'...\n")
        
        try:
            for url in search(search_term, num_results=amount):
                results_list.append(url)
                print(f"[+] {len(results_list)}: {url}")
                logger(url, filename)
                
                # Exit loop once the desired amount is reached
                if len(results_list) >= amount:
                    break
                
                time.sleep(2)  # 2-second delay to avoid being blocked

        except Exception as e:
            print(f"Error during Google search: {e}")
            return

        if not results_list:
            print("\n[!] No results found. Try a different query.")

    except KeyboardInterrupt:
        print("\n")
        print("\033[1;91m[!] User Interruption Detected..!\033[0m")
        sys.exit(1)

    print("\n[•] Done... Exiting...")

# =====# Main Execution #===== #
if __name__ == "__main__":
    dorks()
