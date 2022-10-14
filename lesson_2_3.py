import yaml
data = {
    'list': ['one', 'two'],
    'int': 2,
    'dict': {'int_with_uni_1': '1€', 'int_with_uni_2': '2€'}
}
with open('result.yaml', 'w') as f:
    yaml.dump(data,f, default_flow_style=True, allow_unicode = True)