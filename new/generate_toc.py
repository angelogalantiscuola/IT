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


def generate_toc(files):
    toc_lines = ["# Table of Contents\n"]
    for file in files:
        headers = extract_headers(file)
        print(headers)
        for level, title, anchor in headers:
            print(title)
            # remove parts after  <!-- omit in toc -->
            if "<!-- omit in toc -->" in title:
                title = title.split("<!-- omit in toc -->")[0]
            # add # for each level
            title = "#" * (level - 1) + " " + title
            toc_lines.append(title + "\n")
    return toc_lines


def write_toc(toc_lines, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(toc_lines)


# List of Markdown files
markdown_files = ["1_1_1.md", "1_1_2.md", "1_1_3.md", "1_1_4.md"]

# Generate TOC
toc = generate_toc(markdown_files)

# Write TOC to a file
write_toc(toc, "table_of_contents.md")
