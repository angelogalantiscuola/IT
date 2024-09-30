import os
import re


def extract_headers(file_path):
    headers = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            match = re.match(r"^(#{1,6})\s+(.*)", line)
            if match:
                level = len(match.group(1))
                title = match.group(2)
                anchor = re.sub(r"[^a-zA-Z0-9]+", "-", title.lower()).strip("-")
                headers.append((level, title, anchor))
    return headers


def generate_toc(folder, files):
    toc_lines = [f"# {folder[:-1]}\n"]
    for file in files:
        file_path = os.path.join(folder, file)
        headers = extract_headers(file_path)
        for level, title, anchor in headers:
            # remove parts after  <!-- omit in toc -->
            if "<!-- omit in toc -->" in title:
                title = title.split("<!-- omit in toc -->")[0]
            # add # for each level
            title = "#" * (level) + " " + title
            toc_lines.append(title + "\n")
    return toc_lines


def write_toc(toc_lines, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(toc_lines)


# function to get all the md files in the folder except the table of contents file
def get_md_files(folder, toc_file):
    files = []
    for file in os.listdir(folder):
        if file.endswith(".md") and file != toc_file and not file.startswith("0_") and not file.startswith("00_"):
            files.append(file)
    return files


# folder = "oop/"
folder = "oop/"
toc_file = "table_of_contents.md"
markdown_files = get_md_files(folder, toc_file)

# Generate TOC
toc = generate_toc(folder, markdown_files)

# Write TOC to a file
write_toc(toc, os.path.join(folder, toc_file))
