def packer(name=None, **kwargs):
    print(kwargs)

def unpacker(first_name=None,last_name=None):
    if first_name and last_name:
        print("Hi {} {}".format(first_name,last_name))
    else:
        print("Hi no name")

packer(name="Michael", num=42,spanish_inquisition=None)
unpacker(**{"last_name": "Hernandez", "first_name":"Michael"})
