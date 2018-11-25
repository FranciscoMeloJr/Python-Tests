client_bank_accounts1 = [
    {
        'number': '0001',
        'transit_number': '007'
    },
    {
        'number': '0001',
        'transit_number': '002'
    },
    {
        'number': '0001',
        'transit_number': '003',
        'institution_number': '55',
}
]
client_bank_accounts2 = [
    {
        'number': '0001',
        'transit_number': '007'
    },
    {
        'number': '0001',
        'transit_number': '001'
    }
]
client_bank_accounts3 = []
eligible_institutions = [
    {
    'institution_name': 'BMO',
    'transit_number': '001',
    },
    {
    'institution_name': 'SCOTIA_BANK',
    'transit_number': '002',
    },
    {
    'institution_name': 'NATIONAL',
    'transit_number': '003',
    'institution_number': '27',
    },
{
    'institution_name': 'TD',
    'transit_number': '003',
    'institution_number': '32',
    },
{
    'institution_name': 'XPTO',
    'transit_number': '003',
    'institution_number': '55',
    }
]

def is_there(account_first_number):
    elegible_inst_numbers = []
    for each_bank in eligible_institutions:
        elegible_inst_numbers.append(each_bank['transit_number'])
    set_eleg = set(elegible_inst_numbers)

    # it is there
    if account_first_number in set_eleg:
        return True
    else:
        return False


def find_name(account):
    """
    Find an bank name from the provided account.
    :param account: client's account.
    :return: name of the bank.
    """
    bank_name = {}
    for each_bank in eligible_institutions:
        bank_name[each_bank['transit_number']] = each_bank['institution_name']
    return bank_name[account['transit_number']]


def find_name2(new_dict, account):
    """
    Find the name of a bank from an account.
    :param new_dict: new classification for the keys
    :param account: client's account
    :return: name of the bank.
    """
    for each_bank_key in new_dict.keys():
        p1 = each_bank_key[0]
        p2 = each_bank_key[1]
        if account['transit_number'] == p1:
            if p2 is not -1:
                if p2 ==  account['institution_number']:
                    return new_dict[(p1,p2)]
            else: # so p1 == account
                return new_dict[(p1,p2)]

def create_new_dict():
    """
    Create a new dict with the keys of both: transit+institution
    :return:
    """
    bank_name = {}
    for each_bank in eligible_institutions:
        inst_number = each_bank.get('institution_number')
        if inst_number is None:
            bank_name[(each_bank['transit_number'], -1)] = each_bank['institution_name']
        else:
            bank_name[(each_bank['transit_number'], each_bank['institution_number'])] = each_bank['institution_name']

    return bank_name

def account_name(client_banks):
    """
    This function will find the name of a bank from a client's account.
    """
    dict_banks = create_new_dict()
    result = []
    for each in client_banks:
        # client_bank_accounts[0]
        account_first = each
        account_first_number = account_first['transit_number']
        if is_there(account_first_number):
            temp = "Account registered: " + find_name2(dict_banks, account_first)
            result.append(temp)

        else:
            result.append("Account not registered")

    return result

def do_test():
    """
    This function will do the test:
    """
    result1 = ['Account not registered', 'Account registered: SCOTIA_BANK', 'Account registered: XPTO']
    result2 = ['Account not registered', 'Account registered: BMO']
    result3 = []
    assert result1 == account_name(client_bank_accounts1), "ERROR"
    assert result2 == account_name(client_bank_accounts2), "ERROR"
    assert result3 == account_name(client_bank_accounts3), "ERROR"

do_test()