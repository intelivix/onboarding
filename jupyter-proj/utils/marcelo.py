

def marcelo(x, is_feio=True):
    if is_feio is None:
        raise Exception('marcelo levantou uma excecao')
    elif is_feio:
        return 'marcelo'
    else:
        return 'marcelo bonito'
