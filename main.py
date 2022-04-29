import os
import tkinter as tk
import managers.generator_manager as gm
import managers.text_file_manager as tfm
import tkinter.filedialog as fd

TITLE = "Antoha DWR Excel Reader"
path_dir_test = "Z:\\CWT Documents\\2021\\MP21-09 PP104 POX_ALLOY\\CWT.MP21-09-117\\DWR"

def select_folder():
    path = fd.askdirectory(title="Выбери Папку со Сварочными Excel доками")
    if path:
        ent_select.delete(0, tk.END)
        ent_select.insert(0, path)
        ent_select.xview_moveto(1)

def generate():
    path = ent_select.get()
    lst_excels = get_all_excel_files(path)
    gm.generate(lst_excels)
    tfm.open_generated_list_txt()
    print("End.")

def get_all_excel_files(path: str):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.xlsx')]


if __name__ == '__main__':
    root = tk.Tk()
    root.title(TITLE)

    # Select Frame
    frm_select = tk.Frame(master=root)
    frm_select.grid(row=0, column=0, pady=6, padx=50)

    # "Generate" buttoт
    btn_generate = tk.Button(master=root, width=30, height=2, text="Generate", command=generate)
    btn_generate.grid(row=1, column=0, pady=14)

    lbl_select = tk.Label(frm_select, text = "Папка со Сварочными Excel доками: ")
    ent_select = tk.Entry(frm_select, width = 50)
    btn_select = tk.Button(frm_select, text="Select", command=select_folder)

    lbl_select.grid(row=0, column=0, sticky="w", padx=10)
    ent_select.grid(row=0, column=1, sticky="w", padx=10)
    btn_select.grid(row=0, column=2, sticky="w", padx=10)

    root.mainloop()


    '''lst_excels = get_all_excel_files(path_dir_test)
    print(f"Found {len(lst_excels)} Excel files")
    gm.generate(lst_excels)
    print(f"End.")'''

