# coding=utf-8

# microservices with Python

# pip install web.py

# Python webservices.py

import web
import json

urls = (
    '/paises(/.*)?', 'paises',
)

application = web.application(urls, globals()).wsgifunc()

class paises:
    paises = { 34: { 'España', "ES"}, 33: {"Francia", "FR"} }
    codes = { 400 : '400 Bad Request',
              404 : '404 Not Found',
              405 : '405 Method Not Allowed',
              409 : '409 Conflict'
              }
    def __init__(self):
        web.header('Content-Type', 'application/json', unique=True)

    def GET(self, pais=None):
        print("pais",pais)
        try:
            
            columns = [ 'code', 'nombre', 'iso' ]
            if pais is None:
                output = []
  
                for i,v in self.paises.items():
                            output.append(dict(zip(columns, [i] + list(v))))
            else:
                pais = int(pais[1:])
                if self.paises[pais] is None:
                    raise Exception('Pais no encontrado', 404)
                else:
                    output = []
                    output.append(dict(zip(columns, [pais] + list(self.paises[pais]))))

            print("GET output:",output)

            return json.dumps(output, ensure_ascii=False)

        except Exception as e:
            msg, code = e.args if len(e.args)==2 else (e.args, 404)
            raise web.HTTPError(self.codes[code], data="Error: " + str(msg) + "\n")

    def POST(self, pais=None):
        print("pais",pais)
        try:
            if pais is not None:
                raise Exception('No permitido', 404)
           
            input = web.input(code=None, nombre=None, iso=None)
            
            print("code, nombre,iso:", input['code'], input['nombre'],input['iso'])
            
            if not input['code'] or not input['nombre'] or not input['iso']:
                raise Exception("Faltan datos de entrada", 400)

            pais = int(input['code'])
            if pais in self.paises:
                raise Exception("Elemento existente", 409)
           
            self.paises[pais] = { input['nombre'], input['iso'] }
            
            #
            print("self.paises:", self.paises)
            
            web.created()
            web.header('Location', '/paises/'+str(pais))
            return ''
        except Exception as e:
            msg, code = e.args if len(e.args)==2 else (e.args, 404)
            raise web.HTTPError(self.codes[code], data="Error: " + str(msg) + "\n")

            

    def PUT(self, pais=None):
        print("pais",pais)
        try:

            input = web.input(code=None, nombre=None, iso=None)
            if not input['code'] or not input['nombre'] or not input['iso']:
                raise Exception("Faltan datos de entrada", 400)
             
            # 
            pais = input['code']
            
            if pais is None or len(pais)==1:
                    raise Exception('Pais no indicado', 405)
             

            pais = int(input['code'])
            
            #
            print("pais :", pais)
            
  
           
            self.paises[pais] = { input['nombre'], input['iso'] }
            
            print("self.paises :", self.paises)
                        
            return ''


        except Exception as e:
            msg, code = e.args if len(e.args)==2 else (e.args, 404)
            raise web.HTTPError(self.codes[code], data="Error: " + str(msg) + "\n")            

            
    def DELETE(self, pais=None):
        print("pais",pais)
        try:
        
            input = web.input(code=None)
            if not input['code']:
                raise Exception("Faltan datos de entrada", 400)
             
            pais = input['code']
        
        
            if pais is None or len(pais)==1:
                    raise Exception('Pais no indicado', 405)
             
            pais = int(input['code'])
            
            #
            print("pais :", pais)
            
            if pais not in self.paises:
                raise Exception("Elemento no encontrado", 404)
           
            del self.paises[pais]
            
            #
            print("self.paises :", self.paises)
            
            return ''

        except Exception as e:
            msg, code = e.args if len(e.args)==2 else (e.args, 404)
            raise web.HTTPError(self.codes[code], data="Error: " + str(msg) + "\n")            

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
