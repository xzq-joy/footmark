from footmark.connection import ACSQueryConnection
from footmark.ess import set_params_by_key


class TestConnection(ACSQueryConnection):
    SDKVersion = '2014-05-26'

    def __int__(self, sdk_version=None):
        self.ECSSDK = 'aliyunsdkecs.request.v' + self.SDKVersion.replace('-', '')

        super(TestConnection, self).__init__(acs_access_key_id=None,
                                            acs_secret_access_key=None,
                                            region=None, product=self.ECSSDK,
                                            security_token=None, user_agent=None)

    def create_scaling_configuration(self, **kwargs):
        print(kwargs['group_id'])
        return self.build_request_params(self.format_request_kwargs(**kwargs))


conn = TestConnection()
params = {'group_id': {'name': 'tt'}, 'instance_type': {'ab': '111'}}

# print(conn.create_scaling_configuration(**params))


class TestClass:

    def __int__(self):
        pass

    def format_ess_request_kwargs(self, **kwargs):
        """
        Transfer request parameters for match the sdk params
        :param kwargs:
        :return:
        """
        for key, value in kwargs.items():
            if key == 'scaling_configuration_ids':
                set_params_by_key(key, value, kwargs)

            # scaling_configuration_names = kwargs['scaling_configuration_names']
            # if scaling_configuration_names:
            #     for i in range(len(scaling_configuration_names)):
            #         if i < 10 and scaling_configuration_names[i]:
            #             kwargs['scaling_configuration_name' + bytes(i + 1)] = scaling_configuration_names[i]
            #
            # scaling_group_ids = kwargs['scaling_group_ids']
            # if scaling_group_ids and len(scaling_group_ids) > 0:
            #     for i in range(len(scaling_group_ids)):
            #         if i < 10 and scaling_group_ids[i]:
            #             kwargs['scaling_group_id' + bytes(i + 1)] = scaling_group_ids[i]
            #
            # scaling_group_names = kwargs['scaling_group_names']
            # if scaling_group_names:
            #     for i in range(len(scaling_group_names)):
            #         if i < 10 and scaling_group_names[i]:
            #             kwargs['scaling_group_name' + bytes(i + 1)] = scaling_group_names[i]
            #
            # removal_policies = kwargs['removal_policies']
            # if removal_policies:
            #     for i in range(len(removal_policies)):
            #         if i < 2 and removal_policies[i]:
            #             kwargs['RemovalPolicy' + bytes(i + 1)] = removal_policies[i]
            #
            # instance_ids = kwargs['instance_ids']
            # if instance_ids:
            #     for i in range(len(instance_ids)):
            #         if i < 20 and instance_ids[i]:
            #             kwargs['InstanceId' + bytes(i + 1)] = instance_ids[i]

        return kwargs


params = {'scaling_configuration_ids': None}

test = TestClass()

print(test.format_ess_request_kwargs(**params))
