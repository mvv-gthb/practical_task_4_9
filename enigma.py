RDICT = {1: ('AELTPHQXRU', 'BKNW', 'CMOY', 'DFG', 'IV', 'JZ', 'S'),
         2: ('FIXVYOMW', 'CDKLHUP', 'ESZ', 'BJ', 'GR', 'NT', 'A', 'Q'),
         3: ('ABDHPEJT', 'CFLVMZOYQIRWUKXSG', 'N'),
         4: ('AEPLIYWCOXMRFZBSTGJQNH', 'DV', 'KU'),
         5: ('AVOLDRWFIUQ', 'BZKSMNHYC', 'EGTJPX'),
         6: ('AJQDVLEOZWIYTS', 'CGMNHFUX', 'BPRK'),
         7: ('ANOUPFRIMBZTLWKSVEGCJYDHXQ'),
         8: ('AFLSETWUNDHOZVICQ', 'BKJ', 'GXY', 'MPR'),
         'beta': ('ALBEVFCYODJWUGNMQTZSKPR', 'HIX'),
         'gamma': ('AFNIRLBSQWVXGUZDKMTPCOYJHE'),
         }

def rotor(symbol, n, reverse=False):
    if bool(n):
        step = 1 if not(reverse) else -1
        if not(isinstance(RDICT[n], str)):
            for item in RDICT[n]:
                if symbol in item:
                    crypted_symbol = item[(item.index(symbol) + step) % len(item)]
        else:
            if symbol in RDICT[n]:
                crypted_symbol = RDICT[n][(RDICT[n].index(symbol) + step) % len(RDICT[n])]
    else: crypted_symbol = symbol
    return crypted_symbol

reflector_dict = {
    1 : ('AY', 'BR', 'CU', 'DH', 'EQ',
         'FS', 'GL', 'IP', 'JX', 'KN',
         'MO', 'TZ', 'VW')
}
def reflector(symbol, n):
	if bool(n):
		for item in reflector_dict[n]:
			if symbol.capitalize() in item:
				crypted_symbol = item.replace(symbol.capitalize(), '')
		return crypted_symbol
	else:
		return symbol

def enigma(text, ref, rot1, rot2, rot3):
    rot_list = [rot3, rot2, rot1]
    formatted_str = ''.join([item for item in text.upper() if item.isalnum()])
    forward_crypted_str = ''
    for symbol in formatted_str:
        for rot in rot_list:
            symbol = rotor(symbol, rot)
        forward_crypted_str += symbol
    reflected_crypted_str = ''
    for symbol in forward_crypted_str:
        reflected_crypted_str += reflector(symbol, ref)
    back_crypted_str = ''
    rot_list.reverse()
    backward_crypted_str = ''
    for symbol in reflected_crypted_str:
        for rot in rot_list:
            symbol = rotor(symbol, rot, True)
        backward_crypted_str += symbol
    return backward_crypted_str
