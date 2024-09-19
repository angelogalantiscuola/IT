import os

EXCLUDE_FOLDERS = {"_media", "_temp", "exercises"}
INCLUDE_EXTENSIONS = {".md"}


def generate_markmap_md(root_dir, output_file):
    def traverse_dir(current_dir, depth=2):
        items = sorted(os.listdir(current_dir))
        md_content = ""
        for item in items:
            item_path = os.path.join(current_dir, item)
            if os.path.isdir(item_path):
                if item.startswith(".") or item in EXCLUDE_FOLDERS:
                    continue
                md_content += f"{'#' * depth} {item}\n"
                md_content += traverse_dir(item_path, depth + 1)
            else:
                if item.startswith(".") or not any(item.endswith(ext) for ext in INCLUDE_EXTENSIONS):
                    continue
                md_content += f"{'#' * depth} {item}\n"
        return md_content

    repo_name = os.path.basename(root_dir)
    md_content = f"# {repo_name}\n"
    md_content += traverse_dir(root_dir)

    with open(output_file, "w") as f:
        f.write(md_content)


if __name__ == "__main__":
    root_directory = "."  # Change this to your repo's root directory if needed
    output_markdown_file = "repo_structure.md"
    generate_markmap_md(root_directory, output_markdown_file)
    print(f"Markdown file generated: {output_markdown_file}")
