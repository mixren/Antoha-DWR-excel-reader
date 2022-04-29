
class ExcelModel:
    '''
        'WPS', 'WPQR', 'Welder', 'Type /', 'Dia.', 'Lot'

        'WPS': '302-141',
        'WPQR': '214/17',
        'Welder ID': '87'
        'Type /': 'OK Tigrod 2509'
        'Dia': '2,0'
        'Lot': 'PVV015601910'
    '''

    def __init__(self, wps:str, wpqr:str, welder:str, w_type:str, dia:str, lot:str) -> None:
        self.wps = wps
        self.wpqr = wpqr
        self.welder = welder
        self.w_type = w_type
        self.dia = self._remove_comma(dia)
        self.lot = lot

    def _remove_comma(self, dia:str):
        return dia.replace(',','.')
        
    def get_document(self):
        '''Example: CWT.MP21-09-12.00.00.ITP'''
        return f"{self.drawing}.ITP"

    def get_vendor_job(self):
        '''Example: CWT.MP21-09-12'''
        return self.drawing.split(".0", 1)[0]