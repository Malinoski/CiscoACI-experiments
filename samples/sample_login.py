#!/usr/bin/env python

"""
Simple application
"""

import sys
import acitoolkit.acitoolkit as ACI


def main():

    creds = ACI.Credentials('apic')
    args = creds.get()

    # Login to APIC
    session = ACI.Session(args.url, args.login, args.password)
    resp = session.login()
    if not resp.ok:
        print('Could not login to APIC')
        sys.exit(0)
    else:
        print("Success to login to APIC as user '{}' at url {}".format(args.login, args.url))
        print("Token: {}".format(session.token))


if __name__ == '__main__':
    main()
