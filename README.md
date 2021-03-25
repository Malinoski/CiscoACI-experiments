# Cisco ACI experiments

This experiment creates an APIC/Spine/Leaf environment in a Cisco Sandbox environment and some code Python to access and uses this envoroment.

### Create the environment

Access the [sandbox cisco](https://devnetsandbox.cisco.com), 
search for "ACI Simulator 4.2", and reserve it (takes 15 min approximately).

When the environment is done, you will receive an email with the VPN credentials for that environment (you can use "Cisco AnyConnect").

### Install

```
cd [root project]
python3 -m venv venv
source venv/bin/activate
pip install setuptools
git clone https://github.com/datacenter/acitoolkit.git 
cd acitoolkit
python setup.py install
```

### Use

```
cd [root project]
python samples/sample_login.py
```
