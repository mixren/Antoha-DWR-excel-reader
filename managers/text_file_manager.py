import os
import datetime

M_DIR = "generated"
M_FILE= "generated.txt"
PATH_TXT=os.path.join(M_DIR, M_FILE)

def update_with(*args):
    if not os.path.exists(M_DIR):
        os.makedirs(M_DIR)
    try:
        with open(PATH_TXT, "a+") as f:
            f.write(f"{datetime.datetime.now()}")
            f.write('\n\n')
            for s in args:
                f.write(s)
                f.write('\n\n')
            f.write("\n")
    except Exception as e:
        return print(f"Can't save info to txt file. {e}")

def open_generated_list_txt():
    try:
        os.startfile(os.path.abspath(PATH_TXT))
    except Exception as e:
        print(f"Can't open a file. {e}")