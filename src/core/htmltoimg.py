import imgkit,os


def html_to_img(input_dir, img_format='jpg'):

    html_files = [file for file in os.listdir(input_dir) if file.endswith('.html')]

    for html_file in html_files:

        input_file_path = os.path.join(input_dir, html_file)
        print("Input HTML File : " + input_file_path)

        output_file_dir = os.path.join(input_dir, 'images')
        output_file_path = os.path.join(output_file_dir, os.path.splitext(html_file)[0]+ '.' + img_format)
        print("Output JPG File : " + output_file_path)

        """ options = {
            'disable-smart-width': False
        }"""

        imgkit.from_file(input_file_path, output_file_path)