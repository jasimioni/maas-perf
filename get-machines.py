#!/usr/bin/env python3

import json
import sys
import argparse
import os
import time
import random
import requests
import sys
import json
import urllib
from requests_oauthlib import OAuth1Session
import logging

class MAASClient:
    def __init__(self, apikey, url, timeout=10):
        self.logger = logging.getLogger(__name__)
        self.apikey = apikey
        self.url = url
        consumer_key, key, secret = self.apikey.split(':')
        self.session = OAuth1Session(
            consumer_key, resource_owner_key=key, resource_owner_secret=secret
        )
        self.timeout = timeout

    def _request(self, ep, method='GET', params=None):
        
        url = self.url.rstrip('/') + ep
        self.logger.debug(f"url={url}, method={method}, params={params}")

        if method == 'POST':
            resp = self.session.request(method, url, data=params, verify=False, timeout=self.timeout)
        elif method == 'GET':
            resp = self.session.request(method, url, params=params, verify=False, timeout=self.timeout)
        else:
            raise Exception(f"Unsupported method {method}")
            
        self.logger.debug(f"status_code={resp.status_code}, text={resp.text}")
        return resp

    def _get(self, ep, params):
        return self._request(ep, params=params)

    def _post(self, ep, params=None):
        return self._request(ep, method='POST', params=params)
    
    def machines(self, hostname=None):
        ep = '/api/2.0/machines/'
        resp = self._get(ep, { 'hostname': hostname })

        print(resp)

        machines = resp.json()
        if not machines:
            raise Exception(f"No machine returned with {hostname}")
        return machines
    
    def allocate(self, system_id=None):
        ep = '/api/2.0/machines/'
        ep += f'op-allocate'
        return self._post(ep, params={ "system_id": system_id })

    def release(self, system_id=None):
        ep = '/api/2.0/machines/'
        ep += f'{system_id}/op-release'
        return self._post(ep)

    def lock(self, system_id=None):
        ep = '/api/2.0/machines/'
        ep += f'{system_id}/op-lock'
        return self._post(ep)

    def unlock(self, system_id=None):
        ep = '/api/2.0/machines/'
        ep += f'{system_id}/op-unlock'
        return self._post(ep)
    
    def subnets(self):
        ep = '/api/2.0/subnets/'
        resp = self._get(ep, {})
        subnets = resp.json()
        if not subnets:
            raise Exception(f"No subnets returned")
        return subnets
    
    def fabrics(self):
        ep = '/api/2.0/fabrics/'
        resp = self._get(ep, {})
        fabrics = resp.json()
        if not fabrics:
            raise Exception(f"No fabrics returned")
        return fabrics
        
    def vlans(self, fabric_id=None):
        if fabric_id is None:
            raise Exception(f"fabric_id is required")
        ep = f'/api/2.0/fabrics/{fabric_id}/vlans/'
        resp = self._get(ep, {})
        vlans = resp.json()
        if not vlans:
            raise Exception(f"No vlans returned")
        return vlans
    
    def create_fabric(self, name=None, description=None):
        ep = '/api/2.0/fabrics/'
        resp = self._post(ep, params={ "name": name, "description": description })
        return resp.json()
    
    def create_subnet(self, fabric_id=None, vlan_id=None, cidr=None, gateway_ip=None, dns_servers=None):
        if cidr is None:
            raise Exception(f"cidr is required")
        ep = '/api/2.0/subnets/'
        resp = self._post(ep, params={ "fabric": fabric_id, "vlan": vlan_id, "cidr": cidr, "gateway_ip": gateway_ip, "dns_servers": dns_servers })
        return resp.json()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run a performance test in MAAS")
    parser.add_argument('--apikey', help='MAAS API key. Can be provided using MAAS_API_KEY environment variable.')
    parser.add_argument('--url', help='MAAS URL. Can be provided using MAAS_URL environment variable.')
    args = parser.parse_args()
    
    apikey = args.apikey or os.environ.get('MAAS_API_KEY') 
    if not apikey:
        sys.exit("MAAS API key not provided")
    
    url = args.url or os.environ.get('MAAS_URL')
    if not url:
        sys.exit("MAAS URL not provided")

    client = MAASClient(apikey, url)
    machines = client.machines()

    print(json.dumps(machines, indent=2))