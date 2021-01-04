import os


def get_img_url(line):
    return line.split('\'')[1]


def get_url_orig_size(url):
    parts = url.split('/')
    img = parts[-1]
    num = int(img.split('.')[0])
    suffix = img.split('.')[1]
    num -= 1
    parts[-1] = '.'.join([str(num), suffix])
    return '/'.join(parts)


def main():
    html_fn = os.path.join(os.path.dirname(__file__), 'data/dita.html')
    with open(html_fn, 'r') as fd:
        lines = fd.readlines()
        lines = filter(lambda s: 'jpg' in s and 'url' in s, lines)

    img_urls = [get_url_orig_size(get_img_url(line)) for line in lines]
    img_list_fn = os.path.join(os.path.dirname(__file__), 'data/image_list.txt')
    img_download_sh_fn = os.path.join(os.path.dirname(__file__), 'data/image_command.sh')

    with open(img_list_fn, 'w') as fd:
        fd.write('\n'.join(img_urls))

    with open(img_download_sh_fn, 'w') as fd:
        for url in img_urls:
            fd.write('wget {}\n'.format(url))


if __name__ == '__main__':
    main()
