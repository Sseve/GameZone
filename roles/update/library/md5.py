#!/usr/bin/env python
# check files md5
import os
import hashlib
from ansible.module_utils.basic import *


def get_path():
    args = AnsibleModule(
    argument_spec = dict(
        path = dict(required=True, type='str')
    )
    )

    params = args.params
    return params['path'], args


def check_md5(path):
    if not os.path.exists(path + '/md5.txt'):
        return {"msg": "md5.txt file not exists!"}
    with open(path + '/md5.txt') as fd:
        for line in fd.readlines():
            line = line.replace('\n', '').split(' ')
            remote_md5 = line[1]
            file_name  = path + line[0]
            if not os.path.exists(file_name):
                continue
            with open(file_name, 'rb') as md:
                m = hashlib.md5()
                m.update(md.read())
                local_md5 = m.hexdigest()
            if remote_md5 != local_md5:
                return {"msg": "{} md5 is not same!".format(file_name)}
    return {"msg": "md5 check no error"}


if __name__ == '__main__':
    path, args = get_path()
    result = check_md5(path)
    args.exit_json(**result)