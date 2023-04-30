# __NetZer Desktop__

This is `NetZer desktop` a network analyzer, you can use it to scan a single host or hosts in network.

## __How to use host scanner__

Write IP of host and ports. You can write ports in three forms.

- __One port__. Only write a specific port, example: 80
- __List of ports__. Write some ports separated with commas, example: 22, 80, 443, 8080
- __Range of ports__. Write range of ports to scan, example: [22-443]

## __How to use network scanner__

Write IP of network (or some host into that network) and subnet mask.

## __Setup project__

You need install [python](https://www.python.org/downloads/) and virtualenv. install virtualenv with pip.

```bash
pip install virtualenv
```

Create a new virtual environment using virtualenv.

```bash
virtualenv .venv
```

Active virtualenv (Windows).

```bash
.venv\Scripts\activate
```

Active virtualenv (Linux).

```bash
source .venv/bin/activate
```

Install project dependencies.

```bash
python -m pip install -r requirements.txt
```

Finally, Execute app.py

## __Useful links__

- [python-nmap](https://pypi.org/project/python-nmap/) PyPI.

- [python-nmap](https://xael.org/pages/python-nmap-en.html) homepage.

- [nmap.org](https://nmap.org/)
