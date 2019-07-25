import random
import string
import json


def spider_id_gen(size=15):
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(size))


def webshooter_id_gen(size=15):
    return ''.join(random.choice('-' + string.ascii_letters + string.digits) for x in range(size))


ESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG',
           'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
SPIDER_IDS = [spider_id_gen() for i in range(7)]
WEBSHOOTER_IDS = [webshooter_id_gen() for i in range(7)]

if __name__ == "__main__":
    captchas = []
    size = 50000
    for i in range(size):
        captcha = dict()
        captcha["spider_name"] = "pjerj-consultar-processo"
        captcha["price"] = random.uniform(.003, .3)
        captcha["justica"] = "Estadual"
        captcha["method"] = "deathbycaptcha"
        captcha["price_dbc_gold"] = random.uniform(.001, .2)
        captcha["fonte"] = "pjerj"
        captcha["collection_name"] = "extracao_nextel_base_civel"
        captcha["spider_id"] = random.choice(SPIDER_IDS)
        captcha["webshooter_id"] = random.choice(WEBSHOOTER_IDS)
        captcha["estado"] = random.choice(ESTADOS)
        captcha["correct"] = True
        captcha["duration_seconds"] = random.uniform(3, 15)
        captchas.append(captcha)
    with open(f'../json/captcha-50k.json', 'w') as outfile:
        json.dump(captchas, outfile)
