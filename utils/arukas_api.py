import requests
import json
import re
import base64

Aurkas_token = '03823229-9809-43db-a2b0-5f921547c9b7'
Arukas_secret = 'ye3QzTpWsJM5xEh2RYZ0uYGuuJduRXQXdPVDYYhprbDQUK1DnqdgQEeXTvbSVBdu'

ss_image_name = re.compile('lowid/ss-with-net-speeder.*')
re_ss_ip = re.compile('\d{1,3}-\d{1,3}-\d{1,3}-\d{1,3}')
re_pwd_encry = re.compile('-p 8888 -k (?P<password>.+) -m (?P<encryption>.+)$')


def generate_ss_uri(ss_dict):
    config = '{encrypt_method}:{password}@{ip}:{port}'
    config = config.format(encrypt_method=ss_dict['encryption'],
                           password=ss_dict['password'],
                           ip=ss_dict['ip'], port=ss_dict['port'])
    uri = b'ss://' + base64.urlsafe_b64encode(config.encode())
    return uri.decode()


class ArukasAPI:
    def __init__(self, token=Aurkas_token, secret=Arukas_secret):
        self.headers = {
            "Content-Type: application/vnd.api+json",
            "Accept: application/vnd.api+json"
        }
        self.token = token
        self.secret = secret
        self.session = requests.session()
        self.url_prefix = 'https://app.arukas.io/api/'
        self.session.auth = (self.token, self.secret)
        self.headers.update(self.headers)
        self.ss_set = list()
        self.post_headers = {
            'Content-Type': 'application/json'
        }

    def list_apps(self):
        res = self.session.get(url=self.url_prefix + 'apps')
        apps = self.__parse_res(res)
        return apps

    def get_app(self, id):
        res = self.session.get(url=self.url_prefix + 'apps/' + id)
        app = self.__parse_res(res)
        return app

    def get_containers(self):
        res = self.session.get(url=self.url_prefix + 'containers')
        containers_json = self.__parse_res(res)
        # print(containers_json)
        return containers_json

    def get_ss(self):
        containers = self.get_containers()
        for container in containers['data']:
            # 根据镜像名字匹配
            cmd = None
            if re.fullmatch(ss_image_name, container['attributes']['image_name']):
                cmd = re.fullmatch(re_pwd_encry, container['attributes']['cmd'])
                password = cmd.group('password')
                encryption = cmd.group('encryption')
                for ss in container['attributes']['port_mappings']:
                    ss_dict = dict()
                    ss_dict['ip'] = re.search(re_ss_ip, ss[0]['host']).group().replace('-', '.')
                    ss_dict['port'] = ss[0]['service_port']
                    ss_dict['password'] = password
                    ss_dict['encryption'] = encryption
                    ss_dict['uri'] = generate_ss_uri(ss_dict)
                    self.ss_set.append(ss_dict)

    def __parse_res(self, res):
        res.encoding = 'utf-8'
        return res.json()

    def post_to_site(self):
        data = dict()
        counter = 1
        session = requests.session()
        session.headers.update(self.post_headers)
        for ss in self.ss_set:
            print(counter)
            counter += 1
            data['content'] = ss['uri']
            json_data = json.dumps(data)
            res = session.post(url='http://tofun.online/api/postmessage', data=json_data)
            if res.status_code == 201:
                print('successfully')


instance = ArukasAPI()
# instance.list_apps()
# instance.get_app(id='5bfda19b-72d1-417a-a5ed-06a8ee0f54f4')
# instance.get_containers()
# instance.container_detail(id='8cf67f03-83d4-4693-9287-ece7babe6126')
instance.get_ss()
instance.post_to_site()
# print(instance.ss_set)
