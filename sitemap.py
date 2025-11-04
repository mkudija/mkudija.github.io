import os
from datetime import datetime

# --- CONFIGURATION ---

# 1. Set the root URL of your website
BASE_URL = "https://matthewkudija.com"

# 2. Set the name of this script and the output sitemap
# (Script is assumed to be in the root directory)
THIS_SCRIPT_NAME = "sitemap.py"
SITEMAP_PATH = "sitemap.xml" # Output path in the root
ROOT_DIR = "."

# 3. Directories to scan for .html files
DIRECTORIES_TO_SCAN = [".", "notes", "reading-notes"]

# 4. Files in the root directory to ignore
FILES_TO_IGNORE = [
    "AAPL.html",
    "resume.html",
    "color_test.html",
    "sitemap.xml",      # Ignore the sitemap itself
    THIS_SCRIPT_NAME    # Ignore this script
]

# 5. Page priorities
PAGE_PRIORITIES = {
    "index.html": "1.0",
    "about.html": "0.9",
    "reading-notes/index.html": "0.9",
    "notes/index.html": "0.9"
}
DEFAULT_PRIORITIES = {
    ".": "0.5",
    "notes": "0.7",
    "reading-notes": "0.7"
}


# --- SITEMAP GENERATION ---

def get_html_files(directory, ignore_list):
    """Finds all .html files in a given directory, respecting the ignore list."""
    html_files = []
    for filename in os.listdir(directory):
        # For root directory, check against ignore list
        if directory == ROOT_DIR and filename in ignore_list:
            continue
        if filename.endswith(".html"):
            html_files.append(filename)
    return html_files

def generate_sitemap_entry(url_path, last_mod_date, priority):
    """Creates a single <url> entry for the sitemap."""
    
    # Special case for index.html -> use the base URL
    if url_path == "index.html":
        url = f"{BASE_URL}/"
    else:
        # Ensure URLs use forward slashes, even on Windows
        url = f"{BASE_URL}/{url_path.replace(os.path.sep, '/')}"
        
    return f"""
    <url>
        <loc>{url}</loc>
        <lastmod>{last_mod_date}</lastmod>
        <priority>{priority}</priority>
    </url>"""

if __name__ == "__main__":
    print("Starting sitemap generation...")
    
    # Get current date for <lastmod>
    today_iso = datetime.now().strftime('%Y-%m-%d')
    
    sitemap_entries = []

    for directory in DIRECTORIES_TO_SCAN:
        print(f"Scanning directory: '{directory}'")
        if not os.path.isdir(directory):
            print(f"  -> Warning: Directory '{directory}' not found. Skipping.")
            continue

        # Pass the ignore list only for the root directory scan
        ignore_list = FILES_TO_IGNORE if directory == ROOT_DIR else []
        html_files = get_html_files(directory, ignore_list)
        
        count = 0
        for filename in html_files:
            if directory == ROOT_DIR:
                relative_path = filename
            else:
                # Create the correct relative path (e.g., "notes/file.html")
                relative_path = os.path.join(directory, filename).replace(os.path.sep, '/')
            
            # Determine priority
            if relative_path in PAGE_PRIORITIES:
                priority = PAGE_PRIORITIES[relative_path]
            else:
                priority = DEFAULT_PRIORITIES.get(directory, "0.5")
            
            sitemap_entries.append(generate_sitemap_entry(relative_path, today_iso, priority))
            count += 1
        print(f"  -> Found {count} HTML files in '{directory}'.")

    # 4. Assemble the full sitemap.xml content
    sitemap_header = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">"""
    
    sitemap_footer = """
</urlset>
"""
    
    full_sitemap = sitemap_header + "".join(sitemap_entries) + sitemap_footer
    
    # 5. Write the sitemap.xml file to the root directory
    try:
        with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
            f.write(full_sitemap)
        print(f"\n✅ Sitemap successfully generated!")
        print(f"   Total URLs: {len(sitemap_entries)}")
        print(f"   Saved to: {os.path.abspath(SITEMAP_PATH)}\n\n")
    except Exception as e:
        print(f"\n❌ Error writing sitemap file: {e}\n\n")
