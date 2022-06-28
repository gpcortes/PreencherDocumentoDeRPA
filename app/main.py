from worker import worker
from preencher_formulario import preencherRpa
from os.path import expanduser
import time

home = expanduser("~")

worker = worker()

template = open(home + '/templates/template_rpa.docx', 'rb')

if __name__ == '__main__':
    print('Worker started')
    while True:

        tasks = worker.fetch_tasks()

        for task in tasks:
            print('Task: {}'.format(task.id_))

            rpaID = task.variables['rpaID'].value

            variables = {}

            for taskVariables in task.variables:
                variables[taskVariables] = task.variables[taskVariables].value

            rapDocName, emailPrestador = preencherRpa(rpaID, template, variables)

            taskVariables = {
                'rapDocName': {
                    'name': 'rapDocName',
                    'value': rapDocName
                },
                'emailPrestador' : {
                    'name': 'emailPrestador',
                    'value': emailPrestador
                }
            }

            worker.complete_task(task.id_, taskVariables)

            time.sleep(30)
