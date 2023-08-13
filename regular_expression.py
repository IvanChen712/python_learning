import re


def is_valid_email(addr):
    re_email1 = re.compile(r'^[a-zA-Z0-9._%+]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if re_email1.match(addr):
        return True
    return False


def name_of_email(addr):
    re_email2 = re.compile(r'^<?(\w*\s*\w*)>?\s*?(\w*)?@\w+\.\w+$')
    if re_email2.match(addr):
        return re_email2.match(addr).groups(1)[0]
    else:
        return None


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
