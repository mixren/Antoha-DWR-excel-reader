from excel_model import ExcelModel


class ListExcelModel:

    def __init__(self, lst_excel_model: list[ExcelModel] = []) -> None:
        self.lst_excel_model = lst_excel_model
        
    def extend(self, lst_excel_model: list[ExcelModel]):
        self.lst_excel_model.extend(lst_excel_model)

    def len(self):
        return len(self.lst_excel_model)


    def get_unique_wps_wpqr(self)-> list[list]:
        '''List of lists'''
        lst_str = self.get_unique_wps_wpqr_2()
        return [s.split(', ') for s in lst_str]

    def get_unique_wps_wpqr_2(self)-> list[str]:
        '''List of strings'''
        return list(set([f"{m.wps}, {m.wpqr}" for m in self.lst_excel_model]))

    def get_header_wps_wpqr(self)-> list:
        return ['WPS', 'WPQR']
        
    def get_txt_header_wps_wpqr_2(self)-> str:
        return f"\n{'-'*16}Таблица - WPS, WPQR{'-'*16}\n"


    def get_unique_welder_type_dia_lot(self)-> list[list]:
        '''List of lists'''
        lst_str = self.get_unique_welder_type_dia_lot_2()
        return [s.split(', ') for s in lst_str]

    def get_unique_welder_type_dia_lot_2(self)-> list[str]:
        '''List of strings'''
        return list(set([f"{m.welder}, {m.w_type}, {m.dia}, {m.lot}" for m in self.lst_excel_model]))

    def get_header_welder_type_dia_lot(self)-> list:
        return ['Welder', 'Type', 'Diameter', 'Lot']

    def get_txt_header_welder_type_dia_lot_2(self)-> str:
        return f"\n{'-'*16}Таблица - Welder, Type, Diameter, Lot{'-'*16}\n"

    

