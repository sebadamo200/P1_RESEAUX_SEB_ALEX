import sys
import csv

protocols = {
    'HTTP': 80,
    'HTTPS': 443,
    'SSH': 22,
    'FTP': 21,
    'SMTP': 25,
    'POP3': 110,
    'IMAP': 143,
    'DNS': 53,
    'SNMP': 161,
    'NTP': 123
}


arg = sys.argv[1]
def start_with_tls_version(line):
    return line.startswith('TLS')

def tls_v(file):
    TlsVersion = {}
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if start_with_tls_version(row['Protocol']):
                if row['Protocol'] not in TlsVersion:
                    TlsVersion[row['Protocol']] = 1
                else:
                    TlsVersion[row['Protocol']] += 1
    return TlsVersion

def port_tls_version(file):
    TlsVersion = {}
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if start_with_tls_version(row['Protocol']):
                if row['Destination Port'] not in TlsVersion:
                    TlsVersion[row['Destination Port']] = 1
                else:
                    TlsVersion[row['Destination Port']] += 1
    return TlsVersion


print(port_tls_version(file=arg))
