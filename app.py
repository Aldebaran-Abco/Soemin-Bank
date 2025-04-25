from flask import Flask, render_template, request, redirect
import dropbox
import os

app = Flask(__name__)

# Configuración de Dropbox
DROPBOX_TOKEN = "sl.u.AFoGUp2Go2qaCwGnIj4eb9pyMUbZt4Bm6UXGVaWQKrNapCNJGeNSp7D8poVPs1TEdWszk1lpUr8FBpQev1AUrZ3UDCByeOxLg0PyXXzDakbp8LfBqr2276_dHVdYaeBdimbLJ9FbSDpMhEVqkU92Fj_86tE2QVQtYMc9a2N0c1MQl5Yyu4AIgG0dySdrQBItYGSkA0nLoNKeMjUvnyE-OYKcugeTXxOnKljr5zl0c5Ovlq0mkBiPjo4pjSsNtG64SxmqhWF-RStJVBCos-zzmsfPYKBXTYW0P1fn0X_JnihfgiOVTkw4BzSTNncYql1bBx4RTBk1il8lqurDXBh35hCrS3ku-Q8TXQNzCHFPdjFmppur9Cj-phDW2hYNGwCeC_wIYfd6zlUur2IGUKtPFpAvsG3POE8SjdLHBdHQ6tHoG9ZQr8j3cUafVRfVOAkFcOlCeMx9ak5Fk8J1IhUE86jsRc4qtXLpd8N9mwGoYAhqHa1jzQx2q4z-J8NnSJrypjlPB6c3xRa4CE4aQtFVhSqXjIE0QckHKf37DKWxKHExmW4A0Jd9FGOfX3-6_Cafa4pydKAjzad_AmnCO8fQocQSzQFQ7v5DaKfdrkzq98_mL8JzZ9mRSNxg_apSjYc_q5_y7eaCBua61y5usYIZGIrvPPIyXPaCQfxgQ_O9UZRBpSXIFePDO6C_6XVXUduWHkvQDv4ZabieKwkMDqqNyoCpY-arJRLUcMBGuA-JxSMHGo-nxIFNQR5tV94CiGX4I1Fme4ezm4UsBt6awX5PF8GnCDKUnmo0XQT4mzw3xaX3nlRE3IthZ19pcMeVnKflTLbNrlyyFPVNY3SHbJFZ-zZlQnlm-IXtYk-8TnBpb9E7CxkJcAn-dCOrK2t1haPcWb_89PIbREKSOiQA3iSWeFBv5TwDwLQ3_9CzZ-FRgD0AE_y4z2kNTaW_6dBiPae53XbjdNX5MpfphtYmIDsOKzApKjxwf0gj0liRgjHmIBXsN30xcMTvoNfa0L2_w5SQp5LurArX5yWYvcLvLog9NmgvANnSWrJ2e0TZ7YwivE8TvK6lPg35DJTSpx43b1orrxGCxv0BqjgQuXVn9VsUgqdnwxf7tFXtm2rVm17N8ByO_7cy_nG1usO78OSyl68gspF2TN6H7KRbY_NNEUTtWRfI_L4yDvvqiZznWd3casGTGp_RpcfaWmQNk35795aSJfDcy5pKaQuzmhpPc1DrPOULc1GNzm7GAyTo4vB_Xv0UUCVR_bdVyvjKaWQQM9O7pw126IEhxNH8RoiKKqiubaqk6FMALZfi0C_nvF2hFMrzfeXn9JRg2SsX17tpPWwc95isK0f92IFAv3DBdnVBh5l4ayY3nW_bMA-mE_8kfR3O3clkss4du-pWpndhI0-c6YQ"
DROPBOX_REQUEST_LINK = "https://www.dropbox.com/request/2EwOlXw1Et7Pk7tzuzMf?oref=e"

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return "No se seleccionó ningún archivo."
    
    file = request.files['file']
    if file.filename == '':
        return "Nombre de archivo inválido."

    try:
        # Subir el archivo a Dropbox usando la API (opcional)
        # dbx = dropbox.Dropbox(DROPBOX_TOKEN)
        # dbx.files_upload(file.read(), f"/{file.filename}")
        
        # Redirigir al usuario al enlace de solicitud de Dropbox
        return redirect(DROPBOX_REQUEST_LINK)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)