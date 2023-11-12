from subprocess import Popen
import uvicorn

if __name__ == '__main__':
    uvicorn.run(
            'app-controlnet:app', port=10277, host='0.0.0.0',
            ssl_keyfile='/home/user/ssl.key',
            ssl_certfile='/home/user/ssl.crt'
            )
