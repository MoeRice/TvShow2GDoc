import gspread
from oauth2client.service_account import ServiceAccountCredentials
class Document:


    #OAuth2 Authorization
    def get_user(self):
        scope = ['https://spreadsheets.google.com/feeds']

        credentials = ServiceAccountCredentials.from_json_keyfile_name('PUT-JSON-FILE-HERE.json', scope)

        gc = gspread.authorize(credentials)

        return gc

    #open Spreadsheet, then worksheet
    def Setup(self,token):

        sh = token.open_by_url('SPREADSHEET-URL-GOES-HERE')

        worksheet = sh.get_worksheet(0)

        return worksheet








