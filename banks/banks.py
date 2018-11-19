#Banks
# https://wealthsimple.quip.com/nXXxAfabgWj7/Bank-Account-Filter-Candidate-Description

import numpy as np

client_bank_accounts = [
  {
    'institution_number': '001',
    'transit_number': '12345',
    'account_number': '1342237'
  },
  {
    'institution_number': '004',
    'transit_number': '34533',
    'account_number': '1212347'
  },
  {
    'institution_number': '004',
    'transit_number': '35673',
    'account_number': '7433453'
  },
  {
    'institution_number': '010',
    'transit_number': '30800',
    'account_number': '9054343'
  },
  {
    'institution_number': '010',
    'transit_number': '10000',
    'account_number': '4895602'
  }
]

eligible_institutions = [
  {
    'institution_name': 'BMO',
    'institution_number': '001',
  },
  {
    'institution_name': 'CIBC',
    'institution_number': '010'
  },
  {
    'institution_name': 'Simplii',
    'institution_number': '010',
    'transit_numbers': ['30800']
  },
    {
    'institution_name': 'Complexii',
    'institution_number': '010',
    'transit_numbers': ['10000']
  },
  {
    'institution_name': 'TD',
    'institution_number': '004'
  }
]


"""
Get a list of names from inst_number and inst_transit
"""
def get_from_id_name_bank(inst_number, inst_transit = -1):
    banks_same_id = []
    for each_bank in eligible_institutions:
        if inst_number is each_bank['institution_number']:
            banks_same_id.append(each_bank)
            
    if inst_transit is -1:
        return banks_same_id[0]['institution_name']
    
    else:
        for bank in banks_same_id:
            if bank.get('transit_numbers'):
              print(bank['transit_numbers'])
              print(inst_transit)
              if bank['transit_numbers'][0] is inst_transit:
                return bank['institution_name']

"""
Get the names of the institutions based on client's account.
"""
def get_bank_names():
    bank_names = []
    # iterate over the client banks
    for account in client_bank_accounts:
        # for each one: get the institution numbers (inst_number and transit)
        temp_inst_number = account['institution_number']
        transit = -1
        if account.get('transit_numbers') is not None:
            transit = account['transit_numbers']
            
        # get the name from the other DS        
        temp_inst_name = get_from_id_name_bank(temp_inst_number, transit)
        # put in a list of bank names
        bank_names.append(temp_inst_name)

    # return the list   
    return bank_names


"""
Test the exp and the corrected value for test_get_bank_names
"""
def test_get_bank_names():
    banks = get_bank_names()
    print(banks)
    #assert equals:
    expected = ['BMO', 'TD', 'Simplii']
    np.testing.assert_array_equal(expected,banks)


"""
Test the exp and the corrected value for test_get_from_id_name_bank
"""
def test_get_from_id_name_bank():
    # comparing names of banks:
    assert get_from_id_name_bank('010') == 'CIBC'
    assert get_from_id_name_bank('001') == 'BMO'
    assert get_from_id_name_bank('004') == 'TD'
    assert get_from_id_name_bank('010', '30800') == 'Simplii'
    assert get_from_id_name_bank('010', '10000') == 'Complexii'

"""
Execute the unit tests:
"""
def unit_tests():
  test_get_from_id_name_bank()
  test_get_bank_names()

unit_tests()

#The most important goal here is to cover all edge cases. Make sure to test your code thoroughly.

