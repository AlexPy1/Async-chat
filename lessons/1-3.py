from ipaddress import ip_address
from subprocess import Popen, PIPE
from tabulate import tabulate


def host_ping(list_ip_addresses, timeout=400, requests=1):
    results = {'Доступные узлы': "", 'Недоступные узлы': ""}  # словарь с результатами
    for address in list_ip_addresses:
        try:
            address = ip_address(address)
        except:
            pass
        proc = Popen(f"ping {address} -w {timeout} -n {requests}", shell=False, stdout=PIPE)
        proc.wait()
        if proc.returncode == 0:
            results['Доступные узлы'] += f"{str(address)}\n"
            res_string = f'{address} - Узел доступен'
        else:
            results['Недоступные узлы'] += f"{str(address)}\n"
            res_string = f'{address} - Узел недоступен'
        print(res_string)
    return results


ip_addresses = ['2.2.2.2', '127.0.0.1', '127.0.0.2']
host_ping(ip_addresses)


def host_range_ping(num):
    for i in range(num):
        proc = Popen(f"ping 127.0.0.{i} -w {400} -n {1}", shell=False, stdout=PIPE)
        proc.wait()
        if proc.returncode == 0:
            print(f'127.0.0.{i} - доступен')
        else:
            print(f'127.0.0.{i} - недоступен')


host_range_ping(10)


def host_range_ping_tab(num):
    res = []
    for i in range(num):
        proc = Popen(f"ping 127.0.0.{i} -w {400} -n {1}", shell=False, stdout=PIPE)
        proc.wait()
        if proc.returncode == 0:
            res.append((f'127.0.0.{i}', 'доступен'))
        else:
            res.append((f'127.0.0.{i}', 'недоступен'))
    tab = tabulate(res)
    return tab


print(host_range_ping_tab(5))
