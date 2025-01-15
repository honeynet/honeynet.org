import os
import shutil

content_dir = 'content/blog'  # Path to the blog posts folder
default_banner_src = 'static/images/banner.png'  # Path to the default banner image
banner_filename = 'banner.png'  # Banner image file name
images_folder_name = 'images'  # Folder name for images in each blog post

for subdir, _, files in os.walk(content_dir):
    for file in files:
        if file.endswith('index.md'):
            blog_dir = os.path.dirname(os.path.join(subdir, file))
            images_dir = os.path.join(blog_dir, images_folder_name)
            banner_dest = os.path.join(images_dir, banner_filename)
            
            # Create the images folder if it doesn't exist
            os.makedirs(images_dir, exist_ok=True)

            # Copy the default banner image if it doesn't already exist
            if not os.path.exists(banner_dest):
                shutil.copy(default_banner_src, banner_dest)

            # Update the index.md file to reference the new banner location
            figure_line = f'{{{{<figure src="images/{banner_filename}" alt="Banner" width="50%">}}}}\n'

            index_file_path = os.path.join(blog_dir, file)
            with open(index_file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # Check if a figure line already exists
            if not any('{{<figure ' in line for line in lines):
                # Find the end of the front matter
                try:
                    end_index = lines[1:].index('---\n') + 1
                except ValueError:
                    continue

                # Add the figure line after the front matter
                lines.insert(end_index + 1, figure_line)
                print("Updated blog structure with images folder and banner references.")

                # Write the updated content back to the file
                with open(index_file_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)