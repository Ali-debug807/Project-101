import dropbox

class TransferData:
    def upload_file():
        dbx=dropbox.Dropbox(self.accessToken)
        f=open(filefrom,"rb")
        dbx.files_upload(f.read(),fileto)
def main():
    accessToken='sl.BBAXrEsSTwqhWR2z67YIOaQcdsu3KZL3hzEnlEEhnFVI1ZelXo0uiU8u9ZEdfqZvoFM0NpEk2LUskiKLY4WnxF48ep2DCafTdCt6-JvqhflN6M7Zl3ok0hPTt7EykHE_eITpTq8'
    transferData=TransferData(accessToken)
    fileName=input('Enter the file name to upload')
TransferData.upload_file()