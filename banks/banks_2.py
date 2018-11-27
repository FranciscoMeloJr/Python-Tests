client_bank_accounts = [
  {
    'number': '0001',
    'transit_number': '001'
  }]

  eligible_institutions = [
  {
    'institution_name': 'BMO',
    'transit_number': '001',
  },
  {
    'institution_name': 'SCOTIA_BANK',
    'transit_number': '002',
  }]


def account_name():
    """
    This function will find the name of a bank from a client's account.
    """
    account_first = client_bank_accounts[0]
    account_first_number['transit_number']

    elegible_inst_number = eligible_institutions[0]['transit_number']
    elegible_inst_number.append(eligible_institutions[1]['transit_number'])
    set_eleg = set(elegible_inst_number)
    # it is there
    if account_first_number in set_eleg:
        print("IN")
    else:
        print("OUT")
    # it is not there

account_name()