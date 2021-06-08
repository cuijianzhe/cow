from aliyunsdkpolardb.request.v20170801.DescribeDBClustersRequest import DescribeDBClustersRequest
from aliyunsdkpolardb.request.v20170801.DescribeAccountsRequest import DescribeAccountsRequest
from aliyunsdkpolardb.request.v20170801.DescribeDBClusterEndpointsRequest import DescribeDBClusterEndpointsRequest
from aliyunsdkpolardb.request.v20170801.DescribeDatabasesRequest import DescribeDatabasesRequest
from aliyunsdkpolardb.request.v20170801.DescribeDBClusterAttributeRequest import DescribeDBClusterAttributeRequest



from .base import AliyunCli

class AliyunPolarDB(AliyunCli):
    '''
    阿里云RDS
    '''
    def get_polardbs(self, page_num=1, page_size=20):
        request = DescribeDBClustersRequest()
        request.set_accept_format('json')
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)

        data = self._request(request)
        total = data.get('TotalRecordCount')
        data = data.get('Items')
        data_list = data.get('DBCluster')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data
    def get_polardb_accounts(self, instance_id, username=None, page_num=1, page_size=20):
        '''
        获取RDS下账号
        '''
        request = DescribeAccountsRequest()
        request.set_accept_format('json')
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)
        if username:
            request.set_AccountName(username)
        request.set_DBClusterId(instance_id)
        data = self._request(request)
        data_list = data.get('Accounts')
        data = {
            'data_list': data_list,
        }
        return data
    def get_polardb_connection(self, instance_id, page_num=1, page_size=20):
        '''
        获取连接地址
        :param instance_id:
        :param page_num:
        :param page_size:
        :return:
        '''
        request = DescribeDBClusterEndpointsRequest()
        request.set_accept_format('json')
        request.set_DBClusterId(instance_id)
        data = self._request(request)
        data_list = data.get('Items')
        address_list = []
        for net in data_list:
            network = net.get('AddressItems')[0].get('ConnectionString')
            address_list.append(network)
        return address_list

    def get_polardb_database(self,instance_id,page_num=1, page_size=20):

        request = DescribeDatabasesRequest()
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)
        request.set_accept_format('json')
        request.set_DBClusterId(instance_id)
        data = self._request(request)
        data_list = data.get('Databases').get('Database')
        data = {
            'data_list':data_list
        }
        return data


