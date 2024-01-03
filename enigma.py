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
