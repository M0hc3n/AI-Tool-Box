from browser import document, ajax, alert, console
from browser.html import A,B
from browser.template import Template
  
def show(ev):
    alert('user clicked Alert')
    document['title'] <= "Hello there ! "
  

document['alert'].bind('click', show)
  
def output(ev):
    document['output'].textContent = ev.target.value   

document['input'].bind('input', output)

Template(document['greet']).render(name='Mohcen')
  

url = 'https://api.chucknorris.io/jokes/random'

def on_complete(req):
    import json
    data = json.loads(req.responseText)
    joke = data['value']
    document['joke'].text = joke


def get_joke(ev):
    req = ajax.ajax()
    req.open('GET',url, True)
    req.bind('complete',on_complete)
    document['joke'].text = 'Loading ...'
    req.send()

document['get-joke'].bind('click', get_joke)

        
