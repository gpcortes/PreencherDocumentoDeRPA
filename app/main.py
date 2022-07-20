from worker import worker
from preencher_formulario import preencherRpa
from os.path import expanduser
from os import makedirs
import time
from finanftp import FinanFTP

home = expanduser("~")

worker = worker()

template = open(home + '/templates/template_rpa.docx', 'rb')


def save_document(target_path, filename, document, text):
    if filename != '' or filename != None:
        filename = 'https://finan.cett.dev.br' + filename
        ext = filename.split('.')[-1]
        docName = 'Contrato RPA nº {text} - CPF.{ext}'.format(
            rpaID=text, ext=ext)
        if ftp.download_document(filename, target_path + docName) is True:
            taskVariables[document] = {
                'name': document,
                'value': docName
            }


if __name__ == '__main__':
    print('Worker started')
    while True:

        ftp = FinanFTP()
        tasks = worker.fetch_tasks()

        for task in tasks:
            print('Task: {}'.format(task.id_))

            rpaID = task.variables['rpaID'].value

            variables = {}

            for taskVariables in task.variables:
                variables[taskVariables] = task.variables[taskVariables].value

            docCPF = variables['docCPF'] if 'docCPF' in variables else None
            docDocumentoDeCPF = variables['docDocumentoDeCPF'] if 'docDocumentoDeCPF' in variables else None
            docRG = variables['docRG'] if 'docRG' in variables else None
            docPIS = variables['docPIS'] if 'docPIS' in variables else None
            docComprovanteEndereco = variables['docComprovanteEndereco'] if 'docComprovanteEndereco' in variables else None
            docCertidaoCasamento = variables['docCertidaoCasamento'] if 'docCertidaoCasamento' in variables else None
            docCpfDependente = variables['docCpfDependente'] if 'docCpfDependente' in variables else None
            docIdentidadeConjuge = variables['docIdentidadeConjuge'] if 'docIdentidadeConjuge' in variables else None
            numCPF = variables['cpf'].replace('.', '').replace(
                '-', '') if 'cpf' in variables else None

            makedirs(numCPF, exist_ok=True)

            target_path = home + '/outputs/' + numCPF

            rapDocName, emailPrestador = preencherRpa(
                rpaID, template, variables)

            taskVariables = {
                'rapDocName': {
                    'name': 'rapDocName',
                    'value': rapDocName
                },
                'emailPrestador': {
                    'name': 'emailPrestador',
                    'value': emailPrestador
                }
            }

            save_document(target_path, docDocumentoDeCPF,
                          'docDocumentoDeCPF', rpaID)
            # if docDocumentoDeCPF != '':
            #     docDocumentoDeCPF = 'https://finan.cett.dev.br' + docDocumentoDeCPF
            #     ext = docDocumentoDeCPF.split('.')[-1]
            #     docName = 'Contrato RPA nº {rpaID} - CPF.{ext}'.format(
            #         rpaID=rpaID, ext=ext)
            #     if ftp.download_document(docDocumentoDeCPF, target_path + docName) is True:
            #         taskVariables['docDocumentoDeCPF'] = {
            #             'name': 'docDocumentoDeCPF',
            #             'value': docName
            #         }

            save_document(target_path, docRG, 'docRG', rpaID)
            # if docRG != '':
            #     docRG = 'https://finan.cett.dev.br' + docRG
            #     ext = docDocumentoDeCPF.split('.')[-1]
            #     docName = 'Contrato RPA nº {rpaID} - RG.{ext}'.format(
            #         rpaID=rpaID, ext=ext)
            #     if ftp.download_document(docRG, target_path + docName) is True:
            #         taskVariables['docRG'] = {
            #             'name': 'docRG',
            #             'value': docName
            #         }

            save_document(target_path, docRG, 'docRG', rpaID)
            # if docPIS != '':
            #     docPIS = 'https://finan.cett.dev.br' + docPIS
            #     ext = docDocumentoDeCPF.split('.')[-1]
            #     docName = 'Contrato RPA nº {rpaID} - PIS.{ext}'.format(
            #         rpaID=rpaID, ext=ext)
            #     if ftp.download_document(docPIS, target_path + docName) is True:
            #         taskVariables['docPIS'] = {
            #             'name': 'docPIS',
            #             'value': docName
            #         }

            save_document(target_path, docComprovanteEndereco,
                          'docComprovanteEndereco', rpaID)
            # if docComprovanteEndereco != '':
            #     docComprovanteEndereco = 'https://finan.cett.dev.br' + docComprovanteEndereco
            #     ext = docDocumentoDeCPF.split('.')[-1]
            #     docName = 'Contrato RPA nº {rpaID} - Comprovante de endereço.{ext}'.format(
            #         rpaID=rpaID, ext=ext)
            #     if ftp.download_document(
            #             docComprovanteEndereco, target_path + docName) is True:
            #         taskVariables['docComprovanteEndereco'] = {
            #             'name': 'docComprovanteEndereco',
            #             'value': docName
            #         }

            save_document(target_path, docCertidaoCasamento,
                          'docCertidaoCasamento', rpaID)
            # if docCertidaoCasamento != '':
            #     docCertidaoCasamento = 'https://finan.cett.dev.br' + docCertidaoCasamento
            #     ext = docDocumentoDeCPF.split('.')[-1]
            #     docName = 'Contrato RPA nº {rpaID} - Certidão de casamento.{ext}'.format(
            #         rpaID=rpaID, ext=ext)
            #     if ftp.download_document(
            #             docCertidaoCasamento, target_path + docName) is True:
            #         taskVariables['docCertidaoCasamento'] = {
            #             'name': 'docCertidaoCasamento',
            #             'value': docName
            #         }

            save_document(target_path, docCpfDependente,
                          'docCpfDependente', rpaID)
            # if docCpfDependente != '':
            #     docCpfDependente = 'https://finan.cett.dev.br' + docCpfDependente
            #     ext = docDocumentoDeCPF.split('.')[-1]
            #     docName = 'Contrato RPA nº {rpaID} - CPF do dependente.{ext}'.format(
            #         rpaID=rpaID, ext=ext)
            #     if ftp.download_document(docCpfDependente, target_path + docName) is True:
            #         taskVariables['docCpfDependente'] = {
            #             'name': 'docCpfDependente',
            #             'value': docName
            #         }

            save_document(target_path, docIdentidadeConjuge,
                          'docIdentidadeConjuge', rpaID)
            # if docIdentidadeConjuge != '':
            #     print(docIdentidadeConjuge, type(docIdentidadeConjuge))
            #     docIdentidadeConjuge = 'https://finan.cett.dev.br' + docIdentidadeConjuge
            #     ext = docDocumentoDeCPF.split('.')[-1]
            #     docName = 'Contrato RPA nº {rpaID} - RG do Conjuge.{ext}'.format(
            #         rpaID=rpaID, ext=ext)
            #     if ftp.download_document(
            #             docIdentidadeConjuge, target_path + docName) is True:
            #         taskVariables['docIdentidadeConjuge'] = {
            #             'name': 'docIdentidadeConjuge',
            #             'value': docName
            #         }

            worker.complete_task(task.id_, taskVariables)
            del ftp

            time.sleep(30)
