from faker import Faker
from cpfecnpj import generate_cpf
from datetime import datetime
faker = Faker()
import random

# for i in range(0,1000):
#     pessoa = {
#         "nome" : faker.name(),
#         "apelido" : faker.first_name(),
#         "nasc" : str(faker.date_of_birth()),
#         "email" : faker.email(),
#         "telefone_r" : faker.phone_number(),
#         "endereco" : faker.address(),
#         "complemento" : faker.secondary_address(),
#         "telefone_c" : faker.phone_number(),
#         "atividade_desc" : {1000:'Não Possui',1001:'Negocio informal ( sem CNPJ )', 1002:'Atividade Rural (sem inscrição estadual, DAP ou Registro Min. Pesca)', 1003:'Ambulante', 1004:'Artesão', 1005:'Autônomo'},
#         "escolaridade" : {1:'SEM FORMAÇÃO', 2:'ENSINO FUNDAMENTAL INCOMPLETO', 3:'ENSINO FUNDAMENTAL COMPLETO', 4:'ENSINO MÉDIO INCOMPLETO', 5:'ENSINO MÉDIO COMPLETO', 6:'ENSINO SUPERIOR INCOMPLETO', 7:'ENSINO SUPERIOR COMPLETO', 8:'ESPECIALIZAÇÃO / PÓS-GRADUAÇÃO', 9:'ESPECIALIZAÇÃO', 10:'MESTRADO COMPLETO', 11:'DOUTORADO COMPLETO'},
#         "sexo" : {0:'Masculino',1:'Feminino'},
#         "receberemail" : faker.random_element(elements=('SIM', 'NÃO')),
#         "receber_mala" : faker.random_element(elements=('SIM', 'NÃO')),
#         "receber_sms" : faker.random_element(elements=('SIM', 'NÃO')),
#         "receber_telefone" : faker.random_element(elements=('SIM', 'NÃO')),
#         "cpf" : generate_cpf(),
#         "cep" : faker.postcode_in_state(state_abbr=None),
#         "classificacao" : faker.name(),
#         "importacao" : faker.name(),
#         "valor" : "Teste"
#     }

arquivo = open('informacoes_pessoa_fisica.txt', 'w')
for i in range(0,1000):
    
    nome = faker.name()
    apelido =  faker.first_name()
    nasc = str(faker.date_of_birth())
    email =  faker.email()
    telefone_r =  faker.postalcode_plus4()
    complemento = faker.secondary_address()
    telefone_c = faker.postalcode_plus4()
    atividade_desc = {1000:'Não Possui',1001:'Negocio informal ( sem CNPJ )', 1002:'Atividade Rural (sem inscrição estadual, DAP ou Registro Min. Pesca)', 1003:'Ambulante', 1004:'Artesão', 1005:'Autônomo'}
    escolaridade = {1:'SEM FORMAÇÃO', 2:'ENSINO FUNDAMENTAL INCOMPLETO', 3:'ENSINO FUNDAMENTAL COMPLETO', 4:'ENSINO MÉDIO INCOMPLETO', 5:'ENSINO MÉDIO COMPLETO', 6:'ENSINO SUPERIOR INCOMPLETO', 7:'ENSINO SUPERIOR COMPLETO', 8:'ESPECIALIZAÇÃO / PÓS-GRADUAÇÃO', 9:'ESPECIALIZAÇÃO', 10:'MESTRADO COMPLETO', 11:'DOUTORADO COMPLETO'}
    sexo = {0:'Masculino',1:'Feminino'}
    receberemail = faker.random_element(elements=('SIM', 'NÃO'))
    receber_mala = faker.random_element(elements=('SIM', 'NÃO'))
    receber_sms = faker.random_element(elements=('SIM', 'NÃO'))
    receber_telefone = faker.random_element(elements=('SIM', 'NÃO'))
    cpf = generate_cpf()
    cep = faker.random_element(elements=('60768-020','60544-760','60544-763','60544-766','60749-050','60544-769','60346305','60346310','60346364','60346410','60346520','60346530','60346570','60346620','60347052','60347080','60347215','60347780','60347840','60055304','60055480','60055974','60055974','60060010','60060060'))
    classificacao = faker.name()
    importacao = 'teste'
    valor = "Teste"
    endereco = faker.address()



    code, esc = random.choice(list(escolaridade.items()))
    code = str(code)
    cods, sex=random.choice(list(sexo.items()))
    cods = str(cods)  
    coda, ativ = random.choice(list(atividade_desc.items()))
    coda = str(coda)
    endereco = endereco.replace('\n',' ')
    linha = cpf+"\t"+nome+"\t"+apelido+"\t"+esc+"\t"+code+"\t"+nasc+"\t"+sex+"\t"+cods+"\t"+cep+"\t"+endereco+"\t"+complemento+"\t"+email+"\t"+telefone_r+"\t"+telefone_c+"\t"+telefone_c+"\t"+classificacao+"\t"+ativ+"\t"+coda+"\t"+receberemail+"\t"+receber_mala+"\t"+receber_sms+"\t"+receber_telefone+"\t"+importacao+"\t"+valor+"\n"
    arquivo.write(linha)
    
arquivo.close()
