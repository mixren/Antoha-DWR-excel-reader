import managers.excel_manager as em
from returns.pipeline import is_successful
from models.excel_model import ExcelModel
from models.list_excel_model import ListExcelModel
from tabulate import tabulate
import managers.text_file_manager as tfm

def generate(lst_excels: list):
    all_models = ListExcelModel()
    for exl in lst_excels:
        res = em.read_from_active_sheet(exl, 'WPS', 'WPQR', 'Welder', 'Type /', 'Dia.', 'Lot')
        if is_successful(res):
            print(res.unwrap())
            models = [ExcelModel(wps, wpqr, welder, w_type, dia, lot) for wps, wpqr, welder, w_type, dia, lot in list(zip(*res.unwrap().values()))]
            all_models.extend(models)
        else:
            print(res.failure())
    print(f"\nTotal number of Models: {all_models.len()}")
    table1 = tabulate(all_models.get_unique_wps_wpqr(), headers=all_models.get_header_wps_wpqr())
    table2 = tabulate(all_models.get_unique_welder_type_dia_lot(), headers=all_models.get_header_welder_type_dia_lot())
    
    tfm.update_with(table1, table2)
    print(f"\n{table1}\n\n{table2}")