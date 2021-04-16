from typing import List

import os

IGNORE_FILES = ['.DS_Store', '__pycache__']

def listdir_sieved(dpath: str) -> List[str]:
    dir_list = os.listdir(dpath)

    for ignoref in IGNORE_FILES:
        if ignoref in dir_list:
            dir_list.remove(ignoref)

    return sorted(dir_list)


def cropped_generator():
    final_dir = os.path.join(os.getcwd(), "final")
    cls_list = listdir_sieved(final_dir)
    print(cls_list)

    for cname in cls_list:
        cdir = os.path.join(final_dir, cname)
        print(cdir)

        cropped_dir = os.path.join(cdir, "cropped")
        print(os.path.exists(cropped_dir))

        yield listdir_sieved(cropped_dir)


def main():
    final_dir = os.path.join(os.getcwd(), "final")
    cls_list = listdir_sieved(final_dir)

    gen = cropped_generator()

    for cname in cls_list:
        pictures = next(gen)

        for pic in pictures:
            target_file = os.path.join(final_dir, cname, pic)
            print(target_file)

if __name__ == "__main__":
    main()